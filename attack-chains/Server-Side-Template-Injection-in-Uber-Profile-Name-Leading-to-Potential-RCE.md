---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - ssti
  - jinja2
  - flask
  - rce
  - web
  - email-injection
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Inject-Simple-Jinja2-Expression-into-Uber-Profile-Name]]'
  - '[[procedures/Trigger-Uber-Email-Notification-to-Confirm-SSTI]]'
  - >-
    [[procedures/Exploit-Advanced-Jinja2-Payloads-for-Class-Enumeration-and-RCE]]
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:24:08.808Z'
description: >-
  Exploits SSTI in Uber's Flask Jinja2 template via user profile name field to
  achieve code injection and potential remote code execution during email
  rendering.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# Server-Side Template Injection in Uber Profile Name Leading to Potential RCE

Multi-stage attack chain demonstrating exploitation of SSTI in Uber's rider profile system to inject Jinja2 expressions, confirm rendering in emails, and escalate to potential RCE via Python class access.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Profile Name Injection] --> B[Email Trigger and Confirmation]
    B --> C[Advanced Payload Exploitation]
    C --> D[Potential RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser for profile updates
- Email client to receive and inspect notifications

### Target Environment

- Uber rider.uber.com web application
- Flask backend with Jinja2 templating
- Email service (support@uber.com)

### Initial Access Requirements

- Valid Uber rider account with profile update access
- Ability to receive emails from Uber

## Detailed Attack Procedures

### Step 1: Inject Simple Jinja2 Expression into Profile Name
procedure: [[procedures/Inject-Simple-Jinja2-Expression-into-Uber-Profile-Name]]

**Objective**: Test for SSTI by injecting a basic Jinja2 payload into the user profile name field to verify template rendering.

**Instructions**: Log in to rider.uber.com, navigate to the profile settings, and update the name field with a simple expression like `{{ '7'*7 }}`. Save the changes to submit the input.

**Expected Output**: The profile update succeeds without errors, setting the stage for rendering.

**Success Indicators**:
- Profile name updated successfully
- No immediate validation errors on input

### Step 2: Trigger Email Notification to Confirm SSTI
procedure: [[procedures/Trigger-Uber-Email-Notification-to-Confirm-SSTI]]

**Objective**: Provoke an email notification that renders the injected template, confirming SSTI by observing the evaluated expression.

**Instructions**: After updating the profile name, perform an action that triggers an email, such as another profile update or account activity that sends a confirmation email. Check the received email from support@uber.com for the rendered name.

**Expected Output**: Email titled 'Your Uber account information has been updated' arrives, with the name field displaying '7777777' instead of the raw payload.

**Success Indicators**:
- Email received with evaluated Jinja2 output
- Confirmation of template injection point in email body

### Step 3: Exploit Advanced Jinja2 Payloads for Class Enumeration and RCE
procedure: [[procedures/Exploit-Advanced-Jinja2-Payloads-for-Class-Enumeration-and-RCE]]

**Objective**: Escalate the injection to access Python internals, enumerate classes, and attempt RCE despite input length limits.

**Instructions**: Update the profile name with advanced payloads such as `{{ [].__class__.__base__.__subclasses__() }}` to list subclasses, or `{{ ''.__class__.mro()[1].__subclasses__() }}` for method resolution order exploration. For looping, use `{% for c in [1,2,3] %}{{c,c,c}}{% endfor %}`. Trigger emails to observe outputs and chain for deeper access.

**Expected Output**: Emails render lists of available Python classes or looped outputs, indicating access to internals; further chaining may enable RCE payloads.

**Success Indicators**:
- Rendered output shows Python class/subclass information
- Evidence of arbitrary code execution potential

## Attack Chain Summary

### Key Achievements

1. Confirmed SSTI in profile name field via simple payload rendering in emails
2. Demonstrated access to Python object model through advanced Jinja2 expressions
3. Highlighted path to RCE on email processing server, limited only by input constraints

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T12:00:00Z*
