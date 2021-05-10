class SymbolTable(dict):
    """
    Class responsible for holding pre-defined symbols, and setting new symbols and variables.
    """

    def __init__(self):
        super().__init__
        self.update({
            # Registers R0 to R15
            'R0': 0,
            'R1': 1,
            'R2': 2,
            'R3': 3,
            'R4': 4,
            'R5': 5,
            'R6': 6,
            'R7': 7,
            'R8': 8,
            'R9': 9,
            'R10': 10,
            'R11': 11,
            'R12': 12,
            'R13': 13,
            'R14': 14,
            'R15': 15,

            # Screen Map
            'SCREEN': 16384,

            # Keyboard Input
            'KBD': 24576,

            # Additional
            'SP': 0,
            'LCL': 1,
            'ARG': 2,
            'THIS': 3,
            'THAT': 4
        })

    def set_address(self, symbol, address):
        """
        Set address of symbol (label or variable).
        """
        self[symbol] = address
    
    def get_address(self, symbol):
        """
        Return address of symbol, or -1 if symbol not found in SymbolTable.
        """
        if symbol in self:
            return self[symbol]
        return -1
