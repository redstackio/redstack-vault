---
id: 19d1316e-a40d-44fd-8df2-eb33a2edede4
name: connect-to-ssh-server-with-private-key
type: procedure
verified: true
submitted: true
created_at: '2019-11-25T20:01:51.981244+00:00'
updated_at: '2023-05-26T00:46:10.649666+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques:
  - '[[techniques/Remote Services/T1021.001|T1021.001 - Remote Desktop Protocol]]'
platforms:
  - Linux
tags:
  - Network
commands:
  - '[[commands/ssh-connect-with-private-key]]'
tools:
  - '[[tools/OpenSSH]]'
validated: true
---

# Connect to SSH Server with Private Key

## Summary

Establish an SSH connection to a remote Linux server using a stolen or leaked private key file, bypassing password authentication for initial access in a CTF privilege chain.

## Description

SSH key-based auth allows passwordless login if the public key is in authorized_keys. This procedure uses the -i flag to specify the private key, assuming the key was extracted via Heartbleed or similar.

## Requirements

1. Valid private key file (e.g., id_rsa)
2. Target IP and username
3. SSH client installed

## Defense

Restrict key permissions (600), use key agents, monitor auth logs for failed attempts, and rotate keys post-breach.

## Objectives

1. Authenticate with private key
2. Gain remote shell access
3. Maintain persistence if needed

## Instructions

### Step 1: Prepare Key File

**Context**: Ensure the key is in PEM format and permissions are set correctly.

```bash
chmod 600 $_PRIVATE_KEY
```

### Step 2: Initiate SSH Connection

**Context**: Connect specifying the key and user; this grants shell if the key matches authorized_keys on target.

**Command** ([[commands/ssh-connect-with-private-key]]):
```bash
ssh -i $_PRIVATE_KEY -l $_USER $_TARGET_IP
```

> Expected output is login banner and shell prompt. If host unknown, add -o StrictHostKeyChecking=no; for verbose debugging, add -v.
