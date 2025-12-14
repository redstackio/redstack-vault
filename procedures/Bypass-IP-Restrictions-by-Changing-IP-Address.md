---
tags:
  - ip-bypass
  - proxy
  - vpn
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Connection Proxy]]'
updated_at: '2025-12-14T17:24:42.862Z'
sub_techniques: []
id: f84b6649-04f1-4db2-a57d-c1a02d28a79c
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Connection Proxy]]'
---
# Bypass-IP-Restrictions-by-Changing-IP-Address

## Summary

This procedure changes the attacker's IP address to evade any global or session-based rate limiting imposed by Twitter after exhaustion attempts, allowing continuation of the enumeration without blocks.

## Description

Twitter may apply IP-level restrictions alongside account-based limits. Switching IPs via VPN, proxy, or network change resets the session context, enabling fresh brute force requests while the phone number remains rate-limited from prior exhaustion. This is a standard evasion technique in web-based attacks.

## Requirements

1. Access to IP-changing tools like VPN or proxies.
2. Verification method for new IP (e.g., online checker).
3. Prior exhaustion completed on original IP.

## Defense

Defensive measures and detection strategies:

- Implement device fingerprinting or behavioral analysis beyond IP.
- Correlate attempts across IPs using username patterns.
- Shorten rate limit windows and add multi-factor checks.

## Objectives

1. Evade IP-based blocks to resume testing.
2. Maintain the phone rate limit state from previous steps.
3. Enable efficient brute forcing.

## Instructions

### Step 1: Switch Network

**Context**: Obtain a new IP to reset session limits.

Connect to a VPN service or proxy and disable the previous connection.

> Example: Use a service like ExpressVPN to switch servers.

### Step 2: Verify New IP

**Context**: Confirm the change to ensure no carryover restrictions.

Visit an IP checker site (e.g., whatismyipaddress.com) to note the new IP.

> Successful output: Different IP displayed, and Twitter access unblocked.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Connection Proxy]] Proxy

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ip-bypass]]
- [[proxy]]
- [[vpn]]
