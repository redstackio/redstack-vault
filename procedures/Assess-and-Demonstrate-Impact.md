---
tags:
  - impact-assessment
type: procedure
tools:
  - '[[tools/cURL]]'
  - '[[tools/Browser-Console]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-with-session-cookie]]'
platforms:
  - Web
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 4986f972-0a78-45e3-b4e3-a3c36e3de592
created_at: '2025-12-11T06:10:40.561Z'
updated_at: '2025-12-11T06:10:40.561Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0040]]'
mitre_techniques:
  - '[[T1499]]'
---
# Assess and Demonstrate Impact

## Summary

This procedure evaluates the impact of unauthorized access by documenting exposed data and potential risks.

## Description

After accessing sensitive areas, compile evidence of the breach's scope, such as the number of reports viewed, to demonstrate impact for responsible disclosure.

## Requirements

1. Access to breached data
2. Documentation tools
3. Ethical guidelines for handling sensitive info

## Defense

Defensive measures and detection strategies:

- Regular security audits of session management
- Incident response for leaked credentials

## Objectives

1. Quantify breach impact
2. Prepare evidence
3. Avoid data exfiltration

## Instructions

### Step 1: Document Access

**Context**: Record accessed resources without copying data.

Take redacted screenshots of inbox views and report counts.

> Note exposure of metadata from multiple programs.

### Step 2: Evaluate Risks

**Context**: Analyze potential consequences.

Assess how the access could lead to confidential info leaks.

> Emphasize no malicious intent.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[impact-assessment]]
