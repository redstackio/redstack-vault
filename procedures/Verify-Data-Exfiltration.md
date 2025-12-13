---
tags:
  - xxe
  - verification
  - exfiltration
type: procedure
tools:
  - '[[tools/Curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/analyze-response-for-exfiltration]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 93fce88d-2c23-40d1-85e0-2ad7d775a236
created_at: '2025-12-13T09:00:27.363Z'
updated_at: '2025-12-13T09:00:27.363Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify Data Exfiltration

## Summary

This procedure verifies the success of an XXE exploit by analyzing the server response for exfiltrated data, confirming the vulnerability's impact.

## Description

After sending the payload, inspect the HTTP response for leaked information, such as file contents. This step validates the exploitation and assesses severity. Expected outcomes include visible sensitive data in the response.

## Requirements
1. Successful payload delivery
2. Tool for response analysis
3. Knowledge of expected leaked data patterns

## Defense

Defensive measures and detection strategies:
- Log and alert on responses containing unexpected system data
- Rate-limit XML requests to prevent repeated exploitation attempts

## Objectives
1. Confirm data exposure
2. Document exploit evidence
3. Evaluate overall risk

## Instructions

### Step 1: Capture and Analyze Response

**Context**: Send the payload and pipe the response for analysis.

**Command** ([[commands/analyze-response-for-exfiltration]]):
```bash
curl -X POST -H "Content-Type: application/xml" --data "[xxe payload]" https://subdomain.informatica.com/endpoint | grep "root:"
```

> This filters for passwd-like content.

### Step 2: Validate Exfiltrated Data

**Context**: Manually review for sensitive information.

**Command** ([[commands/analyze-response-for-exfiltration]]):
```bash
curl -X POST -H "Content-Type: application/xml" --data "[xxe payload]" https://subdomain.informatica.com/endpoint > response.txt && cat response.txt
```

> Save and inspect the full response.

## MITRE ATT&CK Mapping

### Tactics
- [[Collection]]

### Techniques
- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used
- [[commands/analyze-response-for-exfiltration]]

## Tools Used
- [[tools/Curl]]

## Tags
- [[xxe]]
- [[verification]]
