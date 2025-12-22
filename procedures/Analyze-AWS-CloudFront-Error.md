---
id: proc-uuid-002
tags:
  - subdomain-takeover
  - aws
  - cloudfront
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - AWS
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:38:39.998Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Analyze AWS CloudFront Error

## Summary

This procedure analyzes error messages from accessing a subdomain to recognize patterns indicative of a dangling CNAME to an unclaimed AWS CloudFront distribution, enabling subdomain takeover identification.

## Description

AWS CloudFront errors for non-existent distributions are a hallmark of subdomain takeover vulnerabilities. By referencing known documentation, such as blog posts detailing AWS CNAME dangling issues, the attacker confirms the root cause: a DNS record pointing to a CloudFront endpoint without an associated active distribution. This step bridges reconnaissance to exploitation in cloud-based attacks.

## Requirements

1. Captured error response from subdomain access
2. Access to external resources like https://labs.detectify.com/2016/10/05/the-story-of-ev-ssl-aws-and-trailing-dot-domains/
3. DNS lookup capability (e.g., dig command)

## Defense

Defensive measures and detection strategies:

- Scan for dangling records using automated tools like Subjack or Takeover
- Monitor CloudFront access logs for anomalous errors on subdomains
- Enforce DNS TTL reductions and regular audits post-reconfiguration

## Objectives

1. Validate the error as a takeover vector
2. Understand the technical root cause
3. Prepare for exploitation by noting the CNAME target

## Instructions

### Step 1: Review Error Message

**Context**: Examine the error for AWS-specific indicators.

No command; manually inspect the response body for phrases like "CloudFront couldn't find a distribution".

> Correlate with known behaviors: The error confirms the CNAME exists but no distribution claims it.

### Step 2: Verify DNS Record

**Context**: Confirm the CNAME points to CloudFront.

Use a DNS tool like dig:

```bash
dig CNAME rider.uber.com
```

> Expected output: A record like "rider.uber.com. CNAME d123456789.cloudfront.net.", indicating the dangling pointer.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[aws]]
- [[cloudfront]]
