---
id: ac-uuid-1181762
tags:
  - subdomain-takeover
  - dns
  - aws
  - ec2
type: attack_chain
tools:
  - '[[tools/dig]]'
tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - AWS
  - Cloud
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Detect-Dangling-DNS-Record-for-Subdomain-Takeover]]'
  - '[[procedures/Claim-Subdomain-via-DNS-Takeover]]'
step_count: 2
techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:31.477Z'
description: >-
  Attack chain exploiting a subdomain takeover vulnerability where a DNS record
  points to a terminated AWS EC2 instance, allowing an attacker to claim the
  subdomain and host malicious content.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Exploit Public-Facing Application]]'
---
---
id: ac-uuid-1181762
name: Subdomain Takeover via Dangling DNS Record on Terminated AWS EC2 Instance
type: attack_chain
description: Attack chain exploiting a subdomain takeover vulnerability where a DNS record points to a terminated AWS EC2 instance, allowing an attacker to claim the subdomain and host malicious content.
verified: false
submitted: false
step_count: 2
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
procedures: [[procedures/Detect-Dangling-DNS-Record-for-Subdomain-Takeover]], [[procedures/Claim-Subdomain-via-DNS-Takeover]]
techniques: [[Gather Victim Host Information]], [[Exploit Public-Facing Application]]
tactics: [[Reconnaissance]], [[Initial Access]]
tags: subdomain-takeover, dns, aws, ec2
platforms: AWS, Cloud
tools: [[tools/dig]]
complexity: medium
skill_level: intermediate
impact_level: high
---

# Subdomain Takeover via Dangling DNS Record on Terminated AWS EC2 Instance

Multi-stage attack chain demonstrating a complete attack workflow for subdomain takeover on a dangling AWS EC2 DNS record.

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
    A[Reconnaissance: Detect Dangling DNS] --> B[Initial Access: Claim Subdomain]
    B --> C[Objective: Host Malicious Content]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/dig]]

### Target Environment

- AWS Cloud platform
- DNS services (e.g., Route 53 or external DNS providers)
- Access to public DNS resolution

### Initial Access Requirements

- No credentials required for reconnaissance
- Internet access for DNS queries
- Optional: AWS account for claiming the resource if it's an S3 bucket or similar, but here it's EC2-related

## Detailed Attack Procedures

### Step 1: Reconnaissance - Detect Dangling DNS Record
procedure: [[procedures/Detect-Dangling-DNS-Record-for-Subdomain-Takeover]]

**Objective**: Identify subdomains with DNS records pointing to non-existent or terminated resources, such as an AWS EC2 instance.

**Instructions**: Use [[commands/dig-resolve-dns]] to query the DNS record for the target subdomain and check if it resolves to a terminated resource.

```bash
dig ███.wavecell.com
```

Verify the resolved IP against AWS EC2 status (e.g., via AWS console or public APIs if accessible). Look for responses indicating a non-responsive host or known terminated instance.

**Expected Output**: DNS resolution showing an IP address associated with a terminated EC2 instance, with no active service responding.

**Success Indicators**:
- DNS record exists but points to unreachable IP
- No HTTP/HTTPS response from the resolved IP
- Confirmation via AWS that the instance is terminated

### Step 2: Initial Access - Claim the Subdomain
procedure: [[procedures/Claim-Subdomain-via-DNS-Takeover]]

**Objective**: Register the dangling resource (e.g., if it's an S3 bucket or aliasable service) to take control of the subdomain and host malicious content.

**Instructions**: If the DNS record points to a claimable AWS service like an S3 bucket, create a new bucket with the exact name. Then, update your own DNS to point to it, or wait for propagation. For EC2, if it's an Elastic IP, request it if available.

Use [[commands/dig-verify-takeover]] post-claim to confirm control:

```bash
dig ███.wavecell.com
```

Upload a test page to the claimed resource and access via the subdomain.

**Expected Output**: Subdomain resolves to your controlled resource, serving your content.

**Success Indicators**:
- Subdomain serves attacker-controlled content
- Potential for phishing or impersonation confirmed
- Brand compromise risks materialized

## Attack Chain Summary

### Key Achievements

1. Identified dangling DNS record pointing to terminated EC2
2. Demonstrated potential for subdomain hijacking
3. Enabled risks like phishing and service impersonation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
