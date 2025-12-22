---
type: procedure
description: >-
  Perform a Cross-Site Request Forgery (CSRF) attack by creating and hosting a
  malicious web page with a hidden form that bypasses basic Referer header
  validation to execute unauthorized actions on a target web application.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Drive-by Compromise|T1189 - Drive-by Compromise]]'
  - '[[techniques/JavaScript|T1059.007 - JavaScript]]'
sub_techniques: []
tags:
  - csrf
  - referer-bypass
  - cross-site-request-forgery
  - web-attack
commands:
  - '[[commands/host-simple-web-server]]'
platforms:
  - web
tools: []
validated: true
---

# CSRF-Attack-Bypassing-Referer-Validation

## Summary

This procedure demonstrates how to execute a CSRF attack by crafting a malicious HTML page with a hidden form that automatically submits a request to a vulnerable web application. The attack bypasses simplistic Referer header validation by hosting the page on a domain or using techniques that make the Referer appear legitimate (e.g., via a trusted third-party site or weak regex checks on the target). When a logged-in user visits the page, the form submits without their knowledge, performing actions like password changes or fund transfers.

## Description

Cross-Site Request Forgery (CSRF) exploits the trust a web application has in a user's browser by tricking the user into submitting a forged request. In this variant, the attacker bypasses Referer header checks, which are meant to ensure requests originate from the legitimate site. Weak implementations (e.g., checking if Referer contains the domain substring) can be evaded by hosting the malicious page on a subdomain, using URL shorteners, or leveraging services like Google Translate that alter the Referer. The target must lack CSRF tokens and rely solely on Referer validation. This is effective against financial apps, admin panels, or any state-changing POST endpoint. Success requires the victim to be authenticated in the target app during the visit.

## Requirements

1. Knowledge of the target's vulnerable endpoint (e.g., POST /transfer with parameters like amount and recipient).
2. Ability to host a web page (local server or remote hosting service).
3. Victim must be a logged-in user of the target application.
4. No CSRF tokens on the target form; only Referer validation present.
5. Basic web development knowledge for crafting HTML/JS.

## Defense

- Implement CSRF tokens (synchronizer pattern) on all state-changing requests.
- Enforce strict Referer and Origin header validation (exact domain match, not substring).
- Use Content-Security-Policy (CSP) headers to restrict cross-site submissions.
- Educate users on phishing links and enable browser protections like SameSite cookies.
- Monitor for anomalous requests from unexpected Referers.

## Objectives

1. Trick an authenticated user into executing an unauthorized action on the target web app.
2. Bypass Referer validation to make the forged request appear legitimate.
3. Achieve actions like data modification or privilege changes without direct access.

## Instructions

### Step 1: Create the Malicious HTML Page

**Context**: Craft a simple HTML page containing a hidden form that targets the vulnerable endpoint. Use auto-submission via JavaScript to trigger the POST request immediately upon page load. Include placeholders for target-specific parameters. To bypass Referer validation, host this on a domain that partially matches the target's (e.g., if target is bank.com, host on evil-bank.com) or use a proxy service that spoofs the header—note that direct browser spoofing of Referer is not possible due to security restrictions, so rely on validation weaknesses.

**Code** ([[codes/CSRF-Hidden-Form-HTML]]):

Embed the code here or save it as index.html, replacing placeholders with actual values (e.g., target URL and form data).

> This step verifies the form structure. Open the HTML in a browser to ensure it auto-submits (test against a local mock server first). Expected: Form data posts to the target without user interaction.

### Step 2: Host the Malicious Page

**Context**: Serve the HTML page from a web server accessible to the victim. Use a simple Python HTTP server for quick local testing or a public hosting service (e.g., GitHub Pages, but avoid for malicious use in real scenarios). Ensure the hosting domain aids in Referer bypass if needed.

**Command** ([[commands/host-simple-web-server]]):
```bash
python3 -m http.server $_PORT
```

> Run this in the directory containing index.html. Access the page at http://your-ip:$_PORT. Expected: Server starts, and visiting the URL triggers the form submission if victim is logged in to target.

### Step 3: Distribute the Page to the Victim

**Context**: Use social engineering to lure the victim to the hosted page, such as embedding the link in an email, forum post, or malicious ad. Ensure the victim is authenticated in the target app (e.g., send after they log in). No technical command here—rely on phishing techniques.

> Send a link like "Check this urgent update: http://your-server.com". Expected: Victim visits while logged in, triggering the CSRF.

### Step 4: Verify the Attack

**Context**: Monitor the target application or use a proxy like Burp Suite to confirm the forged request was processed. Check for the unauthorized action (e.g., transaction history).

> Success if the action completes without errors, and Referer log on target shows the malicious domain (bypassed due to weak check).
