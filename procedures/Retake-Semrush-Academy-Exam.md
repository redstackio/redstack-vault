---
tags:
  - business-logic
  - web
  - exam-retake
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
updated_at: '2025-12-14T17:28:28.556Z'
sub_techniques: []
id: 667aeb7c-2254-4307-a39e-47b779f90a3e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Retake-Semrush-Academy-Exam

## Summary

This procedure restarts the Semrush Academy exam to generate a new submission opportunity, allowing interception of a fresh JSON request for tampering.

## Description

After an initial failed or arbitrary submission, the platform allows retakes. This step initiates the retake without answering questions, focusing on preparing the submission request for modification. The vulnerability stems from the lack of validation, making retakes a vector for replaying tampered data. Expected outcome is a new session with an interceptable request.

## Requirements

1. Prior completion of an exam (even with wrong answers)
2. Access to retake functionality on the platform
3. Developer tools for monitoring

## Defense

Defensive measures and detection strategies:

- Limit retake attempts per user/session
- Validate submission timestamps to prevent manipulation
- Log and alert on multiple submissions in short timeframes

## Objectives

1. Trigger a new exam submission process
2. Prepare for payload interception
3. Avoid legitimate answering to maintain control over the request

## Instructions

### Step 1: Initiate Retake

**Context**: Use the platform's retake option to start a fresh exam instance.

After viewing results or failure, select the retake button. Do not proceed to answer questions.

### Step 2: Prepare for Submission Interception

**Context**: Position tools to capture the upcoming submission.

Open developer tools Network tab and clear previous logs. Proceed to the submission stage by simulating completion (e.g., click next without answering).

**Expected Output**: New request pending, similar structure to initial submission.

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
- [[exam-retake]]
