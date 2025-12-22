---
id: 940d0525-2434-487b-bc5b-b40e57cbad53
name: Kerberos-Pre-Auth-Bruteforcing-with-Kerbrute
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:04.229151+00:00'
updated_at: '2023-04-10T20:26:23.708098+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Kerberos pre-auth bruteforcing]]'
  - '[[tags/Password spraying]]'
commands:
  - '[[commands/kerbrute-user-enumeration]]'
  - '[[commands/kerbrute-password-bruteforce]]'
platforms:
  - Windows
  - Active Directory
tools:
  - '[[tools/Kerbrute]]'
validated: true
---

# Kerberos-Pre-Auth-Bruteforcing-with-Kerbrute

## Summary

This procedure uses the Kerbrute tool to perform Kerberos pre-authentication brute forcing, enabling the enumeration of valid usernames and the cracking of user passwords in an Active Directory environment. It is particularly useful for password spraying attacks or targeted brute forcing during credential access phases of penetration testing or red team engagements.

## Description

Kerberos pre-authentication requires clients to prove knowledge of their password before full authentication tickets are issued, making it a target for brute force attacks. Kerbrute exploits this by sending AS-REQ messages to the Domain Controller (DC) to test username validity or password guesses without triggering full logon events that might lock accounts. This technique is effective in Active Directory domains where pre-auth is enabled (default setting) and can reveal valid accounts or weak passwords. It assumes the attacker has network access to the DC port 88 (Kerberos) and a wordlist for testing. Success depends on avoiding detection thresholds for failed authentications. This maps to MITRE ATT&CK T1110 for brute force via network service accounts.

## Requirements

1. Network access to the target Domain Controller on port 88 (Kerberos).
2. Resolution of the domain name and DC hostname/IP.
3. A wordlist of potential usernames (e.g., from prior reconnaissance) or passwords (common lists like rockyou.txt).
4. Kerbrute tool installed on the attacker's machine.
5. Optional: Existing domain credentials for safer spraying (to mimic legitimate traffic).

## Defense

- Implement strong password policies, requiring complexity and regular rotation to resist brute force.
- Enable multi-factor authentication (MFA) for all accounts to add a layer beyond passwords.
- Monitor Kerberos event logs (Event ID 4768 for TGT requests) for anomalous pre-auth failures and set thresholds for alerting or temporary lockouts.
- Use tools like Microsoft ATA or SIEM to detect spraying patterns across multiple accounts.
- Disable pre-authentication for sensitive service accounts where feasible, though this increases vulnerability to offline attacks.

## Objectives

1. Enumerate valid Active Directory usernames by testing pre-auth responses.
2. Brute force or spray passwords against known valid usernames to obtain credentials.
3. Gain initial access to the domain for further lateral movement or privilege escalation.

## Instructions

### Step 1: Enumerate Valid Usernames

**Context**: Begin by identifying active usernames in the domain. Kerbrute sends Kerberos AS-REQ requests for each username in your list; valid users respond with errors indicating existence (e.g., KDC_ERR_PREAUTH_REQUIRED), while invalid ones return KDC_ERR_C_PRINCIPAL_UNKNOWN. This step helps build a targeted list for password attacks without alerting on full logons.

**Command** ([[commands/kerbrute-user-enumeration]]):
```bash
kerbrute userenum --dc $_DC_HOST -d $_DOMAIN $_USERLIST_FILE
```

> This command tests usernames from the provided file against the specified domain and DC. Run it from a machine with network access to the DC. If successful, it outputs valid usernames. Monitor for rate limiting; use delays if needed via tool flags. Expected output includes lines like "[+] VALID USERNAME: user@domain.local" for confirmed accounts.

### Step 2: Brute Force Passwords for a Target User

**Context**: Once valid usernames are identified, target a specific user (e.g., from Step 1) with a password list. Kerbrute attempts AS-REQ with each password guess; a successful match returns a TGT without further errors. This is ideal for password spraying (few passwords across many users) or brute forcing (many passwords on one user). Limit attempts to avoid lockouts.

**Command** ([[commands/kerbrute-password-bruteforce]]):
```bash
kerbrute bruteforce --dc $_DC_HOST -d $_DOMAIN $_USERNAME $_PASSWORDLIST_FILE
```

> Replace placeholders with actual values (e.g., username from enumeration). The tool iterates through the password list, stopping or continuing based on success. If a match is found, it reports "[+] VALID PASSWORD: password for user@domain.local". Verify credentials post-success with tools like impacket for full access.
