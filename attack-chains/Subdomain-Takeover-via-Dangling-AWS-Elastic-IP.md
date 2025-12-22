---
id: ac-uuid-001
name: Subdomain Takeover via Dangling AWS Elastic IP
tags:
  - subdomain-takeover
  - aws
  - dns
  - elastic-ip
  - phishing
type: attack_chain
tools:
  - '[[tools/recloud]]'
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
verified: false
platforms:
  - AWS
  - Cloud
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Resolve-DNS-Record-for-Subdomain]]'
  - '[[procedures/Allocate-Reusable-AWS-Elastic-IP]]'
  - '[[procedures/Verify-Subdomain-Takeover]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Scanning IP Blocks]]'
updated_at: '2025-12-14T04:51:10.935Z'
description: >-
  Attack chain exploiting a dangling AWS Elastic IP to takeover a subdomain,
  enabling phishing via cookie and CORS access.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Scanning IP Blocks]]'
---
# Subdomain Takeover via Dangling AWS Elastic IP

Multi-stage attack chain demonstrating a complete workflow for exploiting a dangling AWS Elastic IP to takeover a subdomain like mta1a1.spmail.uber.com, leading to DNS zone control and potential phishing.

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
    A[Resolve DNS Record] --> B[Allocate Elastic IP]
    B --> C[Verify Takeover]
    C --> D[Phishing Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/recloud]]
- AWS CLI (configured with researcher account)
- DNS resolution tool like dig

### Target Environment

- AWS Cloud platform
- DNS services
- AWS EC2 and Elastic IP services

### Initial Access Requirements

- AWS account with permissions to allocate Elastic IPs
- Network access to resolve public DNS
- No prior credentials on target; exploits public misconfiguration

## Detailed Attack Procedures

### Step 1: Resolve DNS Record
procedure: [[procedures/Resolve-DNS-Record-for-Subdomain]]

**Objective**: Identify the IP address associated with the target subdomain to check for dangling status.

**Instructions**: Use [[commands/dig-resolve-a-record]] to query the A record of the subdomain:

```bash
dig mta1a1.spmail.uber.com A +short
```

**Expected Output**: The resolved IP address, e.g., 52.XX.XX.XX, which is an AWS Elastic IP.

**Success Indicators**:
- IP address obtained and confirmed as AWS-owned Elastic IP
- IP appears available for reuse (no active association)

### Step 2: Allocate Elastic IP
procedure: [[procedures/Allocate-Reusable-AWS-Elastic-IP]]

**Objective**: Claim the dangling Elastic IP from AWS pool to redirect subdomain traffic.

**Instructions**: Use [[commands/aws-allocate-address]] to request the specific IP in your AWS account:

```bash
aws ec2 allocate-address --domain vpc --address 52.XX.XX.XX
```

Then associate it with an EC2 instance using [[commands/aws-associate-address]]:

```bash
aws ec2 associate-address --instance-id i-1234567890abcdef0 --allocation-id eipalloc-12345678 --allow-reassociation
```

**Expected Output**: Confirmation of IP allocation and association; subdomain now resolves to your instance.

**Success Indicators**:
- IP successfully allocated without error
- DNS resolution points to your controlled resource

### Step 3: Verify Takeover
procedure: [[procedures/Verify-Subdomain-Takeover]]

**Objective**: Confirm control over the subdomain and demonstrate impact like accessing cookies or CORS.

**Instructions**: Host a simple web server on the associated EC2 instance and re-resolve the DNS using [[commands/dig-resolve-a-record]]:

```bash
dig mta1a1.spmail.uber.com A +short
```

Use [[tools/recloud]] to simulate or verify the takeover scenario:

```bash
recloud --ip 52.XX.XX.XX --subdomain mta1a1.spmail.uber.com
```

Test access to subdomain-scoped resources by curling the subdomain:

```bash
curl -H "Host: mta1a1.spmail.uber.com" http://your-ec2-ip
```

**Expected Output**: Subdomain resolves to your server; requests return your hosted content, potentially exposing cookies or bypassing CORS.

**Success Indicators**:
- Subdomain under attacker control
- Ability to serve phishing content or access scoped policies

## Attack Chain Summary

### Key Achievements

1. Identified dangling Elastic IP via DNS resolution
2. Allocated and associated IP to takeover subdomain
3. Demonstrated full DNS zone control for phishing

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Scanning IP Blocks]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Reconnaissance]]

---

*Last updated: 2023-10-01T00:00:00Z*
