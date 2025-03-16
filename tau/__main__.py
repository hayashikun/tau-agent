import asyncio
import argparse
import logging
import sys

from tau.client import MCPClient

logger = logging.getLogger("tau")
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stderr)
stream_handler.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)


async def main():
    parser = argparse.ArgumentParser(description="Tau MCP Client")
    parser.add_argument(
        "-c",
        "--config",
        default="config.json",
        help="Path to the configuration file (default: config.json)",
    )
    args = parser.parse_args()

    c = MCPClient(config_path=args.config, logger=logger)
    try:
        await c.connect_mcp_servers()
        await c.chat_loop()
    finally:
        await c.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
