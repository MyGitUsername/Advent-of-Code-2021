# from .packet import Packet
import aoc.day16.packet as pa
from .util import binary_to_decimal
# from .packet_decoder import PacketDecoder

class Literal(pa.Packet):
    DATA_IDX = 6
    LAST_GROUP_PREFIX = 0
    GROUP_LEN = 5

    def __init__(self, blob, version, typeID):
        super().__init__(blob, version, typeID)
        self._value = None 

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def decode(self):
        val = ''
        remaining_blob = ''
        for i in range(Literal.DATA_IDX, len(self.blob), Literal.GROUP_LEN):
            prefix = int(self.blob[i])
            val += self.blob[i + 1: i + Literal.GROUP_LEN]

            if prefix == Literal.LAST_GROUP_PREFIX:
                remaining_blob = self.blob[i + Literal.GROUP_LEN:]
                self.value = binary_to_decimal(val)
                break 

        return remaining_blob


