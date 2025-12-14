---
id: proc-trigger-webhook-verify-ssrf
tags:
  - ssrf
  - verification
  - logs
type: procedure
tools: []
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
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T17:28:36.476Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Application Access Token]]'
---
# Trigger-Webhook-and-Verify-SSRF

## Summary

This procedure involves editing the configured webhook in HackerOne and sending a test request to activate the SSRF, then checking the logs to confirm access to the AWS metadata service via the `server: EC2ws` header.

## Description

Once the webhook is set, triggering a test request causes HackerOne's backend to fetch the PHP URL, which redirects to the internal AWS endpoint. This exposes metadata if successful. The attack targets AWS EC2 environments. Verification occurs in the webhook delivery logs.

## Requirements

1. Configured webhook from previous procedure
2. Access to HackerOne logs
3. Organizational permissions to view webhook activity

## Defense

Defensive measures and detection strategies:

- Disable or monitor test request features in webhook configs
- Scan logs for internal service responses like `EC2ws`
- Implement request tracing to detect chained redirects

## Objectives

1. Execute the SSRF payload to reach internal AWS metadata
2. Capture evidence of successful bypass in logs
3. Validate the vulnerability for further exploitation

## Instructions

### Step 1: Edit and Test Webhook

**Context**: Initiate the request from the webhook interface.

**Instructions**: In HackerOne settings, edit the webhook if needed, then click 'Test request' or 'Send test' to trigger a delivery.

> Expected: Request sent; no immediate errors.

### Step 2: Review Logs

**Context**: Check for SSRF indicators in the response.

**Instructions**: Navigate to the webhook's activity or delivery logs and inspect the response headers.

> Expected: Logs display `server: EC2ws`, confirming AWS metadata access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Steal Application Access Token]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- aws
- metadata
