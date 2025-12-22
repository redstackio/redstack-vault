---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - validation
  - hijacking
  - dns
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/dig]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-subdomain-test]]'
  - '[[commands/dig-cname-lookup]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:10.868Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Validate Subdomain Hijacking

## Summary

This procedure confirms successful subdomain takeover by re-querying DNS and fetching content from the hijacked domain to ensure attacker control.

## Description

After claiming an S3 bucket, validation involves checking if the subdomain now resolves to the attacker's bucket and serves custom content. In the TikTok report, this would show control over musical.ly without user data exposure, allowing phishing setups. It's a post-exploitation check to measure impact.

## Requirements

1. Hijacked subdomain URL (e.g., musical.ly.example.com)
2. Access to curl or browser for HTTP requests
3. DNS tools for resolution checks

## Defense

Defensive measures and detection strategies:

- Implement certificate transparency monitoring for subdomains
- Use web application firewalls to detect anomalous content on subdomains
- Alert on DNS changes via services like Route 53 monitoring

## Objectives

1. Verify DNS propagation to new bucket
2. Confirm HTTP responses from attacker content
3. Assess potential for further abuse like redirects

## Instructions

### Step 1: Re-Query DNS Record

**Context**: Ensure the CNAME still points to the now-claimed S3 bucket.

**Command** ([[commands/dig-cname-lookup]]):
```bash
dig +short CNAME musical.ly.example.com
```

> Expected output: Confirms 'legacy-bucket.s3.amazonaws.com' resolution.

### Step 2: Fetch Subdomain Content

**Context**: Request the subdomain to see if it serves the uploaded hijack page.

**Command** ([[commands/curl-subdomain-test]]):
```bash
curl -s https://musical.ly.example.com | grep -i hijacked
```

> This fetches and greps for custom content. Expected output: Matches '<h1>Subdomain Hijacked</h1>' if successful.

### Step 3: Check HTTPS and Headers

**Context**: Validate full control including SSL and response codes.

**Command** ([[commands/curl-subdomain-test]]):
```bash
curl -I https://musical.ly.example.com
```

> Expected output: HTTP/1.1 200 OK with S3 headers like x-amz-id-2.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/dig-cname-lookup]]
- [[commands/curl-subdomain-test]]

## Tools Used

- [[tools/dig]]
- [[tools/curl]]

## Tags

- [[validation]]
- [[subdomain]]
- [[hijacking]]
