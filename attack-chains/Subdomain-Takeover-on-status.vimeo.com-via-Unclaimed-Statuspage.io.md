---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - subdomain-takeover
  - dns
  - phishing
  - session-hijacking
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
  - DNS
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Discover-Unclaimed-Subdomain]]'
  - '[[procedures/Claim-Subdomain-for-Takeover]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:51:10.433Z'
description: >-
  Attack chain exploiting an unclaimed subdomain on statuspage.io to takeover
  status.vimeo.com, enabling phishing and session hijacking under the trusted
  Vimeo domain.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Gather Victim Host Information]]'
---
# Subdomain Takeover on status.vimeo.com via Unclaimed Statuspage.io

Multi-stage attack chain demonstrating a subdomain takeover vulnerability, where an unclaimed DNS CNAME record allows an attacker to hijack a trusted subdomain for malicious purposes such as phishing and cookie theft.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Discover Unclaimed Subdomain] --> B[Initial Access: Claim and Control Subdomain]
    B --> C[Impact: Phishing and Session Compromise]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Web browser for accessing pages
- DNS lookup tool (e.g., dig or nslookup)

### Target Environment

- Public DNS resolution
- Access to statuspage.io service
- No authentication required for discovery

### Initial Access Requirements

- Internet access
- No prior credentials needed
- Ability to register a free account on statuspage.io

## Detailed Attack Procedures

### Step 1: Discover Unclaimed Subdomain
procedure: [[procedures/Discover-Unclaimed-Subdomain]]

**Objective**: Identify subdomains with DNS records pointing to external services that are unclaimed, exposing takeover risks.

**Instructions**: Start by performing a DNS lookup on the target subdomain to check its CNAME record using [[commands/dig-cname-lookup]]:

```bash
dig status.vimeo.com CNAME
```

This reveals if it points to hosted.statuspage.io. Then, access the subdomain URL in a browser or with curl to verify if it's unclaimed:

```bash
curl -I http://status.vimeo.com
```

Look for indicators like a default statuspage.io claim page.

**Expected Output**: DNS response showing CNAME to hosted.statuspage.io; HTTP response indicating an unclaimed page.

**Success Indicators**:
- CNAME points to external service without active configuration
- Page shows "claim this page" prompt on statuspage.io

### Step 2: Claim Subdomain for Takeover
procedure: [[procedures/Claim-Subdomain-for-Takeover]]

**Objective**: Register and claim the unclaimed subdomain to gain full control, enabling deployment of malicious content.

**Instructions**: Navigate to statuspage.io and create a free account. During setup, enter the subdomain (status.vimeo.com) to claim it. Once claimed, customize the page with phishing forms or scripts to exploit same-origin policy and steal cookies.

For verification, access the now-controlled subdomain:

```bash
curl http://status.vimeo.com
```

**Expected Output**: Successful claim confirmation; custom content loads under the subdomain.

**Success Indicators**:
- Control panel on statuspage.io shows the subdomain as active
- Malicious page (e.g., fake login) is accessible via the subdomain
- Potential for cookie theft via JavaScript under vimeo.com domain

## Attack Chain Summary

### Key Achievements

1. Identified unclaimed DNS CNAME for status.vimeo.com pointing to statuspage.io
2. Demonstrated ability to claim and control the subdomain without authentication
3. Highlighted risks of phishing, same-origin exploitation, and session hijacking impacting Vimeo users

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Gather Victim Host Information]] Gather Victim Host Information

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Reconnaissance]] Reconnaissance

---
*Last updated: 2023-10-01T12:00:00Z*
