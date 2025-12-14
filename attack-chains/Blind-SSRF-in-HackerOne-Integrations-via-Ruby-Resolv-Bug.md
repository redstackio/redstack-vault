---
id: ac-uuid-1
tags:
  - ssrf
  - blind-ssrf
  - ruby
  - resolv
  - hackerone
type: attack_chain
tools:
  - '[[tools/irb]]'
  - '[[tools/private-address-check]]'
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Investigate-Integrations-SSRF-Protections]]'
  - '[[procedures/Discover-Resolv-getaddresses-Bug]]'
  - '[[procedures/Bypass-SSRF-Filter-with-Encoded-IPs]]'
  - '[[procedures/Attempt-SSRF-Exploitation-for-Network-Scanning]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:53:38.167Z'
description: >-
  A multi-stage attack chain exploiting a blind SSRF vulnerability in
  HackerOne's Integrations feature by abusing inconsistent behavior in Ruby's
  Resolv.getaddresses function, enabling potential internal network scanning.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Blind SSRF in HackerOne Integrations via Ruby Resolv Bug

Multi-stage attack chain demonstrating exploitation of a blind Server-Side Request Forgery (SSRF) in HackerOne's Integrations feature by leveraging a bug in Ruby's Resolv.getaddresses function within the private_address_check gem.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Investigate Integrations] --> B[Discover Resolv Bug]
    B --> C[Bypass Filter]
    C --> D[Attempt Exploitation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/irb]]
- [[tools/private-address-check]]

### Target Environment

- Web platform with Ruby-based backend (e.g., HackerOne Integrations at https://hackerone.com/{BBP}/integrations)
- Required services/ports: Port 22 (SSH) for scanning examples
- Network access requirements: Authenticated access to the target's Integrations panel

### Initial Access Requirements

- Valid user account on HackerOne
- Ability to submit user-supplied URLs in the Integrations feature
- Local Linux environment for testing Ruby resolver behavior

## Detailed Attack Procedures

### Step 1: Investigate Integrations Feature and SSRF Protections
procedure: [[procedures/Investigate-Integrations-SSRF-Protections]]

**Objective**: Analyze the target's Integrations panel to understand SSRF protections and identify the use of the private_address_check gem.

**Instructions**: Access the Integrations panel at https://hackerone.com/{BBP}/integrations and review how user-supplied URLs are processed for resolution and private IP checking.

**Expected Output**: Confirmation that Resolv.getaddresses is used via the private_address_check gem to resolve and filter URLs against a private IP blacklist.

**Success Indicators**:
- Identification of URL resolution mechanism
- Understanding of blacklist-based filtering

### Step 2: Discover Bug in Ruby's Resolv.getaddresses
procedure: [[procedures/Discover-Resolv-getaddresses-Bug]]

**Objective**: Test Ruby's Resolv.getaddresses on different Linux machines to uncover inconsistent resolution of encoded IP addresses.

**Instructions**: Launch an IRB session and execute [[commands/ruby-require-resolv]] followed by [[commands/ruby-resolv-getaddresses-127-000-000-1]] on multiple machines. Compare outputs for encoded IPs like '127.000.000.1', '0177.1', and '0x7f.1'.

```ruby
require 'resolv'
Resolv.getaddresses('127.000.000.1')
```

**Expected Output**: Empty array [] on some machines, indicating the bug; normal resolution ["127.0.0.1"] on others.

**Success Indicators**:
- Inconsistent outputs observed across systems
- Bug confirmed for encoded private IPs

### Step 3: Bypass SSRF Filter Using the Bug
procedure: [[procedures/Bypass-SSRF-Filter-with-Encoded-IPs]]

**Objective**: Craft URLs with encoded private IPs to evade the private address check in the Integrations panel.

**Instructions**: Submit URLs like http://0177.1:22/, http://0x7f.1:22/, or http://127.000.001:22/ in the Integrations feature. The Resolv.getaddresses bug causes an empty array, bypassing the blacklist.

**Expected Output**: Successful request to internal/private addresses without filtering.

**Success Indicators**:
- Requests to localhost or internal IPs are not blocked
- Evidence of filter evasion in application responses

### Step 4: Attempt Exploitation for Data Exfiltration
procedure: [[procedures/Attempt-SSRF-Exploitation-for-Network-Scanning]]

**Objective**: Use the bypass to scan internal networks or attempt data exfiltration, such as port scanning on localhost.

**Instructions**: Leverage the bypassed URLs to probe internal services, e.g., targeting port 22 on encoded localhost IPs. Monitor for responses indicating successful internal access.

**Expected Output**: Potential scan results or error messages revealing internal network details, though full exfiltration may be limited.

**Success Indicators**:
- Internal port responses detected
- Theoretical high-impact access confirmed, even if practical exfiltration fails

## Attack Chain Summary

### Key Achievements

1. Discovered platform-specific bug in Ruby's DNS resolver
2. Bypassed SSRF protections in HackerOne's Integrations
3. Enabled potential internal reconnaissance via blind SSRF
4. Highlighted risks in gem-based filtering mechanisms

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Reconnaissance]]

---
*Last updated: 2023-10-01T00:00:00Z*
