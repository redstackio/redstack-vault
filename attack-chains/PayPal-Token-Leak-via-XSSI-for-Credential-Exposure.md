---
tags:
  - xssi
  - token-leak
  - credential-exposure
  - recaptcha
  - paypal
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Discover-Token-Leak-in-reCAPTCHA-JS]]'
  - '[[procedures/Exploit-XSSI-to-Extract-Token]]'
  - '[[procedures/Induce-Victim-Login-via-Malicious-Link]]'
  - '[[procedures/Replay-Authentication-with-Exposed-Token]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unsecured Credentials]]'
description: >-
  Exploitation of token leak in PayPal's reCAPTCHA JavaScript file via XSSI to
  expose and replay security challenges, leading to credential theft.
skill_level: intermediate
impact_level: high
id: c221bedb-70f3-45de-a25a-a35f271533a8
created_at: '2025-12-11T03:47:56.769Z'
updated_at: '2025-12-11T03:47:56.769Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1552]]'
---
# PayPal Token Leak via XSSI for Credential Exposure

## Overview

This attack chain exploits a vulnerability in PayPal's security challenge flow where sensitive tokens are leaked in a JavaScript file used for reCAPTCHA. An attacker uses cross-site script inclusion (XSSI) from a malicious site to extract these tokens. By tricking a victim into following a login link and entering credentials, the attacker can complete the CAPTCHA challenge, replay the authentication request, and retrieve the victim's PayPal email and plain text password. The impact includes potential credential exposure, which was mitigated by PayPal adding controls to prevent token reuse.

## Attack Flow Visualization

```mermaid
graph LR
    A[Discover Token Leak] --> B[Exploit XSSI]
    B --> C[Induce Victim Login]
    C --> D[Replay Authentication]
    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None specifically required beyond standard web development tools for setting up a malicious site.

### Target Environment

- Web-based platform with reCAPTCHA integration.
- Services: reCAPTCHA.
- Tech Stack: JavaScript.

### Initial Access Requirements

- Ability to host a malicious website.
- Victim must be tricked into visiting the malicious site and following a PayPal login link.

## Detailed Attack Procedures

## Step 1: Identify Token Leakage - [[procedures/Discover-Token-Leak-in-reCAPTCHA-JS]]

### Objective

Identify the leakage of sensitive tokens in the JavaScript file used by reCAPTCHA.

### Instructions

Inspect the publicly accessible JavaScript file from PayPal's reCAPTCHA implementation to detect exposed sensitive tokens that can be included cross-site.

No specific commands are used; this step involves manual or automated web inspection (e.g., viewing source in browser developer tools).

### Validation

Confirm the JS file contains unique tokens usable in POST requests for CAPTCHA solving.

## Step 2: Exploit XSSI to Expose Token - [[procedures/Exploit-XSSI-to-Extract-Token]]

### Objective

Use cross-site script inclusion from a malicious site to extract the security challenge token.

### Instructions

Set up a malicious webpage that includes the vulnerable PayPal JS file via a script tag, then parse the exposed tokens using JavaScript on the attacker's site.

Example HTML/JS snippet on malicious site:

```html
<script src="https://paypal-vulnerable-js-file-url"></script>
<script>
// Parse and extract token from loaded JS
console.log(window.exposedToken); // Assuming token is in global scope
</script>
```

### Validation

Verify the token is successfully extracted and unique for the security challenge.

## Step 3: Trick Victim into Logging In - [[procedures/Induce-Victim-Login-via-Malicious-Link]]

### Objective

Have the victim follow a login link from the malicious site and enter their credentials, triggering the security challenge.

### Instructions

Embed a link to PayPal's login page on the malicious site, potentially using social engineering to entice the victim to click and authenticate.

No specific commands; this is a phishing-like step where the victim encounters the CAPTCHA after entering credentials.

### Validation

Confirm the victim has attempted login and the security challenge is presented.

## Step 4: Complete Challenge and Replay - [[procedures/Replay-Authentication-with-Exposed-Token]]

### Objective

Use the exposed token to complete the CAPTCHA challenge and replay the authentication request to expose credentials.

### Instructions

Replay the victim's authentication POST request using the extracted token to solve the CAPTCHA, retrieving the email and plain text password.

Example using a tool like curl for replay (inferred for demonstration):

```bash
curl -X POST https://paypal-security-challenge-endpoint -d 'token=exposed_token&other_params=victim_data'
```

### Validation

Successfully retrieve the victim's PayPal email and plain text password without further interaction.

## Attack Chain Summary

### Key Achievements

1. Exposed sensitive tokens via XSSI.

2. Tricked victim into initiating authentication.

3. Replayed request to steal credentials.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Unsecured Credentials]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]
