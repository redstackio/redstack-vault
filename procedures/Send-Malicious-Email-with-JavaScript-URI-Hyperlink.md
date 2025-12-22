---
tags:
  - xss
  - email
  - payload-delivery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[T1566.001]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: b0b33393-81ed-4442-bdab-e293051dd748
created_at: '2025-12-14T03:15:53.264Z'
updated_at: '2025-12-14T03:15:53.264Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Send-Malicious-Email-with-JavaScript-URI-Hyperlink

## Summary

This procedure involves crafting and sending an email containing a hyperlink with a javascript: URI payload to a target team address in Respondly, setting up the conditions for an XSS attack when the email is viewed.

## Description

In the context of exploiting Respondly's email viewing feature, this procedure delivers a malicious payload via email. The hyperlink uses a javascript: URI, such as javascript:alert(0);, which is not sanitized in the 'original HTML' view. This allows arbitrary JavaScript execution upon clicking. The attack targets authenticated users who view team emails, potentially leading to session cookie theft or account takeover. Prerequisites include knowledge of the target email address, like kfvm@mail.respond.ly, and access to an email sending service.

## Requirements

1. Access to an email client or SMTP service for sending messages
2. Knowledge of the target Respondly team email address
3. Basic understanding of HTML hyperlink syntax for embedding javascript: URIs

## Defense

Defensive measures and detection strategies:

- Implement email content filtering to block or strip javascript: URIs in incoming messages
- Use HTML sanitization libraries (e.g., DOMPurify) in all email rendering views
- Monitor for anomalous email patterns or test payloads in logs

## Objectives

1. Deliver unsanitized malicious hyperlink to the target email system
2. Ensure the payload remains intact for later execution
3. Position for client-side exploitation in the viewer's browser

## Instructions

### Step 1: Craft the Malicious Email

**Context**: Create an email body with a clickable hyperlink containing the javascript: URI payload to test or exploit the XSS vulnerability.

Use an email client to compose a message. In the body, insert HTML like: <a href="javascript:alert(0);">Click me</a>. Set the recipient to the target address, such as kfvm@mail.respond.ly, and send the email.

> This step simulates social engineering or legitimate testing; in a real attack, the email might mimic a benign notification to entice clicking.

**Expected Output**: Confirmation that the email was sent successfully, and it appears in the Respondly inbox.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.001]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[email]]
- [[payload-delivery]]
