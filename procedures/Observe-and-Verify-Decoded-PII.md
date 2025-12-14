---
id: proc-uuid-3
tags:
  - pii-verification
  - analysis
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:18.003Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Observe-and-Verify-Decoded-PII

## Summary

This procedure involves inspecting the output from decoded Base64 tokens to confirm the presence and validity of exposed PII, such as email addresses, in the context of information disclosure vulnerabilities.

## Description

After decoding, manual review ensures the extracted data is actionable PII. This targets scenarios like Omise's tokens where emails are plainly visible in binary output. The environment is post-decoding analysis on any system. Outcomes include validated emails for impact demonstration, such as potential phishing vectors.

## Requirements

1. Decoded output from previous procedure
2. Text editor or console for inspection
3. Knowledge of email formats

## Defense

Defensive measures and detection strategies:

- Obfuscate PII in tokens or avoid embedding altogether
- Implement data loss prevention (DLP) scans on logs and archives
- Regular PII audits in application data flows

## Objectives

1. Confirm PII extraction success
2. Identify specific exposed information
3. Document for vulnerability reporting

## Instructions

### Step 1: Review Decoded Output

**Context**: Examine the printed results for email patterns.

No command required.

> Look for byte strings like b'mantuhackerone1738@gmail.com'. Verify domain legitimacy (e.g., gmail.com).

### Step 2: Cross-Validate PII

**Context**: Ensure the data matches expected formats and context.

No command required.

> Compare against known test emails or patterns; note any additional PII like timestamps.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[pii-verification]]
