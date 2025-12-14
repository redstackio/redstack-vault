---
id: proc-uuid-1
name: Inject-Malicious-Liquid-Code-into-Notification-Template
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:24.278Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - liquid-injection
  - ssti
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Inject Malicious Liquid Code into Notification Template

## Summary

This procedure involves editing Shopify's notification email templates to insert malicious Liquid code that calls unintended public Ruby methods on objects like OrderDrop, setting up for code execution and information disclosure.

## Description

In Shopify's admin interface, notification templates use the Liquid templating system, which exposes Ruby objects without proper method whitelisting. An attacker with shop admin access can inject Liquid expressions to invoke methods like `methods`, `systemu`, `class`, and `to_yaml` on drops such as OrderDrop or DraftOrderDrop. This is a server-side template injection (SSTI) variant, discovered by exploring Liquid interfaces. The attack requires admin privileges but leads to limited RCE without arguments, primarily for reading sensitive object properties and bypassing access controls.

## Requirements

1. Valid Shopify shop administrator credentials
2. Access to the admin dashboard (Settings > Notifications)
3. Web browser for template editing

## Defense

Defensive measures and detection strategies:

- Implement strict method whitelisting in Liquid rendering to block arbitrary public method calls
- Monitor template edits for suspicious Liquid code (e.g., `to_yaml` or `methods`)
- Enable audit logs for admin actions on notifications and orders

## Objectives

1. Insert code to expose Ruby object methods and properties
2. Prepare template for rendering to achieve info disclosure
3. Enable exfiltration of sensitive data like hashed passwords

## Instructions

### Step 1: Access Notification Settings

**Context**: Navigate to the editable Liquid templates in the Shopify admin.

No command required; use the web UI: Log in to Shopify admin, go to Settings > Notifications, and select the "New Order" template.

> This opens the template editor with a textbox for the email body.

### Step 2: Insert Malicious Liquid Code

**Context**: Append Liquid expressions to call public Ruby methods on the order object.

No command required; in the template textbox, add:

```liquid
{{ methods | json }} {{ systemu }} {{ class }} {{ to_yaml }}
```

> Save the template. This code will execute methods like `to_yaml` to dump object data when rendered.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[JavaScript]] JavaScript (Liquid templating as scripting interface)

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- liquid-injection
- ssti
- shopify
