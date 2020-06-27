import argparse
import binascii
import struct

import dpkt

from pyvaser.filocmd.parse_command import parse_commands


def dump_packet(data):
    data_idx_str = data[0:2]
    data_idx = struct.unpack("<H", data_idx_str)[0]
    direction_str = data[21]
    direction = struct.unpack("B", direction_str)[0]
    if direction == 0x02:
        _dir = "->"
    elif direction == 0x82:
        _dir = "<-"
    else:
        _dir = "??"

    kvaser_data = data[data_idx:]
    print(binascii.hexlify(kvaser_data))
    for cmd in parse_commands(kvaser_data):
        print("{} {} ({})".format(_dir, type(cmd).__name__, binascii.hexlify(kvaser_data)))
        print(cmd.__dict__)
        print("")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pcap", help="pcap file")
    args = parser.parse_args()

    f = open(args.pcap)
    pcap = dpkt.pcapng.Reader(f)
    for ts, buf in pcap:
        dump_packet(buf)
    f.close()


if __name__ == "__main__":
    main()
