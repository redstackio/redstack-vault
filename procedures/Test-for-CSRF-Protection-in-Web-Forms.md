---
tags:
  - csrf
  - web-testing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: informational
detection_risk: low
sub_techniques: []
id: 89ef2f50-05b6-4d4f-a393-51d35ec889f1
created_at: '2025-12-14T17:27:03.053Z'
updated_at: '2025-12-14T17:27:03.053Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-for-CSRF-Protection-in-Web-Forms

## Summary

This procedure tests web forms for Cross-Site Request Forgery (CSRF) vulnerabilities by inspecting token validation and attempting forged requests, as seen in the Hiro platform's email signup form where no protections were enforced.

## Description

CSRF vulnerabilities occur when a web application fails to validate tokens or origins for state-changing requests, allowing attackers to trick users into submitting malicious forms via external sites or links. In this case, the Hiro email signup form lacked CSRF tokens, permitting clickable links to auto-submit signups, though without access to sensitive data or authenticated state changes, the risk was minimal. This procedure outlines manual testing using browser tools to identify such issues in public-facing forms.

## Requirements

1. Access to the target web application (e.g., Hiro platform signup page)
2. Browser with developer tools (e.g., Chrome DevTools)
3. Ability to host or share simple HTML test pages
4. Basic understanding of HTTP requests and forms

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all forms and validate them server-side
- Use same-site cookies (Lax or Strict) to prevent cross-origin requests
- Monitor for anomalous form submissions from unexpected referers

## Objectives

1. Confirm absence of CSRF protections in target forms
2. Demonstrate feasibility of forged requests
3. Evaluate potential impact on user actions

## Instructions

### Step 1: Inspect Form Implementation

**Context**: Examine the target's email signup form to check for CSRF token fields or headers in the HTML and submission requests.

Open the signup page in a browser, right-click the form, and select "Inspect Element." Look for hidden input fields like `<input type="hidden" name="_csrf" value="...">` or custom tokens. Submit the form legitimately and monitor the Network tab in DevTools for token inclusion in POST requests.

If no token is present, note the endpoint URL (e.g., `/signup`) and required fields (e.g., `email`).

### Step 2: Craft and Test Forged Request

**Context**: Create a malicious HTML page to simulate a cross-site request, testing if the server accepts submissions without tokens.

Create an HTML file with an auto-submitting form targeting the endpoint:

```html
<!DOCTYPE html>
<html>
<head><title>CSRF Test</title></head>
<body>
    <p>Click to test CSRF:</p>
    <a href="#" onclick="document.getElementById('testform').submit();">Trigger Signup</a>
    <form id="testform" action="https://hiro-platform.com/signup" method="POST">
        <input type="hidden" name="email" value="victim@example.com">
    </form>
</body>
</html>

```

Host this file locally (e.g., via Python's `http.server`) or upload to a free hosting service, then open the link in a browser while logged into the target site (if applicable). Check if the signup processes without errors.

**Expected Output**: Server accepts the request and creates the email signup entry, confirming the vulnerability.

### Step 3: Assess Impact

**Context**: Evaluate if the vulnerability leads to meaningful exploitation.

Review the form's actions: Does it change state for authenticated users or expose data? In the Hiro case, it only allows benign email signups, so impact is low.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web-vulnerability]]
