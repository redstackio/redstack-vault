---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:26.325320+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
tags:
  - '[[tags/Data Protection API]]'
  - '[[tags/Hekatomb]]'
  - '[[tags/Windows - DPAPI]]'
commands:
  - '[[commands/pip3-install-hekatomb]]'
  - '[[commands/hekatomb-extract-ntlm-hash]]'
platforms:
  - Windows
tools:
  - '[[tools/Hekatomb]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# DPAPI-Credential-Theft-with-Hekatomb

## Summary

This procedure uses the Hekatomb tool to extract DPAPI-protected credentials from a Windows domain environment, enabling attackers to steal sensitive user hashes such as NTLM hashes for further cracking or lateral movement. It targets DPAPI blobs stored on domain controllers or accessible systems to recover encrypted credentials.

## Description

DPAPI (Data Protection API) is a Windows feature that encrypts sensitive data like credentials using user-specific or system master keys. Hekatomb leverages the DPAPIck library to perform remote extraction of these blobs over the network, often via DNS tunneling or direct connections to domain controllers. This technique is effective in Active Directory environments where an attacker has network access and partial credentials, allowing escalation by dumping and cracking hashes for domain users. The procedure assumes the attacker is operating from a Linux-based attack machine with Python installed and has resolved the target's domain controller IP.

## Requirements

1. Network access to the target domain controller (e.g., via compromised host or VPN).
2. Python 3 and pip3 installed on the attacker's machine.
3. Basic knowledge of the target domain name, a username (e.g., administrator), and the domain controller's IP address.
4. Optional: A known hash type or seed for targeted extraction (e.g., NTLM hash prefix).

## Defense

Defensive measures and detection strategies:

- Implement strong password policies and multi-factor authentication to make cracked credentials less useful.
- Monitor for unusual account activity, such as anomalous DNS queries or connections to domain controllers from unexpected sources.
- Disable or restrict access to tools like Hekatomb by blocking Python package installations in controlled environments and using EDR tools to detect DPAPI-related API calls (e.g., CryptUnprotectData).
- Regularly rotate DPAPI master keys and enable advanced auditing for credential access events in Active Directory.

## Objectives

1. Extract DPAPI-protected hashes for domain users to enable offline cracking.
2. Escalate privileges by using recovered credentials for lateral movement or persistence.
3. Gain access to sensitive information protected by DPAPI, such as stored passwords in browsers or applications.

## Instructions

### Step 1: Install Hekatomb Tool

**Context**: Hekatomb must be installed via pip to access its DPAPI extraction capabilities. This step ensures the tool and its dependencies (like DPAPIck) are available on the attacker's machine.

**Command** ([[commands/pip3-install-hekatomb]]):
```bash
pip3 install hekatomb
```

> This command downloads and installs Hekatomb from PyPI. Verify installation by running `hekatomb --help` to see available options. If behind a proxy, add `--proxy` flag as needed.

### Step 2: Extract NTLM Hash Using Hekatomb

**Context**: With Hekatomb installed, target a specific domain user to extract their NTLM hash via DPAPI blobs on the domain controller. This step performs a DNS-based request to pull the protected data, which can then be cracked offline.

**Command** ([[commands/hekatomb-extract-ntlm-hash]]):
```bash
hekatomb -hashes :$_HASH_SEED $_DOMAIN/$_USERNAME@$_DC_IP -debug -dnstcp
```

> Replace placeholders with actual values (e.g., -hashes :ed0052e5a66b1c8e942cc9481a50d56 for NTLM seed, DOMAIN.local/administrator@10.0.0.1). The -debug flag provides verbose output for troubleshooting, and -dnstcp forces TCP for DNS requests to bypass UDP restrictions. Expected output includes extracted hash in a crackable format; pipe to a file for Hashcat or John the Ripper if successful. If the hash seed is unknown, omit or use a wildcard; monitor for errors indicating insufficient privileges.
