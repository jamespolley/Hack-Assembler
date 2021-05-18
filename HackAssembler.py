import sys
from SymbolTable import SymbolTable
from Parser import Parser


class HackAssembler:
    """
    Main class of Hack Assembler. Drives the assembly process. Handles reading of the assembly file and writing of the hack file.
    """

    def __init__(self):
        self.variable_address = 16
        self.symbol_table = SymbolTable()
        self.parser = Parser()
    
    def _get_address(self, line):
        """
        Return address value of instruction. Set new variable if necessary.
        """
        value = line[1:]
        if value.isdigit():
            return value
        address = self.symbol_table.get_address(value)
        if address < 0:
            self.symbol_table.set_address(value, self.variable_address)
            address = self.variable_address
            self.variable_address += 1
        return address
    
    def _get_hack_file(self, asm_file):
        """
        Return file name of '.hack' file, to which assembled binary code will be written.
        """
        return asm_file.replace('.asm', '.hack')
    
    def assemble_part_1(self, asm_file):
        """
        First pass of assembly process. Remove whitespace and comments. Determine memory locations of labels.
        """
        formatted_file = []
        current_index = 0
        for line in asm_file:
            formatted_line = self.parser.format_line(line)
            if formatted_line:
                instruction_type = self.parser.instruction_type(formatted_line)
                if instruction_type == self.parser.L_INSTRUCTION:
                    self.symbol_table.set_address(formatted_line[1:-1], current_index)
                else:
                    formatted_file.append(formatted_line)
                    current_index += 1
        return formatted_file

    def assemble_part_2(self, formatted_file, hack_file):
        """
        Second pass of assembly process. Generate machine code. Write to file.
        """
        with open(hack_file, 'w', encoding='utf-8') as hack_file:
            for line in formatted_file:
                instruction_type = self.parser.instruction_type(line)
                if instruction_type == self.parser.A_INSTRUCTION:
                    address = self._get_address(line)
                    assembled_line = self.parser.a_instruction(address)
                    hack_file.write(assembled_line + '\n')
                else:
                    assembled_line = self.parser.c_instruction(line)
                    hack_file.write(assembled_line + '\n')          

    def assemble(self, asm_file):
        """
        Main assembly method.
        """
        hack_file = self._get_hack_file(asm_file)
        with open(asm_file, 'r', encoding='utf-8') as asm_file:
            formatted_file = self.assemble_part_1(asm_file)
            self.assemble_part_2(formatted_file, hack_file)


def main():
    """
    Handle command line input. Start assembly process.
    """
    if len(sys.argv) !=2:
        print(
            'Error in usage. Please enter a command in the following format:\n    python HackAssembler.py [AssemblerFile.asm]')
        return

    asm_file = sys.argv[1]
    if not asm_file.endswith(".asm"):
        # print('Error with file type. File must end with ".asm"')
        # return Exception('Invalid file type. Must end with ".asm"')
        return
    
    hack_assembler = HackAssembler()

    try:
        hack_assembler.assemble(asm_file)
    except:
        print("Invalid input")
        # Exception('Invalid input')
        pass
    
if __name__ == '__main__':
    main()