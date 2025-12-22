---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:04.263036+00:00'
updated_at: '2023-04-10T20:36:09.914409+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
sub_techniques:
  - '[[sub-techniques/Password Guessing|T1110.001 - Password Guessing]]'
  - '[[sub-techniques/Password Spraying|T1110.003 - Password Spraying]]'
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Kerberos pre-auth bruteforcing]]'
  - '[[tags/Password spraying]]'
commands:
  - '[[commands/kerbrute-user-enumeration]]'
  - '[[commands/kerbrute-brute-user-password]]'
  - '[[commands/kerbrute-password-spray-single-password]]'
  - '[[commands/kerbrute-password-spray-wordlist]]'
platforms:
  - Windows
tools:
  - '[[tools/kerbrute]]'
validated: true
---

# Kerberos-Pre-Auth-Bruteforcing

## Summary

Kerberos pre-auth bruteforcing is a technique to identify weak or default passwords for Active Directory user accounts by sending authentication requests to the Kerberos service. This procedure uses the Kerbrute tool to enumerate valid usernames and then perform targeted brute force attacks or password spraying against them, enabling credential access without triggering full account lockouts.

## Description

In Active Directory environments, Kerberos handles authentication via pre-authentication requests where the client's password encrypts a timestamp sent to the Key Distribution Center (KDC). By brute forcing these requests externally, attackers can test passwords without needing initial domain access. This procedure covers user enumeration to identify targets, single-user brute forcing with a password list, and password spraying across multiple users with common passwords to avoid detection. It targets domain controllers and is effective in environments with weak password policies. Success allows lateral movement or privilege escalation using obtained credentials.

## Requirements

1. Network access to the domain controller (port 88 UDP/TCP open for Kerberos).
2. A wordlist of potential usernames (e.g., common names or from prior recon) and passwords (e.g., rockyou.txt).
3. Kerbrute tool installed on a Linux-based attack machine (Kali recommended).
4. Domain name and DC IP address.

## Defense

- Implement strong password policies with complexity requirements and regular rotations.
- Monitor Kerberos event logs (Event ID 4771 for pre-auth failures) and set account lockout thresholds.
- Use multi-factor authentication (MFA) for all accounts to mitigate password-only attacks.
- Deploy network segmentation to limit external access to domain controllers.

## Objectives

1. Enumerate valid domain usernames via pre-auth responses.
2. Identify weak passwords through brute force or spraying.
3. Obtain valid credentials for further network access.

## Instructions

### Step 1: Enumerate Valid Usernames

**Context**: Begin by enumerating active domain users. Kerbrute sends pre-auth requests for each username in a wordlist; valid users respond differently, allowing identification without credentials. This step builds a target list for subsequent attacks and confirms domain connectivity.

**Command** ([[commands/kerbrute-user-enumeration]]):
```bash
./kerbrute_linux_amd64 userenum -d $_DOMAIN --dc $_DC_IP $_USERNAMES_FILE
```

> This command probes the domain for valid usernames. Replace placeholders with actual values (e.g., -d example.com --dc 10.10.10.10 usernames.txt). It outputs valid users to stdout. Run this first to avoid spraying invalid accounts, which could increase noise.

### Step 2: Brute Force a Specific User's Password

**Context**: For a known high-value user (e.g., from enumeration), perform a targeted brute force using a password wordlist. This tests multiple passwords against one account, useful when focusing on admins or service accounts. Limit attempts to evade lockouts.

**Command** ([[commands/kerbrute-brute-user-password]]):
```bash
./kerbrute_linux_amd64 bruteuser -d $_DOMAIN --dc $_DC_IP $_PASSWORD_FILE $_USERNAME
```

> Execute against a single username with a password list like rockyou.txt. If a match is found, Kerbrute reports the valid password. Monitor for success indicators like a green output line. This is slower but precise for targeted attacks.

### Step 3: Perform Password Spraying Across Users

**Context**: Use password spraying to test one or a few common passwords against many users. This mimics legitimate logins and reduces lockout risk. Ideal after enumeration to quickly find weak accounts. Include delays to simulate human behavior.

**Command** ([[commands/kerbrute-password-spray-single-password]]):
```bash
./kerbrute_linux_amd64 passwordspray -d $_DOMAIN --dc $_DC_IP $_USERS_FILE $_PASSWORD -v --delay $_DELAY -o $_OUTPUT_FILE
```

> For a single common password (e.g., 'Password123'), spray across users from domain_users.txt. Use -v for verbose output and --delay 100 for 100ms pauses. Successful hits are logged to the output file.

**Command** ([[commands/kerbrute-password-spray-wordlist]]):
```bash
./kerbrute_linux_amd64 passwordspray -d $_DOMAIN --dc $_DC_IP $_USERS_FILE $_PASSWORD_FILE
```

> For spraying a full wordlist (e.g., rockyou.txt) across users, but use sparingly to avoid detection. Outputs valid combinations directly. Combine with Step 1's results for efficiency.
