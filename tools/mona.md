---
id: c4796d49-c5df-402f-ab40-dab968fd6b3f
name: mona
type: tool
verified: true
created_at: '2020-03-07T02:03:16.469422+00:00'
updated_at: '2023-05-30T01:08:15.809339+00:00'
commands:
- '[[mona Search for a JMP to ESP Instruction]]'
platforms:
- Windows
tags:
- '[[exploit dev]]'
---

# mona

**Status**: ✓ Verified

## Overview

Immunity debugger plugin made by Corelan with a number of tools which aid in exploitation and debugging.

Popular mona tools: egg - create an egghunter routine find - search for strings, bytes, instructions or files in files and memory findmsp - search memory for all instances or references to a cy

## Description

# Description

Immunity debugger plugin made by Corelan with a number of tools which aid in exploitation and debugging.

Popular mona tools:



- egg - create an egghunter routine

- find - search for strings, bytes, instructions or files in files and memory

- findmsp - search memory for all instances or references to a cyclic pattern

- heap - list heaps available in the process

- jmp - search for pointers that will lead to the code located at the address pointed by a given register

- jop - search for gadgets that can be used in Jump Orientated Programming

- modules - show information on loaded modules

- pattern_create/pattern_offset - generate a cyclic pattern find the offsets

- rop - build ROP gadgets

- seh - search for pointers to routines that will lead to code execution



# Example



{{EMBEDDED_COMMAND_1abf33ab-e658-4148-a552-f6a34a3582d3}}



# Installation

## Install on Windows

1. Download the latest version of mona.py here: [https://github.com/corelan/mona](https://github.com/corelan/mona)
2. Copy mona.py to Immunity's "PyCommands" directory (usually C:\Program Files (x86)\Immunity Inc\Immunity Debugger\PyCommands)







## Platforms

- Windows

## Commands (1)

- [[mona Search for a JMP to ESP Instruction]]

## Tags

- [[exploit dev]]


