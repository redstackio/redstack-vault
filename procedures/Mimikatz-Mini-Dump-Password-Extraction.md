---
type: procedure
verified: true
submitted: false
created_at: '2024-01-01T00:00:00Z'
updated_at: '2024-01-01T00:00:00Z'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Credential Dumping]]'
sub_techniques: []
tags:
  - mini-dump
  - windows-mimikatz
  - credential-access
commands:
  - '[[commands/procdump-create-lsass-dump]]'
  - '[[commands/mimikatz-extract-passwords-from-minidump]]'
platforms:
  - Windows
tools:
  - '[[tools/ProcDump]]'
  - '[[tools/Mimikatz]]'
validated: true
---

# Mimikatz-Mini-Dump-Password-Extraction

## Summary

This procedure outlines the use of Mimikatz to extract plaintext passwords and other credentials from a mini dump file of the LSASS process on a compromised Windows system. It involves first creating a memory dump using ProcDump, then processing the dump offline with Mimikatz's sekurlsa module to retrieve logon credentials, which can facilitate privilege escalation and lateral movement in a network.

## Description

Mimikatz is a post-exploitation tool designed to retrieve authentication credentials from Windows memory structures. In this procedure, the focus is on using the sekurlsa::minidump functionality to analyze a pre-created memory dump of the LSASS process, which stores active session tokens, NTLM hashes, and plaintext passwords. This approach is particularly useful in environments where live execution of Mimikatz might trigger alerts, allowing attackers to dump memory remotely or via scheduled tasks and analyze it offline. The technique targets Windows systems (Windows 7 and later) with administrative access, mapping to credential dumping behaviors observed in advanced persistent threats.

## Requirements

1. Administrative privileges on the target Windows system to access and dump the LSASS process.
2. ProcDump executable available on the system for creating the memory dump file.
3. Mimikatz binary transferred to or present on the analysis machine (can be the same as the target if undetected).
4. Sufficient disk space for the memory dump file, typically several hundred MB to GB depending on system memory.

## Defense

Defensive measures and detection strategies:

- Implement Credential Guard and LSASS protection (Protected Process Light) on Windows 10+ to prevent dumping.
- Monitor for process dump creations, especially of lsass.exe, using Sysmon or EDR tools (Event IDs 10, 4688).
- Deploy application whitelisting to block unsigned tools like ProcDump and Mimikatz.
- Enable PowerShell logging and command-line auditing to detect tool executions.
- Regularly rotate credentials and use multi-factor authentication to limit impact of dumped passwords.

## Objectives

1. Extract plaintext passwords from a memory dump file.
2. Obtain credentials for privileged accounts.
3. Escalate privileges and move laterally within a network.

## Instructions

### Step 1: Create LSASS Memory Dump

**Context**: Generate a full memory dump of the LSASS process, which contains in-memory credentials. This step requires admin rights and uses ProcDump to avoid crashing the process.

**Command** ([[commands/procdump-create-lsass-dump]]):

```cmd
procdump.exe -ma lsass.exe lsass.dmp
```

> Run this from an elevated command prompt. The -ma flag ensures a complete memory acquisition. If ProcDump is not present, alternatives like Task Manager (Create Dump File) can be used, but ProcDump provides more control. Expected output shows dump progress and file size confirmation. Verify the dump file exists and is non-zero size.

### Step 2: Extract Logon Passwords from Dump

**Context**: Load the dump into Mimikatz and retrieve credentials. This can be done non-interactively for automation or interactively for verification.

**Command** ([[commands/mimikatz-extract-passwords-from-minidump]]):

```cmd
mimikatz.exe "sekurlsa::minidump lsass.dmp" "sekurlsa::logonpasswords" "exit"
```

> Execute from the directory containing mimikatz.exe. This sequence loads the dump and dumps logon info, including usernames, domains, NTLM hashes, and plaintext passwords where available (e.g., from WDigest or unencrypted sessions). Output will list authentication packages like NTLM and Kerberos, followed by credential details. If no passwords appear, check for enabled mitigations like Credential Guard.

**Alternative Interactive Method**:

For manual inspection, start Mimikatz interactively and use the code snippet [[codes/Mimikatz-Interactive-Minidump-Logon-Password-Extraction]]. At the mimikatz prompt, enter the commands to load and extract, allowing pausing for output review.
