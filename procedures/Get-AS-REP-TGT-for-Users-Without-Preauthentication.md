---
id: 12ba17ed-fe23-4a33-9dc0-9aff509ae27c
name: Get-AS-REP-TGT-for-Users-Without-Preauthentication
type: procedure
verified: true
submitted: false
created_at: '2020-03-14T00:32:07.045730+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/AS-REP-Roasting|T1558.004 - AS-REP Roasting]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory]]'
  - '[[tags/as-rep-roasting]]'
  - '[[tags/kerberos]]'
commands:
  - '[[commands/getnpusers-request-asrep]]'
platforms:
  - Windows
tools:
  - '[[tools/Impacket]]'
validated: true
---

# Get-AS-REP-TGT-for-Users-Without-Preauthentication

## Summary

This procedure retrieves the AS-REP (Authentication Service Reply) containing the Ticket Granting Ticket (TGT) encryption key for Active Directory users who have the 'Do not require Kerberos preauthentication' (UF_DONT_REQUIRE_PREAUTH) flag enabled. This flag allows attackers to request TGTs without knowing the user's password, enabling offline cracking of the resulting hash to recover credentials.

## Description

In Active Directory environments, the UF_DONT_REQUIRE_PREAUTH user account control flag disables Kerberos preauthentication, making users vulnerable to AS-REP Roasting attacks. This technique involves requesting an AS-REP from the Key Distribution Center (KDC) for targeted users, which returns an encrypted TGT that can be cracked offline using tools like Hashcat. This procedure assumes the attacker has network access to a Domain Controller and knows the username of a vulnerable account. It is commonly used in red team engagements to gain initial credentials for lateral movement or privilege escalation. Success depends on the user having the flag set, which can be enumerated separately using tools like BloodHound or ldapsearch.

## Requirements

1. Network access to the Active Directory Domain Controller (typically over port 88 for Kerberos).
2. Knowledge of the target domain name and a specific username with UF_DONT_REQUIRE_PREAUTH enabled.
3. Impacket suite installed, including the GetNPUsers.py script.
4. Python 3 environment on the attacker's machine.
5. Optional: A wordlist for subsequent hash cracking if the AS-REP hash is obtained.

## Defense

- Monitor for unusual Kerberos AS-REP requests from non-domain joined systems or anomalous IPs using tools like Microsoft ATA or custom SIEM rules.
- Audit user accounts for the UF_DONT_REQUIRE_PREAUTH flag and disable it for service accounts or users who do not require it.
- Implement Kerberos preauthentication enforcement domain-wide via Group Policy.
- Enable logging for Kerberos authentication failures and review for AS-REP roasting patterns (e.g., requests without PAC validation).

## Objectives

1. Request and obtain the AS-REP response containing the user's TGT hash without providing a password.
2. Capture the crackable hash for offline analysis.
3. Validate successful retrieval to confirm the user's vulnerability.

## Instructions

### Step 1: Gather Target Information

**Context**: Before executing the request, collect the necessary domain details, target username, and Domain Controller IP. This ensures the command targets the correct environment and reduces errors from misconfiguration.

Identify the domain (e.g., via nslookup or prior recon) and confirm the user has the vulnerable flag using enumeration tools like [[commands/getnpusers-enumerate-users]] if needed.

### Step 2: Execute AS-REP Request

**Context**: Use the GetNPUsers.py script from Impacket to send a Kerberos AS-REQ to the KDC without preauthentication, prompting the return of the AS-REP with the encrypted TGT.

**Command** ([[commands/getnpusers-request-asrep]]):
```bash
GetNPUsers.py $_DOMAIN/$_USER -dc-ip $_TARGET_IP -no-pass -request
```

This command formats the request as 'domain/username', specifies the DC IP to direct the query, and uses -no-pass to skip preauth. The -request flag ensures only the TGT is requested without further actions. Run this from a Linux or Windows machine with Impacket installed.

### Step 3: Capture and Verify Output

**Context**: Save the output to a file for cracking and inspect it to confirm the hash was retrieved, indicating the user is vulnerable.

Redirect the output to a file: `GetNPUsers.py ... > asrep_hashes.txt`. The hash will be in a format like `$krb5asrep$23$username@DOMAIN:HASH` suitable for Hashcat (mode 18200).

If no hash is returned, the user likely requires preauth—try another target or verify the flag.
