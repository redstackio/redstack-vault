---
type: code
language: powershell
verified: true
platforms:
  - Windows
tags:
  - shellcode
  - dcom
  - injection
validated: true
---

# Invoke-Excel4DCOM64-Shellcode-Injection

## Code

```powershell
# Full script available at: https://gist.github.com/Philts/85d0f2f0a1cc901d40bbb5b44eb3b4c9
# Invoke-Excel4DCOM64.ps1 - Injects shellcode into remote excel.exe via Excel 4.0 macros over DCOM
# Usage: .\Invoke-Excel4DCOM64.ps1 -ComputerName TARGET -Shellcode (Get-Content shellcode.bin -Encoding Byte)
```

## Description

This PowerShell script exploits DCOM to remotely instantiate 64-bit Excel, executes an Excel 4.0 (XLM) macro for memory allocation, and injects provided shellcode into the Excel process for execution. Designed for advanced payload delivery in red team operations targeting Windows domains with Office.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $ComputerName | Target remote computer | 'TARGET-PC' |
| $Shellcode | Byte array of shellcode to inject | @(0xFC, 0x48, ...) |
| $Proxy | Optional proxy for evasion | 'http://127.0.0.1:8080' |

## Usage

Download the script and execute with target details and shellcode (e.g., from msfvenom). Used in lateral movement after initial access; pairs with Invoke-ExShellcode for triggering. Deliver via existing foothold or phishing.

## Detection

- Monitor for remote Excel instantiations via DCOM (Event ID 10000 in DCOM logs).
- Sysmon events for excel.exe memory allocations or injections (Rule 10: ProcessAccess).
- EDR alerts on XLM macro execution or unusual PowerShell-DCIM activity.

## Related

- [[procedures/DCOM-Office-Remote-Code-Execution]]
