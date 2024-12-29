import sys
from cmd4_client import Cmd4_client
from gpt_client import Gpt_client
from cli_client import Cli_client

if __name__ == "__main__":
    # このスクリプトをたたかれた場合、gptclient,
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [options]")
        sys.exit(1)

    command = sys.argv[1]

    if command in ["set", "get"]:
        client = Cmd4_client()
    elif command == "gpt":
        client = Gpt_client()
    elif command == "brightness":
        client = Cli_client()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

    client.execute(sys.argv[2:])