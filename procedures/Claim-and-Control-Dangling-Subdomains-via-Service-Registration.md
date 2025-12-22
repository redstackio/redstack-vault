---
id: proc-uuid-002
tags:
  - subdomain-takeover
  - service-claim
  - dns-hijack
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/dig-dns-query]]'
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:24.188Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim and Control Dangling Subdomains via Service Registration

## Summary

This procedure demonstrates registering a claimable third-party service (e.g., AWS S3 bucket) that a dangling DNS record points to, thereby taking control of the subdomain and redirecting traffic to attacker-controlled content.

## Description

Once a dangling DNS record is identified (e.g., a *.ttcdn.co subdomain CNAME'd to an unregistered S3 bucket), the attacker creates an account with the service provider if needed and registers the exact resource name. This hijacks the subdomain's resolution without altering the target's DNS. In the Shopify case, this could allow impersonation of CDN services. Prerequisites: Identified dangling record and access to the provider's portal. Expected outcomes: Full control over the subdomain for hosting malware, phishing, or data exfiltration.

## Requirements

1. Account with the service provider (e.g., AWS for S3).
2. Exact name of the dangling resource from DNS query.
3. Web browser for registration portal.

## Defense

Defensive measures and detection strategies:

- Use short TTLs on DNS records and automate cleanup on service decommissioning.
- Monitor service provider logs for suspicious registrations matching domain patterns.
- Implement subdomain validation in applications to detect hijacks.

## Objectives

1. Register the dangling service to assume control of the subdomain.
2. Verify and demonstrate control by hosting test content.
3. Prepare for malicious use, such as phishing or redirection.

## Instructions

### Step 1: Register the Dangling Service

**Context**: Use the service provider's interface to create the resource matching the dangling CNAME.

No command; manually log into the provider (e.g., AWS Console > S3 > Create Bucket named 'dangling-bucket').

### Step 2: Configure Service for Control

**Context**: Upload content or configure the service to serve attacker pages, ensuring the subdomain resolves correctly.

For S3, enable static website hosting and upload an index.html with verification text.

### Step 3: Verify Takeover

**Context**: Confirm the subdomain now points to and loads the controlled content.

**Command** ([[commands/dig-dns-query]]):
```bash
dig +short example.ttcdn.co
```

> Query the subdomain post-registration. Expected output: Resolves to the new service IP or endpoint. Then, browse to http://example.ttcdn.co to see uploaded content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-query]]

## Tools Used


## Tags

- [[subdomain-takeover]]
- [[service-claim]]
