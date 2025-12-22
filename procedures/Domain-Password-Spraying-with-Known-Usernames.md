---
id: a561570c-b7ad-456f-a170-3deda49b185a
name: Domain-Password-Spraying-with-Known-Usernames
type: procedure
verified: true
submitted: false
created_at: '2023-01-11T20:38:26.144387+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Brute Force]]'
  - '[[Valid Accounts]]'
sub_techniques:
  - '[[Password Spraying]]'
tags:
  - Enumeration
  - Password Spray
commands:
  - '[[commands/CrackMapExec-Retrieve-Password-Policy]]'
  - '[[commands/CrackMapExec-Test-Single-User-Password]]'
  - '[[commands/CrackMapExec-Spray-Multiple-User-Passwords]]'
platforms:
  - Windows
tools:
  - '[[tools/CrackMapExec]]'
validated: true
---

# Domain-Password-Spraying-with-Known-Usernames

## Summary

This procedure performs password spraying against a Windows domain controller using known usernames and a dictionary of common passwords. It aims to identify valid credential combinations without triggering account lockouts by distributing attempts across multiple users and passwords, leveraging tools like CrackMapExec to test authentication over SMB.

## Description

Password spraying is an effective technique for credential access in Active Directory environments when usernames are known but passwords are not. By attempting a small set of common passwords against many users (rather than brute-forcing one user), it minimizes the risk of lockouts due to failed login policies. This procedure targets domain controllers via SMB, retrieves optional password policy information to inform spraying strategy, tests individual combinations cautiously, and scales to multi-user spraying. It is typically used in red team engagements after initial enumeration has yielded a list of usernames from sources like LDAP queries or OSINT. Success grants valid credentials for lateral movement or privilege escalation.

## Requirements

1. List of target usernames (e.g., from prior enumeration via LDAP or net commands)
2. Password dictionary file with common passwords (e.g., rockyou.txt or custom list of 10-50 entries to avoid lockouts)
3. Network access to the domain controller (SMB port 445 open)
4. Valid low-privilege credentials or null session for initial policy checks (optional)
5. Installed CrackMapExec tool on the attacker's machine
6. Understanding of domain password policies to pace attempts (e.g., lockout threshold)

## Defense

Defensive measures and detection strategies:

- Implement account lockout policies with low thresholds (e.g., 5 failed attempts) and monitor for spraying patterns across users
- Enable SMB signing and auditing for authentication failures via Windows Event Logs (Event ID 4625)
- Use network segmentation to limit SMB access from untrusted sources
- Deploy tools like Microsoft ATA or Splunk for anomaly detection in login patterns
- Enforce strong password policies and multi-factor authentication (MFA) for domain accounts

## Objectives

1. Retrieve domain password policy to understand lockout thresholds and complexity requirements
2. Validate individual username-password pairs without excessive noise
3. Perform distributed password spraying to discover valid credentials
4. Avoid account lockouts by limiting attempts per user

## Instructions

### Step 1: Retrieve Password Policy

**Context**: Optionally query the domain controller for password policy details, such as lockout thresholds and password complexity rules. This informs how aggressively to spray passwords and helps avoid immediate lockouts. Use existing credentials if available; otherwise, attempt with null sessions.

**Command** ([[commands/CrackMapExec-Retrieve-Password-Policy]]):
```bash
crackmapexec $_TARGET_IP -u $_USERNAME -p $_PASSWORD --pass-pol
```

> This command connects to the target IP via SMB and retrieves policy information. Replace $_TARGET_IP with the DC's IP, $_USERNAME and $_PASSWORD with test credentials (or empty for null). Expected output includes lockout threshold (e.g., 5 bad attempts) and password history length, allowing you to plan spraying (e.g., limit to 4 attempts per user).

### Step 2: Test Single Username-Password Combination

**Context**: Before full spraying, test a single promising username-password pair to validate the setup and confirm SMB access without triggering policies. This is useful for high-confidence guesses from prior intel.

**Command** ([[commands/CrackMapExec-Test-Single-User-Password]]):
```bash
crackmapexec smb $_TARGET_IP -u $_USERNAME -p $_PASSWORD --no-bruteforce
```

> Execute this to attempt authentication for one user-password pair. The --no-bruteforce flag ensures a single attempt. Success is indicated by a green [++] output showing valid credentials; failure shows red [-]. Use this to confirm tool connectivity before scaling.

### Step 3: Perform Multi-User Password Spraying

**Context**: Load a list of usernames and passwords to spray across the domain. Distribute attempts (e.g., one password per user cycle) to stay under lockout limits. Monitor for valid hits and stop if lockouts occur.

**Command** ([[commands/CrackMapExec-Spray-Multiple-User-Passwords]]):
```bash
crackmapexec smb $_TARGET_IP -u $_USER_FILE -p $_PASSWORD_FILE
```

> This sprays passwords from $_PASSWORD_FILE against users in $_USER_FILE (text files, one per line). It cycles through combinations efficiently. Green [++] lines indicate successful authentications with plaintext passwords. If lockouts are detected (e.g., via policy from Step 1), pause and rotate passwords/users. Collect valid creds for further use.
