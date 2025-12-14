---
tags:
  - ssrf
  - bypass
  - ruby
  - testing
type: procedure
tools:
  - '[[tools/IRB]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/require-private-address-check]]'
  - '[[commands/private-address-check-0.0.0.0]]'
platforms:
  - Ruby
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: f210adb1-695e-4cfe-b41a-808223191427
created_at: '2025-12-14T04:08:54.866Z'
updated_at: '2025-12-14T04:08:54.866Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test Private Address Check Gem Bypass

## Summary

This procedure tests the private_address_check Ruby gem to confirm it fails to recognize 0.0.0.0 as a private address, enabling SSRF bypasses in applications like HackerOne that rely on it for filtering.

## Description

The private_address_check gem is used to validate IP addresses and block private ones in SSRF scenarios. However, its exclusion list omits the 0.0.0.0/8 netblock, causing `PrivateAddressCheck.private_address?('0.0.0.0')` to return false. This procedure uses IRB to load the gem and execute the check, verifying the flaw in a controlled Ruby environment. Prerequisites include Ruby installed with the gem available (e.g., via `gem install private_address_check`).

## Requirements

1. Ruby environment with IRB
2. private_address_check gem installed
3. Basic knowledge of Ruby syntax

## Defense

Defensive measures and detection strategies:

- Update or patch the gem to include 0.0.0.0/8 in private address checks
- Implement additional SSRF protections like URL parsing normalization
- Monitor IRB or Ruby console usage in development environments for anomaly detection

## Objectives

1. Verify the gem's misclassification of 0.0.0.0
2. Confirm the bypass potential for SSRF exploitation
3. Document the flaw for reporting or patching

## Instructions

### Step 1: Launch IRB and Load Gem

**Context**: Start an interactive Ruby session and require the gem to prepare for testing.

**Command** ([[commands/require-private-address-check]]):
```ruby
require 'private_address_check'
```

> This loads the private_address_check library. Expected output: `true` if successful, indicating the gem is available.

### Step 2: Test Private Address Check

**Context**: Execute the method to check if 0.0.0.0 is treated as private, revealing the flaw.

**Command** ([[commands/private-address-check-0.0.0.0]]):
```ruby
PrivateAddressCheck.private_address?("0.0.0.0")
```

> This queries the gem's logic. Expected output: `false`, confirming 0.0.0.0 evades private address detection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/require-private-address-check]]
- [[commands/private-address-check-0.0.0.0]]

## Tools Used

- [[tools/IRB]]

## Tags

- ssrf
- ruby
- gem-testing
