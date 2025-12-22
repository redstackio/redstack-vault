---
id: 63b427ee-c687-4853-9c92-c1251790ad45
name: Execute-Stored-DOM-XSS-in-Comment-Section
type: procedure
verified: true
submitted: true
created_at: '2020-08-05T14:55:04.907320+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
tags:
  - '[[tags/DOM XSS]]'
  - '[[tags/injection]]'
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/Web Applications]]'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
commands: []
tools: []
validated: true
---

# Execute-Stored-DOM-XSS-in-Comment-Section

## Summary

This procedure demonstrates how to exploit a stored DOM-based Cross-Site Scripting (XSS) vulnerability in a web application's comment section, such as a blog. By injecting a malicious JavaScript payload that bypasses basic HTML encoding, the payload is stored on the server and executed in the browser of any user who views the page, potentially leading to session hijacking, data theft, or further attacks.

## Description

Stored DOM XSS occurs when user input, such as a comment, is stored on the server without proper sanitization and then dynamically inserted into the Document Object Model (DOM) of a different page via client-side JavaScript. Unlike reflected XSS, the payload persists and affects all users viewing the affected page. In this scenario, the application encodes angle brackets in the input, but a bypass using a leading empty tag ("<>") allows the script to execute. This technique targets web applications with insufficient output encoding for DOM manipulations, commonly seen in content management systems or forums. The attack requires no special privileges beyond the ability to submit comments and relies on the victim's browser executing the injected script.

## Requirements

1. Access to a vulnerable web application with a comment submission feature (e.g., blog post comments).
2. A modern web browser (e.g., Chrome, Firefox) with developer tools enabled for inspection.
3. No elevated privileges needed; assumes authenticated or public comment submission.
4. Basic knowledge of HTML and JavaScript for payload crafting.

## Defense

Defensive measures and detection strategies:

- Implement strict Content Security Policy (CSP) to restrict inline script execution.
- Sanitize and encode all user input on both server and client sides using libraries like DOMPurify.
- Validate and escape HTML entities in stored content before rendering.
- Monitor for anomalous JavaScript execution in browser logs or via Web Application Firewall (WAF) rules targeting common XSS payloads.
- Use HTTP-only cookies for session management to prevent theft via document.cookie.

## Objectives

1. Inject a malicious payload into a stored comment field that bypasses encoding.
2. Verify the payload is stored without execution during submission.
3. Confirm execution when the page is reloaded or viewed by another user.
4. Demonstrate potential for broader impact, such as alert popups or data exfiltration.

## Instructions

### Step 1: Test Initial Payload Submission

**Context**: Attempt to submit a basic XSS payload to identify encoding behavior. This step confirms if the application encodes angle brackets, preventing immediate execution.

Navigate to the comment submission form on the target page (e.g., blog post). Enter the following payload in the comment field:

```
<img src=1 onerror=alert(1)>
```

Submit the comment and inspect the response or page source using browser developer tools (F12 > Elements tab) to check if the payload is encoded (e.g., &lt; and &gt;).

### Step 2: Analyze Encoding and Modify Payload

**Context**: Observe that the application encodes the angle brackets, neutralizing the script tag. Modify the payload to prepend an empty tag ("<>") to break out of the encoded context and allow execution in the DOM.

Return to the comment form and submit the modified payload:

```
<><img src=1 onerror=alert(1)>
```

Submit the comment. This bypasses the encoding by closing any potential attribute or tag context before injecting the script.

### Step 3: Verify Storage and Submission Success

**Context**: Ensure the modified payload is accepted and stored by the server without errors. This confirms the vulnerability exists for persistence.

After submission, check for a success message or redirect indicating the comment was saved. Do not reload the page yet to avoid premature execution.

### Step 4: Trigger Payload Execution

**Context**: View the page containing the stored comment to execute the payload in the DOM. This simulates impact on other users.

Navigate back to the blog or page displaying comments. The payload should now execute, triggering an alert box with "1" due to the onerror handler.

Inspect the DOM in developer tools to confirm the script was inserted and executed without encoding issues.

### Step 5: Validate Impact and Cleanup

**Context**: Confirm the attack's success and assess potential for escalation. In a real scenario, replace alert(1) with more malicious code like stealing cookies.

If the alert appears, the exploit succeeded. Document the vulnerable endpoint and recommend fixes. Delete the test comment if possible to avoid affecting other users.
