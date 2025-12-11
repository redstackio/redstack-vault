---
tags:
  - hackerone
  - report-creation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/ruby-redact-pii]]'
platforms:
  - Web
techniques:
  - '[[Gather Victim Host Information]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 2e32b2b5-6edf-404c-bb70-5a3942857d17
created_at: '2025-12-11T06:10:15.684Z'
updated_at: '2025-12-11T06:10:15.684Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0043]]'
mitre_techniques:
  - '[[T1592]]'
---
# Create Dummy Report on HackerOne

## Summary

This procedure involves creating a dummy report on the HackerOne platform to serve as a foundation for inviting collaborators and exploiting information disclosure vulnerabilities.

## Description

By submitting a new report, attackers can access the collaboration features, allowing them to add users and trigger GraphQL requests that leak sensitive information like emails. This is typically done in a web browser on the HackerOne site, requiring a valid account.

## Requirements

1. Valid HackerOne account with report submission privileges.
2. Web browser with access to hackerone.com.
3. Basic knowledge of the HackerOne interface.

## Defense

Defensive measures and detection strategies:

- Monitor for unusual report creation patterns or dummy reports.
- Implement rate limiting on report submissions and invitations.

## Objectives

1. Establish a report for collaborator invitations.
2. Prepare for GraphQL mutation exploitation.
3. Enable subsequent steps for email disclosure.

## Instructions

### Step 1: Navigate to Report Submission

**Context**: Access the HackerOne dashboard to start a new report.

Log in to HackerOne and go to the 'Submit Report' section.

> Fill in minimal details for a dummy report.

### Step 2: Submit the Report

**Context**: Complete and send the report.

Enter placeholder information and submit.

> The report should now be visible in your list.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[hackerone]]
- [[report-creation]]
