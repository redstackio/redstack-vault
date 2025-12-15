---
tags:
  - auth-bypass
  - verification
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
updated_at: '2025-12-14T17:32:48.309Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
id: 8faef49e-2e11-468f-a598-fd813a645ad4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-Submission-to-Test-Program

## Summary

This procedure confirms a successful report submission to a sandbox test program after API bypass, validating the ban circumvention.

## Description

After executing the API submission, check the sandbox program's dashboard or use API response to verify report creation. This step ensures the bypass works without UI errors, highlighting the vulnerability's impact on spam potential.

## Requirements

1. Submitted report ID from API response
2. Access to sandbox program UI
3. curl for re-verification if needed

## Defense

Defensive measures and detection strategies:

- Audit API submissions in program dashboards
- Flag unexpected reports from banned users
- Cross-check submission logs

## Objectives

1. Confirm report landed in test program
2. Validate bypass efficacy
3. Expected outcome: Report visible in UI

## Instructions

### Step 1: Check Program Dashboard

**Context**: Log in to the sandbox program to view reports.

**Command** (Manual UI action):

Navigate to Reports section.

> Look for the test report. Expected output: Report listed with details.

### Step 2: Optional API Verification

**Context**: If UI access restricted, query API for reports.

**Command** ([[commands/curl-hackerone-report-submission]] modified for GET):
```bash
curl "https://api.hackerone.com/v1/hackers/reports" -u "testhackerone-creative:pYnONekvxUTvHbKF7Jp64qh9STIhhdXvKmefWOeR8YU="
```

> Expected output: JSON list including the new report.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/curl-hackerone-report-submission]]

## Tools Used

- [[tools/curl]]

## Tags

- auth-bypass
- verification
- hackerone
