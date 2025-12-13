---
tags:
  - certificate-analysis
  - exfiltration
type: procedure
tools:
  - '[[tools/openssl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/openssl-x509]]'
platforms:
  - Linux
techniques:
  - '[[Data from Cloud Storage]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1d62ca0c-6b2a-4b46-9e36-025b7dad5f0e
created_at: '2025-12-13T09:00:27.287Z'
updated_at: '2025-12-13T09:00:27.287Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Cloud Storage]]'
---
# Analyze Leaked Certificates

## Summary

This procedure uses openssl to parse and extract details from leaked certificate files obtained via XXE exfiltration.

## Description

After exfiltrating files like node.crt and node.key, openssl is used to display certificate information in text form, revealing issuer, validity, subject, and extensions, which could enable further attacks like MITM.

## Requirements

1. Leaked certificate files
2. OpenSSL installed
3. Basic command-line knowledge

## Defense

Defensive measures and detection strategies:

- Secure sensitive files with proper permissions
- Encrypt at-rest data

## Objectives

1. Extract certificate metadata
2. Identify exploitation opportunities
3. Assess security impact

## Instructions

### Step 1: Parse Certificate

**Context**: Analyze the leaked node.crt file.

**Command** ([[commands/openssl-x509]]):
```bash
openssl x509 -in node.crt -text -noout
```

> Outputs certificate details in text format.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Cloud Storage]]

### Sub-Techniques



## Commands Used

- [[commands/openssl-x509]]

## Tools Used

- [[tools/openssl]]

## Tags

- [[certificate-analysis]]
- [[Exfiltration]]
