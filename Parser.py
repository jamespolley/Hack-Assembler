import re
from Code import Code

class Parser():
    """
    Class responsible for formatting, identifying symbol type, and handling conversion of instructions.
    """

    # Types of Instructions
    A_INSTRUCTION = 0
    C_INSTRUCTION = 1
    L_INSTRUCTION = 2

    # Whitespace & Comments Regular Expression
    RE_FORMAT = r"(\s)|(//.*)"
    
    # Symbol & A-Instruction (Address) Regular Expressions
    RE_SYMBOL = r"[a-zA-Z_\$\.:][a-zA-Z0-9_\$\.:]*"
    RE_A_INSTRUCTION = re.compile(r"^@(\d*|" + RE_SYMBOL + ")$")

    # Parts of C-Instruction & C-Instruction (Computation) Regular Expressions
    RE_DEST = r"(?:(M|D|MD|A|AM|AD|AMD)=)?"
    RE_COMP = (
        r"(0|1|-1|D|A|!D|!A|-D|-A|D\+1|A\+1|D-1|A-1|D\+A|D-A|A-D|D&A|D\|A|"
        r"M|!M|-M|M\+1|M-1|D\+M|D-M|M-D|D&M|D\|M)")
    RE_JUMP = r"(?:;(JGT|JEQ|JGE|JLT|JNE|JLE|JMP))?"
    RE_C_INSTRUCTION = re.compile(r"^%s%s%s$" % (RE_DEST, RE_COMP, RE_JUMP))

    # L-Instruction (Label) Regular Expression
    RE_L_INSTRUCTION = re.compile(r"^\(" + RE_SYMBOL + r"\)$")

    def __init__(self):
        self.code = Code()

    def format_line(self, line):
        """
        Remove whitespace and comments from line.
        """
        formatted_line = re.sub(self.RE_FORMAT, '', line)
        if len(formatted_line) > 0:
            return formatted_line
        return False
    
    def instruction_type(self, instruction):
        """
        Identify instruction type, and return corresponding integer constant.
        """
        if re.match(self.RE_A_INSTRUCTION, instruction):
            return self.A_INSTRUCTION
        if re.match(self.RE_C_INSTRUCTION, instruction):
            return self.C_INSTRUCTION
        if re.match(self.RE_L_INSTRUCTION, instruction):
            return self.L_INSTRUCTION
        return

    def a_instruction(self, address):
        """
        Convert assembly A-instruction to binary.
        """
        return self.code.a_instruction(address)

    def c_instruction(self, instruction):
        """
        Convert assembly C-instruction to binary.
        """
        dest = self._get_dest(instruction)
        comp = self._get_comp(instruction)
        jump = self._get_jump(instruction)
        return self.code.c_instruction(dest, comp, jump)

    def _get_dest(self, instruction):
        """
        Return 'dest' part of C-instruction, or an empty string if missing.
        """
        return re.search(self.RE_DEST, instruction)[0][:-1] or ''
    
    def _get_comp(self, instruction):
        """
        Return 'comp' part of C-instruction.
        
        Note: To be valid, C-instruction must contain this part.
        """
        return instruction.split('=')[-1].split(';')[0]
    
    def _get_jump(self, instruction):
        """
        Return 'jump' part of C-instruction, or a empty string if missing.
        """
        if ';' in instruction:
            return instruction.split(';')[1]
        return ''