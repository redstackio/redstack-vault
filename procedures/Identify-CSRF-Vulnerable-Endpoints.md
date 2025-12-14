---
tags:
  - csrf
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:15.950Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 63cf5e3a-02b6-4599-9a61-3c8abbc6724a
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-CSRF-Vulnerable-Endpoints

## Summary

This procedure involves inspecting web application endpoints to detect Cross-Site Request Forgery (CSRF) vulnerabilities, specifically focusing on state-changing POST requests lacking protective tokens or validations, as seen in the TopCoder wiki's user preference editing features.

## Description

In a CSRF attack, attackers exploit the trust a web application has in a user's browser by forging requests from malicious sites. This procedure targets applications like the TopCoder wiki, where endpoints such as https://apps.topcoder.com/wiki/users/editmypreferences.action and https://apps.topcoder.com/wiki/users/editemailpreferences.action process POST requests without CSRF tokens, origin validation, or other anti-CSRF measures. By examining network traffic and form structures, attackers confirm the vulnerability, enabling subsequent exploitation to alter user settings like general preferences or email notifications without consent. Prerequisites include basic web development knowledge and access to browser tools; the target must be a public-facing web app with user authentication.

## Requirements

1. Web browser with developer tools (e.g., Chrome or Firefox)
2. Access to the target application (publicly accessible wiki or similar)
3. Authentication to the application to simulate legitimate requests
4. Knowledge of HTTP request structures and common CSRF defenses

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing forms and validate them server-side
- Enforce origin and referrer header checks for POST requests
- Use SameSite=Strict or Lax cookies to prevent cross-site request inclusion
- Monitor for anomalous preference changes in user audit logs

## Objectives

1. Confirm absence of CSRF protections on targeted endpoints
2. Document request payloads for replication in PoC attacks
3. Assess potential impact on authenticated user actions

## Instructions

### Step 1: Authenticate to the Target Application

**Context**: Gain a legitimate session to observe real request flows during preference editing.

Log in using the application's authentication endpoints:

- Navigate to https://apps.topcoder.com/wiki/login.action or https://accounts.topcoder.com/member
- Enter valid credentials to establish an authenticated session.

> This step ensures cookies and session tokens are set, allowing inspection of protected requests.

### Step 2: Inspect Preference Editing Endpoints

**Context**: Use developer tools to capture and analyze HTTP requests for CSRF indicators.

Open developer tools (F12), go to the Network tab, and attempt to edit preferences:

- Visit https://apps.topcoder.com/wiki/users/editmypreferences.action
- Fill out and submit the general preferences form
- Repeat for email preferences at https://apps.topcoder.com/wiki/users/editemailpreferences.action

Examine the POST requests:

- Check form HTML for hidden CSRF token fields (e.g., <input type="hidden" name="_token" value="...">)
- Inspect request headers for custom tokens or validation (e.g., X-CSRF-Token)
- Verify if the server enforces Origin or Referer headers

> Expected output: Requests succeed without token validation, confirming vulnerability. No errors on missing tokens indicate lack of protection.

### Step 3: Validate Forgery Feasibility

**Context**: Test if requests can be replicated from a different origin.

Copy the POST payload (e.g., form data like username, preferences) and simulate in a tool like Postman or curl from a non-origin domain.

> Success if the request processes without origin checks, altering preferences.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web-recon]]
