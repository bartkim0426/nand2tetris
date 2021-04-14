// pseudo code
// // set variable
// a = RAM[0]
// b = RAM[1]
// c = RAM[2]
// i = 0
// sum = 0
// 
// LOOP:  // a + a + .. + a -> b times
//     if i >= b goto END
//     sum = sum + a
//     i = i + 1
//     c = sum
//     goto LOOP
// 
// END:
//     goto END

@R0   // M = RAM[0]
D=M   // a = RAM[0]
@a    // M = a
M=D   // a = RAM[0]

@R1   // M = RAM[1]
D=M   // b = RAM[1]
@b    // M = b
M=D   // b = RAM[1]

@i   // M = i
M=0  // i = 0
@sum // M = sum
M=0  // sum = 0

(LOOP)
    // if i >= b goto END
    // i >= b -> i-b >= 0
    @b    // M = b
    D=M   // D = b
    @i    // M = i
    D=M-D // D=i-b
    @END
    D;JGE // if i - b > 0 goto END

    // i = i + 1
    @i     // M = i
    M=M+1  // i = i + 1

    // sum = sum + a
    @a    // M = a
    D=M   // D = a
    @sum  // M = sum
    M=M+D // sum = sum + a

    // RAM[2] = sum
    D=M   // D = sum
    @R2   // M = RAM[2]
    M=D   // RAM[2] = sum

    // unconditionally goto LOOP
    @LOOP
    0;JMP

(END)
@END
0;JMP
