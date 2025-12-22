---
tags:
  - xss
  - injection
  - shopify
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:52:21.011Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: b352a769-0b3b-456e-822a-bf5bbdde8e45
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Inject-Malicious-Payload-into-Store-Contact-Email

## Summary

This procedure injects a stored XSS payload into the Shopify store's contact email field via the admin interface, exploiting lack of input sanitization to store malicious HTML/JS that later renders on public pages.

## Description

In a Shopify store with admin access, navigate to the general settings and modify the contact email field with a payload that breaks out of the expected email format using HTML attributes and event handlers. The payload leverages an img tag with onerror to execute JS upon rendering. This sets up persistence for the XSS when the email is displayed publicly on apps.shopify.com shop profiles after propagation. Prerequisites include valid admin credentials; outcomes include stored malicious content ready for victim-side execution, potentially leading to session theft.

## Requirements

1. Admin access to a Shopify store (*.myshopify.com/admin)
2. Web browser for UI interaction
3. Knowledge of XSS payload crafting

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization for email fields (e.g., allow only RFC-compliant emails)
- Use Content Security Policy (CSP) to block inline JS execution on public pages
- Monitor admin changes to contact fields via audit logs
- Scan for anomalous HTML in stored data

## Objectives

1. Store unsanitized JS payload in backend
2. Ensure payload survives validation during save
3. Prepare for public rendering without escaping

## Instructions

### Step 1: Access Admin Settings

**Context**: Log in and reach the general settings page to locate the contact email field.

Navigate to `https://<store>.myshopify.com/admin/settings/general` and find the 'Store contact email' input.

### Step 2: Craft and Inject Payload

**Context**: Enter a payload that closes the email context and injects an executable img tag.

Enter the following payload in the field:

```
luc1d"><img/src="x"onerror=alert(document.domain)>@wearehackerone.com
```

Save the settings. This breaks out with ">, injects <img src="x" onerror=alert(document.domain)>, and appends a valid domain to mimic an email.

**Expected Output**: Settings save successfully; payload stored in the field.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]
- [[shopify]]
