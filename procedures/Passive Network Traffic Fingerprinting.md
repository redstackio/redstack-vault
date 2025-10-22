---
id: f3302b27-d0ce-4038-9595-768e2f3012fa
name: Passive Network Traffic Fingerprinting
type: procedure
verified: true
submitted: true
created_at: '2019-09-12T18:07:35.334769+00:00'
updated_at: '2023-05-26T00:51:21.284862+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Sniffing|T1040 - Network Sniffing]]'
platforms:
- Linux
- Windows
tags:
- '[[data exposure]]'
- '[[Network]]'
commands:
- '[[p0f Passive Traffic Fingerprinting]]'
---

# Passive Network Traffic Fingerprinting

**Status**: ✓ Verified

## Summary

Analyze network traffic passively in order to fingerprint devices and services communicating. 

## Description

# Description

Analyze network traffic passively in order to fingerprint devices and services communicating.

# Instructions

**Command** ([[p0f Passive Traffic Fingerprinting]]):

```bash
p0f -i $_INTERFACE -p -o $_OUTPUT.log
```

## Platforms

- Linux
- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Sniffing|T1040 - Network Sniffing]]

## Commands Used

- [[p0f Passive Traffic Fingerprinting]]

## Tags

- [[data exposure]]
- [[Network]]
