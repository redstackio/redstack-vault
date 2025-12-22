---
type: procedure
description: >-
  Injects a simple mathematical expression into a Groovy template to demonstrate
  Server-Side Template Injection (SSTI) and execute arbitrary code evaluation.
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Template Injection|T1221 - Template Injection]]'
sub_techniques: []
tags:
  - ssti
  - groovy
  - injection
  - web
commands:
  - '[[commands/curl-groovy-ssti-test]]'
tools: []
platforms:
  - Web
skill_level: beginner
impact_level: medium
detection_risk: low
verified: true
validated: true
---

# Groovy-SSTI-Basic-Math-Injection

## Summary

This procedure demonstrates a basic Server-Side Template Injection (SSTI) vulnerability in applications using Groovy as a template engine. By injecting a simple mathematical expression like '${9*9}', the template evaluates it server-side and returns the result (81), confirming code execution capability. This serves as an entry point for more complex injections leading to remote code execution (RCE).

## Description

Groovy is a flexible scripting language often used in Java-based web applications for dynamic templating, such as in Grails or custom JSP/Thymeleaf setups. SSTI occurs when user input is unsafely interpolated into templates without proper escaping, allowing attackers to inject Groovy expressions that are evaluated on the server. This basic injection tests for vulnerability by performing a harmless math operation, but it can escalate to command execution (e.g., '${new java.lang.ProcessBuilder("id").start().inputStream.text}'). The target environment is typically a web app with a vulnerable input field, like a search parameter or user profile field. Success indicates potential for data exfiltration, RCE, or server compromise.

## Requirements

1. Network access to the target web application (e.g., via browser or proxy).
2. Identification of a parameter or input field processed by Groovy templating (e.g., via error messages or known frameworks).
3. Tools like curl or Burp Suite for sending crafted requests.
4. Basic knowledge of HTTP requests and URL encoding.

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs before templating, using safe rendering modes in Groovy (e.g., disable expression evaluation).
- Implement a Web Application Firewall (WAF) to detect common SSTI payloads like '${' or '<%'.
- Enable application logging for template evaluation errors and monitor for anomalous outputs like unexpected numbers or strings in responses.
- Use static analysis tools to scan for unsafe template usage in code.

## Objectives

1. Confirm SSTI vulnerability by evaluating a simple expression.
2. Establish a baseline for escalating to command execution or data access.
3. Demonstrate low-risk testing without causing harm to the target.

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Locate an input field or parameter in the web app that is reflected or processed server-side, such as a search box or dynamic content generator. Test with a benign string like 'test' to see if it's interpolated into the template.

Send a request to the endpoint using [[commands/curl-groovy-ssti-test]] with a non-malicious payload:

```bash
curl -X GET "http://target.com/search?q=test" -v
```

> This verifies the input is processed. Look for the input echoed back in the response body. If it appears unescaped (e.g., as plain text within template markers), proceed to injection testing.

### Step 2: Inject Basic Math Expression

**Context**: Craft a payload using Groovy's expression syntax to perform a multiplication (9*9=81). This tests if the template engine evaluates the injected code. If successful, the response will contain '81' instead of the literal '${9*9}'.

Modify the request parameter to include the payload using [[commands/curl-groovy-ssti-test]]:

```bash
curl -X GET "http://target.com/search?q=%24%7B9*9%7D" -v
```

> URL-encode the payload ('${9*9}' becomes '%24%7B9*9%7D') to bypass basic filters. The WHY: This step confirms evaluation by producing a numeric result not present in the input.

### Step 3: Verify and Escalate Check

**Context**: Compare the output to confirm injection. If '81' appears, the vulnerability is confirmed. Optionally, test a slightly more complex expression like '${Runtime.getRuntime().exec("whoami")}' but only in controlled environments to avoid RCE.

Re-run the injection and inspect the response:

```bash
curl -X GET "http://target.com/search?q=%24%7B9*9%7D" | grep -i 81
```

> If the output shows '81', success is verified. Decision point: If no evaluation occurs (e.g., literal '${9*9}' returned), try alternative syntax like '<% out.print(9*9); %>' or check for framework-specific wrappers. Escalate by chaining to command execution procedures if confirmed.
