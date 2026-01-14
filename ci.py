import sys
import anyio
import dagger

async def main():
    config = dagger.Config(log_output=sys.stderr)

    async with dagger.Connection(config) as client:
        src = client.host().directory(".")

        print("Building the container...")
        app_container = src.docker_build()

        print("Running API tests...")
        try:
            await app_container.with_exec(["pytest", "tests/"]).stdout()
            print("All tests passed")
        except dagger.DaggerError:
            print("Tests failed. Build aborted.")
            sys.exit(1)

        print("Publishing to local registry via tunnel...")
        
        registry_tunnel = client.host().service([
            dagger.PortForward(frontend=5001, backend=5001)
        ])
        
        endpoint = await registry_tunnel.endpoint()
        
        image_ref = f"{endpoint}/text-analyzer:v1"
        addr = await app_container.publish(image_ref)
        
        print(f"Pipeline complete! Image published to: {addr}")

if __name__ == "__main__":
    try:
        anyio.run(main)
    except KeyboardInterrupt:
        sys.exit(0)
