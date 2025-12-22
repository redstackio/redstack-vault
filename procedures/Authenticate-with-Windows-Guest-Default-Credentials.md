---
id: 5def7b2c-b500-4da4-9010-ef4eca42b821
name: Authenticate-with-Windows-Guest-Default-Credentials
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:30.651568+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
  - '[[techniques/Default Accounts|T1078.001 - Default Accounts]]'
sub_techniques: []
tags:
  - '[[tags/default-credentials]]'
  - '[[tags/guest-account]]'
  - '[[tags/windows-credentials]]'
commands:
  - '[[commands/net-user-guest-enumerate]]'
  - '[[commands/net-use-authenticate-guest-empty]]'
platforms:
  - Windows
tools: []
validated: true
---

# Authenticate-with-Windows-Guest-Default-Credentials

## Summary

This procedure checks the status of the Windows Guest account and attempts authentication using its default empty password. Many Windows systems leave the Guest account enabled with no password, allowing low-privilege access for enumeration, file sharing, or further exploitation.

## Description

The Windows Guest account is a built-in local account intended for limited access. By default, it has an empty password (NTLM hash: 31d6cfe0d16ae931b73c59d7e0c089c0), which administrators often fail to secure. This procedure first enumerates the account status to confirm it is active and then tests authentication over the network using SMB. Success grants initial foothold access, enabling further discovery or persistence. This technique is common in lateral movement scenarios where default credentials are exploited.

## Requirements

1. Network access to the target Windows system (e.g., via SMB ports 445 open).
2. Local execution privileges on an attacker-controlled Windows machine or compatible system to run net commands.
3. Target hostname or IP address.

## Defense

- Disable the Guest account using 'net user guest /active:no' or Group Policy.
- Set a strong password for the Guest account if it must remain enabled.
- Monitor authentication logs (Event ID 4624) for Guest account logons and failed attempts.
- Restrict SMB access with firewalls and require SMB signing.

## Objectives

1. Confirm the Guest account is active and uses default empty password.
2. Authenticate to the target system using Guest credentials.
3. Establish a low-privilege session for further enumeration.

## Instructions

### Step 1: Enumerate Guest Account Status

**Context**: Use the net user command to query the Guest account details, verifying if it is active and whether a password is required. This step confirms the account's configuration without authentication.

**Command** ([[commands/net-user-guest-enumerate]]):
```cmd
net user guest
```

> This command displays account properties. Look for 'Account active: Yes' and 'Password required: No' to indicate default empty password vulnerability.

### Step 2: Attempt Authentication with Empty Password

**Context**: Test network authentication using the Guest account with an empty password via SMB IPC$ share. Success indicates the default credentials are valid, allowing access to shared resources.

**Command** ([[commands/net-use-authenticate-guest-empty]]):
```cmd
net use \\$_TARGET\IPC$ /user:guest ""
```

> Replace $_TARGET with the target's hostname or IP. If successful, it establishes a null session for further actions like share enumeration. Disconnect with 'net use \\$_TARGET\IPC$ /delete' after testing.
