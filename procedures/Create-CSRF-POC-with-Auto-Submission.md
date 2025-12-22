---
tags:
  - csrf
  - poc
  - social-engineering
type: procedure
tools:
  - '[[tools/Burp-Suite-Professional]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/Exploit-CSRF-XSS-POST]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.437Z'
sub_techniques: []
id: 25490a46-2e84-469b-a024-818fab367c58
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Create-CSRF-POC-with-Auto-Submission

## Summary

This procedure generates an HTML-based proof-of-concept for CSRF that auto-submits a malicious POST request with the XSS payload, tricking authenticated users into executing the exploit.

## Description

Using Burp Suite, create a self-submitting form targeting the vulnerable endpoint. The JavaScript auto-submit and history.pushState mimic a legitimate navigation, bypassing user awareness. When visited by a logged-in victim, it forges the request, reflects the XSS, and executes script for session theft or phishing.

## Requirements

1. Payload from prior crafting step
2. Hosting capability for the HTML file (e.g., attacker server)
3. Victim interaction via link (phishing/social engineering)

## Defense

Defensive measures and detection strategies:

- Require CSRF tokens for all POST forms
- Educate users on not visiting untrusted links while authenticated
- Implement referrer policy checks and monitor cross-origin requests

## Objectives

1. Automate request forgery without user input
2. Spoof origin to evade basic checks
3. Achieve XSS execution in victim context

## Instructions

### Step 1: Generate PoC HTML

**Context**: Build the form with hidden fields containing the payload.

Use Burp Suite's 'Generate CSRF PoC' feature on the intercepted request to create the base HTML, then add auto-submit script.

### Step 2: Enhance with Origin Spoofing

**Context**: Add JavaScript to push state and submit seamlessly.

Modify the script: <script>history.pushState({}, '', '/deals'); document.forms[0].submit();</script>

### Step 3: Test and Deploy

**Context**: Verify the PoC triggers the exploit.

Host the HTML and visit while authenticated; expect alert execution.

Incorporate [[commands/Exploit-CSRF-XSS-POST]] as the form action payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/Exploit-CSRF-XSS-POST]]

## Tools Used

- [[tools/Burp-Suite-Professional]]

## Tags

- [[csrf]]
- [[poc]]
