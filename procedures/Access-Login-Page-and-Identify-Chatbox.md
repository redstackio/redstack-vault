---
tags:
  - web-access
  - reconnaissance
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
updated_at: '2025-12-14T04:08:55.208Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: b668081a-2aab-41a0-8442-7cb8c7c221ee
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Login-Page-and-Identify-Chatbox

## Summary

This procedure involves navigating to the Stripo Inc login page and locating the chatbox feature, which serves as the entry point for injecting payloads to exploit SSRF and command injection vulnerabilities.

## Description

The login page at https://my.stripo.email/cabinet/#/login?guid=&tn=&locale=en contains a chat input field that processes user input without proper validation, allowing attackers to trigger server-side requests and commands. This step sets up the environment for subsequent exploitation, requiring no authentication and targeting a public-facing web application.

## Requirements

1. Web browser (e.g., Chrome, Firefox)
2. Internet access to the target URL
3. Basic knowledge of web page inspection

## Defense

Defensive measures and detection strategies:

- Implement input validation on chat features to restrict external URLs and commands
- Monitor server logs for unexpected outbound requests or DNS queries
- Use web application firewalls (WAF) to block anomalous input patterns

## Objectives

1. Gain access to the vulnerable login interface
2. Identify the chatbox for payload injection
3. Prepare for SSRF and command injection testing

## Instructions

### Step 1: Navigate to Login Page

**Context**: Directly access the target URL to load the login interface.

No command required; use browser to visit:

https://my.stripo.email/cabinet/#/login?guid=&tn=&locale=en

> The page should load without errors, displaying the login form and chatbox.

### Step 2: Locate Chat Input Field

**Context**: Inspect the page to find the chatbox element for input submission.

Use browser developer tools (F12) to identify the input field, typically a text area labeled for chat or support.

> Successful identification allows proceeding to payload injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web-access]]
- [[Reconnaissance]]
