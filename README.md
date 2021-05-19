# Nand2tetris

Project for creating [nand2tetris](https://www.nand2tetris.org/) HECK computer from the bottom.

## Project

### 1. Boolean functions and gate logic

All files is in [projects/01](./projects/01/) directory with `name.hdl`

- And, Or, Not, Xor
- Mux, Dmux
- And16, Dmux4Way, Mux16, Mux4Way16, Mux8Way16, Or16, Or8Way

### 2. Boolean arthmetic and the alu
- Add16, Inc16, Or16Way
- [HalfAdder](./projects/02/HalfAdder.hdl), [FullAdder](./projects/02/FullAdder.hdl)
- [ALU](./projects/02/ALU.hdl)

### 3. Memory
- [Bit](./projects/03/Bit.hdl)
- [PC](./projects/03/PC.hdl)
- [RAM8](./projects/03/RAM8.hdl), [RAM64](./projects/03/RAM64.hdl), 
- [RAM512](./projects/03/RAM512.hdl), [RAM4K](./projects/03/RAM4K.hdl), [RAM16K](./projects/03/RAM16K.hdl)
- [Register](./projects/03/Register.hdl)

### 4. Machine Language
- [Fill](./projects/04/Fill.asm): fill screen to black when pressing key
- [Mult](./projects/04/Mult.asm): multiply input register

### 5. Computer Architecture
- [Memory](./projects/05/Memory.hdl)
- [CPU](./projects/05/CPU.hdl)
- [Computer](./projects/05/Computer.hdl)

### 6. Assembly Languages and Assemblers


## Summary

- [01. Boolean functions and gate logic](https://github.com/bartkim0426/TIL/blob/master/nand2tetris/01-boolean-functions.md)
- [02. Boolean arthmetic and the alu](https://github.com/bartkim0426/TIL/blob/master/nand2tetris/02-boolean-arthmetic-and-the-alu.md)
- [03. Memory](https://github.com/bartkim0426/TIL/blob/master/nand2tetris/03-memory.md)
- [04. Machine Language](https://github.com/bartkim0426/TIL/blob/master/nand2tetris/04-Machine-Languages.md)
- [05. Computer Architecture](https://github.com/bartkim0426/TIL/blob/master/nand2tetris/05.-Computer-Architecture.md)
- [06 Assembly Languages and Assemblers](https://github.com/bartkim0426/TIL/blob/master/nand2tetris/06.-Assembly-Languages-and-Assemblers.md)
