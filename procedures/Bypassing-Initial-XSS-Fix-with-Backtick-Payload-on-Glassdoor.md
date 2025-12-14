---
tags:
  - xss
  - reflected-xss
  - bypass
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/glassdoor-xss-poc-bypass]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 4a166ce5-95bc-4ad0-9a23-ec98a6f53bb5
created_at: '2025-12-14T00:11:25.409Z'
updated_at: '2025-12-14T00:11:25.409Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Bypassing Initial XSS Fix with Backtick Payload on Glassdoor

## Summary

This procedure bypasses an initial insufficient fix for the reflected XSS in utm_source by using backticks to close strings and inject an alert payload, proving the vulnerability persists.

## Description

After an initial remediation attempt, a new payload using backticks was crafted to close the string and execute JavaScript. This was tested on the same endpoint, leading to another alert execution. The final fix involved proper HTML encoding.

## Requirements

1. Web browser such as [[tools/Firefox]]
2. Access to the target URL post-initial fix
3. Knowledge of the initial vulnerability

## Defense

Defensive measures and detection strategies:

- Ensure comprehensive input sanitization including backticks and encoded characters
- Deploy WAF rules to detect common XSS patterns
- Conduct thorough post-fix testing

## Objectives

1. Bypass the initial fix
2. Execute arbitrary JavaScript again
3. Force a proper remediation

## Instructions

### Step 1: Navigate to Bypass POC URL

**Context**: Visit the crafted bypass URL to inject the backtick payload and trigger the XSS.

**Command** ([[commands/glassdoor-xss-poc-bypass]]):
```bash
https://www.glassdoor.com/employers/sem-dual-lp/?utm_source=%60%2balert/**/(1)%2b%60
```

> This URL uses backticks to close the string and execute an alert; expect a pop-up with '1'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/glassdoor-xss-poc-bypass]]

## Tools Used

- [[tools/Firefox]]

## Tags

- [[xss]]
- [[bypass]]
