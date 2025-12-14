---
tags:
  - wordpress
  - lms
  - message-creation
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
updated_at: '2025-12-14T17:32:29.193Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 012e4cdf-c7c7-4239-aeed-ffe74b5ebcad
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Private-Question-in-Sensei-LMS

## Summary

This procedure simulates a student submitting a private question to a teacher in a Sensei LMS course, creating a sensei-message object with a numeric ID that can later be exploited.

## Description

As part of the vulnerability chain, this step generates private message data intended only for authenticated users. Using the frontend course interface, a question is submitted via the contact feature, storing it as a sensei-message post type. The target is a WordPress site with Sensei LMS <= 4.4.3. Expected outcome: A private message entry accessible via REST API if permissions are bypassed.

## Requirements

1. Student-level access to the WordPress frontend (or simulated)
2. An existing course with contact feature enabled
3. Browser access to the site

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on message submissions
- Log all user interactions with private features
- Enforce authentication for all messaging endpoints

## Objectives

1. Create a vulnerable private message object
2. Assign a sequential numeric ID to the message
3. Set up data for unauthorized disclosure

## Instructions

### Step 1: Navigate to Course

**Context**: Access the course page as a student.

Enroll in or view the course frontend at /courses/course-slug/.

### Step 2: Submit Question

**Context**: Use the private contact form to ask a question.

Fill in the question form and submit. This creates a sensei-message post.

**Expected Output**: Submission confirmation; message stored in database.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[wordpress]]
- [[lms]]
- [[message-creation]]
