---
id: fecdd907-c237-465a-81a7-490308997bc6
name: Stored-XSS-via-Onclick-Attribute-with-Partial-Encoding
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T11:31:07.939575+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - '[[tags/injection]]'
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/Stored XSS]]'
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

# Stored-XSS-via-Onclick-Attribute-with-Partial-Encoding

## Summary

This procedure demonstrates how to exploit a stored XSS vulnerability in a web application's comment section where user input is reflected into an onclick event handler attribute. The application partially encodes characters like <>, ", and escapes ' and \, but can be bypassed using a crafted javascript: URL payload to execute arbitrary JavaScript, such as triggering an alert popup.

## Description

Stored XSS occurs when user-supplied input is stored on the server (e.g., in a database) and later reflected back to users without proper sanitization, leading to script execution in other users' browsers. In this scenario, the vulnerability is in a comment feature where input is inserted into an HTML onclick attribute. The encoding protects against direct script tags or quotes but fails against a javascript: protocol URI that breaks out of the attribute context. This technique is useful in red team engagements to simulate attacker persistence by injecting payloads that execute when admins or other users interact with the comments. The target environment is typically a web application with user-generated content sections like forums or comment boards. Expected outcomes include successful JavaScript execution, confirming the vulnerability for further exploitation like session hijacking or data theft.

## Requirements

1. Access to a vulnerable web application with a comment or user input section that stores and displays content.
2. A modern web browser (e.g., Chrome, Firefox) for manual testing and viewing source code.
3. Basic knowledge of HTML attributes and JavaScript execution contexts.
4. No special privileges required; assumes unauthenticated user access to post comments.

## Defense

Defensive measures and detection strategies:

- Implement comprehensive input validation and output encoding using libraries like OWASP ESAPI or DOMPurify to neutralize HTML and JavaScript contexts.
- Use Content Security Policy (CSP) headers to restrict inline script execution and javascript: URIs.
- Sanitize stored data on the server-side before database insertion and on output before rendering.
- Monitor for anomalous JavaScript execution via client-side logging or server-side anomaly detection in user inputs.
- Employ Web Application Firewalls (WAFs) with rules tuned for XSS payloads, including encoded variants.

## Objectives

1. Identify reflection points in onclick attributes by inspecting stored content.
2. Craft a bypass payload exploiting partial encoding to execute JavaScript.
3. Verify execution by triggering the payload and observing the alert.
4. Demonstrate potential for broader impact, such as stealing cookies or redirecting users.

## Instructions

### Step 1: Post Initial Test Comment

**Context**: Begin by submitting a benign comment containing a random string to identify how the application reflects and encodes user input in the onclick attribute. This step confirms the storage and reflection mechanism without triggering any execution.

Navigate to the comment section of the application. Enter a simple test string, such as "test123", in the comment field along with any required details like name or email. Submit the comment.

**Expected Output**: The comment appears in the list, and upon viewing the page source (right-click > View Page Source), the string is reflected inside an onclick event handler, e.g., something like onclick="someFunction('test123')", with visible encoding on <>, ", ', and \ if present.

### Step 2: Inspect Reflected Input

**Context**: Examine the HTML source to understand the exact reflection context and encoding applied. This reveals the onclick attribute's structure and confirms partial protections, allowing payload crafting.

Reload the page or view the source code where the comment is rendered. Search for your test string to locate the onclick attribute containing it.

**Expected Output**: Identification of the attribute format, such as <a onclick="viewComment('encoded_input')">Hi admin</a>, showing how special characters are handled (e.g., < becomes &lt;, but certain breaks are possible).

### Step 3: Craft and Submit Malicious Payload

**Context**: Modify the input to inject a javascript: URL that breaks out of the onclick attribute using the partial encoding weaknesses. The payload leverages unencoded characters to close the attribute and execute code on click.

Return to the comment section and edit or post a new comment with the following payload in the input field: javascript:foo?&'-alert(1)-'

Submit the comment.

**Expected Output**: The payload is stored and reflected in the onclick attribute, appearing mangled but functional in source, e.g., onclick="viewComment('javascript:foo?&'-alert(1)-')".

### Step 4: Trigger and Verify Execution

**Context**: Interact with the injected comment to execute the payload, confirming the XSS vulnerability. This simulates how an attacker could affect other users, such as admins reviewing comments.

Navigate back to the comment section. Locate and click on the injected comment (e.g., the "Hi admin" link).

**Expected Output**: A JavaScript alert popup displays "1", indicating successful code execution.

### Step 5: Validate and Escalate

**Context**: Confirm the vulnerability's scope and potential for escalation. Test variations to steal data or perform actions.

In the browser console or by modifying the payload, replace alert(1) with more impactful code, like alert(document.cookie), and re-test by clicking.

**Expected Output**: Execution of the escalated payload, revealing cookies or other client-side data, proving the vulnerability's exploitability for session theft or phishing.
