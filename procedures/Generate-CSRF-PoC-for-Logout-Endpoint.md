---
id: proc-uuid-1
name: Generate-CSRF-PoC-for-Logout-Endpoint
tags:
  - csrf
  - poc-generation
  - web-exploit
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:27:23.217Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Generate-CSRF-PoC-for-Logout-Endpoint

## Summary

This procedure outlines creating a proof-of-concept (PoC) HTML page that exploits a CSRF vulnerability on a web application's logout endpoint by forging a POST request without CSRF token validation, allowing testers to demonstrate forced logouts.

## Description

In scenarios like the Courier app, the logout endpoint (e.g., https://www.trycourier.app/logout) lacks CSRF protection, enabling attackers to craft HTML that auto-submits a form when visited by an authenticated user. This disrupts sessions, forces re-authentication, and can target admins for denial-of-service. The procedure uses Burp Suite to generate and test the PoC, ensuring it includes auto-submission via JavaScript to mimic user interaction seamlessly.

## Requirements

1. Access to Burp Suite Professional for PoC generation.
2. Knowledge of the target logout URL and method (POST).
3. A testing environment where you can authenticate to the app.

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints, including logout.
- Use Content Security Policy (CSP) to restrict form submissions to same-origin.
- Monitor for anomalous logout requests from unexpected referers.

## Objectives

1. Generate a functional CSRF PoC that triggers logout without user intent.
2. Validate the PoC in a controlled environment.
3. Demonstrate the vulnerability's exploitability.

## Instructions

### Step 1: Intercept and Analyze Logout Request

**Context**: Use Burp Suite to capture a legitimate logout request and understand its structure.

Launch Burp Suite Proxy and configure your browser to route traffic through it. Authenticate to the target app, perform a manual logout, and intercept the request in Burp Repeater.

**Expected Output**: Captured POST request to /logout with no CSRF token visible.

### Step 2: Generate CSRF PoC HTML

**Context**: Use Burp's CSRF PoC generator to create the HTML form.

In Burp Repeater, right-click the request and select "Engagement tools > Generate CSRF PoC". Customize the HTML to include auto-submission: add <script> to submit the form on load and redirect to '/' to suppress warnings.

Example PoC structure:

```html
<html>
<body>
  <form action="https://www.trycourier.app/logout" method="POST" id="csrf-form">
    <!-- No CSRF token -->
  </form>
  <script>
    document.getElementById('csrf-form').submit();
    window.history.pushState('', '/', '/');
  </script>
</body>
</html>
```

**Expected Output**: Save the generated HTML file for hosting.

### Step 3: Test the PoC

**Context**: Verify the PoC forces logout when loaded while authenticated.

Host the HTML locally (e.g., via Python's http.server) and visit it in an authenticated browser session.

**Expected Output**: Automatic logout from the target app upon page load.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[poc]]
- [[web]]
