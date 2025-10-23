---
id: db375fe9-0830-4016-b90d-2f711533e542
name: Immunity Debugger Mona Plugin
type: cheatsheet
verified: true
created_at: '2019-09-21T00:36:54.672816+00:00'
updated_at: '2023-05-30T20:11:07.794233+00:00'
---

# Immunity Debugger Mona Plugin

**Status**: ✓ Verified

## Description

Mona is a plugin for Immunity Debugger, here are a list of commands to help with exploit development







**Command** ([[mona Config Working Directory]]):

```bash
!mona config -set workingfolder c:\$_PATH\%p
```





Cyclic patterns help you calculate offsets when attempting a buffer overflow. By creating a pattern then supplying the pattern as the payload, offsets can be identified with additional scripts.





**Command** ([[mona Create Unique Cylic Pattern]]):

```bash
!mona pc $_LENGTH
```





Use the value overwritten into key registers to identify the offset, and number of bytes needed to overwrite the target.





**Command** ([[mona Calculate Unique Pattern Offset to EIP]]):

```bash
!mona pattern_offset $_HEX_PATTERN
```





Using "-r" searches the process binary and all DLL's loaded in memory at execution time for the instruction. The result is stored in c:\logs\process-name\jmp.txt





**Command** ([[mona Search for a JMP to ESP Instruction]]):

```bash
!mona jmp -r esp
```







**Command** ([[mona Find Opcode Instruction to JMP ESP]]):

```bash
!mona find -s "\xff\xe4"
```







**Command** ([[mona Generate Byte Array excluding known badchars]]):

```bash
!mona bytearray -cpb "\x00\x0a"
```







**Command** ([[mona Generate egghunter]]):

```bash
!mona egg -t w00t
```






