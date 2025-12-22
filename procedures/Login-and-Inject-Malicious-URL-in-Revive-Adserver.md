---
tags:
  - xss
  - injection
  - revive-adserver
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:41.649Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 443b2466-0ed9-407e-9dac-7b6778e777f2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Login-and-Inject-Malicious-URL-in-Revive-Adserver

## Summary

This procedure covers logging in as a standard user to the Revive Adserver and injecting a malicious payload into the Website URL field in the inventory management section, exploiting lack of input sanitization to store XSS and open redirect payloads.

## Description

In Revive Adserver, the Website URL field in Inventory > Website > Website Properties does not properly sanitize inputs, allowing storage of HTML and JavaScript attributes. An attacker with user access can inject a payload that persists in the database and executes when rendered in admin previews, leading to arbitrary code execution or redirects. This targets PHP-based web applications vulnerable to stored XSS.

## Requirements

1. Valid standard user credentials for Revive Adserver
2. Web browser access to the application
3. Knowledge of the target instance URL

## Defense

Defensive measures and detection strategies:

- Implement input validation and sanitization for URL fields using whitelists
- Output encode all user inputs when rendering in HTML contexts
- Use Content Security Policy (CSP) to block inline scripts and redirects
- Monitor for anomalous redirects or JavaScript execution in logs

## Objectives

1. Gain initial access to inject persistent payload
2. Store malicious URL without detection
3. Set up for admin-level exploitation

## Instructions

### Step 1: Authenticate as User

**Context**: Log in to access the inventory interface.

Navigate to the Revive Adserver login page and enter user credentials.

> Successful login grants access to the dashboard.

### Step 2: Access Website Properties

**Context**: Reach the vulnerable form.

From the dashboard, select Inventory > Website > Website Properties.

> The form loads with the URL input field.

### Step 3: Inject Payload and Save

**Context**: Enter and persist the malicious input.

In the URL field, input: `http://Test"><img src=x onclick=window.location="http://google.com">` and click Save Changes.

> The payload is stored without sanitization, ready for later rendering.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]
- [[revive-adserver]]
