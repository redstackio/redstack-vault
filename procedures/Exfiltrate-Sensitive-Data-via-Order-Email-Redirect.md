---
id: proc-uuid-3
name: Exfiltrate-Sensitive-Data-via-Order-Email-Redirect
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:24.257Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Credentials In Files]]'
sub_techniques: []
tags:
  - exfiltration
  - credentials
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---

# Exfiltrate Sensitive Data via Order Email Redirect

## Summary

This procedure manipulates an existing order to redirect its confirmation email to an attacker-controlled address, triggering the malicious template to render and deliver sensitive data exfiltration via email.

## Description

With the template injected, an attacker prepares a victim-touched order (e.g., one edited by the shop owner), changes the associated customer email to their own, and resends the confirmation. This causes Shopify to render the template with the `{{ to_yaml }}` code, embedding a YAML dump of the order object—including hashed passwords and other properties—directly into the email body sent to the attacker. This bypasses direct access controls, achieving remote information disclosure.

## Requirements

1. Admin access to orders and customers
2. An existing order interacted with by the target victim
3. Attacker-controlled email address
4. Malicious template already in place

## Defense

Defensive measures and detection strategies:

- Restrict email editing to verified customers only
- Audit resend actions and template renders for data leaks
- Sanitize email content before sending to prevent embedded sensitive dumps

## Objectives

1. Redirect email delivery to attacker
2. Trigger template rendering for data inclusion
3. Receive exfiltrated sensitive information like hashed credentials

## Instructions

### Step 1: Prepare Victim Order

**Context**: Select an order last touched by the desired victim to associate disclosed data.

No command required; in Shopify admin, go to Orders, select a relevant order (e.g., one edited by shop owner).

> Ensure the order qualifies for notification resend.

### Step 2: Redirect Customer Email

**Context**: Change the email to attacker-controlled for receipt of the rendered template.

No command required; from the order, navigate to the customer details and update the email field to your controlled address.

> Save the changes.

### Step 3: Resend Confirmation Email

**Context**: Trigger rendering and sending of the malicious template.

No command required; in the order details, click "Resend order confirmation".

```liquid
This executes: {{ to_yaml }} in the email body
```

> The email arrives with YAML dump containing sensitive data.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Credentials In Files]] Credentials In Files (via object dumps in email)

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- exfiltration
- credentials
- shopify
