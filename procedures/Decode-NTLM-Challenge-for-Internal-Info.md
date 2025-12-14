---
tags:
  - ntlm
  - decoding
  - recon
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Windows
techniques:
  - '[[Gather Victim Network Information]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 58eca2ca-93f8-4506-aa96-84f3d98d96aa
created_at: '2025-12-14T17:31:19.113Z'
updated_at: '2025-12-14T17:31:19.113Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Network Information]]'
---
# Decode-NTLM-Challenge-for-Internal-Info

## Summary

This procedure decodes the base64-encoded NTLM Type 2 challenge from a web server's WWW-Authenticate header to extract sensitive internal details such as domain names, computer names, DNS information, and operating system versions.

## Description

NTLM challenges contain AV pairs (Attribute-Value pairs) that inadvertently leak internal network configuration when triggered improperly. Using tools like Burp Suite's decoder, the blob is parsed to reveal elements like NetBIOS names, DNS domains, and timestamps, providing reconnaissance for further attacks like targeted SMB exploitation.

## Requirements

1. Captured HTTP response with WWW-Authenticate: NTLM header
2. Decoder tool (Burp Suite extension or online NTLM parser)
3. Basic understanding of NTLM protocol structure

## Defense

Defensive measures and detection strategies:

- Configure NTLM to minimize AV pair disclosures (e.g., disable unnecessary flags)
- Log and alert on NTLM challenge responses to unauthenticated requests
- Implement network segmentation to limit exposure of internal details

## Objectives

1. Parse challenge to obtain host and domain identifiers
2. Identify OS versions for vulnerability assessment
3. Build a map of internal infrastructure

## Instructions

### Step 1: Extract and Base64 Decode

**Context**: Copy the encoded NTLM value from the WWW-Authenticate header in Burp Suite.

**Command** (Manual in Burp):
```bash
# Paste encoded string into Burp Decoder > Base64 Decode
# Example encoded: TlRMTVNTUAABAAAAB4IIogAAAAAAAAAAAAAAAAAAAAAYABgA....
```

> This yields the binary NTLM message. Look for the challenge structure starting after the NTLMSSP signature.

### Step 2: Parse AV Pairs

**Context**: Use Burp's NTLM Challenge Decoder extension to interpret the binary data, extracting fields like Target Name, NbComputerName, and DnsDomainName.

**Command** (Extension feature):
```bash
# In Burp: Select decoded blob > NTLM Challenge Decoder > Analyze
```

> Expected output includes Target: MTNICT, MsvAvNbComputerName: ZACNVSPRWSBS01, MsvAvDnsDomainName: mtnict.local, OS version: Windows Server 2012 R2 / Windows 8.1.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Gather Victim Network Information]] Gather Victim Network Information

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- ntlm-decode
- internal-recon
