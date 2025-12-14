---
id: proc-inject-xss-respondly-groupname
tags:
  - xss
  - payload-injection
  - account-creation
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:36.195Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Respondly-Group-Name

## Summary

This procedure involves creating a Respondly account using a malicious JavaScript payload in the group name field, exploiting the lack of input sanitization to store persistent XSS that can later be triggered for code execution.

## Description

In the Respondly application, the group name input during account registration is not properly sanitized, allowing attackers to inject HTML and JavaScript. The payload `"><img src=x onerror=alert(4)>" closes any open HTML tags and injects an image element that executes JavaScript on error, demonstrating the vulnerability. This stored payload can affect any user viewing the account details, including admins reviewing feedback emails, leading to potential session theft or data exfiltration.

## Requirements

1. Access to a web browser with JavaScript enabled
2. Valid email address for registration (no prior credentials needed)
3. Internet connection to reach https://app.respond.ly

## Defense

Defensive measures and detection strategies:

- Implement server-side input validation and HTML escaping for all user inputs, especially those rendered in HTML contexts
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript alerts or error events in application logs

## Objectives

1. Store malicious JavaScript payload in the application's database via group name
2. Set up conditions for persistent XSS execution upon rendering
3. Demonstrate potential for client-side attacks like alert popping or further payload delivery

## Instructions

### Step 1: Prepare and Navigate to Registration

**Context**: Access the Respondly signup page to begin account creation.

Navigate to https://app.respond.ly and click on the registration option. Fill in required fields like email and password, but focus on the group name input.

### Step 2: Inject the Payload

**Context**: Enter the XSS payload in the group name field to bypass sanitization.

In the group name field, input: `"><img src=x onerror=alert(4)>"

Complete the form submission to create the account.

> The payload will be accepted and stored without modification, confirming injection success via post-registration confirmation page.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[persistent-xss]]
