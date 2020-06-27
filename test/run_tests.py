import argparse
import binascii
import struct
import sys

import serial


def arduino_can_send(conn, can_id, can_data):
    _id = binascii.hexlify(can_id.to_bytes(2, byteorder="big"))
    out = _id + b" " + hex(len(can_data))[2:].encode() + b" " + \
        binascii.hexlify(can_data) + b"\r\n"
    conn.write(out)
    ret = conn.readline()
    if ret.startswith(b"ERR:"):
        print(ret)
        sys.exit(1)


def arduino_can_recv(conn):
    msg = conn.readline()
    (can_id, data_len, data_hex) = msg.split(b" ")
    can_id = int(can_id, 16)
    data_len = int(data_len, 16)
    return (can_id, data_len, binascii.unhexlify(data_hex[:-2]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("arduino_dev",
                        help="Arduino device. Either path to its /dev file or COMx thing.")
    args = parser.parse_args()

    conn = serial.Serial(args.arduino_dev, 115200)
    print(conn.readline())  # consume the "Starting" message
    #print(arduino_can_recv(conn))
    arduino_can_send(conn, 0x7ff, b"qqqqq")


if __name__ == "__main__":
    main()