---
id: proc-weblate-html-injection
tags:
  - html-injection
  - weblate
  - support-form
type: procedure
tools:
  - '[[tools/Request-Tracker]]'
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
updated_at: '2025-12-14T17:25:12.640Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-HTML-Payload-into-Weblate-Support-Form

## Summary

This procedure exploits a lack of input sanitization in Weblate's Request Tracker (RT) support form by submitting an HTML img tag payload across all fields, poisoning the ticket content for later execution when viewed by administrators.

## Description

The Weblate support system, built on Request Tracker, processes form submissions without properly escaping HTML, allowing arbitrary tags to be injected. By filling fields like subject and body with a payload such as `<img src="https://attacker-server.com/track.gif">`, the ticket becomes a vector for passive tracking. This targets public-facing forms on weblate.org and hosted.weblate.org, requiring no authentication. Expected outcomes include ticket creation and payload persistence in the RT database, ready for admin interaction.

## Requirements

1. Public internet access to weblate.org/support or hosted.weblate.org/support
2. Control of an external server to host the tracking image (e.g., a simple HTTP endpoint)
3. Basic knowledge of HTML and web forms

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and HTML escaping in RT form processing (e.g., using libraries like DOMPurify)
- Disable automatic loading of external images in email clients and RT web panels
- Monitor support ticket submissions for anomalous content patterns, such as img tags

## Objectives

1. Create a poisoned support ticket with executable HTML
2. Ensure payload survives storage and rendering in RT
3. Position for information disclosure upon admin view

## Instructions

### Step 1: Prepare the Payload

**Context**: Craft a minimal HTML img tag that loads from your server without alerting users.

No command needed; manually construct: `<img src="https://your-server.com/track.gif">` (replace with your endpoint).

> This payload is passive and blends as broken text in forms.

### Step 2: Submit to Support Form

**Context**: Access the form and inject the payload into every field to maximize execution chances.

Use a browser to navigate to https://weblate.org/support/ or https://hosted.weblate.org/support/. Fill all inputs (e.g., name, email, subject, message) with the payload string. Submit the form.

> Form submission creates a ticket in RT; payload is stored unescaped.

### Step 3: Verify Submission

**Context**: Confirm the ticket was accepted without errors.

Check for a success message or email confirmation (if provided). If possible, submit a benign ticket to compare.

> Success: Ticket ID or confirmation displayed; no rejection of HTML content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Request-Tracker]]

## Tags

- [[html-injection]]
- [[weblate]]
