---
id: proc-uber-trigger-xss-134124
name: Trigger-XSS-via-m-uber-Login
tags:
  - xss
  - trigger
  - uber
  - login
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
updated_at: '2025-12-14T03:15:26.604Z'
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
# Trigger-XSS-via-m-uber-Login

## Summary

This procedure triggers the execution of the stored self-XSS payload by logging into m.uber.com, where the invite code is displayed without proper HTML escaping, allowing JavaScript to run in the authenticated user's browser.

## Description

After setting the payload on uber.com, accessing m.uber.com and signing in causes the invite code to be rendered in the user profile, likely within a `<span>` tag. The lack of escaping enables breakout and script execution, such as alerts or data exfiltration. This self-XSS can be extended via social engineering to trick users into setting malicious codes. Expected outcomes include arbitrary JS execution, limited to the victim's own session.

## Requirements

1. Payload already set via prior procedure
2. Access to m.uber.com (mobile-optimized Uber site)
3. Same authenticated account

## Defense

Defensive measures and detection strategies:

- Apply output encoding (e.g., HTML entity encoding) when displaying user input
- Implement strict CSP headers to block inline scripts
- Log and alert on XSS payload patterns in user profiles

## Objectives

1. Render the stored payload on m.uber.com
2. Execute injected JavaScript upon login
3. Demonstrate potential for session theft or phishing

## Instructions

### Step 1: Access m.uber.com

**Context**: Open the mobile Uber site in a browser to initiate the login process.

Navigate to m.uber.com using a desktop or mobile browser.

### Step 2: Sign In

**Context**: Authenticate with the account containing the malicious invite code to trigger display.

Enter credentials and log in. The profile page will load, displaying the invite code.

> Upon rendering, the payload executes, e.g., `<span>uber</span><script>alert(document.domain)</script>` breaks out of the tag.

### Step 3: Observe Execution

**Context**: Verify the XSS by checking for script output, such as alerts or console logs.

Inspect the page source or developer console for execution confirmation. For exfiltration, modify payload to send cookies via fetch or img src.

**Expected Output**: JavaScript runs, e.g., alert popup or network request stealing session data.

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
- [[trigger]]
