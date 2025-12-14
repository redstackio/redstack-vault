---
id: proc-verify-forwarding
tags:
  - ssrf
  - verification
  - aws
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:46.889Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify Request Forwarding to Controlled Domain

## Summary

This procedure monitors an attacker-controlled server to confirm that SSRF requests are forwarded from Slack's AWS backend, distinguishing internal processing from frontend CDN behavior.

## Description

After the bypass, logs on the controlled domain should show incoming requests from amazonaws.com IPs, not CloudFront edge locations. This verifies true SSRF, as the backend server (e.g., on AWS EC2/S3) handles the forwarding. Requires server access for logging and aligns with exploiting CloudFront/S3 services in the environment.

## Requirements

1. Controlled domain with logging enabled (e.g., access logs)
2. Execution of prior bypass step
3. Ability to inspect IP origins

## Defense

Defensive measures and detection strategies:

- Block outbound requests to untrusted domains from backends
- Log all internal forwarding and alert on anomalous destinations
- Use VPC endpoints to restrict backend network access

## Objectives

1. Confirm SSRF reaches backend
2. Identify origin as AWS internal
3. Validate exploitation chain

## Instructions

### Step 1: Monitor Server Logs

**Context**: Watch for incoming requests during bypass execution.

No command required; check server logs:

- Tail access logs on your domain's web server (e.g., Apache/Nginx)
- Execute the bypass request from Burp

> Expected output: Log entry with request from amazonaws.com IP.

### Step 2: Analyze Origin IP

**Context**: Differentiate backend from frontend.

No command required; inspect logs:

- Verify IP is not a CloudFront edge (e.g., via AWS IP ranges)

> Expected output: Origin matches AWS backend patterns, confirming internal forwarding.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

-

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[ssrf]]
- [[verification]]
- [[aws]]
