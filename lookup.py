class lookup:
    """Stores the lookup table for wire color/stars/etc."""

    def __init__(self):
        self.lookuptable = {}
        with open("lookuptable.txt") as file:
            content = file.read()
        # The table associated with the bomb manual version 1 r.3 given on page 13 shows that

        self.lookuptable = {'{0:08b}'.format(i): self.__str_to_bool(content[i]) for i in range(2 ** 7)}

        # for i in range(2**7):
        #   self.lookuptable[BitVector(intVal = i)] = self.__str_to_bool(content[i])

    def lookup(self, bitstr):
        return self.lookuptable[bitstr]

    def __str_to_bool(self, char):
        if char == "0":
            return False
        if char == "1":
            return True
