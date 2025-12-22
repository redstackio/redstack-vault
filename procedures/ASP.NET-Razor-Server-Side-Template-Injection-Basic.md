---
id: 33642f6f-aa7b-46ce-8514-5e5c602ad75e
name: ASP.NET-Razor-Server-Side-Template-Injection-Basic
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:38.901483+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Template Injection|T1221 - Template Injection]]'
sub_techniques: []
tags:
  - '[[tags/ASP.NET Razor]]'
  - '[[tags/Server Side Template Injection]]'
  - ssti
  - razor-injection
commands: []
platforms:
  - Web
  - ASP.NET
tools: []
validated: true
---

# ASP.NET-Razor-Server-Side-Template-Injection-Basic

## Summary

This procedure demonstrates a basic server-side template injection (SSTI) attack in ASP.NET Razor, a templating engine used for dynamic web pages. By injecting malicious Razor syntax into user-controlled input fields that are rendered as templates, an attacker can execute arbitrary C# code on the server, leading to outcomes like data disclosure or remote code execution. The example uses a simple arithmetic operation to verify code execution without causing harm.

## Description

ASP.NET Razor allows embedding C# code within HTML using syntax like @{ ... }. If user input is directly interpolated into Razor templates without sanitization, attackers can inject code blocks that execute on the server during rendering. This vulnerability is common in legacy or misconfigured ASP.NET applications where dynamic content generation lacks proper escaping.

In this scenario, the attack targets an input field (e.g., a search box or user profile field) that feeds into a Razor view. The injected code declares variables, performs an addition, and outputs the result, proving arbitrary execution. More advanced attacks could escalate to file reads, command execution, or privilege escalation. This technique requires identifying reflection points where input becomes template code and testing for execution.

## Requirements

1. Access to a vulnerable ASP.NET Razor application with user-controlled input rendered as templates (e.g., via a web form or API endpoint).
2. Knowledge of the application's structure to locate injectable points (e.g., using browser developer tools or proxy interception).
3. No special privileges needed initially, but server-side execution assumes the web app's process context (e.g., IIS worker process).

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all user inputs before rendering in templates; use Html.Encode or Razor's @Html.Raw only for trusted content.
- Implement content security policies (CSP) and output encoding to prevent code injection.
- Regularly monitor and analyze server logs for suspicious activity, such as unexpected C# execution traces or error patterns indicating injection attempts.
- Apply strict access controls and least privilege principles to the web application pool, limiting file system and network access.

## Objectives

1. Execute arbitrary C# code on the server via Razor template injection.
2. Demonstrate the impact of SSTI by outputting computed results to confirm execution.
3. Verify vulnerability without causing disruption, setting the stage for more advanced exploitation.

## Instructions

### Step 1: Identify Injectable Input Point

**Context**: Locate a user input field in the ASP.NET application that is directly rendered into a Razor template without escaping. Common points include search forms, comment sections, or dynamic content generators. Use browser inspection or a proxy to observe how input is processed.

Inspect the page source or network requests to confirm input flows to a .cshtml file.

### Step 2: Craft Basic Injection Payload

**Context**: Test for SSTI by injecting a simple Razor code block that performs an arithmetic operation and outputs the result. This verifies code execution without side effects.

Construct the payload as: `@{int a = 1; int b = 2; int c = a + b;}@c`

- The @{ ... } block executes the C# code.
- @c outputs the result (3) to the response.

### Step 3: Inject and Submit Payload

**Context**: Submit the payload via the identified input field (e.g., in a POST request or form submission). If using a proxy like Burp Suite, intercept and modify the request body.

Submit the input containing the payload. For example, if the field is a search query, enter the full string.

### Step 4: Verify Execution

**Context**: Check the application response for the output of the injected code, confirming server-side execution.

Expected success: The page renders the number 3 (or computed value) where the input would normally appear, instead of the raw payload string.

If no output appears, try variations like wrapping in quotes or testing simpler payloads like `@{1+1}` to output 2.
