---
id: proc-001
tags:
  - web-access
  - lab-setup
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:56.730Z'
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
# Access-Web-Security-Academy-Lab

## Summary

This procedure outlines accessing PortSwigger's Web Security Academy lab to establish a session for testing error conditions in a web application environment.

## Description

In the context of vulnerability discovery, initial access to the target lab is essential. The PortSwigger Web Security Academy provides isolated lab instances for practicing web security techniques. This step involves navigating to the academy, selecting a lab, and loading the interactive environment, which runs on a Node.js backend. No authentication is required, making it publicly accessible. The goal is to prepare for subsequent interactions that may trigger errors.

## Requirements

1. Web browser with JavaScript enabled
2. Internet connection (initially stable)
3. Access to https://portswigger.net/web-security

## Defense

Defensive measures and detection strategies:

- Monitor lab access logs for unusual patterns
- Implement rate limiting on lab instance loads

## Objectives

1. Establish a valid session in the lab environment
2. Verify the lab is responsive
3. Prepare for error-inducing actions

## Instructions

### Step 1: Navigate to Academy

**Context**: Open the academy portal to select a lab exercise.

Browse to https://portswigger.net/web-security and choose a lab from the available topics, such as SQL injection or XSS.

> Expected output: Lab selection page loads, allowing choice of an instance.

### Step 2: Load Lab Instance

**Context**: Start the interactive lab session.

Click 'Start Lab' or equivalent to spawn an isolated instance. Interact minimally, such as viewing the welcome page or submitting a basic request.

> Expected output: Lab interface appears with unique URL and functional elements.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web-access
- lab-setup
