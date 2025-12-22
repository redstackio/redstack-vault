---
id: 9236cb6e-c76f-49f1-9396-f747ca069b47
name: Test-for-Expression-Language-Injection
type: procedure
verified: true
submitted: true
created_at: '2020-07-25T13:21:48.498222+00:00'
updated_at: '2023-05-26T18:36:58.311747+00:00'
platforms:
  - Web
tags:
  - '[[tags/Expression-Language-Injection]]'
  - '[[tags/injection]]'
  - '[[tags/Web-Applications]]'
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
sub_techniques: []
commands:
  - '[[commands/curl-el-injection-test]]'
tools: []
validated: true
---

# Test-for-Expression-Language-Injection

## Summary

This procedure tests for Expression Language (EL) Injection vulnerabilities in web applications, where user-controlled input such as search fields or parameters is parsed by an EL interpreter, potentially allowing execution of arbitrary expressions or malicious JSP tags. It focuses on identifying if benign mathematical expressions are evaluated, which indicates a vulnerability that could be escalated to remote code execution (RCE).

## Description

Expression Language Injection occurs in Java-based web applications using JSP or similar technologies when user input is directly interpolated into EL contexts without proper sanitization. Attackers can inject expressions like mathematical operations or JSP tags (e.g., ${7*7}) to manipulate application logic or execute code. This procedure demonstrates testing with a simple arithmetic payload to verify if the EL engine evaluates the input, observing changes in response output. It targets input fields like search boxes and is applicable in reconnaissance or vulnerability assessment phases. Successful detection confirms the app is vulnerable to more advanced exploits, such as command injection via EL functions.

## Requirements

1. Access to a web application with user-controlled input fields (e.g., search parameters, form fields) that may use EL for processing.
2. A browser or HTTP client tool like curl for sending requests.
3. Basic knowledge of the target application's endpoints (e.g., via browsing or reconnaissance).
4. Network connectivity to the target web server, typically over HTTP/HTTPS on port 80/443.

## Defense

Defensive measures and detection strategies:

- Implement input validation and sanitization to escape EL metacharacters (e.g., $, { , } ) in user inputs.
- Use parameterized queries or EL-aware templating engines that disable dynamic expression evaluation.
- Enable web application firewall (WAF) rules to detect and block EL payloads like ${...} or $(...).
- Monitor application logs for anomalous evaluations or errors related to EL parsing.
- Conduct regular code reviews and use static analysis tools to identify unsafe EL usage in JSP files.

## Objectives

1. Identify if user input is processed by an EL interpreter.
2. Confirm vulnerability by observing evaluation of injected expressions in responses.
3. Escalate to advanced testing if basic payloads succeed, aiming for RCE.
4. Document indicators for reporting or further exploitation.

## Instructions

### Step 1: Identify Vulnerable Input Points

**Context**: Locate fields or parameters in the web application that accept user input and may be processed server-side with EL, such as search boxes, filters, or session variables. This step ensures targeted testing without unnecessary noise.

Inspect the application using browser developer tools or manual navigation to find forms. Look for GET/POST parameters like 'q', 'search', or 'query'.

**Decision Point**: If no obvious inputs are found, use reconnaissance tools to map the app; otherwise, proceed to testing.

### Step 2: Test with Benign EL Payload

**Context**: Inject a simple, non-malicious EL expression to check if the interpreter evaluates it. A mathematical operation like $(99999+1) should resolve to 100000 if vulnerable, indicating EL parsing without execution risks.

Use the [[commands/curl-el-injection-test]] to send the payload via HTTP request. Replace placeholders with the actual target URL and parameter.

**Command** ([[commands/curl-el-injection-test]]):
```bash
curl -X GET "http://$_TARGET_URL/search?q=$(99999+1)" -v
```

> This command sends a GET request with the EL payload in the 'q' parameter. The '-v' flag provides verbose output to inspect headers and responses. Expected behavior: If vulnerable, the response body (e.g., search results) will reflect the evaluated result (100000) instead of the literal string "$(99999+1)".

**Decision Point**: If the response shows the literal payload, the field may not be vulnerable—test other inputs. If evaluated, proceed to confirmation.

### Step 3: Verify and Observe Response

**Context**: Analyze the application's output to confirm EL evaluation. Look for changes in search results, error messages, or rendered content that match the payload's result.

Review the response from Step 2. Manually submit the same payload via the browser's search field for visual confirmation. Compare literal input vs. evaluated output.

For example, entering "$(99999+1)" in a search field should return results as if searching for "100000" if EL is active.

**Expected Output**: Response body showing evaluated expression, e.g., search results for "100000" or direct output of the computed value. No errors if sanitized, but successful evaluation without literal display confirms vulnerability.

**Decision Point**: If confirmed, escalate to advanced payloads (e.g., ${7*7} for JSP EL); if not, report as secure or test alternative parameters.

### Step 4: Escalate Testing if Vulnerable

**Context**: If basic evaluation succeeds, test for code execution potential using EL functions or JSP tags. This step verifies if the vulnerability allows RCE.

Attempt a payload like "${runtime.exec('whoami')}" in the same input, observing for command output or errors indicating execution.

Use [[commands/curl-el-injection-test]] again, modifying the payload:
```bash
curl -X GET "http://$_TARGET_URL/search?q=${runtime.exec('whoami')}" -v
```

> Monitor for server-side execution indicators, such as command output in responses or log anomalies. Avoid in production without authorization.

**Success Criteria**: Any evidence of command execution (e.g., user context in response) confirms full EL Injection exploitability.
