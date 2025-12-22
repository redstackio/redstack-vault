---
id: 555e4567-e89b-12d3-a456-426614174005
name: Login-as-Victim-and-Open-Malicious-HTML
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:20.891Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[T1566.001]]'
sub_techniques: []
tags:
  - victim-login
  - social-engineering
  - phishing
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---

# Login-as-Victim-and-Open-Malicious-HTML

## Summary

This procedure simulates or tricks the victim into logging in to IntenseDebate and loading the malicious HTML file to set up the XSS trigger.

## Description

Social engineering is used to deliver the xss.html file (e.g., via email or download link). The victim must authenticate their session for the POST request to be under their context, reflecting the payload. This step bridges setup and execution.

## Requirements

1. Victim credentials
2. Access to xss.html file
3. Social engineering method (e.g., email)

## Defense

Defensive measures and detection strategies:

- Train users on phishing recognition
- Block or scan local file executions in sensitive contexts

## Objectives

1. Authenticate victim session
2. Load payload file
3. Position for submission

## Instructions

### Step 1: Victim Authentication

**Context**: Ensure session is active.

Have the victim log in to https://www.intensedebate.com using their credentials.

> Confirm dashboard access.

### Step 2: Load HTML File

**Context**: Open the file in browser.

Direct the victim to open the local xss.html file in their browser while logged in.

> File should load showing the submit button.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.001]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[victim-login]]
- [[social-engineering]]
- [[Phishing]]
