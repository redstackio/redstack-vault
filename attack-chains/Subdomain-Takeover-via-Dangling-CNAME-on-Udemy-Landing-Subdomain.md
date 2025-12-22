---
tags:
  - subdomain-takeover
  - dns
  - unbounce
  - phishing
  - xss
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - DNS
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Dangling-CNAME-Records]]'
  - '[[procedures/Verify-Subdomain-Availability-on-Unbounce]]'
step_count: 2
techniques:
  - '[[Hardware]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:24.218Z'
description: >-
  Demonstrates discovery of a dangling DNS CNAME record for landing.udemy.com
  pointing to Unbounce, enabling potential subdomain takeover for phishing or
  XSS attacks.
skill_level: intermediate
impact_level: high
id: 295f2fd0-26a2-45cc-95d3-8f3df898dd44
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Hardware]]'
  - '[[Exploit Public-Facing Application]]'
---
# Subdomain Takeover via Dangling CNAME on Udemy Landing Subdomain

Multi-stage attack chain demonstrating a complete attack workflow for identifying and verifying a subdomain takeover vulnerability.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discover CNAME Record] --> B[Verify Availability]
    B --> C[Potential Takeover and Phishing]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[commands/dig-cname-query]]

### Target Environment

- DNS resolution access
- Internet connectivity for third-party service verification
- No specific ports required beyond standard DNS (port 53)

### Initial Access Requirements

- Public DNS query access
- No credentials needed for discovery phase
- Ability to contact third-party support (e.g., Unbounce chat)

## Detailed Attack Procedures

### Step 1: Discover Dangling CNAME Record
procedure: [[procedures/Discover-Dangling-CNAME-Records]]

**Objective**: Query DNS records to identify CNAMEs pointing to unclaimed third-party services, revealing potential takeover opportunities.

**Instructions**: Use [[commands/dig-cname-query]] to query the CNAME for the target subdomain:

```bash
dig landing.udemy.com CNAME
```

Analyze the output for pointers to services like unbouncepages.com. Note the TTL (e.g., 300 seconds) to understand propagation times.

**Expected Output**: CNAME record showing landing.udemy.com points to pages.unbounce.com or similar, with no active claim.

**Success Indicators**:
- CNAME record returned pointing to a third-party service
- No A/AAAA records indicating active hosting

### Step 2: Verify Availability on Third-Party Service
procedure: [[procedures/Verify-Subdomain-Availability-on-Unbounce]]

**Objective**: Confirm the subdomain is unclaimed on the third-party platform, allowing registration for takeover.

**Instructions**: Contact Unbounce support via their chat or email interface. Provide the CNAME details and inquire if the domain (e.g., udemy.com) is linked or claimed. Do not attempt registration without authorization.

**Expected Output**: Confirmation from support that the domain/subdomain is available and not linked.

**Success Indicators**:
- Support verifies no active claim
- Potential to register and host content on the subdomain

## Attack Chain Summary

### Key Achievements

1. Identified dangling CNAME for landing.udemy.com pointing to unbouncepages.com
2. Verified unclaimed status via Unbounce support
3. Highlighted risk of phishing or XSS on legitimate Udemy subdomain

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Hardware]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]
- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
