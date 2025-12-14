---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: Verify-Dangling-DNS-Record
tags:
  - dns-verification
  - dangling-record
  - cname
type: procedure
tools:
  - '[[tools/Dig]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-cname-query]]'
  - '[[commands/curl-heroku-check]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Scanning IP Blocks]]'
updated_at: '2025-12-14T17:30:18.254Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Scanning IP Blocks]]'
---
# Verify-Dangling-DNS-Record

## Summary

This procedure queries DNS to confirm if a subdomain has a dangling CNAME record pointing to an unclaimed cloud resource, such as a deleted Heroku application, enabling takeover potential.

## Description

Dangling records occur when a service is deleted but DNS isn't updated. In the Uber case, 'dangling.uber.com' pointed to 'deleted-app.herokuapp.com'. This step uses DNS tools to verify resolvability and service status, requiring only public DNS access.

## Requirements

1. Identified subdomain from enumeration
2. DNS resolver access (e.g., dig installed)
3. Optional: curl for HTTP probing

## Defense

Defensive measures and detection strategies:

- Automate DNS audits with scripts checking CNAME targets
- Monitor for unresolved cloud endpoints using SIEM rules
- Enforce TTL reductions on dynamic DNS records

## Objectives

1. Resolve the subdomain's CNAME target
2. Confirm the target service is deleted or claimable
3. Validate takeover feasibility

## Instructions

### Step 1: Query DNS CNAME

**Context**: Use dig to fetch the CNAME record for the subdomain.

**Command** ([[commands/dig-cname-query]]):
```bash
dig example.uber.com CNAME
```

> Returns the CNAME if present, e.g., 'example.uber.com. 3600 IN CNAME dangling-app.herokuapp.com.'. Expected: Confirmation of cloud pointer.

### Step 2: Probe Service Availability

**Context**: Check if the CNAME target responds, indicating deletion.

**Command** ([[commands/curl-heroku-check]]):
```bash
curl -I https://dangling-app.herokuapp.com
```

> If deleted, expect 404 or Heroku's 'no such app' page. Expected: Error response confirming availability for claim.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Scanning IP Blocks]] Scanning IP Blocks

### Sub-Techniques


## Commands Used

- [[commands/dig-cname-query]]
- [[commands/curl-heroku-check]]

## Tools Used

- [[tools/Dig]]

## Tags

- [[dns-verification]]
- [[dangling-record]]
