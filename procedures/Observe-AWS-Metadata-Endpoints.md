---
tags:
  - ssrf
  - aws
  - enumeration
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-observe-metadata]]'
platforms:
  - Web
  - AWS
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: f26c2abd-83d2-4ef1-9b08-c8650637be3c
created_at: '2025-12-14T03:46:09.166Z'
updated_at: '2025-12-14T03:46:09.166Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe-AWS-Metadata-Endpoints

## Summary

This procedure involves analyzing the response from an SSRF-triggered metadata fetch to identify and observe available AWS EC2 instance metadata endpoints, providing reconnaissance on the target's cloud environment.

## Description

Following an initial SSRF request, the server's response exposes a directory of metadata paths. This procedure details how to interpret this output, which includes instance identifiers, security groups, and other configurations. In the context of the DoD bug bounty report, this step revealed endpoints like 'ami-id' and 'instance-id', aiding in mapping the internal AWS setup for subsequent exploitation.

## Requirements

1. Successful output from prior SSRF trigger
2. Basic understanding of AWS metadata structure
3. HTTP client for follow-up requests if needed

## Defense

Defensive measures and detection strategies:

- Use AWS IAM policies to restrict metadata access
- Enable VPC flow logs to detect anomalous internal traffic patterns
- Implement WAF rules to flag SSRF attempts based on URL patterns

## Objectives

1. Parse and list exposed metadata endpoints
2. Identify sensitive paths for further targeting
3. Gather instance details without alerting defenses

## Instructions

### Step 1: Review and Probe Metadata Response

**Context**: Examine the SSRF response to catalog endpoints, then re-request if necessary to confirm details.

**Command** ([[commands/curl-observe-metadata]]):
```bash
curl "https://█████/api/v1/download-url?url=http://169.254.169.254/latest/meta-data/"
```

> The command re-fetches the metadata. Expected output includes a newline-separated list of keys (e.g., ami-id, instance-id). Use this to note paths leading to credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-observe-metadata]]

## Tools Used


## Tags

- [[ssrf]]
- [[aws]]
- [[enumeration]]
