---
id: proc-uuid-2
tags:
  - csrf
  - poc
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:50.269Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft CSRF Proof-of-Concept HTML

## Summary

This procedure details creating a malicious HTML page that exploits CSRF vulnerabilities by auto-submitting a form to a target endpoint, specifically tailored for the Firefox accounts password reset to use the attacker's email and capture victim-submitted details.

## Description

Using Burp Suite's CSRF PoC generator, the attacker crafts an HTML form targeting https://accounts.firefox.com/reset_password with hidden inputs for email (attacker's address), reset_password_confirm=false, email_to_hash_with='', and UTM parameters (utm_medium=email, utm_campaign=fx-password-changed-success, utm_content=fx-reset-password). JavaScript is added to auto-submit on load, enabling cross-origin forgery when a victim visits the page. This requires hosting capabilities and results in the victim's browser sending the request, disclosing their info in the reset email.

## Requirements

1. Burp Suite Professional for PoC generation
2. Knowledge of HTML and JavaScript for form submission
3. Attacker's email registered on the target service

## Defense

Defensive measures and detection strategies:

- Validate request origins and include unique CSRF tokens in forms
- Log and alert on reset requests with mismatched referer headers
- Educate users on phishing link avoidance

## Objectives

1. Generate functional CSRF payload for the endpoint
2. Ensure auto-submission works cross-origin
3. Test locally to confirm reset email delivery

## Instructions

### Step 1: Generate PoC with Burp Suite

**Context**: Intercept a legitimate reset request to base the PoC on real parameters.

In Burp Suite, proxy a reset request, right-click the POST to /reset_password, and select "Engagement tools > Generate CSRF PoC".

**Expected Output**: Burp outputs HTML with form and auto-submit script.

### Step 2: Customize Hidden Fields

**Context**: Modify the generated HTML to use attacker's email and add UTM params.

Edit the HTML: Set <input type="hidden" name="email" value="attacker@example.com">, add <input type="hidden" name="reset_password_confirm" value="false">, <input type="hidden" name="email_to_hash_with" value="">, <input type="hidden" name="utm_medium" value="email">, etc.

**Expected Output**: Updated HTML ready for hosting.

### Step 3: Add Auto-Submit JavaScript

**Context**: Ensure immediate submission on page load.

Include <script>document.forms[0].submit();</script> at the end of the body.

**Expected Output**: Page loads and submits form instantly; test by opening in browser to receive reset email.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[poc]]
- [[web]]
