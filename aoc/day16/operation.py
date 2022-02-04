import aoc.day16.packet as pa

class Operation(pa.Packet):
    # LTI stands for Length Type Id
    LTI_IDX = 6
    LTI_0_LEN = 15
    LTI_1_LEN = 11

    def __init__(self, blob, version, typeID):
        super().__init__(blob, version, typeID)
        self._length_type_id = int(blob[Operation.LTI_IDX])
    
    @property
    def length_type_id(self):
        return self._length_type_id

    @length_type_id.setter
    def length_type_id(self, length_type_id):
        self._length_type_id = length_type_id

    def decode(self):
        field_start = Operation.LTI_IDX + 1

        if self.length_type_id == 0:
            subpacket_start = field_start + Operation.LTI_0_LEN
        elif self.length_type_id == 1:
            subpacket_start = field_start + Operation.LTI_1_LEN
        else:
            raise ValueError('length type id is not a valid number: must be 1 or 0')

        return self.blob[subpacket_start:]
