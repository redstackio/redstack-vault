---
type: procedure
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Pass the Hash|T1075 - Pass the Hash]]'
sub_techniques: []
tags:
  - active-directory-attacks
  - overpass-the-hash
  - impacket
commands:
  - '[[commands/get-tgt-using-nt-hash]]'
  - '[[commands/authenticate-with-psexec-using-tgt]]'
  - '[[commands/get-tgt-using-aes-key]]'
  - '[[commands/add-tgt-to-keytab-with-ktutil]]'
  - '[[commands/obtain-tgt-with-kinit]]'
  - '[[commands/verify-tgt-with-klist]]'
platforms:
  - Windows
tools:
  - '[[tools/Impacket]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# OverPass-the-Hash-with-Impacket

## Summary

OverPass-the-Hash with Impacket is a procedure that enables authentication to Active Directory environments using NTLM hashes instead of plaintext passwords. By leveraging Impacket's getTGT.py tool, an attacker can request a Kerberos Ticket Granting Ticket (TGT) from the Key Distribution Center (KDC) using the NT hash, which can then be used for subsequent Kerberos-based authentications to remote systems, facilitating lateral movement without needing the original password.

## Description

This procedure exploits the Kerberos authentication protocol in Windows Active Directory by passing the NTLM hash directly to generate a TGT. Impacket, a collection of Python classes for working with network protocols, provides the necessary tools like getTGT.py to perform this operation. Once the TGT is obtained, it can be exported to a credential cache (ccache) file and used with tools like psexec.py for remote execution. An alternative path uses AES keys if available. This technique is particularly useful in post-compromise scenarios where hashes have been extracted (e.g., via Mimikatz or LSASS dumping) and allows attackers to impersonate users across the domain. The target environment is typically a Windows domain with Kerberos enabled, and success relies on the hash being valid and the attacker's machine being able to reach the domain controller on port 88 (Kerberos).

## Requirements

1. Valid NTLM hash (or AES key) of a domain user account
2. Impacket library installed on a Linux-based attacker machine (e.g., Kali Linux)
3. Network access to the domain's Key Distribution Center (KDC) on TCP/UDP port 88
4. Python 2 or 3 environment with required dependencies (e.g., PyCrypto or equivalent)

## Defense

Defensive measures and detection strategies:

- Use strong, unique passwords and avoid reusing credentials across systems to limit hash validity
- Implement multi-factor authentication (MFA) for all accounts to prevent stolen credential usage
- Monitor network traffic for anomalous Kerberos authentication patterns, such as unusual TGT requests from non-domain-joined systems or spikes in AS-REQ/AS-REP exchanges
- Enable advanced auditing for Kerberos events (Event ID 4768, 4769) and use tools like Microsoft ATA or SIEM for anomaly detection
- Restrict Kerberos pre-authentication where possible and enforce Protected Users group membership to block pass-the-hash

## Objectives

1. Retrieve a Kerberos TGT using the NTLM hash of a domain user
2. Authenticate to remote systems using the obtained TGT for lateral movement
3. Verify successful ticket acquisition and enable further post-exploitation activities

## Instructions

### Step 1: Obtain TGT Using NT Hash

**Context**: Begin by using the NTLM hash to request a Kerberos TGT from the domain's KDC. This step authenticates the hash without requiring the plaintext password and saves the ticket to a ccache file for later use. This is the core of the OverPass-the-Hash technique.

**Command** ([[commands/get-tgt-using-nt-hash]]):
```bash
python getTGT.py -hashes ":$_NT_HASH" $_DOMAIN/$_USERNAME
```

> This command initiates an Authentication Service (AS) request to the KDC. Replace $_NT_HASH with the user's NTLM hash (e.g., aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0), $_DOMAIN with the domain name (e.g., lab.ropnop.com), and $_USERNAME with the target username. The colon before the hash indicates an empty LM hash. Expected output includes a message like "Saving ticket in <username>.ccache" confirming the TGT was generated successfully.

