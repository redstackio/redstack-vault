---
type: procedure
description: >-
  Extract NTP authentication hashes from a target NTP server using timeroast.py
  and crack them offline with Hashcat to obtain the symmetric key for potential
  time manipulation attacks.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/NTP Attacks]]'
  - '[[tags/Timeroasting]]'
  - '[[tags/Hash Cracking]]'
commands:
  - '[[commands/timeroast-extract-ntp-hashes]]'
  - '[[commands/hashcat-crack-ntp-md5]]'
platforms:
  - Linux
tools:
  - '[[tools/timeroast]]'
  - '[[tools/Hashcat]]'
skill_level: intermediate
impact_level: medium
detection_risk: high
validated: true
---

# Timeroasting-NTP-Servers-to-Crack-Authentication-Keys

## Summary

This procedure demonstrates how to perform a timeroasting attack on an NTP server to extract MD5 authentication hashes and crack them using Hashcat. The resulting symmetric key can be used to forge NTP responses, potentially allowing time manipulation on client systems, which could extend the validity of time-sensitive authentication tickets like Kerberos in an Active Directory environment.

## Description

NTP servers often use MD5-based authentication (mode 1 or symmetric key mode) to verify requests and responses. The timeroast.py tool exploits this by sending crafted requests to elicit authentication challenges, capturing the resulting hashes. These hashes are then cracked offline with Hashcat using mode 31300 (NTP MD5 hash). Once cracked, the key enables impersonation of the NTP server, allowing an attacker to manipulate system clocks on dependent clients. This is particularly useful in environments where precise time synchronization is required for Kerberos authentication, as skewing time can invalidate or extend ticket lifetimes. The technique requires network access to the NTP server (typically UDP port 123) and assumes the server is vulnerable to hash extraction via unauthenticated queries.

## Requirements

1. Network access to the target NTP server on UDP port 123.
2. timeroast.py tool installed and executable (Python-based script).
3. Hashcat installed with GPU support for efficient cracking.
4. A wordlist or dictionary for offline cracking (e.g., rockyou.txt).
5. Root privileges on the attacker's machine for running timeroast.py.

## Defense

- Disable NTP MD5 authentication and use NTS (Network Time Security) for encrypted, authenticated time sync.
- Restrict NTP server access via firewall rules, allowing only trusted clients/subnets.
- Monitor NTP traffic for unusual request patterns or high-volume queries indicative of hash extraction attempts.
- Regularly rotate NTP symmetric keys and audit server logs for authentication failures.
- Implement NTP pool diversity to avoid single points of failure for time manipulation.

## Objectives

1. Extract MD5 authentication hashes from the target NTP server.
2. Crack the hashes to recover the symmetric key.
3. Enable potential time manipulation for persistence or evasion in time-dependent authentication systems.
4. Verify successful key recovery for further exploitation.

## Instructions

### Step 1: Extract NTP Authentication Hashes

**Context**: Use timeroast.py to send crafted NTP requests to the target server, eliciting MD5 authentication challenges. The tool captures the hashes and saves them to a file for cracking. This step exploits the server's response to unauthenticated queries, assuming MD5 mode is enabled.

**Command** ([[commands/timeroast-extract-ntp-hashes]]):
```bash
sudo ./timeroast.py $_TARGET_IP | tee ntp-hashes.txt
```

> Run this command from the directory containing timeroast.py. Replace $_TARGET_IP with the NTP server's IP address. The sudo is required for raw socket access to send UDP packets. Expected output includes captured hashes in a format suitable for Hashcat (e.g., 'ntp-md5::server-ip:port:hash'). If no hashes are captured, the server may not support MD5 auth or queries are blocked.

### Step 2: Crack the Extracted Hashes

**Context**: Feed the captured hashes into Hashcat for offline brute-force or dictionary attack. Mode 31300 specifically handles NTP MD5 hashes. This step recovers the plaintext symmetric key if it's weak or in your wordlist, allowing forgery of NTP packets.

**Command** ([[commands/hashcat-crack-ntp-md5]]):
```bash
hashcat -m 31300 ntp-hashes.txt $_WORDLIST
```

> Specify a strong wordlist in $_WORDLIST (e.g., /usr/share/wordlists/rockyou.txt). Monitor progress with Hashcat's status output. If successful, the cracked key will be displayed (e.g., 'ntp-md5::server-ip:port:plaintext-key'). Use --force for GPU acceleration if needed. Failure indicates a strong key or insufficient wordlist; consider rules-based attacks with -r option.

### Step 3: Verify Key and Test Manipulation

**Context**: Once cracked, test the key by crafting a forged NTP response using tools like ntpdc or scapy to adjust a client's time. This confirms the attack's viability for broader exploitation, such as Kerberos ticket manipulation.

**Instructions**: Use the recovered key with a packet crafting tool (e.g., scapy) to send a spoofed NTP response to a client. Monitor the client's clock adjustment via ntpq -p. Success is indicated by the client accepting the forged time offset.
