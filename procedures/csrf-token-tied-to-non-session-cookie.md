---
id: fa066408-fc28-4499-8a39-8179257adba9
name: CSRF Token Tied To a Non Session Cookie
type: procedure
verified: true
submitted: true
created_at: '2020-08-25T10:51:02.222275+00:00'
updated_at: '2023-05-26T18:29:53.020873+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - csrf
  - web-applications
commands: []
platforms:
  - Web
tools:
  - '[[tools/burp-suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# CSRF Token Tied To a Non Session Cookie

## Summary

This procedure exploits a CSRF vulnerability where the CSRF token is stored in a separate cookie (csrfkey) not tied to the session cookie. By injecting the attacker's csrfkey into the victim's cookie via a reflected search parameter and using a crafted HTML form, an attacker can force unauthorized actions like changing the victim's email address without proper CSRF validation.

## Description

In some web applications, the session management uses a primary session cookie for authentication, while a separate csrfkey cookie handles CSRF protection. If these are not properly linked, an attacker can manipulate the csrfkey independently. This procedure demonstrates identifying the decoupling by testing cookie behaviors in Burp Suite, injecting the csrfkey via a vulnerable search endpoint that reflects input into the Set-Cookie header, and delivering a CSRF proof-of-concept (PoC) HTML form that auto-submits using a JavaScript payload. The attack targets state-changing endpoints like email changes, leading to account takeover or data modification. It requires proxying traffic through Burp Suite and assumes the target has a reflected XSS-like vulnerability in the search function for cookie injection.

## Requirements

1. Burp Suite Professional or Community Edition with proxy and Repeater enabled.
2. Access to the target web application as an authenticated user (attacker account).
3. An incognito/private browser window for simulating victim behavior.
4. Victim's email address and basic knowledge of the target's change email endpoint.
5. Network access to the target application without restrictions.

## Defense

Defensive measures and detection strategies:

- Ensure CSRF tokens are uniquely tied to session IDs and regenerate on each request.
- Implement strict cookie attributes (HttpOnly, Secure, SameSite=Strict) for both session and CSRF cookies.
- Sanitize and validate all reflected inputs, especially in headers like Set-Cookie.
- Monitor for anomalous cookie modifications and unauthorized state changes via web application firewall (WAF) rules.
- Enable comprehensive logging of authentication and state-changing requests to detect token mismatches.

## Objectives

1. Confirm the CSRF token is decoupled from the session cookie.
2. Inject the attacker's csrfkey into the victim's browser via reflected search input.
3. Deliver and execute a CSRF PoC to perform unauthorized actions on the victim's account.
4. Achieve account modification, such as changing the victim's email to the attacker's.

## Instructions

### Step 1: Identify and Intercept the Change Email Request

**Context**: Proxy browser traffic through Burp Suite to capture the change email request, which is a state-changing POST endpoint vulnerable to CSRF.

Use Burp Suite proxy to intercept requests from the browser.

Navigate to the change email functionality and submit a request to change the email. Forward the intercepted request to the Repeater tab for analysis.

**Expected Output**: Captured POST request to /changemail or similar, including session cookie and csrf token in the body.

### Step 2: Verify CSRF Token Decoupling

**Context**: Test cookie behaviors to confirm the csrfkey is independent of the session cookie, allowing substitution without session invalidation.

In Burp Repeater, modify the session cookie value and resend the request.

Observe the response: It should log you out (session invalidation).

Then, modify only the csrfkey cookie value and resend.

**Expected Output**: Response indicating "invalid CSRF token" without session logout, confirming decoupling.

### Step 3: Capture Victim's Change Email Request in Incognito

**Context**: Simulate the victim's session in an incognito window to obtain a legitimate request structure, including the victim's csrf token.

Open an incognito window, log in as the victim (or simulate unauthenticated if applicable), and navigate to the change email page.

With Burp intercept enabled, submit the change email request and forward to Repeater.

**Expected Output**: Intercepted POST request with victim's session cookie and csrf token.

### Step 4: Substitute CSRF Key and Token

**Context**: Swap the csrfkey from the attacker's cookie into the victim's request to bypass validation, proving the vulnerability.

In Burp Repeater, replace the victim's csrfkey cookie with the attacker's csrfkey.

Also replace the csrf token in the request body with the attacker's token.

Resend the request.

**Expected Output**: Successful response (e.g., 200 OK) confirming the email change without errors.

### Step 5: Identify Search Reflection Vulnerability

**Context**: Locate an endpoint (e.g., search function) that reflects user input into the Set-Cookie response header, enabling cookie injection.

In the browser (proxied through Burp), navigate to the search functionality and submit a test search term (e.g., "test").

Intercept the request in Burp and forward to Repeater.

**Expected Output**: Response headers showing the search term reflected in the Set-Cookie header, e.g., Set-Cookie: session=...test..., with no CSRF protection on this GET request.

### Step 6: Craft Cookie Injection URL

**Context**: Construct a malicious search URL that injects the attacker's csrfkey into the Set-Cookie header via CRLF injection in the reflected search parameter.

Use the reflected search endpoint to build the URL:

`/?search=test%0d%0aSet-Cookie:%20csrfKey=your-csrfkey-here`

Replace "your-csrfkey-here" with the actual attacker's csrfkey value from Burp.

Send this URL to the victim (e.g., via phishing link).

**Expected Output**: Victim's browser receives a Set-Cookie header injecting the attacker's csrfkey.

### Step 7: Generate CSRF PoC HTML Form

**Context**: Use Burp Suite's CSRF PoC generator to create an HTML form mimicking the change email request, including the csrf token.

In Burp Repeater, right-click the captured change email request and select "Engagement tools" > "Generate CSRF PoC".

Configure the PoC to target the victim's domain, include the csrf token in the form fields, and ensure no additional protections are added.

**Expected Output**: HTML form code ready for modification and delivery.

### Step 8: Modify PoC with Auto-Submit Payload

**Context**: Enhance the PoC to auto-submit upon loading by injecting a JavaScript payload that triggers form submission when an image fails to load.

Remove any existing script tags from the generated PoC.

Insert the following code inline: Replace the img src with the cookie injection URL from Step 6.

Reference [[codes/csrf-auto-submit-payload]] for the exact snippet.

```html
<img src="https://target.com/?search=test%0d%0aSet-Cookie:%20csrfKey=your-csrfkey-here" onerror="document.forms[0].submit()">
```

Deliver the modified HTML to the victim (e.g., via email or hosted page).

**Expected Output**: Upon loading, the victim's csrfkey is injected, and the form auto-submits, changing the email to the attacker's.
