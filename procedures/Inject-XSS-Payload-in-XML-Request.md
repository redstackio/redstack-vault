---
id: be471ff8-6c7c-4d5e-9f9b-01abbc9c0af7
name: Inject-XSS-Payload-in-XML-Request
type: procedure
verified: true
submitted: true
created_at: '2020-09-05T19:47:45.073202+00:00'
updated_at: '2023-05-26T01:14:33.662061+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - owasp
  - owasp top 10
  - web applications
commands:
  - '[[commands/curl-send-xml-search-request]]'
  - '[[commands/curl-inject-xss-xml-payload]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: medium
detection_risk: high
validated: true
---

# Inject-XSS-Payload-in-XML-Request

## Summary

This procedure demonstrates how to inject a cross-site scripting (XSS) payload into an XML-based request to a web application, exploiting reflected input fields that process XML data. When the server reflects the input without proper sanitization, the payload executes JavaScript in the victim's browser, potentially leading to session hijacking, data theft, or further attacks. It is commonly used against search functionalities or API endpoints that accept XML input.

## Description

Cross-site scripting (XSS) vulnerabilities allow attackers to inject malicious scripts into web pages viewed by other users. In this scenario, the attack targets XML requests, such as those used in SOAP APIs or custom XML parsers in web applications. By submitting a search string or parameter within an XML structure, the attacker intercepts and modifies the request to include a JavaScript payload. If the application echoes the input back in the HTML response without encoding, the script executes, displaying an alert or performing other actions. This technique is effective against legacy systems or misconfigured XML handlers that fail to sanitize user input. Prerequisites include network access to the target web application and a proxy tool like Burp Suite for request manipulation. The procedure maps to MITRE ATT&CK technique T1059.007 (JavaScript) under the Execution tactic, as it leverages client-side script execution for malicious purposes.

## Requirements

1. Access to a vulnerable web application with an XML-accepting endpoint (e.g., search feature via POST with XML body).
2. Burp Suite or similar proxy tool installed and configured to intercept traffic ([[tools/Burp-Suite]]).
3. Network connectivity to the target application, typically over HTTP/HTTPS on port 80/443.
4. Basic knowledge of URL encoding and XML structure to craft payloads without breaking the request format.

## Defense

Defensive measures and detection strategies:

- Implement input validation and sanitization for all XML inputs, using libraries like OWASP ESAPI or XML parsers with secure flags (e.g., disabling external entity processing).
- Encode output in responses to prevent script execution, such as using HTML entity encoding for reflected data.
- Deploy Web Application Firewalls (WAFs) with rules to detect common XSS payloads like <script>alert(.</li>
- Enable Content Security Policy (CSP) headers to restrict inline script execution.
- Monitor application logs for anomalous requests containing script tags or encoded payloads, and use client-side monitoring tools to detect unexpected JavaScript execution.

## Objectives

1. Identify and intercept an XML request from a user input field in the target web application.
2. Inject a malicious JavaScript payload into the XML structure to test for reflection without sanitization.
3. Verify successful XSS execution by observing script output in the response, such as an alert box.
4. Demonstrate potential for more advanced payloads to steal cookies or perform actions on behalf of the user.

## Instructions

### Step 1: Submit Initial Search Request

**Context**: Begin by sending a legitimate search request to the application to capture the baseline XML structure. This establishes the normal request format and identifies the input field (e.g., a <search> tag) that will be targeted for injection. Use a tool like curl to simulate the request or interact directly with the application while proxying through Burp Suite.

**Command** ([[commands/curl-send-xml-search-request]]):
```bash
curl -X POST http://target-app.com/search -H "Content-Type: application/xml" -d '<search><query>normal search term</query></search>'
```

> This command sends a basic XML POST request with a neutral search term. Expected output is a response echoing the query, such as an HTML page displaying "Results for: normal search term". Intercept this in Burp Suite to confirm the XML body structure. If the response reflects the input unsanitized, proceed to injection.

### Step 2: Intercept and Modify the Request

**Context**: Use Burp Suite to intercept the request after submitting the initial search. Locate the XML parameter (e.g., <query>) and replace its value with the URL-encoded XSS payload. This step tests whether the application processes and reflects the malicious input without escaping special characters like < and >.

**Command** ([[commands/curl-inject-xss-xml-payload]]):
```bash
curl -X POST http://target-app.com/search -H "Content-Type: application/xml" -d '<search><query>%3E%3Cscript%3Ealert(%27123%27)%3C/script%3E%3C/search>'
```

> Replace the query value with the encoded payload (%3E%3Cscript%3Ealert(%27123%27)%3C/script%3E%3C, which decodes to ><script>alert('123')</script><). Forward the modified request in Burp or run directly with curl. The payload closes any open tags and injects the script. If vulnerable, the response will include the executable script.

### Step 3: Verify Payload Execution

**Context**: Observe the application's response for signs of execution. In a browser context (or simulated via proxy), the injected script should trigger an alert box or other JavaScript behavior. This confirms the reflection vulnerability and successful XSS.

No specific command is needed here; inspect the HTTP response body for the unencoded <script> tag. If an alert pops up in the browser, the attack succeeded. For automated verification, check the response content for the payload string using tools like grep on the output file (e.g., curl -o response.xml).

> Expected output in a vulnerable response: HTML containing <script>alert('123')</script>, leading to a browser alert dialog displaying "123". If no execution occurs, the input may be sanitized—try variations like bypassing filters with different encodings.
