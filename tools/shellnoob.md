---
id: 3b13d2e1-5f78-46ad-a103-21f39a48bf9c
name: shellnoob
type: tool
verified: false
created_at: '2019-08-28T21:17:29.237387+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# shellnoob

## Overview

Writing shellcodes has always been super fun, but some parts are extremely boring and error prone. Focus only on the fun part, and use ShellNoob!Features: convert shellcode between different formats and sources. Formats currently supported: asm, bin, hex, obj, exe, C, python, ruby, pretty, safeasm,

## Description

Writing shellcodes has always been super fun, but some parts are extremely boring and error prone. Focus only on the fun part, and use ShellNoob!Features:

convert shellcode between different formats and sources. Formats currently supported: asm, bin, hex, obj, exe, C, python, ruby, pretty, safeasm, completec, shellstorm. (All details in the “Formats description” section.)

interactive asm-to-opcode conversion (and viceversa) mode. This is useful when you cannot use specific bytes in the shellcode and you want to figure out if a specific assembly instruction will cause problems.

support for both ATT & Intel syntax. Check the –intel switch.

support for 32 and 64 bits (when playing on x86_64 machine). Check the –64 switch.

resolve syscall numbers, constants, and error numbers (now implemented for real! :-)).

portable and easily deployable (it only relies on gcc/as/objdump and python). It is just one self-contained python script, and it supports both Python2.7+ and Python3+.

in-place development: you run ShellNoob directly on the target architecture!

built-in support for Linux/x86, Linux/x86_64, Linux/ARM, FreeBSD/x86, FreeBSD/x86_64.

“prepend breakpoint” option. Check the -c switch.

read from stdin / write to stdout support (use “-” as filename)

uber cheap debugging: check the –to-strace and –to-gdb option!

Use ShellNoob as a Python module in your scripts! Check the “ShellNoob as a library” section.

Verbose mode shows the low-level steps of the conversion: useful to debug / understand / learn!

Extra plugins: binary patching made easy with the –file-patch, –vm-patch, –fork-nopper options! (all details below)
