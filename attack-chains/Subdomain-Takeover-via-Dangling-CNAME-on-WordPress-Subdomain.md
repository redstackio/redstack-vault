---
id: ac-subdomain-takeover-wordpress
tags:
  - subdomain-takeover
  - dns
  - cname
  - wordpress
type: attack_chain
tools:
  - '[[tools/host]]'
tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - DNS
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Detect-and-Confirm-Subdomain-Takeover]]'
step_count: 2
techniques:
  - '[[Hardware]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:24.168Z'
description: >-
  Demonstrates discovery and confirmation of a subdomain takeover vulnerability
  through misconfigured DNS records pointing to an abandoned WordPress.com
  subdomain, enabling potential control and malicious hosting.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Hardware]]'
  - '[[Exploit Public-Facing Application]]'
---
# Subdomain Takeover via Dangling CNAME on WordPress Subdomain

Multi-stage attack chain demonstrating the discovery and confirmation of a subdomain takeover vulnerability on code.wordpress.net, where DNS records alias to an abandoned WordPress.com subdomain, allowing potential attacker control for hosting malicious content or impersonation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Observe Subdomain Error] --> B[Confirm DNS Misconfiguration]
    B --> C[Potential Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/host]]

### Target Environment

- Web browser for initial access
- Command-line interface with DNS tools
- Required services/ports: DNS (port 53), HTTP (port 80)
- Network access requirements: Internet connectivity to resolve public DNS and access web URLs

### Initial Access Requirements

- No credentials required
- External network position (public internet)
- No prior access needed

## Detailed Attack Procedures

### Step 1: Observe Subdomain Error
procedure: [[procedures/Detect-and-Confirm-Subdomain-Takeover]]

**Objective**: Access the target subdomain to identify signs of misconfiguration, such as error messages indicating unclaimed domain mapping.

**Instructions**: Open a web browser and navigate to the target subdomain URL, e.g., http://code.wordpress.net. Observe the displayed error message, which suggests the domain is aliased to an unupgraded or abandoned service.

**Expected Output**: Error page stating: "Warning! Domain mapping upgrade for this domain not found. Please log in and go to the Domains Upgrades page of your blog to use this domain."

**Success Indicators**:
- Error message related to domain mapping appears
- No legitimate content loads, indicating potential abandonment

### Step 2: Confirm DNS Misconfiguration
procedure: [[procedures/Detect-and-Confirm-Subdomain-Takeover]]

**Objective**: Perform a DNS lookup to trace the CNAME chain and confirm the dangling record pointing to an unclaimed WordPress.com service.

**Instructions**: Use the [[commands/host-dns-lookup]] command to query the DNS records of the target subdomain:

```bash
host code.wordpress.net
```

Analyze the output for CNAME aliases leading to load balancers of an abandoned service.

**Expected Output**: Resolution showing aliases: "code.wordpress.net is an alias for wpprojects.wordpress.com. wpprojects.wordpress.com is an alias for lb.wordpress.com. lb.wordpress.com has address 192.0.78.13 lb.wordpress.com has address 192.0.78.12"

**Success Indicators**:
- CNAME chain reveals dangling pointers to unclaimed subdomains
- IP addresses match known service providers (e.g., WordPress.com load balancers)

## Attack Chain Summary

### Key Achievements

1. Identified subdomain misconfiguration through web access error
2. Confirmed vulnerability via DNS resolution, exposing takeover opportunity
3. Highlighted potential for attacker to claim the subdomain and host malicious content

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Hardware]] Gather Victim Host Information: Domains
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
