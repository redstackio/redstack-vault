---
id: proc-linkedin-setup
tags:
  - linkedin
  - setup
  - assessment
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:34.043Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Prepare-LinkedIn-Skill-Assessment-Setup

## Summary

This procedure sets up a legitimate skill assessment on LinkedIn to generate a deletable result, serving as the foundation for intercepting and modifying the deletion request in an IDOR attack.

## Description

In the context of exploiting LinkedIn's IDOR vulnerability, the attacker first authenticates and completes a skill assessment to trigger the deletion endpoint. This creates a valid request that can be intercepted and repurposed to target other users. The target environment is the LinkedIn web platform, requiring only a standard browser session. Expected outcomes include access to the assessments hub and a visible delete option.

## Requirements

1. Valid LinkedIn account credentials
2. Browser access to https://www.linkedin.com
3. Ability to complete a simple skill quiz (e.g., HTML basics)

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on assessment completions per account
- Monitor unusual assessment patterns or rapid deletions
- Require multi-factor confirmation for skill result changes

## Objectives

1. Generate a legitimate deletable skill assessment result
2. Position for request interception
3. Ensure authenticated session for endpoint access

## Instructions

### Step 1: Authenticate to LinkedIn

**Context**: Log in to establish a valid session required for assessment access.

No specific command; use browser to navigate to https://www.linkedin.com and enter credentials.

> Successful login redirects to the homepage with personalized content.

### Step 2: Complete a Skill Assessment

**Context**: Take and pass (or fail) an assessment to create a result entry.

Navigate to a skill like HTML via search, start the quiz, and submit.

> Upon completion, a result page appears with badge if passed or retake option if failed.

### Step 3: Access Assessments Hub

**Context**: Locate the result for deletion initiation.

Visit https://www.linkedin.com/skill-assessments/hub/quizzes/?channel=JOBS_HOME_NAVIGATION_BAR. If failed, use https://www.linkedin.com/skill-assessments/hub/reports/?channel=JOBS_HOME_NAVIGATION_BAR&resultType=TO_RETAKE.

> Hub loads with list of assessments; click badge or retake button to view details.

### Step 4: Initiate Deletion

**Context**: Trigger the delete action to prepare for interception.

Click the kebab menu icon next to the result and select 'Delete results'.

> Dialog confirms deletion; this is where proxy interception begins in subsequent procedures.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[linkedin]]
- [[setup]]
- [[assessment]]
