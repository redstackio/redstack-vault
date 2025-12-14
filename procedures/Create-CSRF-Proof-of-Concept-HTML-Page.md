---
tags:
  - csrf
  - poc
  - html-form
type: procedure
tools: []
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
updated_at: '2025-12-14T17:27:42.309Z'
skill_level: low
impact_level: high
detection_risk: low
sub_techniques: []
id: 1d8cd4d3-0a47-4fa4-bd2c-29ac5a851e57
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-CSRF-Proof-of-Concept-HTML-Page

## Summary

This procedure creates a simple HTML page with an auto-submitting form to exploit CSRF vulnerabilities in web applications like UPchieve, targeting authenticated POST endpoints to perform unauthorized actions such as modifying user data or submitting forms on behalf of the victim.

## Description

In the UPchieve application, multiple POST endpoints (e.g., /api/calendar/save, /api/training/score) lack CSRF token validation and use session cookies without the SameSite attribute. This allows browsers to include the cookie in cross-origin requests. The procedure involves crafting an HTML form with hidden inputs matching the endpoint's expected parameters and JavaScript to submit it upon page load. The attack relies on the victim visiting the page while authenticated, leveraging the browser's credential auto-inclusion. Impacts include arbitrary actions like setting availability, submitting quizzes, sending password resets, or updating volunteer information, though CORS blocks response reading.

## Requirements

1. Knowledge of vulnerable endpoint URL and required POST parameters (e.g., from app analysis or documentation)
2. Text editor to write HTML
3. Understanding of form-urlencoded data structure

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing POST endpoints
- Set session cookies with SameSite=Strict or Lax attribute
- Monitor for anomalous actions like unexpected quiz submissions or resets from user accounts
- Use Content-Security-Policy to restrict form actions

## Objectives

1. Forge an authenticated request to a vulnerable endpoint
2. Perform unauthorized user actions silently
3. Demonstrate impact without direct session access

## Instructions

### Step 1: Identify Target Endpoint and Parameters

**Context**: Analyze the application to find vulnerable POST endpoints and their expected form data. For UPchieve, examples include /api/calendar/save for availability (e.g., availability[Sunday][12a]=true) or /auth/reset/send for email resets.

No command required; review app source or use browser dev tools to inspect legitimate forms.

### Step 2: Construct the HTML Form

**Context**: Build the HTML with a hidden form targeting the endpoint and JavaScript for auto-submission to ensure execution on page load.

Create the file csrf_poc.html:

```html
<!DOCTYPE html>
<html>
<head><title>CSRF PoC</title></head>
<body>
  <form id="csrf-form" action="https://hackers.upchieve.org/api/calendar/save" method="POST">
    <input type="hidden" name="availability[Sunday][12a]" value="true">
    <!-- Add more hidden inputs for other parameters -->
  </form>
  <script>
    document.getElementById('csrf-form').submit();
  </script>
</body>
</html>
```

> This submits the form as application/x-www-form-urlencoded, mimicking legitimate requests. Adapt action and inputs for other endpoints, e.g., for quiz: action="/api/training/score", inputs for quiz_id and answers.

### Step 3: Test the PoC Locally

**Context**: Verify the form submits correctly without errors.

Open the HTML in a browser (while logged into the target app in another tab) and check network tab for the POST request and server response (e.g., {"msg":"Schedule saved"}).

**Expected Output**: Successful POST with victim's session cookie included.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[poc]]
