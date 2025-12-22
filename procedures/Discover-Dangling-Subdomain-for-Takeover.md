---
tags:
  - subdomain-takeover
  - dns-recon
  - aws-s3
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/dig-check-dns]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:38:39.737Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 0bd3a919-abce-48bf-88dc-a8f93f6f624d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Discover Dangling Subdomain for Takeover

## Summary

This procedure identifies subdomains with dangling DNS records that point to unclaimed cloud resources, such as AWS S3 buckets, enabling potential subdomain takeover attacks.

## Description

In a subdomain takeover attack, attackers scan for DNS records (CNAME or alias) that resolve to cloud services like AWS S3 but no longer point to active resources owned by the target. By querying DNS and checking HTTP responses, the attacker confirms the resource is unclaimed. This is common in development or admin subdomains like 'dev-admin' where buckets may be deleted without updating DNS. Prerequisites include public DNS access and basic networking knowledge; no target credentials are needed.

## Requirements

1. Internet access for DNS queries
2. DNS resolution tool like dig installed
3. Knowledge of target domain and potential subdomains (e.g., from prior recon)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling entries using tools like dnsdumpster or custom scripts
- Implement DNS monitoring alerts for changes or unresolved records
- Use subdomain management tools to automate cleanup of unused records

## Objectives

1. Identify misconfigured DNS records pointing to cloud endpoints
2. Verify the endpoint is unclaimed and exploitable
3. Prepare for bucket claiming to achieve subdomain control

## Instructions

### Step 1: Query DNS Resolution

**Context**: Perform a DNS lookup on the suspected subdomain to check if it resolves to a cloud service endpoint.

**Command** ([[commands/dig-check-dns]]):
```bash
dig dev-admin.periscope.tv
```

> This command queries the DNS for the subdomain and displays the CNAME or A record. Look for resolutions to patterns like *.s3-website-*.amazonaws.com, indicating an S3 bucket endpoint.

### Step 2: Verify Endpoint Availability

**Context**: Access the resolved URL via HTTP to confirm no active content is served, indicating an unclaimed resource.

**Command** ([[commands/curl-check-endpoint]]):
```bash
curl -I http://dev-admin.periscope.tv.s3-website-us-west-2.amazonaws.com
```

> Expect a 403 Forbidden or XML error response from AWS, confirming the bucket is not configured or claimed. If it serves custom content, it's not dangling.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/dig-check-dns]]
- [[commands/curl-check-endpoint]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- [[subdomain-takeover]]
- [[dns-recon]]
