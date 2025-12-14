---
tags:
  - xss
  - stored-xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:26.157Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 96728a84-041f-46f4-9d6d-89abc8280b2a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Website-Properties

## Summary

This procedure demonstrates how to inject a stored XSS payload into the Website URL field of Revive Adserver's inventory management interface, exploiting lack of input sanitization to store malicious HTML and JavaScript for later execution.

## Description

In Revive Adserver, the Website Properties form in the inventory section allows users to edit website details, including the URL field. Due to insufficient sanitization, attackers can inject HTML tags and JavaScript, such as an img tag with an onclick redirect. This payload is stored in the database and rendered unsafely when previewed, leading to XSS execution in the viewer's browser context. The attack requires a valid user account with inventory access and targets administrators who preview affiliate tags.

## Requirements

1. Valid user credentials with access to Inventory > Websites
2. Network access to the Revive Adserver admin panel
3. Web browser for form submission

## Defense

Defensive measures and detection strategies:

- Implement input validation and sanitization for URL fields using whitelisting (e.g., validate against URL patterns)
- Output encoding when rendering stored data (e.g., HTML entity encoding for user inputs)
- Content Security Policy (CSP) to restrict inline scripts and redirects
- Monitor for anomalous redirects or JavaScript execution in logs

## Objectives

1. Store malicious payload in the Website URL field
2. Ensure payload survives storage without modification
3. Set up for subsequent XSS triggering in admin previews

## Instructions

### Step 1: Login and Navigate to Website Properties

**Context**: Authenticate and access the vulnerable form to prepare injection.

Instructions: Log in with user credentials, navigate to Inventory > Websites > Website Properties, and open an existing or new website entry for editing.

### Step 2: Enter Malicious Payload

**Context**: Craft and submit the payload to exploit the lack of sanitization.

Instructions: In the Website URL field, input `http://Test"><img src=x onerror=window.location="http://google.com">` (note: onerror can be used if onclick is filtered; adjust based on testing). Complete other form fields minimally, then submit the form.

> The payload closes any open HTML attributes/tags and injects an img element that triggers the redirect on load or interaction.

### Step 3: Verify Storage

**Context**: Confirm the payload is stored for later use.

Instructions: After saving, edit the properties again to check if the payload remains intact in the URL field.

**Expected Output**: Payload displays unchanged in the form.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[revive-adserver]]
