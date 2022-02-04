from ..file_reader import FileReader
import aoc.day16.packet as pa
from .util import decode_typeID, decode_version, hex_to_binary
import os

class PacketDecoder:
    def __init__(self, hex):
        self._hex = hex
        self._binary = hex_to_binary(hex) 
        self._sum_of_versions = None
        self._packets = []

    @property
    def hex(self):
        return self._hex

    @property
    def binary(self):
        return self._binary

    @property
    def sum_of_versions(self):
        return self._sum_of_versions

    @sum_of_versions.setter
    def sum_of_versions(self, sum_of_versions):
        self._sum_of_versions = sum_of_versions

    @property
    def packets(self):
        return self._packets

    @packets.setter
    def packets(self, packets):
        self._packets = packets

    def decode(self, blob):
        # import pdb
        # pdb.set_trace()

        if len(blob) >= pa.Packet.MIN_PACKET_LEN:
            typeID = decode_typeID(blob)
            version = decode_version(blob)

            packet = pa.Packet.build_packet(blob, version, typeID)
            self.packets.append(packet)

            remaining_blob = packet.decode()
            if remaining_blob != None:
                self.decode(remaining_blob)

if __name__ == "__main__":
    fr = FileReader(os.path.dirname(__file__) + '/input.txt')
    hex_blob = fr.lines()[0]
    pd = PacketDecoder('A0016C880162017C3686B18A3D4780') # 'A0016C880162017C3686B18A3D4780')
    pd.decode(pd.binary)
    sum_of_versions = sum([p.version for p in pd.packets])
    print(f'sum of versions: {sum_of_versions}')
