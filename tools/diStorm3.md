---
id: 0ae46660-1add-455b-b9b9-e437d37be3c2
name: diStorm3
type: tool
verified: false
created_at: '2019-08-28T21:17:24.506769+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# diStorm3

## Overview

diStorm is a lightweight, easy-to-use and fast decomposer library. diStorm disassembles instructions in 16, 32 and 64 bit modes. Supported instruction sets: FPU, MMX, SSE, SSE2, SSE3, SSSE3, SSE4, 3DNow! (w/ extensions), new x86-64 instruction sets, VMX, AMD’s SVM and AVX!. The output of new interf

## Description

diStorm is a lightweight, easy-to-use and fast decomposer library. diStorm disassembles instructions in 16, 32 and 64 bit modes. Supported instruction sets: FPU, MMX, SSE, SSE2, SSE3, SSSE3, SSE4, 3DNow! (w/ extensions), new x86-64 instruction sets, VMX, AMD’s SVM and AVX!. The output of new interface of diStorm is a special structure that can describe any x86 instruction, this structure can be later formatted into text for display too. diStorm is written in C, but for rapidly use, diStorm also has wrappers in Python/Ruby/Java and can easily be used in C as well. It is also the fastest disassembler library!. The source code is very clean, readable, portable and platform independent (supports both little and big endianity). diStorm solely depends on the C library, therefore it can be used in embedded or kernel modules. Note that diStorm3 is backward compatible with the interface of diStorm64 (however, make sure you use the newest header files).




