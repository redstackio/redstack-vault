---
tags:
  - reconnaissance
  - dangling-dns
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-check-http-status]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:39:09.407Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 4a20d512-6c5c-445e-9f63-5d02f63be046
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Identify and Verify Dangling Subdomains

## Summary

This procedure involves checking HTTP responses of enumerated subdomains for 404 errors and verifying if they indicate unclaimed hosting services, such as Squarespace, to pinpoint takeover opportunities.

## Description

After enumeration, probe subdomains to find those returning 404s, which may signal deprovisioned hosts. For www.codefi.consensys.net, the 404 page reveals a Squarespace mapping without a claimed site, allowing takeover. This step filters for exploitable dangling records.

## Requirements

1. List of subdomains from prior enumeration
2. curl or similar HTTP client
3. Browser for manual verification

## Defense

Defensive measures and detection strategies:

- Automate HTTP probing of subdomains to detect 404s early
- Update or remove CNAME records for deprovisioned services promptly
- Use services like dnsdumpster or security scanners for ongoing audits

## Objectives

1. Filter subdomains with non-standard 404 responses
2. Confirm unclaimed status of third-party hosting
3. Prepare for takeover exploitation

## Instructions

### Step 1: Check HTTP Status Codes

**Context**: Send requests to each subdomain to capture status codes.

**Command** ([[commands/curl-check-http-status]]):
```bash
while read subdomain; do curl -s -o /dev/null -w "%{http_code} %{url_effective}\n" http://$subdomain/; done < subdomains.txt > status_codes.txt
```

> Outputs status codes like "404 http://www.codefi.consensys.net/". Filter for 404s.

### Step 2: Verify Unclaimed Service

**Context**: Access suspect subdomains in a browser to inspect error pages.

No command; navigate to http://www.codefi.consensys.net/ and look for Squarespace message.

> Confirm: "Domain Not Claimed. This domain has been mapped to Squarespace, but it has not yet been claimed by a website. If this is your domain, claim it in the Domains tab of your Website Manager."

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used

- [[commands/curl-check-http-status]]

## Tools Used


## Tags

- [[Reconnaissance]]
- [[dangling-dns]]
- [[subdomain-takeover]]
