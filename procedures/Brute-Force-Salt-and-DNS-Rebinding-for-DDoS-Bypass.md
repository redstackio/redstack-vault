---
id: proc-uuid-12
tags:
  - salt-bruteforce
  - dns-rebinding
  - ddos
type: procedure
tools:
  - '[[tools/Go]]'
tactics:
  - '[[Command and Control]]'
commands:
  - '[[commands/go-salt-bruteforce]]'
  - '[[commands/echo-md5-payload-hash]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
  - '[[T1071.004]]'
updated_at: '2025-12-14T17:24:55.501Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Command and Control]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
  - '[[T1071.004]]'
---
# Brute-Force-Salt-and-DNS-Rebinding-for-DDoS-Bypass

## Summary

This procedure brute-forces a weak MD5 salt using known input/hash pairs from rockyou.txt, crafts a payload targeting localhost, and uses DNS rebinding to evade local IP checks, triggering a self-DDoS that reveals the flag.

## Description

The /attack-box/launch hashes md5(salt + target) with salt from wordlist; crack via script. Rebind DNS to resolve to 127.0.0.1 after initial check. Targets Go-based DDoS tools.

## Requirements

1. Go compiler for salt script
2. DNS rebind service/domain
3. Known hash pair

## Defense

Defensive measures and detection strategies:

- Use strong salts/random keys
- Validate IPs without DNS reliance
- Block rebinding domains

## Objectives

1. Recover salt
2. Craft localhost payload
3. Bypass checks for DDoS

## Instructions

### Step 1: Brute-Force Salt

**Context**: Use Go script with wordlist.

**Command** ([[commands/go-salt-bruteforce]]):
```bash
./salt.go
```

> Finds salt 'mrgrinch463'.

### Step 2: Generate Payload Hash

**Context**: Hash salt + '127.0.0.1'.

**Command** ([[commands/echo-md5-payload-hash]]):
```bash
echo -n "mrgrinch463127.0.0.1" | md5sum
```

> Outputs 3e3f8df1658372edf0214e202acb460b.

### Step 3: Launch with Rebinding

**Context**: Submit payload with rebind domain.

Use domain that rebinds to 127.0.0.1; DDoS triggers flag.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control]] Command and Control

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[T1071.004]] DNS Manipulation (Rebinding)

### Sub-Techniques

- None

## Commands Used

- [[commands/go-salt-bruteforce]]
- [[commands/echo-md5-payload-hash]]

## Tools Used

- [[tools/Go]]

## Tags

- [[salt-bruteforce]]
- [[dns-rebinding]]
- [[ddos]]
