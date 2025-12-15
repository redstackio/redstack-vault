---
id: proc-hackerone-access-report-dos
tags:
  - web
  - hackerone
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:30.808Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-HackerOne-Report-for-DoS-Preparation

## Summary

This procedure involves logging into the HackerOne platform and accessing or creating a report using a sandboxed team to prepare for denial of service exploitation, bypassing partial rate limits on non-sandboxed teams.

## Description

In the context of testing or exploiting the DoS vulnerability in HackerOne's report view, this step ensures access to a report where comments can be spammed without immediate restrictions. Sandboxed teams allow unrestricted actions for testing, while non-sandboxed may have some rate-limiting but do not prevent the overall attack. The target environment is the web-based HackerOne platform, and outcomes include readiness for comment flooding leading to server overload.

## Requirements

1. Valid HackerOne account credentials with access to create or view reports.
2. Use of a sandboxed team for optimal testing (avoids rate limits).
3. Web browser with internet access to hackerone.com.

## Defense

Defensive measures and detection strategies:

- Implement account-level rate limiting on report access and creation.
- Monitor for unusual login patterns or sandboxed team usage spikes.

## Objectives

1. Secure initial access to a HackerOne report.
2. Prepare the environment for subsequent comment spamming.
3. Ensure minimal restrictions for exploitation.

## Instructions

### Step 1: Log In to HackerOne

**Context**: Authenticate to the platform to gain access to reports.

Navigate to https://hackerone.com and log in with your credentials. Select or create a sandboxed team if available.

### Step 2: Access or Create Report

**Context**: Obtain a report ID for targeting, such as by submitting a test vulnerability report or selecting an existing one.

Go to the reports section, create a new report if needed (e.g., a dummy vulnerability), or select an existing test report (e.g., ID 137508). Note the report ID for later steps.

**Expected Output**: Report page loads, showing the comment interface.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web]]
- [[hackerone]]
- [[initial-access]]
