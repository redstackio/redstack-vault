---
id: a2656929-20d1-45a0-9985-7cae6491f22e
name: DOM-XSS-In-InnerHTML-Sink-Using-location-search
type: procedure
verified: true
submitted: true
created_at: '2020-08-24T07:39:15.560499+00:00'
updated_at: '2023-05-26T18:11:44.221162+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - '[[tags/injection]]'
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/Web Applications]]'
commands: []
platforms:
  - Web
tools: []
validated: true
---

# DOM-XSS-In-InnerHTML-Sink-Using-location-search

## Summary

This procedure demonstrates how to identify and exploit a DOM-based Cross-Site Scripting (XSS) vulnerability where user input from the URL's location.search is unsafely inserted into the page using innerHTML, allowing arbitrary JavaScript execution in the victim's browser context.

## Description

DOM-based XSS occurs when client-side JavaScript processes data from sources like location.search without proper sanitization and inserts it into the DOM using sinks like innerHTML. This can lead to script execution, session hijacking, or data theft. The technique targets web applications that reflect URL parameters directly into HTML content. In this scenario, the application uses innerHTML to populate a div with search query data, enabling attackers to inject malicious payloads via the URL. This is common in search functionalities or dynamic content loaders. Prerequisites include access to the vulnerable page and a modern web browser for testing.

## Requirements

1. Access to a web application with a search functionality that uses location.search and innerHTML.
2. A web browser (e.g., Chrome, Firefox) with developer tools enabled.
3. Optional: A proxy tool like Burp Suite for intercepting and modifying requests, though manual URL manipulation suffices for basic testing.
4. No special credentials required if the page is publicly accessible.

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs from URL parameters before inserting into the DOM; use textContent instead of innerHTML.
- Implement Content Security Policy (CSP) to restrict inline script execution.
- Use libraries like DOMPurify for safe HTML rendering.
- Monitor for anomalous JavaScript execution via browser security tools or web application firewalls (WAFs).
- Enable strict input validation on the client-side and server-side reflection points.

## Objectives

1. Verify if the search functionality reflects input via innerHTML without escaping.
2. Inject and execute a JavaScript payload to confirm XSS vulnerability.
3. Demonstrate the impact through alert execution, simulating potential data exfiltration or defacement.
4. Expected outcome: Successful popup alert confirming arbitrary code execution.

## Instructions

### Step 1: Test for Reflection with Neutral Input

**Context**: Enter a harmless string to check if the input from location.search is reflected in the page's HTML structure without sanitization. This confirms the data flow to innerHTML.

Navigate to the search page and append a random string to the URL, e.g., ?search=randomstring. View the page source (Ctrl+U or right-click > View Page Source) and search for the string.

> If the string appears unescaped in a JavaScript context using innerHTML (e.g., document.getElementById('div').innerHTML = location.search.substring(1);), proceed to payload injection.

### Step 2: Inspect JavaScript Code for innerHTML Usage

**Context**: Examine the client-side JavaScript to identify the exact sink where location.search data is inserted, confirming the vulnerability path.

Open browser developer tools (F12), go to the Sources or Elements tab, and search for 'innerHTML' in the scripts. Look for code like element.innerHTML = decodeURIComponent(location.search.slice(1)) or similar.

> Expected: Identification of the vulnerable script line that processes location.search data.

### Step 3: Inject XSS Payload

**Context**: Craft and deliver a payload that exploits the innerHTML sink to execute JavaScript, breaking out of the HTML context.

Modify the URL to include the payload in the search parameter, e.g., ?search=%3Cimg%20src%3D1%20onerror%3Dalert(1)%3E (URL-encoded). Load the page and observe for execution.

Reference the payload code: [[codes/XSS-Image-OnError-Alert]]

> The payload uses an invalid src to trigger onerror, executing alert(1). If successful, an alert box pops up.

### Step 4: Verify Exploitation

**Context**: Confirm the vulnerability by checking for code execution and assessing potential impact.

After loading the payload URL, check the browser console for errors or execution traces. If the alert appears, the XSS is confirmed. Test further payloads for escalation, like stealing cookies via alert(document.cookie).

> Success criteria: Alert executes without errors, proving DOM manipulation and JS injection.
