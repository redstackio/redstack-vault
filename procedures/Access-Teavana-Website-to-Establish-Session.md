---
id: bf2e579d-3c9a-4c69-b758-96a7421fb7fd
name: Access-Teavana-Website-to-Establish-Session
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:12.739Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
tags:
  - xss
  - initial-access
  - web
platforms:
  - Web
commands: []
tools: []
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

# Access-Teavana-Website-to-Establish-Session

## Summary

This procedure involves normally accessing the teavana.com website to establish a browser session and cookie context, which is a prerequisite for triggering the reflected XSS in the subsequent steps.

## Description

In the context of exploiting the reflected XSS vulnerability on teavana.com's Locale-Change endpoint, an initial normal visit to the site is required to set up session cookies or establish the browser's context. This ensures that when the malicious URL is visited, the JavaScript executes within the site's domain and session, allowing access to cookies or other sensitive data. The target environment is a web application built on Demandware (Salesforce Commerce Cloud), and no special privileges are needed.

## Requirements

1. Web browser with JavaScript enabled (e.g., Chrome, Firefox)
2. Internet access to teavana.com
3. No authentication or credentials required

## Defense

Defensive measures and detection strategies:

- Monitor for unusual traffic patterns to the site from the same IP
- Implement session management best practices to limit cookie exposure
- Use Content Security Policy (CSP) to restrict script execution

## Objectives

1. Establish a valid session on teavana.com
2. Set browser cookies for site context
3. Prepare for payload delivery without alerting defenses

## Instructions

### Step 1: Navigate to Homepage

**Context**: This step simulates legitimate user access to load the site and initiate session establishment.

No specific command needed; use browser:

Open https://www.teavana.com in your browser.

> The page should load the homepage, and checking Network tab in developer tools (F12) will show cookies being set, such as session IDs or locale preferences.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[initial-access]]
- [[web]]
