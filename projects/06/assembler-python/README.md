# Hack language assembler with python

Assembler for translate Hack language to machine code

For More information, check [here](https://github.com/bartkim0426/TIL/blob/master/nand2tetris/06.-Assembly-Languages-and-Assemblers.md)

## Design

### modules
- Parser
- Code
- SymbolTable
- Main

### implementation
- Create simple Parser without symbol
- Create Code translator
- Create symbol translator function
- Merge symbol function into parser

### usage

```
$ python assembler.py xxx.asm
```

### Pseudocode

- parser

```
Parser
  Initialize instructions from input generator

  remove whitespaces
  
  if coments
    ignore
  else
  yield instruction
```

- translator

```
Translator
  Initialize 
```

### test

```
$ python -m unittest tests.py
```

