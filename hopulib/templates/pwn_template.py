#!/usr/bin/python3
from pwn import *
import re
import sys
import itertools

# connection parameter setup
HOST, PORT = '192.168.0.1', 1337
context.terminal = ["tmux", "splitw", "-h"]
context.update(log_level='debug')

# run parameters
DEBUG = True
PRELOAD = False

def main():
    args = ["./binary"]
    if (PRELOAD):
        libc_loc = "./libc"
        p = process(args, env={"LD_PRELOAD": libc_loc}
    else:
        p = process(args)
    else:
            p = remote(HOST, PORT)

            # start pwn process
            proc = PWNProcess(p)

    # Useful commands:
    # ============================
    #
    #   LIBC & ELF Manipulation
    #   =======================
    #   libc = ELF("./libc-generic.so")
    #   elf = ELF("./generic_binary")
    #   elf.got['function'] #-> returns addr
    #   system = libc.symbols['system'] #-> returns addr of symbol
    #   binsh = libc.search('/bin/sh').next() #-> returns addr of str
    #
    #   Proccess Manip & DBG
    #   =======================
    #   gdb.attach(p, '''   #attach to the proc, p
    #       set follow-fork-mode child
    #       break *0x08048099
    #       continue
    #       ''')
    #
    #   p.sendline(line)
    #   p.recv(1024)
    #   p.revcuntil("thing")
    #   p.sendlineafter("recved", "wanttosend")
    #
    #   Pretty Printing & Bytes
    #   =======================
    #   p64(0xdeadbeef) #int to bytes
    #   u64("\xef\xbe\xad\xde") #bytes to int
    #   log.success("string")
    #   log.info("string")

if __name__ == '__main__':
    main()