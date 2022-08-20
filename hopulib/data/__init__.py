import struct


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


def unpack(barray, size, le=True, signed=False):
    unpack_map = {
        8: unpack8,
        16: unpack16,
        32: unpack32,
        64: unpack64
    }

    unpacker = unpack_map.get(size, None)
    if not unpacker:
        raise Exception("Attempting pack a non-supported size")

    return unpacker(barray, le=le, signed=signed)

def pack8(num, le=True):
    """
    TODO
    :param num:
    :param le:
    :return:
    """

    signed = num < 0
    fmt = ""


def pack(number, size, le=True, signed=False):
    """
    TODO
    :param number:
    :param size:
    :param le:
    :param signed:
    :return:
    """
    pack_map = {
    }

    packer = pack_map.get(size, None)
    if not packer:
        raise Exception("Attempting pack a non-supported size")

    return packer()
