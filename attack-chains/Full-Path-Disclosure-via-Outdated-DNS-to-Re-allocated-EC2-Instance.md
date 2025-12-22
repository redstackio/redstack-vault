---
id: ff114345-d082-447f-a80c-300844fe3d12
name: Full Path Disclosure via Outdated DNS to Re-allocated EC2 Instance
type: attack_chain
description: >-
  Attack chain exploiting outdated DNS records pointing to a re-allocated AWS
  EC2 instance, leading to full path disclosure through server error messages.
verified: false
submitted: true
step_count: 2
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.357Z'
procedures:
  - '[[procedures/DNS-Resolution-for-Subdomain-Discovery]]'
  - '[[procedures/Trigger-Server-Error-for-Path-Disclosure]]'
techniques:
  - '[[Gather Victim Network Information]]'
  - '[[Exploit Public-Facing Application]]'
tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
tags:
  - dns-misconfig
  - info-disclosure
  - path-disclosure
  - aws-ec2
platforms:
  - Web
  - AWS
tools: []
complexity: low
skill_level: beginner
impact_level: low
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Network Information]]'
  - '[[Exploit Public-Facing Application]]'
---

# Full Path Disclosure via Outdated DNS to Re-allocated EC2 Instance

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Resolve DNS for Subdomain] --> B[Access Endpoint and Trigger Error]
    B --> C[Path Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None specific (standard DNS and HTTP tools like dig and curl)

### Target Environment

- AWS EC2 instances with web servers
- Outdated DNS records for subdomains
- Publicly resolvable subdomains

### Initial Access Requirements

- Internet access for DNS resolution and HTTP requests
- No credentials required
- No prior access needed

## Detailed Attack Procedures

### Step 1: DNS Resolution for Subdomain Discovery
procedure: [[procedures/DNS-Resolution-for-Subdomain-Discovery]]

**Objective**: Identify the IP address associated with the target subdomain to detect potential misconfigurations.

**Instructions**: Use [[commands/dig-resolve-subdomain]] to perform a DNS lookup on the subdomain:

```bash
dig 27.prd.vine.co
```

**Expected Output**: DNS resolution showing the IP address of the EC2 instance, revealing it points to a previously deallocated Vine-owned instance now re-allocated.

**Success Indicators**:
- IP address resolved successfully
- IP indicates an AWS EC2 instance (e.g., via whois or known ranges)

### Step 2: Trigger Server Error for Path Disclosure
procedure: [[procedures/Trigger-Server-Error-for-Path-Disclosure]]

**Objective**: Access the web endpoint to trigger an error that discloses internal server paths due to misconfiguration.

**Instructions**: Send an HTTP request to the resolved endpoint using [[commands/curl-access-endpoint]]:

```bash
curl -v http://27.prd.vine.co/
```

**Expected Output**: Server error response (e.g., 500 Internal Server Error) containing full internal file paths, such as /var/www/html/... on the re-allocated instance.

**Success Indicators**:
- Error message exposes server paths
- No authentication required; paths reveal internal structure

## Attack Chain Summary

### Key Achievements

1. Discovered misconfigured DNS pointing to unintended EC2 instance
2. Triggered path disclosure without exploitation
3. Identified low-severity information leak for potential further reconnaissance

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Gather Victim Network Information]] Gather Victim Network Information
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
