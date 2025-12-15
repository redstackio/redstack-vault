---
tags:
  - review
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 3c6e1810-b41f-4841-a961-2227ae6b0d52
created_at: '2025-12-14T17:25:47.362Z'
updated_at: '2025-12-14T17:25:47.362Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-Feedback-Review-Process

## Summary

This procedure simulates a legitimate review closure to prepare the vulnerable POST request for interception, using security team credentials to close the test report and enter feedback.

## Description

As part of the IDOR exploitation chain, a security team member (e.g., phspade) accesses the test report, closes it, and initiates the review by selecting feedback options like 'Friendliness' and entering public/private comments. This triggers the /hacker_reviews endpoint. The target is the HackerOne admin interface, requiring team access. Outcomes include the request being ready for proxy interception.

## Requirements

1. Security team account with report management permissions
2. Access to the specific test report ID
3. Proxy tool configured for traffic interception

## Defense

Defensive measures and detection strategies:

- Log all review actions with user and report ID validation
- Alert on mismatched user-report associations during reviews

## Objectives

1. Close the report to enable review
2. Populate feedback fields to generate the POST request
3. Set up for parameter modification

## Instructions

### Step 1: Access and Close Report

**Context**: Log in as security team and locate the test report.

Navigate to the program dashboard, find the report, and set status to 'Closed'.

### Step 2: Start Review and Enter Feedback

**Context**: Click review button and input details to trigger submission.

Select 'Friendliness' radio button, enter Public feedback: 'Japz is awesome :)' and Private feedback: 'Thanks for your report.'

**Expected Output**: Review form ready for submission, POST request queued.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[review]]
- [[web]]
