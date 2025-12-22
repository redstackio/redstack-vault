---
type: code
language: powershell
verified: true
tags:
  - credential-access
  - file-search
  - looting
platforms:
  - Windows
validated: true
---

# PowerShell-Windows-Password-File-Search-Script

## Code

```powershell
cd C:\ & findstr /SI /M "password" *.xml *.ini *.txt
findstr /si password *.xml *.ini *.txt *.config 2>nul >> results.txt
findstr /spin "password" *.*
```

## Description

This PowerShell script performs a multi-stage search for password strings in files on the Windows C: drive. It starts with a root-level filename scan, appends content matches from config files to results.txt, and ends with a recursive full-filesystem search with line numbers. Designed for post-exploitation credential looting to identify plaintext passwords in configs or documents.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| results.txt | Output file for appended matches (hardcoded; modify script to parameterize) | results.txt |
| "password" | Search term (appears multiple times; can be replaced with regex patterns like "pass|key") | password |

## Usage

Execute in a PowerShell session on a compromised Windows host with read access to C:\. Run as: powershell -ExecutionPolicy Bypass -Command "<paste script>". Review results.txt for extracted credentials, then use tools like hashcat for cracking if hashes are found. Commonly chained after initial access in privilege escalation workflows.

## Detection

- Monitor PowerShell logs for findstr executions (Module Logging, Script Block Logging).
- File access audits for mass reads on config files (Event ID 4663).
- Suspicious file creation like results.txt in temp directories.
- EDR alerts on recursive file searches from non-admin processes.

## Related

- [[procedures/Windows-Password-Looting-via-File-Contents-Search]]
