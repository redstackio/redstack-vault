---
tags:
  - business-logic
  - web
  - exam-submission
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:28.568Z'
sub_techniques: []
id: c823659d-b9c8-478a-8939-8422d4ce76e8
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Complete-Initial-Exam-Submission

## Summary

This procedure involves submitting an initial exam in Semrush Academy with arbitrary answers to capture the baseline JSON submission request, setting the stage for later tampering.

## Description

In the Semrush Academy platform, exams are submitted via a JSON payload over a web API. Without server-side validation, the client-side request can be intercepted. This step completes a submission with incorrect or random answers to observe the request structure, where answers are represented as an object with question keys mapped to '1' (correct) or empty strings (incorrect). The target environment is a standard web browser accessing the exam interface.

## Requirements

1. Active Semrush Academy account with exam access
2. Browser with developer tools enabled (e.g., Chrome F12)
3. Basic understanding of network request inspection

## Defense

Defensive measures and detection strategies:

- Implement server-side answer validation against question database
- Use session tokens or nonces in submissions to prevent replay attacks
- Monitor for anomalous submission patterns, like rapid retakes with perfect scores

## Objectives

1. Capture the exam submission request structure
2. Identify the JSON payload format for answers
3. Establish a baseline for modification in subsequent steps

## Instructions

### Step 1: Access and Start Exam

**Context**: Log in to Semrush Academy and begin the exam to load the submission mechanism.

Navigate to the exam page and start the test. Answer questions arbitrarily without concern for correctness.

### Step 2: Submit Exam and Intercept Request

**Context**: Submit the exam to trigger the API request, then inspect it in developer tools.

Click submit. Open the Network tab in developer tools, filter for the submission request (likely a POST to an endpoint like /exam/submit), and view the request payload.

**Expected Output**: JSON payload visible, e.g., {"answers": {"question1": "", "question2": "1"}}, confirming the structure.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[business-logic]]
- [[web]]
- [[exam-submission]]
