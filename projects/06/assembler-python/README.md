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
Reader
  Read asm file
  yield line
end

Parser
  Initialize instructions from input generator

  remove whitespaces
  
  if coments
    ignore
  else
  yield instruction
end
```

- translator

```
Translator
  if field is a-instruction
    return translate_a_instruction(field)
    
  if field is c-instruction
    return translate_c_instruction(field)
end
```

- assembler

```
Assembler
  reader = Reader(xxx.asm)
  parser = Parser(reader)
  
  output_file = xxx.hack
  
  for field in parser:
    binary_value = translator(field)
    write binary_value to output_file
end
```

### test

```
$ python -m unittest tests.py
```

