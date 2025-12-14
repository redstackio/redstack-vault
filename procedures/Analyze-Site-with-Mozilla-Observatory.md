---
tags:
  - scan
  - observatory
  - csp
type: procedure
tools:
  - '[[tools/Mozilla-Observatory]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:28:12.627Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: a1766e16-2ee6-4595-9d13-63a45cd6aa27
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Analyze-Site-with-Mozilla-Observatory

## Summary

This procedure uses the Mozilla Observatory tool to scan a website for security header implementations, specifically checking for CSP and clickjacking protections to validate vulnerabilities.

## Description

Mozilla Observatory is a free online tool that grades websites based on security practices, including header analysis. In this context, it confirms the lack of CSP frame-ancestors and X-Frame-Options on targets like etherscamdb.info, providing a report with recommendations. This is useful in reconnaissance phases of web attacks to prioritize exploitable sites without local tools.

## Requirements

1. Internet access to https://observatory.mozilla.org
2. Target domain URL
3. No installation needed (web-based)

## Defense

Defensive measures and detection strategies:

- Regularly scan your own site with Observatory to maintain high scores
- Automate header checks in CI/CD pipelines
- Alert on low Observatory grades in monitoring systems

## Objectives

1. Validate missing CSP and frame protections externally
2. Obtain a security grade and specific warnings for clickjacking
3. Generate evidence for vulnerability reports

## Instructions

### Step 1: Access Observatory

**Context**: Navigate to the tool and input the target.

Visit https://observatory.mozilla.org and enter the target domain, e.g., etherscamdb.info, then click 'Analyze'.

### Step 2: Review Scan Results

**Context**: Interpret the report for CSP and framing issues.

Wait for the scan to complete (usually seconds). Examine the 'Content Security Policy' and 'Clickjacking Protection' sections in the results.

> Expected output: Low or zero score for CSP, with warnings like 'No CSP header implemented' and clickjacking risk highlighted.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Mozilla-Observatory]]

## Tags

- [[scan]]
- [[csp]]
