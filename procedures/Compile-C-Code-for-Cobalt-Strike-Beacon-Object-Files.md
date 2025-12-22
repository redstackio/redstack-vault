---
id: faa80fbf-1788-4702-a3f7-7f2fe2bd24e6
name: Compile-C-Code-for-Cobalt-Strike-Beacon-Object-Files
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:16.791690+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
sub_techniques:
  - '[[sub-techniques/Binary Padding|T1027.001 - Binary Padding]]'
tags:
  - '[[tags/Beacon Object Files]]'
  - '[[tags/Cobalt Strike]]'
  - defense-evasion
  - obfuscation
commands:
  - '[[commands/compile-c-code-visual-studio-cl]]'
  - '[[commands/compile-c-code-mingw-x86]]'
  - '[[commands/compile-c-code-mingw-x64]]'
platforms:
  - Windows
tools:
  - '[[tools/Cobalt Strike]]'
validated: true
---

# Compile-C-Code-for-Cobalt-Strike-Beacon-Object-Files

## Summary

This procedure demonstrates how to compile C source code into object files (.o) that can be loaded and executed within a Cobalt Strike Beacon payload. By embedding custom C code as object files, attackers can evade antivirus detection during post-exploitation, allowing arbitrary code execution without writing full binaries to disk.

## Description

In post-exploitation scenarios, after gaining initial access via a Cobalt Strike Beacon, attackers often need to execute custom code while avoiding detection. This technique compiles C code into an object file, which is then loaded into the Beacon using the `beacon_object` command and executed via `execute_assembly`. This approach obfuscates the payload by avoiding direct binary execution and leverages the Beacon's in-memory capabilities. It is particularly useful for maintaining persistence, privilege escalation, or data exfiltration on Windows targets. The process requires a development environment with C compilers like Visual Studio (cl.exe) or MinGW (gcc variants) and assumes the attacker has Cobalt Strike client access. Success results in an object file ready for Beacon integration, with no disk artifacts beyond the temporary .o file.

## Requirements

1. Cobalt Strike client installed and a live Beacon session established on the target.
2. C source code file (e.g., containing arbitrary code like a simple message box or shell spawn).
3. Windows development environment with either Visual Studio Build Tools (for cl.exe) or MinGW-w64 installed (for gcc cross-compilers).
4. Administrative access on the compilation machine (attacker's system); no special privileges needed on the target beyond the Beacon foothold.

## Defense

- Implement strict application whitelisting (e.g., AppLocker or WDAC) to block unsigned binaries and Cobalt Strike artifacts.
- Deploy endpoint detection and response (EDR) tools that monitor for in-memory code execution and Beacon-like behaviors (e.g., unusual API calls to LoadLibrary or VirtualAlloc).
- Regularly update antivirus signatures and enable behavior-based detection for obfuscated payloads.
- Monitor network traffic for Cobalt Strike C2 patterns and audit compilation tools like cl.exe or gcc for anomalous usage.

## Objectives

1. Compile custom C code into a position-independent object file (.o) compatible with Beacon.
2. Load the object file into an active Cobalt Strike Beacon session.
3. Execute the loaded object file in-memory to perform arbitrary actions on the target.

## Instructions

### Step 1: Prepare the C Source File

**Context**: Create or obtain the C source code you want to execute via Beacon. Ensure it is position-independent (no absolute addresses) and includes necessary headers for Windows API if needed. Save it as a .c file, e.g., custom_payload.c, containing your arbitrary code (e.g., a function to spawn a shell or display a message).

> No command needed here; use a text editor to write the file. Verify the code compiles standalone by testing with a simple main() function first.

### Step 2: Compile Using Visual Studio (cl.exe)

**Context**: Use Microsoft's cl.exe compiler to generate a 32-bit or 64-bit object file. This flag set (/c for compile-only, /GS- to disable buffer security checks) ensures a clean .o file without linking, suitable for Beacon loading. This step produces hello.o (or your specified output) if successful.

**Command** ([[commands/compile-c-code-visual-studio-cl]]):
```cmd
cl.exe /c /GS- $_SOURCE_FILE.c /Fo$_OBJECT_FILE.o
```

> Run this in a Visual Studio Developer Command Prompt. Replace $_SOURCE_FILE with your .c filename (e.g., hello) and $_OBJECT_FILE with the desired output name (e.g., hello). Expected output includes compilation messages ending with no errors, and the file $_OBJECT_FILE.o is created in the current directory (size ~1-10 KB depending on code).

### Step 3: Compile Using MinGW x86 (32-bit)

**Context**: For 32-bit targets, use the i686 MinGW cross-compiler to generate a compatible object file. The -c flag compiles without linking, producing a .o file loadable by Beacon on x86 Windows systems.

**Command** ([[commands/compile-c-code-mingw-x86]]):
```bash
i686-w64-mingw32-gcc -c $_SOURCE_FILE.c -o $_OBJECT_FILE.o
```

> Execute in a terminal with MinGW in PATH. Use placeholders for $_SOURCE_FILE (e.g., hello) and $_OBJECT_FILE (e.g., hello). Success is indicated by no warnings/errors and the creation of $_OBJECT_FILE.o.

### Step 4: Compile Using MinGW x64 (64-bit)

**Context**: For 64-bit targets, employ the x86_64 MinGW variant. This ensures architecture compatibility with modern Windows Beacons, maintaining obfuscation benefits.

**Command** ([[commands/compile-c-code-mingw-x64]]):
```bash
x86_64-w64-mingw32-gcc -c $_SOURCE_FILE.c -o $_OBJECT_FILE.o
```

> Run in a bash-compatible environment (e.g., Git Bash or WSL). Substitute placeholders as needed. Verify by checking file creation and size; errors would indicate syntax issues in the C code.

### Step 5: Load and Execute in Cobalt Strike Beacon

**Context**: With the .o file ready, transfer it to the Beacon session (e.g., via upload command) and load it using Cobalt Strike's built-in Aggressor Script functions. This step assumes a live Beacon; execute to run the custom code in-memory.

> In the Cobalt Strike console, use: `beacon_object $1` where $1 is the path to your .o file, followed by `execute_assembly $2` with the assembly reference. Expected output in Beacon: Confirmation of load (e.g., "Object loaded") and execution results (e.g., output from your C code, like a spawned process PID).
