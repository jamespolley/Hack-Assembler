class Code:
    """
    Class responsible for converting assembly instructions into binary code.
    """

    # Code parts for C-Instruction
    dest_codes = ['', 'M', 'D', 'MD', 'A', 'AM', 'AD', 'AMD']
    comp_codes = {'0': '0101010', '1': '0111111', '-1':'0111010', 'D':'0001100', 'A': '0110000', '!D': '0001101', '!A': '0110001', '-D': '0001111', '-A': '0110011', 'D+1': '0011111', 'A+1': '0110111', 'D-1': '0001110', 'A-1': '0110010', 'D+A': '0000010', 'D-A': '0010011', 'A-D':'0000111', 'D&A': '0000000', 'D|A': '0010101', 'M': '1110000', '!M': '1110001', '-M': '1110011', 'M+1': '1110111', 'M-1': '1110010', 'D+M': '1000010', 'D-M': '1010011', 'M-D': '1000111', 'D&M': '1000000', 'D|M': '1010101'}
    jump_codes = ['', 'JGT', 'JEQ', 'JGE', 'JLT', 'JNE', 'JLE', 'JMP']

    @staticmethod
    def _binary(num):
        """
        Convert integer string into binary string.
        """
        return bin(int(num))[2:]
    
    def a_instruction(self, address):
        """
        Convert assembly language A-instruction string into binary string.
        """
        return '0' + self._binary(address).zfill(15)

    def c_instruction(self, dest, comp, jump):
        """
        Convert assembly language C-instruction string into binary string.
        """
        dest_code = str(self._binary(self.dest_codes.index(dest)).zfill(3))
        comp_code = self.comp_codes[comp]
        jump_code = str(self._binary(self.jump_codes.index(jump)).zfill(3))
        return '111' + comp_code + dest_code + jump_code
