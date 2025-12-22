---
id: 5564aa0f-ec14-465c-8fc1-b3b7b7022b5f
name: Bypass-Tag-Filtering-in-Reflected-XSS-Using-Custom-Tags
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T09:45:04.773041+00:00'
updated_at: '2023-05-26T01:28:22.475157+00:00'
platforms:
  - Web
tags:
  - '[[tags/injection]]'
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/Reflected XSS]]'
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

# Bypass-Tag-Filtering-in-Reflected-XSS-Using-Custom-Tags

## Summary

This procedure demonstrates how to bypass web application filters that block standard HTML tags like <script> in reflected XSS vulnerabilities by using a custom tag with an event handler, such as onfocus, to execute JavaScript code and steal sensitive data like cookies.

## Description

Many web applications implement tag filtering to prevent reflected cross-site scripting (XSS) attacks by blocking common HTML tags that could execute JavaScript. However, these filters often fail to block custom or non-standard tags. This technique exploits such weaknesses by injecting a custom tag (e.g., <xss>) combined with an event handler like onfocus and a tabindex attribute to force focus, triggering the JavaScript payload. The attack relies on the application's reflection of user input in the response without proper sanitization of attributes or custom elements. It is particularly effective against applications using incomplete allowlists or blacklists for HTML parsing. The target environment is typically a web application with a reflected search or input parameter, such as a comment or search field.

## Requirements

1. Access to a vulnerable web application with reflected input (e.g., a search parameter that echoes user input).
2. Browser developer tools or a proxy like Burp Suite for inspecting and modifying requests/responses.
3. Knowledge of the reflected parameter location (e.g., in the page body or URL).
4. No special credentials required, but the application must reflect input without encoding.

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to restrict inline script execution and unsafe attributes.
- Use strict HTML sanitization libraries (e.g., DOMPurify) that strip all event handlers and custom tags.
- Validate and encode all user inputs, especially reflected parameters, using context-aware escaping.
- Monitor for anomalous JavaScript execution via client-side logging or server-side anomaly detection.
- Employ web application firewalls (WAFs) with rules for detecting event handler patterns like onfocus or tabindex in inputs.

## Objectives

1. Confirm input reflection in the application response.
2. Verify that standard XSS payloads are blocked by tag filters.
3. Inject and trigger a custom tag-based payload to execute JavaScript.
4. Extract sensitive data, such as document cookies, via the alert or other exfiltration method.

## Instructions

### Step 1: Verify Input Reflection

**Context**: Test the application to confirm that user input is reflected in the response without sanitization, setting the stage for payload injection.

Enter a random alphanumeric string (e.g., "test123") into the vulnerable input field, such as a search box or comment section, and submit it.

View the page source (right-click > View Page Source) and search for the string to locate where it is reflected.

**Expected Output**: The string appears unencoded in the HTML response, typically within a div or span element.

### Step 2: Test Standard XSS Payload

**Context**: Attempt a basic reflected XSS payload to confirm that common tags are blocked, indicating the presence of tag filtering.

Enter the following payload into the input field and submit: `<script>alert(1)</script>`.

Inspect the response in the page source or browser console for any execution or blocking indicators.

**Expected Output**: The payload is reflected but does not execute; the application may display a blocking message or sanitize the tag, preventing the alert.

### Step 3: Craft Custom Tag Payload

**Context**: Use a custom tag with an event handler to bypass the filter, leveraging onfocus to execute JavaScript when the element gains focus via tabindex.

Construct the payload: `<xss id=x onfocus=alert(document.cookie) tabindex=1>`. URL-encode it for the parameter (e.g., %3Cxss+id%3Dx+onfocus%3Dalert%28document.cookie%29%20tabindex%3D1%3E).

To automate delivery, use the following JavaScript code snippet in the browser console or as an exploit page: [[codes/JavaScript-Redirect-to-Reflected-XSS-with-Custom-Tag]].

Replace the URL placeholder with the vulnerable application's endpoint.

**Expected Output**: Upon loading the exploit, the browser redirects to the vulnerable URL, focuses on the custom element, triggers the onfocus event, and displays an alert with the document's cookies.

### Step 4: Validate Execution and Exfiltration

**Context**: Confirm successful XSS execution and data theft, ensuring the bypass works as intended.

After triggering the payload, check the alert for cookie contents or any exfiltrated data.

If using a proxy, intercept the request to verify the encoded payload is sent correctly.

**Expected Output**: Alert box pops up containing cookie data (e.g., session tokens), indicating successful JavaScript execution.
