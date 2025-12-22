---
id: proc-uuid-detect-1181762
name: Detect-Dangling-DNS-Record-for-Subdomain-Takeover
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:26.832Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Gather Victim Host Information]]'
sub_techniques: []
tags:
  - subdomain-takeover
  - dns
  - recon
commands:
  - '[[commands/dig-resolve-dns]]'
platforms:
  - AWS
  - Cloud
tools:
  - '[[tools/dig]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---

# Detect-Dangling-DNS-Record-for-Subdomain-Takeover

## Summary

This procedure identifies subdomain takeover opportunities by detecting DNS records that point to terminated or non-existent cloud resources, such as an AWS EC2 instance, enabling attackers to claim the subdomain for malicious purposes.

## Description

In this scenario, a subdomain like ███.wavecell.com has a DNS record (e.g., CNAME or A record) still pointing to a terminated AWS EC2 instance. During reconnaissance, query the DNS to reveal the dangling record. If the resource is claimable (e.g., via AWS services), an attacker can register it to redirect traffic. This leads to phishing, brand impersonation, or content injection risks. Prerequisites include public DNS access and basic knowledge of cloud services.

## Requirements

1. Internet access for DNS queries
2. Target subdomain name (e.g., ███.wavecell.com)
3. Optional: AWS account to verify resource status

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for terminated resources using AWS Config or DNS monitoring tools
- Implement automated cleanup scripts for DNS on instance termination
- Monitor for anomalous traffic to subdomains and use certificate transparency logs to detect takeovers

## Objectives

1. Discover dangling DNS records pointing to inactive resources
2. Assess takeover feasibility for the subdomain
3. Identify potential impact on brand and user trust

## Instructions

### Step 1: Query DNS Resolution

**Context**: Resolve the subdomain's DNS record to check for dangling pointers.

**Command** ([[commands/dig-resolve-dns]]):
```bash
dig ███.wavecell.com
```

> This command queries the DNS for the subdomain, outputting the resolved IP or CNAME. Look for an IP associated with AWS EC2 (e.g., in the AWS range) but unresponsive to pings or HTTP requests, indicating termination.

### Step 2: Verify Resource Status

**Context**: Confirm the pointed resource is terminated and claimable.

**Command** ([[commands/dig-resolve-dns]]):
```bash
dig +short ███.wavecell.com | xargs -I {} nslookup {} 2>/dev/null || echo "Unresponsive"
```

> Pipe the resolved IP to nslookup or curl to test responsiveness. No response confirms dangling status. Cross-reference with AWS EC2 console if possible.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/dig-resolve-dns]]

## Tools Used

- [[tools/dig]]

## Tags

- [[subdomain-takeover]]
- [[DNS]]
- [[recon]]
