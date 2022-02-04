class Packet:
    LITERAL = 4
    MIN_PACKET_LEN = 11

    def __init__(self, blob, version, typeID):
        self._blob = blob
        self._version = version
        self._typeID = typeID

    @property
    def blob(self):
        return self._blob

    @blob.setter
    def blob(self, blob):
        self._blob = blob

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, version):
        self._version = version

    @property
    def typeID(self):
        return self._typeID

    @typeID.setter
    def typeID(self, typeID):
        self._typeID = typeID

    def decode(self):
        pass

    @staticmethod
    def build_packet(blob, version, typeID):
        import aoc.day16.literal as li
        import aoc.day16.operation as op

        if typeID == Packet.LITERAL:
            return li.Literal(blob, version, typeID)
        else:
            return op.Operation(blob, version, typeID)
