---
tags:
  - subdomain-takeover
  - aws-elb
  - vulnerability-scan
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-probe-http]]'
verified: false
platforms:
  - AWS
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:23.938Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 8694dcfe-3eb9-4bd6-870d-ecb054e7df5b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Confirm-AWS-ELB-Takeover

## Summary

This procedure confirms control of a subdomain by an AWS Elastic Load Balancer by triggering error conditions that reveal backend-specific pages, validating the takeover from a dangling DNS record.

## Description

To solidly prove takeover, send malformed requests that elicit ELB error pages. For mk.prd.vine.co, appending %00 (null byte) resulted in a 400 Bad Request with AWS ELB error content, confirming the IP's reassignment from Twitter's decommissioned EC2 to another user's ELB. This step escalates from probing to verification of exploitation potential, like serving phishing content.

## Requirements

1. Confirmed accessible subdomain from prior steps
2. HTTP client supporting path manipulation
3. Knowledge of AWS ELB error signatures

## Defense

Defensive measures and detection strategies:

- Automate DNS sweeps to remove stale records post-decommissioning
- Integrate ELB access logs with SIEM for anomalous subdomain traffic
- Employ subdomain validation in certificate issuance processes

## Objectives

1. Trigger ELB-specific error responses
2. Verify third-party control via error page content
3. Quantify takeover impact on domain reputation

## Instructions

### Step 1: Malformed Path Request

**Context**: Use invalid URL encoding to force a bad request on the ELB.

**Command** ([[commands/curl-probe-http]]):
```bash
curl -i http://mk.prd.vine.co/%00
```

> Expected output: HTTP/1.1 400 Bad Request, Server: awselb/2.0, with AWS ELB error HTML.

### Step 2: Inspect Error Body

**Context**: Download and review the full error page for AWS indicators.

**Command** ([[commands/curl-probe-http]]):
```bash
curl http://mk.prd.vine.co/%00 > error.html
cat error.html | grep -i aws
```

> Expected output: References to AWS or ELB in the body, confirming takeover.

### Step 3: Validate Non-Original Response

**Context**: Compare against expected Twitter/Vine responses.

**Command** ([[commands/curl-probe-http]]):
```bash
curl -i http://mk.prd.vine.co/ | head -20
```

> Look for absence of original branding and presence of generic AWS errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-probe-http]]

## Tools Used


## Tags

- [[subdomain-takeover]]
- [[aws-elb]]
- [[scan]]
