---
id: c2813919-dc42-4254-93e7-85ac31a3c2bb
name: Jinjava-SSTI-Uppercase-String-and-Request-Object-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:39.941391+00:00'
updated_at: '2023-04-10T20:23:50.015759+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Template Injection|T1221 - Template Injection]]'
sub_techniques: []
tags:
  - '[[tags/Jinjava]]'
  - '[[tags/Jinjava-Basic-Injection]]'
  - '[[tags/Server-Side-Template-Injection]]'
commands:
  - '[[commands/jinjava-inject-uppercase-string]]'
  - '[[commands/jinjava-access-request-object]]'
platforms:
  - Web
  - Python
tools: []
validated: true
---

# Jinjava-SSTI-Uppercase-String-and-Request-Object-Injection

## Summary

This procedure demonstrates a basic Server-Side Template Injection (SSTI) attack in Jinjava, a Python-based templating engine, by injecting payloads to convert a string to uppercase and access the request object. These initial injections confirm the vulnerability and provide a foothold for further code execution, potentially leading to remote code execution (RCE) and data exfiltration in vulnerable web applications.

## Description

Jinjava, used in applications like HubSpot, renders user-controlled input as templates, enabling SSTI if inputs are not sanitized. This procedure targets basic injections to test for template rendering capabilities. The uppercase string injection verifies that Jinjava syntax is executable, while accessing the request object exposes server-side context like headers and session data. In a real attack scenario, this occurs in web apps where user inputs (e.g., search fields, profiles) are directly interpolated into templates without escaping. Success allows escalation to arbitrary code execution by chaining with more advanced payloads, such as accessing internal classes or executing system commands. Prerequisites include identifying a reflection point via tools like Burp Suite or manual testing.

## Requirements

1. Network access to a web application using Jinjava templating (e.g., via browser or proxy like Burp Suite).
2. Identification of a user-controlled input field that renders output as a Jinjava template (e.g., search box, username display).
3. No authentication required for public endpoints, but low-privilege access may be needed for authenticated pages.
4. A proxy tool to intercept and modify requests if direct input is not feasible.

## Defense

- Implement strict input sanitization and validation, escaping user inputs before template rendering using Jinjava's safe rendering modes.
- Deploy a Web Application Firewall (WAF) configured to detect SSTI patterns, such as Jinjava syntax like {{ }} or .toUpperCase().
- Regularly audit and update Jinjava libraries to patched versions and avoid direct user input in templates.
- Enable application logging for template rendering errors and monitor for anomalous outputs like object dumps.

## Objectives

1. Confirm SSTI vulnerability by executing basic Jinjava functions.
2. Access server-side request object to gather contextual information for further exploitation.
3. Establish a foundation for advanced SSTI payloads leading to RCE.
4. Expose potential sensitive data in request attributes without triggering alerts.

## Instructions

### Step 1: Test Uppercase String Injection

**Context**: Inject a simple Jinjava payload to convert a lowercase string to uppercase, confirming that the application executes template syntax. This step verifies SSTI without accessing sensitive objects, serving as a low-risk probe.

**Command** ([[commands/jinjava-inject-uppercase-string]]):

In the vulnerable input field (e.g., search parameter), enter the payload:

```
{{ 'a'.toUpperCase() }}
```

Submit the request and observe the rendered output. This executes the toUpperCase() method on the string 'a' within the Jinjava engine.

**Expected Output**: The page displays 'A' instead of the literal payload, indicating successful template execution.

### Step 2: Access Request Object

**Context**: Once uppercase injection confirms SSTI, inject to retrieve the request object, which contains HTTP request details like headers, method, and session info. This reveals server internals for chaining attacks, such as inspecting for secrets in attributes.

**Command** ([[commands/jinjava-access-request-object]]):

In the same input field, enter the payload:

```
{{ request }}
```

Submit and check the response. The request keyword references the current HTTP request context in Jinjava.

**Expected Output**: The page renders a string representation of the request object, such as "com.hubspot.jinjava.context.TemplateContextRequest@23548206", confirming access to server-side objects.

### Step 3: Verify and Escalate

**Context**: Validate both injections succeeded without errors, then prepare for escalation by combining payloads or accessing further objects (e.g., {{ request.getAttribute('sensitive') }}). Monitor for rate limiting or alerts.

No specific command; manually inspect outputs from previous steps. If successful, document exposed data and test chained payloads like {{ request.getClass().forName('java.lang.Runtime').getMethod('getRuntime').invoke(null).exec('id') }} for RCE (advanced, not covered here).

**Expected Output**: Consistent rendering of injected results without server errors; object dumps provide actionable intel.
