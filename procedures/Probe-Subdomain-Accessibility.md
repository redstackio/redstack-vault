---
tags:
  - subdomain-takeover
  - http-probe
  - aws
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-probe-http]]'
verified: false
platforms:
  - AWS
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T05:32:23.952Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: f900efec-5f97-47ec-883e-323df7b71468
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Probe-Subdomain-Accessibility

## Summary

This procedure tests the current accessibility of a target subdomain by sending HTTP requests and analyzing responses for status codes, headers, and content that indicate control by an unauthorized entity, such as an AWS ELB.

## Description

Following monitoring, direct probing confirms if a subdomain has become responsive due to DNS misconfiguration. In this case, querying mk.prd.vine.co revealed an open port 443 with an upgrade-required response and AWS server header, suggesting the underlying IP was reassigned from a decommissioned EC2 to another user's load balancer. This step validates the takeover potential without exploitation.

## Requirements

1. Public access to the target subdomain
2. HTTP client for requests
3. Ability to inspect response headers and body

## Defense

Defensive measures and detection strategies:

- Enforce strict DNS TTL and cleanup policies for decommissioned resources
- Monitor for unexpected HTTP responses on internal subdomains
- Use web application firewalls to block anomalous traffic

## Objectives

1. Confirm subdomain resolution and HTTP responsiveness
2. Identify foreign server signatures in headers
3. Assess immediate takeover viability

## Instructions

### Step 1: Basic HTTP Access

**Context**: Send a simple GET request to check port and basic response.

**Command** ([[commands/curl-probe-http]]):
```bash
curl -i http://mk.prd.vine.co/
```

> Expected output: HTTP/1.1 426 Upgrade Required, Server: awselb/2.0, indicating port open and AWS control.

### Step 2: HTTPS Attempt

**Context**: Test secure port if HTTP redirects or for completeness.

**Command** ([[commands/curl-probe-http]]):
```bash
curl -i -k https://mk.prd.vine.co/
```

> Use -k to ignore cert errors; expect similar upgrade response or TLS details.

### Step 3: Header Inspection

**Context**: Extract and review specific headers for anomalies.

**Command** ([[commands/curl-probe-http]]):
```bash
curl -I http://mk.prd.vine.co/ | grep -i server
```

> Expected output: Server: awselb/2.0, confirming non-original backend.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Active Scanning: Vulnerability Scanning

### Sub-Techniques


## Commands Used

- [[commands/curl-probe-http]]

## Tools Used


## Tags

- [[subdomain-takeover]]
- [[http-probe]]
- [[recon]]
