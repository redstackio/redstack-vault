---
id: ac-2552243-dod-takeover
tags:
  - subdomain-takeover
  - dns
  - cname
  - aws-elb
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
  - AWS
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Dangling-CNAME-Record]]'
  - '[[procedures/Verify-Subdomain-Takeover-with-POC]]'
step_count: 2
techniques:
  - '[[Hardware]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:38:39.671Z'
description: >-
  Attack chain exploiting a dangling DNS CNAME record pointing to a non-existent
  AWS ELB, enabling subdomain takeover to host malicious content and perform
  phishing or XSS under a DoD domain.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Hardware]]'
  - '[[Exploit Public-Facing Application]]'
---
# DoD Subdomain Takeover via Dangling AWS ELB CNAME Record

Multi-stage attack chain demonstrating a subdomain takeover on a U.S. Department of Defense domain by exploiting a dangling CNAME record to a deleted AWS Elastic Load Balancer (ELB) endpoint. This allows an attacker to claim control over the subdomain, host malicious content, receive emails, execute XSS, steal cookies, and trick password managers into autofilling credentials, potentially leading to phishing or credential theft under a trusted DoD subdomain.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Discover Dangling CNAME] --> B[Initial Access: Verify and Takeover Subdomain]
    B --> C[Impact: Host Malicious Content and Exploit]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- DNS enumeration tools (e.g., dig, nslookup)
- Web browser or curl for verification

### Target Environment

- Target: DoD domain with misconfigured DNS
- Required services/ports: DNS (port 53), HTTP/HTTPS (ports 80/443)
- Network access requirements: Public internet access to query DNS and access the subdomain

### Initial Access Requirements

- No credentials required
- Public network position
- No prior access needed; relies on public DNS misconfiguration

## Detailed Attack Procedures

### Step 1: Discover Dangling CNAME Record
procedure: [[procedures/Discover-Dangling-CNAME-Record]]

**Objective**: Enumerate subdomains and identify dangling DNS records pointing to unclaimed cloud resources, such as a non-existent AWS ELB.

**Instructions**: Start by enumerating subdomains of the target domain using DNS tools. Then, query the CNAME record for suspicious subdomains to check if they point to deleted AWS resources.

Use [[commands/dig-cname-lookup]] to query the CNAME for the target subdomain:

```bash
dig CNAME █████.defense.gov
```

Follow up by checking if the pointed-to ELB endpoint exists by attempting to resolve it:

```bash
dig open-elb-prod-277276106.us-east-1.elb-amazonaws.com
```

**Expected Output**: The first command returns a CNAME to 'open-elb-prod-277276106.us-east-1.elb.amazon.com', and the second shows NXDOMAIN or no response, indicating the resource is deleted.

**Success Indicators**:
- CNAME record points to a non-existent AWS ELB
- Subdomain resolves but leads to no active service

### Step 2: Verify Subdomain Takeover with POC
procedure: [[procedures/Verify-Subdomain-Takeover-with-POC]]

**Objective**: Confirm control over the subdomain by claiming the dangling resource and hosting a proof-of-concept file to demonstrate takeover.

**Instructions**: Since the CNAME points to an unclaimed AWS ELB endpoint, provision a new resource (e.g., an S3 bucket or similar service if applicable) that matches the dangling name. Then, access the subdomain to host and retrieve a POC file.

Use [[commands/curl-access-poc]] to verify control by accessing a hosted POC file on the taken-over subdomain:

```bash
curl http://█████.defense.gov/proof.e7437329-ab61-4f22-a049-df5b3685313a.txt
```

If the takeover is successful, upload a simple text file via the claimed AWS resource and confirm retrieval.

**Expected Output**: The curl command returns the content of the POC file, confirming the attacker controls the subdomain's web presence.

**Success Indicators**:
- POC file is accessible via the DoD subdomain
- Subdomain now serves attacker-controlled content

## Attack Chain Summary

### Key Achievements

1. Identified a dangling CNAME to a deleted AWS ELB, exposing the DoD subdomain to takeover.
2. Verified control by hosting and accessing a POC file under the trusted domain.
3. Enabled potential impacts like phishing, XSS, cookie theft, and credential autofill attacks.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Hardware]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]
- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
