---
id: b77a13c7-6d53-44c6-9078-e3a2ac00c9a3
type: procedure
verified: true
submitted: true
created_at: '2020-08-24T07:04:48.559617+00:00'
updated_at: '2023-05-26T18:30:17.805758+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - '[[tags/DOM XSS]]'
  - '[[tags/injection]]'
  - '[[tags/owasp]]'
  - '[[tags/Web Applications]]'
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
---

# DOM XSS in Document.write Sink Using Location.search

## Summary

This procedure demonstrates how to exploit a DOM-based Cross-Site Scripting (XSS) vulnerability where the location.search parameter is unsafely inserted into a document.write sink, specifically within an img src attribute. By injecting a crafted payload, an attacker can break out of the attribute and execute arbitrary JavaScript, such as displaying an alert, to confirm the vulnerability.

## Description

DOM-based XSS occurs when client-side JavaScript processes data from sources like location.search without proper sanitization and inserts it into dangerous sinks like document.write. In this scenario, the vulnerable code likely resembles document.write('<img src="' + location.search.substring(1) + '">'), allowing attackers to append closing quotes and tags to inject executable code. This technique is common in legacy web applications and can lead to session hijacking, data theft, or further exploitation if chained with other vulnerabilities. The target environment is a web application accessible via a browser, assuming no server-side protections like Content Security Policy (CSP) block inline scripts.

## Requirements

1. Access to a web browser (e.g., Chrome, Firefox) with developer tools enabled.
2. Direct access to the vulnerable webpage URL where the search parameter is reflected in document.write.
3. No authentication required for the test page, though real-world scenarios may need valid session cookies.
4. Basic knowledge of HTML attribute escaping and JavaScript execution contexts.

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) with 'unsafe-inline' restrictions to block inline script execution.
- Sanitize and encode location.search inputs using libraries like DOMPurify before insertion into document.write; prefer textContent or createElement for dynamic content.
- Use modern alternatives like innerHTML with validation or avoid document.write entirely in favor of safer DOM manipulation.
- Monitor browser console for script errors and enable XSS Auditor in browsers; server-side logging of unusual query parameters can aid detection.

## Objectives

1. Confirm reflection of location.search in document.write sink.
2. Break out of the img src attribute to inject malicious HTML/JavaScript.
3. Execute arbitrary JavaScript to demonstrate code injection success.
4. Validate the vulnerability for potential escalation to data exfiltration or session manipulation.

## Instructions

### Step 1: Test Reflection with Random Input

**Context**: Verify that the search parameter is directly reflected into the document.write sink without sanitization, typically within an img src attribute. This establishes the injection point.

Navigate to the vulnerable URL and append a random alphanumeric string to the search parameter, e.g., ?search=random123. Submit or load the page.

Right-click on the page and select "View Page Source" (or use Ctrl+U) to inspect the HTML. Look for the img tag where the input appears unsanitized in the src attribute.

**Expected Output**: The source shows something like <img src="random123">, confirming direct insertion.

### Step 2: Break Out of the Attribute

**Context**: Test attribute breakout by appending a closing quote and greater-than symbol to escape the src attribute and enter the tag body or subsequent content.

Modify the URL to include ?search=random123%22%3E (URL-encoded ">") and reload the page.

Inspect the page source or rendered HTML to confirm the breakout.

**Expected Output**: The page displays the "> characters outside the img tag, or the img src becomes malformed (e.g., src="random123" >), indicating successful escape.

### Step 3: Inject and Execute Payload

**Context**: Craft a payload to close the attribute, inject an executable element like an SVG with onload, and trigger JavaScript execution. This confirms the XSS vulnerability.

Update the URL with the payload ?search=%22%3E%3Csvg%20onload%3Dalert(1)%3E%2A (URL-encoded version of "><svg onload=alert(1)>*). Reload the page.

Observe the browser behavior for the alert dialog.

**Expected Output**: A JavaScript alert box pops up displaying "1", proving arbitrary code execution.

### Step 4: Validate and Document

**Context**: Ensure the execution is consistent and note any variations, such as CSP blocks or encoding issues, for reporting or further testing.

Repeat the payload injection multiple times and test variations (e.g., alert(document.cookie) for cookie access). Use browser developer tools (F12) to inspect console for errors or network requests.

**Expected Output**: Consistent alert execution without errors; console may log the injected script if logging is enabled.

## Expected Output

Successful exploitation results in arbitrary JavaScript execution, visible as an alert dialog. Page source inspection shows the injected SVG element within the document.write output, confirming the sink manipulation.
