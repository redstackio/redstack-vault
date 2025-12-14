---
tags:
  - subdomain-takeover
  - dns
  - ns-records
  - cloud
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - DNS
  - Cloud
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Dangling-NS-Records]]'
  - '[[procedures/Claim-Unclaimed-DNS-Zone]]'
  - '[[procedures/Host-Proof-of-Concept-on-Taken-Over-Subdomain]]'
step_count: 3
techniques:
  - '[[Hardware]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:01.841Z'
description: >-
  Attack chain exploiting dangling NS records to take over a subdomain, enabling
  malicious content hosting and potential account takeovers.
skill_level: intermediate
impact_level: high
id: 9a1c6982-a5e6-4f0b-a42e-7d4a7cde4ca5
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Hardware]]'
  - '[[Exploit Public-Facing Application]]'
---
---
id: 123e4567-e89b-12d3-a456-426614174000
name: Subdomain Takeover via Dangling NS Records on us-east4.37signals.com
type: attack_chain
description: "Attack chain exploiting dangling NS records to take over a subdomain, enabling malicious content hosting and potential account takeovers."
verified: false
submitted: false
step_count: 3
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
procedures: [[procedures/Discover-Dangling-NS-Records]], [[procedures/Claim-Unclaimed-DNS-Zone]], [[procedures/Host-Proof-of-Concept-on-Taken-Over-Subdomain]]
techniques: [[Hardware]], [[Exploit Public-Facing Application]]
tactics: [[Reconnaissance]], [[Initial Access]]
tags: subdomain-takeover, dns, ns-records, cloud
platforms: DNS, Cloud
tools: []
---

# Subdomain Takeover via Dangling NS Records on us-east4.37signals.com

Multi-stage attack chain demonstrating a complete subdomain takeover workflow via misconfigured DNS NS records.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Discover Dangling NS] --> B[Initial Access: Claim Zone]
    B --> C[Execution: Host Malicious Content]
    C --> D[Impact: Takeover and Exploitation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- DNS lookup tools like [[commands/dig-dns-query]]
- Access to a cloud DNS provider account (e.g., AWS Route 53)

### Target Environment

- DNS infrastructure with potential misconfigurations
- Cloud provider services (redacted, likely AWS)
- No specific ports required; DNS queries over port 53

### Initial Access Requirements

- Public DNS resolution access
- Attacker account on the target cloud DNS provider
- No prior credentials on the victim domain

## Detailed Attack Procedures

### Step 1: Discover Dangling NS Records
procedure: [[procedures/Discover-Dangling-NS-Records]]

**Objective**: Identify misconfigured NS records pointing to unclaimed zones to find takeover opportunities.

**Instructions**: Query the DNS for NS records of the target subdomain using [[commands/dig-dns-query]]:

```bash
dig NS us-east4.37signals.com
```

Analyze the output for nameservers belonging to a cloud provider that are not claimed. Verify if the zone is unclaimed by attempting to access the provider's console for that zone.

**Expected Output**: NS records listing unclaimed nameservers, e.g., ns-123.awsdns-01.com.

**Success Indicators**:
- NS records point to external, unclaimed cloud zone
- Zone availability confirmed in provider console

### Step 2: Claim Unclaimed DNS Zone
procedure: [[procedures/Claim-Unclaimed-DNS-Zone]]

**Objective**: Register the dangling zone in the attacker's control to gain subdomain authority.

**Instructions**: Log into the cloud provider's DNS console (e.g., AWS Route 53) and create a new hosted zone for the identified unclaimed domain. No specific command; this is a UI action, but verify with [[commands/dig-dns-query]] post-claim:

```bash
dig NS us-east4.37signals.com
```

The NS records should now resolve to the attacker's nameservers.

**Expected Output**: Hosted zone created successfully; DNS queries reflect attacker control.

**Success Indicators**:
- Zone claimed without errors
- Victim subdomain NS records now point to attacker's zone

### Step 3: Host Proof-of-Concept on Taken-Over Subdomain
procedure: [[procedures/Host-Proof-of-Concept-on-Taken-Over-Subdomain]]

**Objective**: Demonstrate control by hosting content, simulating phishing or XSS exploitation.

**Instructions**: In the claimed zone, add DNS records (e.g., A record pointing to attacker's server) and upload a simple HTML page. Access via browser: http://us-east4.37signals.com/takeover.html. Verify resolution with [[commands/dig-dns-query]]:

```bash
dig A us-east4.37signals.com
```

Host the page on the attacker's server to confirm takeover.

**Expected Output**: Custom page loads at the subdomain URL.

**Success Indicators**:
- Malicious page accessible via subdomain
- Potential for cookie-based takeovers or XSS confirmed

## Attack Chain Summary

### Key Achievements

1. Identified and exploited dangling NS records for subdomain takeover
2. Gained full DNS control over us-east4.37signals.com
3. Demonstrated impact through proof-of-concept hosting, enabling further attacks like phishing or XSS

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Hardware]] Gather Victim Host Information: DNS
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
