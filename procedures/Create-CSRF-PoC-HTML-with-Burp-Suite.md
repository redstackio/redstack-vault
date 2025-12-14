---
id: proc-uuid-1
tags:
  - csrf
  - poc-generation
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite-Professional]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:29.639Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-CSRF-PoC-HTML-with-Burp-Suite

## Summary

This procedure uses Burp Suite to capture a legitimate profile update request from the LGTM platform and convert it into a malicious HTML form for CSRF exploitation, targeting the savePublicInformation endpoint.

## Description

In the context of the LGTM platform's Account Settings, the savePublicInformation API lacks proper CSRF protection, with a nonce that is account-specific but reusable multiple times. An attacker intercepts a normal POST request using Burp Suite, modifies the payload to include malicious profile data (e.g., a phishing website), and generates an HTML file with a form that auto-submits or prompts submission. This allows exploitation against an authenticated victim by tricking them into loading the HTML in their browser. Prerequisites include access to Burp Suite and a legitimate session to capture the initial request.

## Requirements

1. Burp Suite Professional installed and configured as a browser proxy
2. Active session on LGTM platform to capture a real savePublicInformation request
3. Knowledge of target profile fields to modify (name, username, location, website, organization)

## Defense

Defensive measures and detection strategies:

- Implement unique, single-use CSRF tokens that regenerate per request or session
- Enforce same-site cookie policies (e.g., Strict or Lax) to prevent cross-origin requests
- Monitor for anomalous profile changes via audit logs and alert on rapid modifications

## Objectives

1. Generate a functional HTML PoC for CSRF exploitation
2. Include reusable nonce to enable repeated attacks
3. Prepare for delivery to victim (e.g., via email or malicious site)

## Instructions

### Step 1: Intercept Legitimate Request

**Context**: Configure Burp Suite to proxy browser traffic and trigger a profile save on LGTM to capture the POST request.

Navigate to Account Settings on https://lgtm-com.pentesting.semmle.net/, modify a profile field, and submit to intercept in Burp's Proxy > HTTP history.

**Expected Output**: Captured POST to /internal_api/v0.2/savePublicInformation with form data including nonce.

### Step 2: Modify and Generate HTML PoC

**Context**: Use Burp's Repeater or manual editing to alter form values to malicious ones, then export as HTML.

In Burp, right-click the request > Engagement tools > Generate CSRF PoC, customize inputs (e.g., website=malicious-phish.com), and save the HTML file.

**Expected Output**: HTML file with <form method="POST" action="https://lgtm-com.pentesting.semmle.net/internal_api/v0.2/savePublicInformation"> and hidden inputs like <input type="hidden" name="website" value="http://attacker.com/malware">, plus nonce and apiVersion=1.

### Step 3: Validate PoC Structure

**Context**: Review the HTML to ensure it uses existing session cookies for authentication.

Open the HTML in a text editor and confirm no additional auth is needed; the form relies on browser cookies.

**Expected Output**: Confirmed form targets correct endpoint with all required fields.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Professional]]

## Tags

- [[csrf]]
- [[poc-generation]]
