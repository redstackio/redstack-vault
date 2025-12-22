---
id: f3821842-e7cd-4945-a90b-27fb637ae3e6
name: Stored-XSS-to-Bypass-CSRF-Tokens
type: procedure
verified: true
submitted: true
created_at: '2020-08-05T15:51:59.892318+00:00'
updated_at: '2023-05-26T18:36:32.403480+00:00'
platforms:
  - Web
tags:
  - '[[tags/CSRF]]'
  - '[[tags/injection]]'
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/Web Applications]]'
  - '[[tags/xss]]'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
commands: []
tools: []
validated: true
---

# Stored-XSS-to-Bypass-CSRF-Tokens

## Summary

This procedure demonstrates how to chain a stored cross-site scripting (XSS) vulnerability with a cross-site request forgery (CSRF) attack to bypass anti-CSRF token protections. By injecting a malicious JavaScript payload into a user-controlled input field, such as a blog comment section, the payload executes in the context of other users' browsers, retrieves the valid CSRF token from the target form, and submits a forged request to perform an unauthorized action, like changing the victim's email address.

## Description

Stored XSS allows attackers to inject persistent malicious scripts into web applications, which execute when other users view the affected content. In this scenario, the application implements CSRF tokens to prevent unauthorized requests, but the XSS payload can dynamically fetch and include the token in a forged POST request, effectively bypassing the protection. This technique targets web applications with user-generated content features (e.g., comments or forums) vulnerable to stored XSS and state-changing endpoints protected by CSRF tokens. The attack requires no direct interaction from the victim beyond viewing the injected content, making it highly effective for account takeover or data modification. Expected outcomes include successful execution of the forged action on the victim's behalf, such as email changes, without triggering CSRF validation failures.

## Requirements

1. Access to create a legitimate user account on the target web application.
2. Identification of a stored XSS vulnerability in a user-controlled input field, such as a comment section, that renders HTML/JavaScript for other users.
3. Knowledge of the target endpoint's structure, including the form action URL (e.g., /email/change-email) and CSRF token field name (e.g., name="csrf").
4. A modern web browser for testing and injection; no additional tools required beyond developer tools for payload crafting.
5. The target must have an authenticated session for the victim user viewing the content.

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to restrict inline script execution and external resource loading.
- Sanitize and escape all user inputs, especially in stored contexts like comments, using libraries like DOMPurify.
- Enforce strict CSRF token validation on all state-changing endpoints and regenerate tokens per session.
- Monitor for anomalous JavaScript execution in user-generated content via client-side logging or server-side anomaly detection.
- Use web application firewalls (WAFs) to detect and block common XSS payloads and unusual XMLHttpRequest patterns.

## Objectives

1. Inject a stored XSS payload that executes in victims' browsers to perform unauthorized actions.
2. Dynamically retrieve and utilize CSRF tokens to bypass token-based protections.
3. Achieve account modification (e.g., email change) on the victim's behalf without direct access.
4. Demonstrate the chaining of XSS and CSRF for elevated impact in web application testing.

## Instructions

### Step 1: Create Account and Authenticate

**Context**: Establish a legitimate session on the target application to access features like the comment section and identify vulnerable endpoints. This step ensures the attacker can interact with the application as a normal user.

Log in to the web application using the created account credentials. Navigate to the main dashboard or profile section to confirm authentication.

**Expected Output**: Successful login redirect to the authenticated user dashboard, with session cookies set in the browser.

### Step 2: Identify Target Endpoint and CSRF Implementation

**Context**: Analyze the state-changing form (e.g., email change) to understand the POST method, required parameters, and CSRF token location. This reconnaissance informs the payload design.

Navigate to the "Change Email" page. Right-click and view page source to inspect the form. Look for the <form> tag with method="post", action URL (e.g., /email/change-email), and hidden input like <input type="hidden" name="csrf" value="TOKEN">.

**Expected Output**: Source code revealing the form structure, confirming POST submission and CSRF token in a hidden field.

### Step 3: Craft XSS Payload to Fetch CSRF Token and Submit Forged Request

**Context**: Develop a JavaScript payload that uses XMLHttpRequest to retrieve the current page's CSRF token, parse it, and send a POST request with the token and malicious data (e.g., new email). This bypasses CSRF by using the victim's valid token.

Use the following payload, which targets the /email endpoint to extract the token and submits to /email/change-email:

**Code** ([[codes/JavaScript-XSS-Payload-for-CSRF-Bypass]]):

```javascript
<script>
var req = new XMLHttpRequest();
req.onload = handleResponse;
req.open('get','/email',true);
req.send();
function handleResponse() {
    var token = this.responseText.match(/name="csrf" value="(\w+)"/)[1];
    var changeReq = new XMLHttpRequest();
    changeReq.open('post', '/email/change-email', true);
    changeReq.send('csrf='+token+'&email=test@test.com')
};
</script>
```

Customize the URLs (/email and /email/change-email), token regex, and payload data (e.g., email=test@test.com) based on the target's structure. Test the payload in a local environment or using browser console to ensure it fetches and uses the token correctly.

**Expected Output**: The script executes silently, sending the POST request with the valid token and updated email parameter.

### Step 4: Inject Payload into Vulnerable Stored XSS Field

**Context**: Deliver the payload via the stored XSS vector, such as a blog comment section, so it persists and executes for any authenticated user viewing the page.

Navigate to the comment section or other user-input field vulnerable to stored XSS. Submit the crafted payload from Step 3 as the comment content. Save/submit the comment to store it on the server.

**Expected Output**: The comment is saved without sanitization errors, and the payload script is embedded in the page source.

### Step 5: Verify Execution on Victim Session

**Context**: Confirm the attack by simulating or observing victim interaction, ensuring the payload executes and modifies the account.

Have a victim (or use a test account) view the page with the injected comment while authenticated. Monitor network traffic or check the victim's account for changes (e.g., email updated to test@test.com).

**Expected Output**: Victim's email successfully changed to the injected value, with no CSRF validation errors in server logs.

### Step 6: Validate and Clean Up

**Context**: Ensure the attack succeeded and remove the payload to avoid detection or further issues in testing environments.

Check application logs or user profile for the modification. Delete the injected comment to mitigate ongoing risks.

**Expected Output**: Confirmation of account change; payload removed without residual effects.
