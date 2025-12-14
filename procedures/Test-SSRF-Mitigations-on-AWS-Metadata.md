---
tags:
  - ssrf
  - aws
  - mitigation-test
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
updated_at: '2025-12-14T04:39:09.901Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 6cb7b910-1656-431e-abda-650c65257eda
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test SSRF Mitigations on AWS Metadata

## Summary

Test direct SSRF attempts targeting AWS Instance Metadata Service to identify and understand IP-based mitigations in Concrete CMS backend.

## Description

The AWS Instance Metadata Service is accessible at 169.254.169.254 on EC2 instances. Concrete CMS implements mitigations in backend/file.php (lines 794-804) that verify resolved IP addresses against a blocklist, preventing direct access to internal endpoints. This procedure tests these blocks to confirm the need for bypass techniques like DNS rebinding.

## Requirements

1. Concrete CMS on AWS EC2
2. Access to upload interface
3. Awareness of internal IP ranges

## Defense

Defensive measures and detection strategies:

- Strengthen IP validation to include DNS rebinding checks
- Use request signing or outbound proxy for fetches
- Monitor for repeated failed internal access attempts

## Objectives

1. Confirm SSRF vector exists but is mitigated
2. Document mitigation logic for bypass planning
3. Validate target environment is AWS-hosted

## Instructions

### Step 1: Attempt Direct Metadata Fetch

**Context**: Use upload to target metadata endpoint.

Submit `http://169.254.169.254/latest/meta-data/` as remote URL.

> Expected: Error or block due to IP verification.

### Step 2: Review Backend Code

**Context**: If accessible, inspect backend/file.php lines 794-804.

Look for IP resolution and blocklist checks.

> Expected: Code snippet showing `gethostbyname` and IP comparison.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[aws]]
