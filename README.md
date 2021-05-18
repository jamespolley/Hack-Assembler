# Hack-Assembler
Hack-Assembler is a machine language assembler for the 16-bit Hack assembly language. This is the final project in part 1 of the course [Build a Modern Computer from First Principles: From Nand to Tetris](https://www.coursera.org/learn/build-a-computer).

## Description
Hack-Assembler accepts a program written in the Hack Assembly Language as a *.asm* file, converts it into Hack Machine Language (binary), and finally writes the assembled code to a *.hack* file of the same name (creates file if necessary).

The assembler is implemented in the following components:
1. **HackAssembler.py**: Main class. Drives the assembly process. Handles reading of the assembly file (*.asm*) and writing the of hack file (*.hack*).
2. **SymbolTable.py**: Class responsible for holding pre-defined symbols, and setting new symbols and variables.
3. **Parser.py**: Class responsible for formatting, identifying symbol types, and handling conversion of instructions.
4. **Code.py**: Class responsible for converting assembly instructions into binary code.

For more information about the Hack Assembly Language, the Hack Machine Language, and this project's specifications, see [The Elements of Computer Systems: Chapter 6](https://b1391bd6-da3d-477d-8c01-38cdf774495a.filesusr.com/ugd/44046b_89a8e226476741a3b7c5204575b8a0b2.pdf).


## Example Usage
```bash
$ python HackAssembler.py assets\Add.asm
```
