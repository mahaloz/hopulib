import struct


#
# CONVERTERS:
# - bytes to int and back
# - bytes fit into exact bit sizes: 8, 16, 32, 64
# - byte string converted to int
#

def unpack8(barray, le=True, signed=False):
    fmt = f"{'<' if le else '>'}{'b' if signed else 'B'}"
    return struct.unpack(fmt, barray)[0]


def unpack16(barray, le=True, signed=False):
    fmt = f"{'<' if le else '>'}{'h' if signed else 'H'}"
    return struct.unpack(fmt, barray)[0]


def unpack32(barray, le=True, signed=False):
    fmt = f"{'<' if le else '>'}{'i' if signed else 'I'}"
    return struct.unpack(fmt, barray)[0]


def unpack64(barray, le=True, signed=False):
    fmt = f"{'<' if le else '>'}{'q' if signed else 'Q'}"
    return struct.unpack(fmt, barray)[0]


def unpack(barray: bytes, size=None, le=True, signed=False) -> int:
    """
    Will attempt to unpack a series of bytes into an integer. Works for
    fixed sizes and unknown sizes.

    >>> unpack(b"\xff", signed=True)
    >>> -1
    >>> unpack(b"\xad\xde")
    >>> 57005

    :param barray:
    :param size:    Optional size in bits
    :param le:      True for little endian, False for big
    :param signed:
    :return:
    """
    if not size:
        bits = len(barray) * 8
        if bits > 64:
            size = None
        elif bits > 32:
            size = 64
        elif bits > 16:
            size = 32
        elif bits > 8:
            size = 16
        else:
            size = 8
    else:
        bsize = size // 8
        pad_byte = b"\xff" if signed else b"\x00"
        barray = barray.ljust(bsize, pad_byte) if le else barray.rjust(bsize, pad_byte)

    unpack_map = {
        8: unpack8,
        16: unpack16,
        32: unpack32,
        64: unpack64,
        # is a byte str
        None: bytes_to_int,
    }

    unpacker = unpack_map.get(size, None)
    if not unpacker:
        raise Exception("Attempting unpack on a non-supported size")

    return unpacker(barray, le=le, signed=signed)


def pack8(num, le=True):
    signed = num < 0
    fmt = f"{'<' if le else '>'}{'b' if signed else 'B'}"
    return struct.pack(fmt, num)


def pack16(num, le=True):
    signed = num < 0
    fmt = f"{'<' if le else '>'}{'h' if signed else 'H'}"
    return struct.pack(fmt, num)


def pack32(num, le=True):
    signed = num < 0
    fmt = f"{'<' if le else '>'}{'i' if signed else 'I'}"
    return struct.pack(fmt, num)


def pack64(num, le=True):
    signed = num < 0
    fmt = f"{'<' if le else '>'}{'q' if signed else 'Q'}"
    return struct.pack(fmt, num)


def pack(number: int, size=None, le=True) -> bytes:
    """
    Packs an integer into a byte array. Will automatically detect if signed and create a signed
    packing if needed. Will also try to return the smallest possible amount of bytes if size is
    not specifed.

    >>> pack(-1)
    >>>  b'\xff'
    >>> pack(-1, size=64)
    >>>  b'\xff\xff\xff\xff\xff\xff\xff\xff'
    >>> pack(0x1337, size=32, le=False)
    >>> b'\x00\x00\x137'

    :param number:
    :param size:    Optional size in bits
    :param le:      True for little endian, False for big
    :return:
    """

    if not size:
        bits = number.bit_length()
        if bits > 64:
            size = None
        elif bits > 32:
            size = 64
        elif bits > 16:
            size = 32
        elif bits > 8:
            size = 16
        else:
            size = 8

    pack_map = {
        64: pack64,
        32: pack32,
        16: pack16,
        8: pack8,
        # int is huge!
        None: int_to_bytes,
    }
    packer = pack_map.get(size, None)
    if not packer:
        raise Exception("Attempting pack on a non-supported size")

    return packer(number, le=le)


def bytes_to_int(barray: bytes, le=True, **kwargs) -> int:
    """
    >>> bytes_to_int(b"this is my long string", le=True)
    >>> 38698242349707737316460680542623506145837885271140468

    :param barray:
    :param le:      True for little endian, False for big
    :return:
    """
    return int.from_bytes(barray, "little" if le else "big")


def int_to_bytes(num: int, le=True, **kwargs) -> bytes:
    """
    >>> int_to_bytes(0x676e6972747320676e6f6c20796d2073692073696874, le=True)
    >>> b'this is my long string'

    :param num:
    :param le:      True for little endian, False for big
    :return:
    """
    bits = num.bit_length()
    bsize = bits // 8 + 1
    return num.to_bytes(bsize, "little" if le else "big")

