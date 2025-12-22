---
id: proc-uuid-002
name: Validate Dangling DNS for Takeover
tags:
  - validation
  - takeover-check
  - dns
type: procedure
tools:
  - '[[tools/subjack]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/subjack-validate]]'
  - '[[commands/dig-ns-query]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:51:10.562Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Validate Dangling DNS for Takeover

## Summary

This procedure scans enumerated subdomains for known takeover vulnerabilities by checking if DNS records point to claimable cloud services, confirming exploitability before claiming.

## Description

Following enumeration, validation involves fingerprinting DNS responses against databases of vulnerable service patterns (e.g., AWS error pages for unclaimed buckets). Tools like Subjack automate this by sending probes and parsing responses. In the Adobe Marketo case, this revealed dangling records on marketo.net subdomains. Prerequisites: Subdomain list from prior step; outcomes: Confirmed vulnerable subdomains ready for exploitation.

## Requirements

1. Subdomain list file
2. Installed validation tools
3. Public DNS access

## Defense

Defensive measures and detection strategies:

- Automate DNS cleanup on service deprovisioning
- Monitor for takeover attempts via cloud provider logs
- Use services like SecurityTrails for historical DNS tracking

## Objectives

1. Identify claimable dangling records
2. Confirm service unavailability
3. Generate takeover report

## Instructions

### Step 1: Scan for Takeover Fingerprints

**Context**: Use a specialized tool to check against known vulnerable patterns.

**Command** ([[commands/subjack-validate]]):
```bash
subjack -w subdomains.txt -t 100 -o takeovers.json -ssl
```

> This scans with 100 threads, outputs JSON report. Expected output: Entries like {"subdomain": "test.marketo.net", "service": "aws-s3", "status": "vulnerable"}.

### Step 2: Manual DNS Verification

**Context**: Double-check suspicious records with direct queries.

**Command** ([[commands/dig-ns-query]]):
```bash
dig example-subdomain.marketo.net CNAME
```

> Queries specific CNAME. Expected output: Points to non-existent service, e.g., NXDOMAIN or error.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/subjack-validate]]
- [[commands/dig-ns-query]]

## Tools Used

- [[tools/subjack]]

## Tags

- [[validation]]
- [[takeover-check]]
