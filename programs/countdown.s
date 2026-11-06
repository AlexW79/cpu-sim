; countdown.s - count R1 down from 5 to 0
        MOV R1, #5
loop:   SUB R1, R1, #1      ; R1 = R1 - 1
        CMP R1, #0          ; is R1 equal to 0?
        BNE loop            ; if not, go back to loop
        HALT