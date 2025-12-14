---
id: proc-create-malicious-ticket
tags:
  - xss
  - injection
  - wordpress
  - supportflow
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
updated_at: '2025-12-14T03:16:08.109Z'
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
# Create-Malicious-SupportFlow-Ticket

## Summary

This procedure involves submitting a new ticket through the SupportFlow plugin with a crafted JavaScript payload in the subject field, exploiting the lack of esc_attr() escaping to store the payload persistently for later execution.

## Description

The SupportFlow plugin handles ticket creation on the frontend or support portal, storing the subject in the database without proper sanitization when filters like wptexturize are disabled. The payload breaks out of the input value attribute (e.g., via ">) and injects a <script> tag. This stored XSS affects any admin viewing the ticket list or details, as the subject is echoed into an admin form input on class-supportflow-admin.php line 905 without escaping. Prerequisites include the disabled filter; exploitation requires authenticated access to create tickets.

## Requirements

1. Authenticated session with ticket submission privileges (e.g., logged-in user or public form if enabled).
2. WPTexturize filter disabled via prior procedure.
3. SupportFlow plugin active on the target WordPress site.

## Defense

Defensive measures and detection strategies:

- Apply esc_attr() to all output in plugin forms (patch the plugin).
- Sanitize inputs server-side with wp_kses_post() or similar.
- Monitor ticket subjects for suspicious patterns like <script> via WAF or logging.

## Objectives

1. Store unescaped JavaScript in the ticket subject database field.
2. Ensure the payload survives storage and retrieval without alteration.
3. Set up conditions for execution upon admin interaction.

## Instructions

### Step 1: Access Ticket Creation Form

**Context**: Navigate to the SupportFlow ticket submission interface, typically via a support page or dashboard widget, and prepare to enter details.

**Command** (Manual form submission, no CLI command):

> Log in if required and locate the 'New Ticket' form. Fill in required fields like email or name, but focus on the subject.

### Step 2: Inject Payload in Subject Field

**Context**: Enter the malicious payload in the subject input to break out of the attribute and inject script, then submit to store it.

**Command** (Manual input):

> Use payload: `1"><script>alert('hi');</script>` in the subject field. Complete the form (e.g., add a benign message body) and click 'Submit'.

> Expected output: Success message confirming ticket creation; check SupportFlow -> All Tickets (as admin) to see the subject with raw payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- injection
- wordpress
- supportflow