### Step 2: Authenticate to Remote System Using TGT

**Context**: With the TGT in the credential cache, export the cache environment variable and use it to authenticate to a remote target via psexec.py. This allows command execution on the target without re-entering credentials, demonstrating lateral movement.

**Command** ([[commands/authenticate-with-psexec-using-tgt]]):
```bash
export KRB5CCNAME="$_CCACHE_FILE"
python psexec.py "$_DOMAIN/$_USERNAME@$_TARGET_HOST" -k -no-pass
```

> Set the KRB5CCNAME environment variable to point to the ccache file generated in Step 1 (e.g., /path/to/username.ccache). Then run psexec.py with the domain, username, and target host (e.g., labwws02.lab.ropnop.com). The -k flag uses Kerberos tickets, and -no-pass skips password prompts. Expected output shows a successful connection and an interactive shell on the target, such as "Impacket v0.9.24 - Copyright 2020 SecureAuth Corporation" followed by command prompt.

### Step 3: Obtain TGT Using AES Key (Alternative)

**Context**: If an AES key (e.g., from a krbtgt account) is available instead of the NT hash, use it to request the TGT. This is useful when hashes are unavailable but Kerberos keys are compromised.

**Command** ([[commands/get-tgt-using-aes-key]]):
```bash
python getTGT.py -aesKey "$_AES_KEY" $_DOMAIN/$_USERNAME
```

> Provide the 256-bit AES key in hexadecimal format for $_AES_KEY (e.g., xxxxxxxxxxxxxxkeyaesxxxxxxxxxxxxxxxx). Specify the domain and username as before. Expected output mirrors Step 1, saving the ticket to a ccache file.

### Step 4: Add TGT to Keytab with ktutil

**Context**: Convert the TGT into a keytab file for persistent storage and reuse in tools that support keytabs. This step uses ktutil to add the principal and hash to a keytab, enabling offline ticket generation.

**Command** ([[commands/add-tgt-to-keytab-with-ktutil]]):
```bash
ktutil -k $_KEYTAB_FILE add -p "$_USERNAME@$_DOMAIN" -e arcfour-hmac-md5 -w "$_NT_HASH" --hex -V 5
```

> Specify the output keytab file for $_KEYTAB_FILE (e.g., ~/mykeys.keytab), the principal as username@domain, and the NT hash in hex without the LM portion. The encryption type arcfour-hmac-md5 is standard for NT hashes. Expected output from ktutil is a confirmation like "Entry for principal <principal> with kvno 5, encryption type arcfour-hmac-md5 added to keytab".

### Step 5: Obtain Ticket with kinit Using Keytab

**Context**: Use the keytab to request a fresh TGT via kinit, which authenticates against the KDC using the stored credentials. This verifies the keytab and prepares tickets for service requests.

**Command** ([[commands/obtain-tgt-with-kinit]]):
```bash
kinit -t $_KEYTAB_FILE "$_USERNAME@$_DOMAIN"
```

> Point to the keytab file created in Step 4 and provide the principal. Expected output is a success message like "kinit: /tmp/krb5cc_0 initial ticket is correctly configured" or no errors, with the ticket saved to the default cache.

### Step 6: Verify TGT with klist

**Context**: List the current Kerberos tickets to confirm the TGT was obtained and is valid. This step validates all prior actions and shows ticket details like expiration time.

**Command** ([[commands/verify-tgt-with-klist]]):
```bash
klist
```

> This command displays all cached tickets. Expected output includes the TGT details, such as "Ticket cache: FILE:/tmp/krb5cc_0\nDefault principal: $_USERNAME@$_DOMAIN\n\nServer: krbtgt/$_DOMAIN@$_DOMAIN\nKerberos 5 Ticket <hash>, kvno 5\n\nStart time: ..., End time: ...", confirming the ticket is active.
