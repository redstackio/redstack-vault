---
type: procedure
description: >-
  Inject basic Ruby expressions into ERB templates to execute simple
  calculations, demonstrating server-side template injection in Ruby-based web
  applications.
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
sub_techniques: []
tags:
  - ssti
  - ruby
  - erb
  - injection
  - web
commands: []
tools: []
platforms:
  - Web
skill_level: beginner
impact_level: low
detection_risk: medium
verified: true
validated: true
---

# Ruby-ERB-Server-Side-Template-Injection-Basic-Calculations

## Summary

This procedure demonstrates a basic server-side template injection (SSTI) vulnerability in Ruby applications using ERB (Embedded Ruby) templates. By injecting simple Ruby expressions into unsanitized user input fields that are rendered as part of the template, an attacker can execute arbitrary code on the server, starting with harmless calculations like squaring a number or multiplying values. This serves as an entry point to more dangerous payloads and is common in Ruby on Rails applications with improper input handling.

## Description

Server-side template injection occurs when user-supplied input is directly embedded into a template engine without proper escaping or sanitization, allowing execution of code in the template's language. In Ruby applications, ERB is the default templating system in Rails, enabling dynamic content generation. An attacker identifies an input point (e.g., a search parameter or user profile field) that flows into an ERB-rendered view. By injecting ERB tags like `<%= expression %>`, the server evaluates the expression during rendering. This procedure focuses on basic arithmetic to confirm the vulnerability without causing harm, but it can escalate to file reads, command execution, or data exfiltration. Target environments include Ruby on Rails web apps (versions vulnerable to unsanitized ERB rendering, e.g., pre-5.0 without strong parameters). Expected outcomes include server-evaluated results displayed in the response, confirming code execution.

## Requirements

1. Access to a vulnerable Ruby web application with an input field rendered via ERB templates (e.g., a search box or form parameter).
2. Basic knowledge of Ruby syntax for crafting expressions.
3. Tools like a browser or proxy (e.g., Burp Suite) to manipulate and submit inputs; no special privileges needed beyond unauthenticated access.
4. Network connectivity to the target application.

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and validation using Rails' strong parameters or libraries like Loofah to escape ERB tags in user input.
- Use sandboxed template rendering (e.g., ERB's trim_mode or safe buffers) to prevent code execution.
- Deploy a web application firewall (WAF) to detect and block common SSTI payloads like `<%=`, `<%`, or Ruby keywords in inputs.
- Enable application logging for template rendering errors and monitor for anomalous outputs like unexpected numbers or strings from calculations.
- Regularly audit templates for direct user input interpolation and upgrade to secure versions of Rails with built-in protections.

## Objectives

1. Confirm SSTI vulnerability by injecting and executing a basic Ruby expression to perform a calculation.
2. Observe server-side evaluation of the injected code in the application response.
3. Establish a foundation for escalating to more complex payloads, such as reading environment variables or executing system commands.
4. Understand the risk of ERB templates in user-facing inputs leading to remote code execution.

## Instructions

### Step 1: Identify the Injection Point

**Context**: Locate a user input field in the web application that is directly interpolated into an ERB template without sanitization. Common points include search forms, profile fields, or URL parameters rendered in views (e.g., `/search?q=user_input` where `q` is embedded as `<%= @query %>`).

Inspect the application using browser developer tools or a proxy to trace how input flows to the template. Test with benign inputs like plain text to confirm rendering.

**Expected Output**: The input appears unchanged in the response, indicating direct template insertion.

### Step 2: Inject Basic Square Calculation Payload

**Context**: Craft and submit a simple ERB payload to calculate the square of a number (e.g., 7^2 = 49). This tests if the server evaluates Ruby expressions within `<%= %>` tags, confirming SSTI without side effects.

In the identified input field, enter: `<%= 7 * 7 %>`. Submit the form or request (e.g., via GET/POST). If using a proxy, intercept and modify the request body or parameters.

**Expected Output**: The response renders `49` instead of the literal string `<%= 7 * 7 %>`, proving server-side execution.

### Step 3: Test Multiplication with Variables

**Context**: Extend the injection to use Ruby variables or more complex expressions, such as multiplying two numbers. This verifies consistent execution and builds confidence in the vulnerability.

Inject: `<%= a = 7; a * a %>` (assigns 7 to `a` and squares it). Submit and observe. For multiplication of distinct values, try `<%= 5 * 9 %>` expecting `45`.

**Expected Output**: The calculated result (e.g., `49` or `45`) appears in the page output, with no syntax errors.

### Step 4: Verify and Escalate Safely

**Context**: Confirm the injection works across multiple inputs and check for limitations (e.g., output filtering). Do not proceed to destructive payloads in unauthorized testing.

Repeat injections with variations like `<%= Time.now %>` to output the current server time, confirming full expression evaluation.

**Expected Output**: Dynamic server data (e.g., timestamp) in the response, indicating arbitrary code execution capability.

> **Note**: If the output shows escaped tags (e.g., `&lt;%= 7 * 7 %&gt;`), the input is sanitized—vulnerability not present. Escalate only in controlled environments, linking to advanced procedures like [[Ruby-SSTI-Command-Execution]] for further exploitation.
