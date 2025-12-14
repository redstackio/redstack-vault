---
id: proc-uuid-3
tags:
  - ssrf
  - bypass
  - encoded-ip
type: procedure
tools:
  - '[[tools/private-address-check]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:53:38.150Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-SSRF-Filter-with-Encoded-IPs

## Summary

This procedure exploits the Resolv.getaddresses bug to bypass private IP filtering in SSRF-protected applications like HackerOne Integrations by submitting URLs with encoded private IPs that resolve to empty arrays.

## Description

The private_address_check gem fails to block requests when Resolv.getaddresses returns [], as empty results don't match the private blacklist. Attackers craft URLs like http://0177.1:22/ to target internal services (e.g., localhost port 22). This blind SSRF allows potential scanning but may not enable direct exfiltration due to lack of response visibility. Requires knowledge of the target's resolution environment.

## Requirements

1. Authenticated access to the vulnerable Integrations panel
2. Knowledge of buggy Linux resolver behavior
3. List of encoded private IP variants

## Defense

Defensive measures and detection strategies:

- Switch to Socket.getaddrinfo for robust resolution: require 'socket'; Socket.getaddrinfo(hostname, nil).sample[3]
- Decode and normalize all hostnames before processing
- Implement allowlists for permitted hosts instead of blacklists

## Objectives

1. Evade private IP detection using empty resolution results
2. Enable requests to internal endpoints like localhost
3. Demonstrate filter bypass for further attacks

## Instructions

### Step 1: Craft Encoded URL Payloads

**Context**: Generate URLs using encoded forms of 127.0.0.1 to trigger the bug.

No command; manually create payloads: http://127.000.000.1:22/, http://0177.1:22/, http://0x7f.1:22/.

> These should resolve to [] on vulnerable systems, bypassing checks.

### Step 2: Submit to Integrations Panel

**Context**: Input the crafted URLs in the user-supplied field of https://hackerone.com/{BBP}/integrations.

Submit via the web form.

> Observe if the request proceeds without private IP errors, indicating bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/private-address-check]]

## Tags

- ssrf
- bypass
