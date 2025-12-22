---
type: procedure
description: >-
  Exploit stored XSS in an href attribute where double quotes are HTML encoded,
  allowing JavaScript execution via unquoted javascript: URLs.
verified: true
submitted: true
created_at: '2020-08-27T10:48:07.947143+00:00'
updated_at: '2023-05-26T18:18:24.650583+00:00'
platforms:
  - Web
tags:
  - injection
  - owasp
  - owasp-top-10
  - stored-xss
  - web-applications
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
commands: []
tools: []
validated: true
---

# Stored-XSS-in-Href-Attribute-with-HTML-Encoded-Double-Quotes

## Summary

This procedure exploits a stored cross-site scripting (XSS) vulnerability in a web application's comment section where user input is reflected into an anchor tag's href attribute. The application HTML encodes double quotes to prevent direct JavaScript injection, but an attacker can bypass this by using a javascript: URL payload that does not require quotes, such as `javascript:alert(1)`, leading to arbitrary JavaScript execution when users interact with the malicious link.

## Description

Stored XSS occurs when user-supplied input is stored on the server (e.g., in a database) and later displayed to other users without proper sanitization. In this scenario, the vulnerable application processes comment inputs, including fields like name and website URL, and renders them as HTML anchor tags. The href attribute receives the website input, and while the application encodes double quotes (e.g., converting " to &quot;), it fails to neutralize javascript: schemes. An attacker submits a payload like `javascript:alert(1)` in the website field, which gets stored and reflected as `<a href="javascript:alert(1)">attacker-name</a>`. When victims view the comments and click the link, the JavaScript executes in their browser context. This technique is effective against applications using partial output encoding that assumes quotes are the primary vector for XSS. The target environment is typically a web application with user-generated content features, such as blogs or forums, running on any modern web server.

## Requirements

1. Valid user account or anonymous access to the web application's comment submission feature.
2. A modern web browser (e.g., Chrome, Firefox) to submit and observe the payload.
3. Network access to the target web application without restrictions on POST requests to the comment endpoint.
4. Basic knowledge of HTML and JavaScript to craft and verify the payload.

## Defense

Defensive measures and detection strategies:

- Implement comprehensive input validation and output encoding using libraries like OWASP ESAPI or DOMPurify to neutralize javascript: URLs and other schemes in href attributes.
- Use Content Security Policy (CSP) with strict policies (e.g., unsafe-inline disallowed) to prevent inline JavaScript execution.
- Sanitize stored user input by stripping or whitelisting allowed protocols in URL fields (e.g., only http/https).
- Monitor for anomalous JavaScript execution via browser logs or web application firewall (WAF) rules detecting javascript: in user inputs.
- Employ client-side scanning with tools like XSS auditors in browsers or server-side scanning with static analysis.

## Objectives

1. Inject a stored XSS payload into a comment field that bypasses quote encoding in href attributes.
2. Verify payload storage and reflection without alteration that breaks execution.
3. Trigger JavaScript execution (e.g., alert popup) upon user interaction with the malicious link.
4. Demonstrate potential for further exploitation, such as session hijacking or data theft.

## Instructions

### Step 1: Access the Comment Section and Submit Test Input

**Context**: Begin by navigating to the vulnerable comment section to understand input fields and reflection behavior. Submit benign input to confirm how the application renders comments, particularly how URL fields are placed in href attributes.

**Action**: Open the target web application in your browser, locate the blog post or page with the comment form, and enter test details such as name: "Test User", website: "http://example.com", and a sample comment. Submit the form via the POST request.

> This step establishes a baseline for reflection. Expected behavior: The comment appears below the post with an anchor tag like `<a href="http://example.com">Test User</a>` linking to the website.

### Step 2: Observe Reflection in the Rendered Comment

**Context**: Inspect the stored comment to verify how user input is processed and displayed. This reveals if double quotes are encoded and identifies the exact placement of the href attribute.

**Action**: Refresh the page or navigate back to the comment section to view the submitted comment. Right-click the rendered anchor tag and select "Inspect Element" in the browser's developer tools to examine the HTML source.

> Look for encoding: If you submitted a quoted URL like "http://example.com", it should appear as `href=&quot;http://example.com&quot;`. This confirms the application's partial protection against quoted payloads but vulnerability to unquoted schemes.

### Step 3: Submit the Malicious Payload

**Context**: Craft and inject the XSS payload using a javascript: URL that avoids double quotes, exploiting the encoding limitation to achieve code execution.

**Action**: Return to the comment form and enter: name: "hello hackers", website: "javascript:alert(1)", comment: "Click the name to test". Submit the form.

> The payload `javascript:alert(1)` is chosen because it executes immediately on click without needing quotes, bypassing the encoding. No tools are required beyond the browser.

### Step 4: Verify Execution

**Context**: Confirm the payload's success by interacting with the reflected content, ensuring JavaScript runs in the victim's context (simulated by your own browser session).

**Action**: Reload the page to view the new comment. Click on the "hello hackers" link in the rendered comment, which should appear as `<a href="javascript:alert(1)">hello hackers</a>`.

> Expected outcome: An alert dialog box pops up displaying "1". If no popup appears, inspect the HTML to check for additional encoding or sanitization on the javascript: scheme and adjust the payload accordingly (e.g., try `JaVaScRiPt:alert(1)` for case-insensitive checks).
