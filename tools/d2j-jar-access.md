---
id: 5fa6bfd8-7be1-4641-a72e-3f44277071d9
name: d2j-jar-access
type: tool
verified: false
created_at: '2019-08-28T21:17:38.417209+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# d2j-jar-access

## Overview

dex2jar contains following components: dex-reader is designed to read the Dalvik Executable (.dex/.odex) format. It has a light weight API similar with ASM. dex-translator is designed to do the convert job. It reads the dex instruction to dex-ir format, after some optimize, convert to ASM format. d

## Description

dex2jar contains following components:

dex-reader is designed to read the Dalvik Executable (.dex/.odex) format. It has a light weight API similar with ASM.

dex-translator is designed to do the convert job. It reads the dex instruction to dex-ir format, after some optimize, convert to ASM format.

dex-ir used by dex-translator, is designed to represent the dex instruction

dex-tools tools to work with .class files. here are examples: Modify a apk, DeObfuscate a jar

d2j-smali [To be published] disassemble dex to smali files and assemble dex from smali files. different implementation to smali/baksmali, same syntax, but we support escape in type desc “Lcom/dex2jar\t\u1234;”

dex-writer [To be published] write dex same way as dex-reader.
