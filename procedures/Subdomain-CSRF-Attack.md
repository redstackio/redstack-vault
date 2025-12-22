---
type: procedure
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - '[[techniques/Drive-by Compromise|T1189 - Drive-by Compromise]]'
  - '[[techniques/Steal Web Session Cookie|T1539 - Steal Web Session Cookie]]'
sub_techniques: []
tags:
  - csrf
  - subdomain-takeover
  - referer-bypass
  - cross-site-request-forgery
commands:
  - '[[commands/curl-send-csrf-request-with-custom-referer]]'
tools:
  - '[[tools/Burp-Suite]]'
platforms:
  - web
verified: true
validated: true
---

# Subdomain-CSRF-Attack

## Summary

The Subdomain CSRF Attack exploits a misconfigured or taken-over subdomain to perform a Cross-Site Request Forgery (CSRF) on the target domain. By hosting a malicious page on the attacker's controlled subdomain (e.g., vulnerable.target.com), the attacker can craft requests that appear to originate from a trusted subdomain, bypassing strict referer header validation. This allows unauthorized actions, such as changing user settings or stealing session data, on behalf of an authenticated victim who visits the malicious page.

## Description

In this attack, the attacker first gains control of a subdomain through takeover (e.g., unused DNS records pointing to abandoned services like GitHub Pages or Heroku). Once controlled, a malicious HTML page with an auto-submitting form is hosted there. When a victim (already authenticated to the target domain) is lured to visit this page—via phishing or drive-by—the form submits a forged request to the target domain's sensitive endpoint. The referer header, set to the subdomain URL, tricks the server into accepting the request if validation only checks for the parent domain rather than exact matches or other protections like tokens. This technique evades CSRF protections and can lead to account takeover, data modification, or session hijacking in web applications.

## Requirements

1. Control over a subdomain of the target domain (via takeover or misconfiguration).
2. Knowledge of the target's sensitive endpoints and required form parameters (e.g., via reconnaissance).
3. Victim authentication to the target site (e.g., active session cookie).
4. Ability to host HTML content on the subdomain and lure victims to visit it.
5. Tools for header manipulation if simulating without browser (e.g., curl or Burp Suite).

## Defense

- Implement strict referer policy validation, checking for exact domain matches or using CSRF tokens.
- Monitor and audit DNS records to prevent subdomain takeovers; use services like DNS monitoring tools.
- Enforce same-site cookie attributes (Lax/Strict) and HTTP-only flags to limit cross-origin requests.
- Deploy Content Security Policy (CSP) to restrict form submissions and script execution.
- Educate users on phishing and use multi-factor authentication (MFA) for sensitive actions.

## Objectives

1. Execute unauthorized actions (e.g., password reset, email change) on the victim's behalf.
2. Bypass referer-based CSRF protections using subdomain spoofing.
3. Achieve account takeover or data exfiltration from the target application.

## Instructions

### Step 1: Prepare Malicious CSRF Payload

**Context**: Create an HTML page with an auto-submitting form that targets a sensitive endpoint on the main domain. This payload will be hosted on the controlled subdomain to set the referer appropriately.

Use the [[codes/HTML-CSRF-Form-for-Subdomain-Attack]] code snippet as the basis.

Save it as csrf.html and customize the form action and hidden fields based on the target's endpoint (e.g., /change-email).

**Expected Output**: A functional HTML file ready for hosting.

### Step 2: Host Payload on Controlled Subdomain

**Context**: Upload the crafted HTML to the taken-over subdomain to ensure requests from it appear trusted. This step assumes subdomain control is already achieved (e.g., via DNS reconfiguration).

Host the file at a path like https://vulnerable.target.com/csrf.html using the subdomain's hosting service (e.g., AWS S3, GitHub Pages).

Verify accessibility by visiting the URL in a browser; confirm the form auto-submits without errors.

**Expected Output**: Page loads and immediately redirects/submits to the target endpoint.

### Step 3: Simulate or Execute the Forged Request

**Context**: Send the CSRF request with the subdomain as the referer to bypass validation. This can be done via browser (luring victim) or simulated with tools for testing.

For simulation, use [[commands/curl-send-csrf-request-with-custom-referer]] to mimic the request:

**Command** ([[commands/curl-send-csrf-request-with-custom-referer]]):
```bash
curl -X POST -H "Referer: $_MALICIOUS_SUBDOMAIN/csrf.html" -d "$_FORM_DATA" $_TARGET_ENDPOINT
```

> This command sends a POST with custom referer. Include victim's session cookie via -b "session=abc123" if testing authenticated flow. Observe if the server processes the request without rejection.

For real execution, direct the victim to the malicious URL using phishing; use [[tools/Burp-Suite]] to intercept and verify the referer in transit.

**Expected Output**: Server response indicating successful action (e.g., 200 OK with confirmation message) or account changes verifiable in the application.

### Step 4: Verify Attack Success

**Context**: Confirm the unauthorized action was performed by checking the victim's account or application logs.

Log in as the victim (or monitor if possible) to see changes (e.g., updated email). If using Burp, review request/response for acceptance.

**Expected Output**: Evidence of executed action, such as modified user data or session hijack indicators.
