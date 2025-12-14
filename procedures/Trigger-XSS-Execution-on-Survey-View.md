---
tags:
  - xss
  - execution
  - client-side
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
updated_at: '2025-12-14T03:16:37.531Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: d3626008-d569-401d-80b7-d38a8fd6f999
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-on-Survey-View

## Summary

This procedure involves enticing victims to view the compromised survey, causing the stored XSS payload to execute in their browser context, allowing arbitrary JavaScript to run and perform actions like session hijacking or data exfiltration.

## Description

Once the payload is stored via the 'site' parameter, any organization member accessing the survey page will render the unsanitized content, executing the JavaScript. This leads to impacts such as stealing session cookies or keystrokes within the Larksuite domain. The attack relies on social engineering to get views but exploits the persistence of stored XSS.

## Requirements

1. Valid survey URL from injection step
2. Access to communication channels (e.g., email, Slack) for sharing
3. Monitoring setup on attacker server for exfiltrated data

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and suspicious survey links
- Implement XSS auditors or WAF rules to block script injection
- Log and alert on unexpected external requests from authenticated sessions

## Objectives

1. Cause payload execution in victim browsers
2. Collect stolen data via exfiltration
3. Achieve session hijacking if cookies are captured

## Instructions

### Step 1: Distribute Survey Link

**Context**: Share the survey to prompt views by targets.

No command; send the URL: `https://larksuite.com/survey/survey123` via organization chat or email, e.g., "Please review this survey."

### Step 2: Monitor Execution

**Context**: Watch for incoming data from the payload's fetch request.

Set up a simple server (e.g., using netcat or a web server) to log requests to `http://attacker.com/steal`.

**Expected Output**: HTTP GET requests with query params containing victim cookies, e.g., `/steal?data=sessionid=abc123`.

### Step 3: Validate Impact

**Context**: Test with a benign payload first to confirm execution without harming.

Replace payload with `<script>alert('XSS Triggered');</script>` and view the survey yourself; alert should pop up on load.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- execution
- hijacking
