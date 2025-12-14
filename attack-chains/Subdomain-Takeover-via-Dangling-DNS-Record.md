---
tags:
  - subdomain-takeover
  - dns
  - dangling-record
  - phishing
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
  - '[[procedures/Identify-and-Exploit-Dangling-DNS-for-Subdomain-Takeover]]'
step_count: 1
techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Hardware]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:23.920Z'
description: >-
  Attack chain demonstrating the discovery and potential exploitation of a
  dangling DNS record leading to subdomain takeover, enabling phishing or
  spoofing.
skill_level: intermediate
impact_level: high
id: a801e60f-34f0-41ff-be3d-26af3d1a974e
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Hardware]]'
  - '[[Exploit Public-Facing Application]]'
---
# Subdomain Takeover via Dangling DNS Record

Multi-stage attack chain demonstrating a complete attack workflow for identifying and potentially exploiting dangling DNS records to achieve subdomain takeover.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Identify Dangling DNS] --> B[Initial Access: Subdomain Takeover]
    B --> C[Objective: Phishing or Spoofing]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None specific; uses standard DNS query tools like dig or nslookup.

### Target Environment

- DNS infrastructure with potential misconfigurations.
- Access to public DNS resolvers.
- No privileged access required.

### Initial Access Requirements

- Public internet access.
- Knowledge of target domain.
- No credentials needed.

## Detailed Attack Procedures

### Step 1: Reconnaissance and Identification
procedure: [[procedures/Identify-and-Exploit-Dangling-DNS-for-Subdomain-Takeover]]

**Objective**: Discover unused or dangling DNS records pointing to claimable third-party services, enabling potential subdomain takeover.

**Instructions**: Query the target's DNS records to identify CNAMEs or other records pointing to unused services. Use [[commands/dig-query-dns]] to perform a DNS lookup on suspected subdomains:

```bash
dig sales.mixmax.com CNAME
```

Analyze the response for pointers to expired or unused services (e.g., Heroku, GitHub Pages). If a dangling record is found, verify if the service can be registered by the attacker.

**Expected Output**: DNS response showing a CNAME to a third-party service that is no longer in use by the target.

**Success Indicators**:
- CNAME points to an unused/expired service.
- Service registration is possible for the attacker.

## Attack Chain Summary

### Key Achievements

1. Identification of dangling DNS record for sales.mixmax.com.
2. Assessment of takeover potential for phishing or spoofing.
3. Prompt remediation by target to remove the record.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Hardware]] Domains
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
