---
id: proc-create-polldaddy-quiz
tags:
  - quiz-creation
  - polldaddy
  - web
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
updated_at: '2025-12-14T03:46:31.450Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Polldaddy-Multiple-Choice-Quiz

## Summary

This procedure outlines creating a basic multiple-choice quiz on the Polldaddy platform, serving as the initial setup for injecting stored XSS payloads in subsequent steps.

## Description

In the context of exploiting stored XSS in Polldaddy, this procedure establishes a quiz as the attack vector. Polldaddy's quiz creation interface allows users to build interactive quizzes, and this step prepares the structure for embedding malicious content. No technical exploits occur here; it's preparatory. Expected outcome: A saved quiz draft accessible for further modification.

## Requirements

1. Active Polldaddy account (sign up at polldaddy.com if needed)
2. Web browser with JavaScript enabled
3. Internet connection for platform access

## Defense

Defensive measures and detection strategies:

- Monitor user account activity for unusual quiz creation patterns
- Implement rate limiting on quiz submissions
- Log all quiz creation events for anomaly detection

## Objectives

1. Establish a quiz structure to host the XSS payload
2. Ensure quiz is configurable for media embeds
3. Prepare for payload injection without triggering alerts

## Instructions

### Step 1: Access Quiz Creation Interface

**Context**: Log in and navigate to the quiz builder to start a new quiz.

Browse to Polldaddy's dashboard, select "Create Quiz", and choose the multiple-choice question type. Enter a title like "Test Quiz" and add at least one question with options.

> No specific command; perform via web UI. Expected output: Quiz editor loads with question fields populated.

### Step 2: Configure Basic Quiz Settings

**Context**: Set up questions to make the quiz functional and save the draft.

Add 2-3 multiple-choice questions (e.g., "What is 2+2?" with options A:4, B:5). Do not add media yet. Click "Save" to persist the quiz.

> Web UI action. Expected output: Confirmation message and quiz ID generated.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[quiz-creation]]
- [[polldaddy]]
