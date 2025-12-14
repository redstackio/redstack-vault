---
tags:
  - xss
  - payload-injection
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
updated_at: '2025-12-14T03:47:18.403Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 50abf2fe-721b-46f5-a69a-d2291846357d
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Client-with-XSS-Payload

## Summary

This procedure covers creating a new client in the admin panel and injecting a stored XSS payload into the Custom Attribute 1 field of the Ubiquiti UCRM application, exploiting lack of input sanitization.

## Description

The attack leverages the client creation form to store malicious JavaScript in a custom field, which is later rendered without proper encoding on the client details page. The payload used is `"><IMG src=x onerror=prompt(1);>"">><marquee><img src=x onerror=confirm(3)></marquee>"/`, breaking out of any attribute context and executing on page load or interaction.

## Requirements

1. Active admin session in the application.
2. Access to the client creation form.
3. Knowledge of XSS payloads that evade basic filters.

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with HTML entity encoding (e.g., &lt; for <).
- Use Content Security Policy (CSP) to restrict inline JavaScript execution.
- Validate and escape custom attribute values before database storage and rendering.

## Objectives

1. Inject and store executable JavaScript in the database.
2. Ensure payload survives form submission without alteration.
3. Set up for persistent execution on victim views.

## Instructions

### Step 1: Navigate to Client Creation

**Context**: Access the form for adding new clients.

In the admin dashboard, go to Clients > Add New Client.

> Form loads with fields including Custom Attributes. Expected output: Empty form ready for input.

### Step 2: Inject Payload

**Context**: Enter the malicious payload in the vulnerable field.

In Custom Attribute 1, input: `"><IMG src=x onerror=prompt(1);>"">><marquee><img src=x onerror=confirm(3)></marquee>"/`

> Payload placed in text input. Expected output: No immediate error; field accepts HTML/JS.

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
- [[payload-injection]]
