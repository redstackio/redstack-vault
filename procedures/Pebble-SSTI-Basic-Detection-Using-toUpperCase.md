---
type: procedure
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[Template Injection]]'
sub_techniques: []
tags:
  - ssti
  - pebble
  - template-injection
  - detection
commands:
  - '[[commands/curl-pebble-ssti-test]]'
tools: []
platforms:
  - Web
  - Java
skill_level: beginner
impact_level: high
detection_risk: low
verified: true
validated: true
---

# Pebble-SSTI-Basic-Detection-Using-toUpperCase

## Summary

This procedure outlines a basic method to detect Server-Side Template Injection (SSTI) vulnerabilities in web applications using the Pebble template engine. By injecting a payload that leverages the toUpperCase() method on a string, attackers can confirm if the input is interpreted as a template expression, potentially leading to arbitrary code execution if exploited further.

## Description

Server-Side Template Injection (SSTI) occurs when user input is unsafely embedded into a template, allowing attackers to inject malicious template syntax that gets evaluated server-side. Pebble, a Java-based templating engine inspired by Twig, is commonly used in Java applications and is susceptible to SSTI if not properly sanitized. This procedure focuses on a basic detection technique using the toUpperCase() method to verify template evaluation without causing harm. If successful, it confirms the vulnerability, which can then be escalated to read files, execute commands, or access system resources via Java classes like Runtime.exec(). This is particularly relevant for web applications built with frameworks like Spring Boot that integrate Pebble for rendering dynamic content. Detection is low-risk but high-impact, as confirmed SSTI often leads to full server compromise.

## Requirements

1. Network access to the target web application (e.g., via browser or proxy).
2. A vulnerable input field that is processed through the Pebble template engine, such as a search parameter, username field, or error message renderer.
3. Basic tools like curl for sending HTTP requests or Burp Suite for interception (curl is sufficient for this basic test).
4. Knowledge of the application's input points; reconnaissance may be needed to identify template-rendered outputs.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization, whitelisting allowed characters and escaping user input before passing to the template engine.
- Use Pebble's safe rendering modes or disable dangerous extensions like auto-escaping overrides.
- Deploy a Web Application Firewall (WAF) configured to detect template syntax patterns such as {{ }} or common SSTI payloads.
- Regularly audit and update Pebble and dependent libraries to patch known vulnerabilities; enable logging for template evaluation errors.
- Conduct code reviews for dynamic template usage and employ static analysis tools to identify unsafe interpolation.

## Objectives

1. Confirm the presence of an SSTI vulnerability in a Pebble-based application.
2. Demonstrate template expression evaluation without causing disruption.
3. Lay groundwork for potential escalation to arbitrary code execution if the vulnerability is confirmed.
4. Highlight the risks of unsanitized template inputs in Java web applications.

## Instructions

### Step 1: Prepare the SSTI Detection Payload

**Context**: Create or identify the injection payload using the toUpperCase() method. This tests if the template engine evaluates expressions by converting a lowercase string to uppercase. Replace SOMESTRING in the payload with a simple test value like "hello" to expect "HELLO" in the output.

**Code Reference** ([[codes/Pebble-SSTI-toUpperCase-Detection-Payload]]):

The payload is: {{ SOMESTRING.TOUPPERCASE() }}

> This step ensures the payload is correctly formatted for Pebble's expression syntax. If the application echoes the input directly, the output should show the transformed string, confirming SSTI. Why: Direct string output would show the literal payload, but evaluation indicates server-side processing.

### Step 2: Inject the Payload via HTTP Request

**Context**: Send the prepared payload to a vulnerable endpoint, such as a search form or profile field that renders user input via Pebble templates. Use curl to simulate the request and observe the response for evaluation.

**Command** ([[commands/curl-pebble-ssti-test]]):
```bash
curl -X GET "$_TARGET_URL?search=$_PAYLOAD"
```

> Execute the command with the target URL (e.g., http://example.com/search) and the payload (e.g., {{ "hello".TOUPPERCASE() }}). Expected output: If SSTI is present, the response will render "HELLO" instead of the literal payload. If not, it shows {{ "hello".TOUPPERCASE() }} unchanged. Why: This verifies if the input is parsed as a template expression. Decision point: If no change, try other inputs or endpoints; if uppercase appears, vulnerability confirmed—proceed to advanced payloads for RCE.

### Step 3: Verify and Escalate if Confirmed

**Context**: Analyze the response for success indicators. If confirmed, note the injection point for further exploitation, such as injecting Java interop payloads for command execution.

> No specific command needed here, but monitor the HTTP response body for the transformed output. Success: Uppercase string appears. If partial evaluation occurs, refine the payload syntax (Pebble is case-sensitive for methods).
