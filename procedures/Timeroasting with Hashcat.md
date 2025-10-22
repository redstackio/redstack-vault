---
id: b692b1ac-557e-45ab-b1de-1201cff063e6
name: Timeroasting with Hashcat
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:05.052942+00:00'
updated_at: '2023-04-10T20:36:14.018918+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Timeroasting]]'
commands:
- '[[Crack NTP hashes with hashcat]]'
- '[[Run timeroast.py to get NTP hashes]]'
---

# Timeroasting with Hashcat

## Summary

Timeroasting is a technique used to manipulate the timestamps of kerberos tickets to extend their validity period. Attackers can use this technique to maintain persistence in the target environment. By cracking NTP hashes with Hashcat, an attacker can obtain the NTP server's symmetric key, which ca

## Description

# Description

Timeroasting is a technique used to manipulate the timestamps of kerberos tickets to extend their validity period. Attackers can use this technique to maintain persistence in the target environment. By cracking NTP hashes with Hashcat, an attacker can obtain the NTP server's symmetric key, which can be used to manipulate the time on the target system. This procedure will allow an attacker to perform timeroasting attacks on the target system.

## Requirements

1. Access to the target system

1. Hashcat tool installed

1. NTP hash to crack

## Defense

1. Regularly monitor and review the NTP server configuration and logs

1. Implement network segmentation to limit the impact of a compromised NTP server

1. Use secure protocols such as NTS (Network Time Security) to secure NTP communication

## Objectives

1. Extend the validity period of kerberos tickets

1. Maintain persistence in the target environment

# Instructions

1. The `timeroast.py` script is used to retrieve NTP timestamps from a target machine. The resulting hashes are saved to a file called `ntp-hashes.txt`. This file can then be used as input for the `hashcat` command to crack the hashes. The `-m 31300` flag specifies the hash type to be cracked, which in this case is the NTP hash.

**Code**: [[sudo ./timeroast.py 10.0.0.42 | tee ntp-hashes.txt]]

> This command is useful for cracking NTP hashes, which can be used to gain access to a target machine. By retrieving the hashes using `timeroast.py` and then cracking them with `hashcat`, an attacker can potentially gain access to the target machine's network. It is important to note that this command should only be used for legal and ethical purposes, such as in a penetration testing scenario with proper authorization.

**Command** ([[Run timeroast.py to get NTP hashes]]):

```bash
sudo ./timeroast.py 10.0.0.42 | tee ntp-hashes.txt
```

**Command** ([[Crack NTP hashes with hashcat]]):

```bash
hashcat -m 31300 ntp-hashes.txt
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Crack NTP hashes with hashcat]]
- [[Run timeroast.py to get NTP hashes]]

## Tags

- [[Active Directory Attacks]]
- [[Timeroasting]]
