#!/usr/bin/env python3

from IPython import embed

from sensors.flipper.client import Client
from util import print_hex, print_screen


def main(path: str = "/dev/ttyACM0"):
    client = Client(path)
    print_screen(client.snapshot_screen())

    embed(colors="neutral")


if __name__ == "__main__":
    main()
