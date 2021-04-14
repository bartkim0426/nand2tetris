// pseudo code
// (RESET)
// addr = SCREEN
// kbd = KBD
// 
// (KBDCHECK)
// if kbd > 0 goto BLACK
// if kbd == 0 goto WHITE
// 
// WHITE:
//     filled = 0
//     goto CHANGE
// 
// BLACK:
//     filled = -1
//     goto CHANGE
// 
// CHANGE:
//     addr = filled
//     addr = addr + 1
//     d = kbd - screen
// 
//     if d = 0 goto RESET
//     goto CHANGE

(RESET)
    @SCREEN       // M = screen (RAM[16384]), A = 16384
    D=A           // D = 16384
    @screen_count // M = screen_count
    M=D           // screen_count = 16384


(KBC_CHECK)
    @KBD          // M = KBD (RAM[24576]), A = 24576
    D=M           // D = KBD
    @BLACK
    D;JGT         // if KBD > 0 goto BLACK
    @WHITE
    D;JEQ         // if KBD == 0 goto WHITE

    @KBD_CHECK
    0;JMP         // infinitly check keyboard


(BLACK)
    @filled       // M = filled
    M=-1          // filled = -1
    @CHANGE_SCREEN
    0;JMP         // unconditionally goto CHANGE_SCREEN


(WHITE)
    @filled       // M = filled
    M=0           // filled = 0
    @CHANGE_SCREEN
    0;JMP         // unconditionally goto CHANGE_SCREEN


(CHANGE_SCREEN)
    @filled       // M = filled
    D=M           // D = filled (-1 for BLACK, 0 for WHITE)

    @screen_count // M = screen_count, A = 16384 (address)
    A=M           // A =16384 (이게 필요한지 테스트)
    M=D           // RAM[16384] = filled (-1 or 0)

    @screen_count // M = screen_count (RAM[0])
    D=M+1         // D = 16384 + 1

    @KBD          // A = 24576
    D=A-D         // D = 24576 - (16384 + 0)
                  // D = 8191, 8190, 8189, ... 0

    @screen_count // M = screen_count
    M=M+1         // M = RAM[0] + 1 = 16384 + 1

    @RESET        // if D == 0 goto RESET
    D;JEQ

    @CHANGE_SCREEN       // unconditionally LOOP in CHANGE
    0;JMP
