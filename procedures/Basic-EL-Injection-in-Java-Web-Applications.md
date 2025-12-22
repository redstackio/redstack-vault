---
id: a1c0aea9-9475-485f-96da-469c8667da7e
name: Basic-EL-Injection-in-Java-Web-Applications
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:38.953322+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - >-
    [[techniques/Command and Scripting Interpreter|T1059.001 - Command and
    Scripting Interpreter: Java]]
sub_techniques: []
tags:
  - '[[tags/Expression Language EL]]'
  - '[[tags/Expression Language EL - Basic injection]]'
  - '[[tags/Server Side Template Injection]]'
  - ssti
  - rce
  - java
commands:
  - '[[commands/inject-basic-el-expressions]]'
platforms:
  - Web
  - Java
tools: []
validated: true
---

# Basic-EL-Injection-in-Java-Web-Applications

## Summary

This procedure demonstrates how to perform a basic Expression Language (EL) injection attack on Java-based web applications, such as those using JSP or JSF. By injecting malicious EL expressions into user-controlled inputs, attackers can evaluate arbitrary expressions, access server-side data, and potentially achieve remote code execution (RCE) by invoking Java classes and methods.

## Description

Expression Language (EL) is a scripting component of JavaServer Pages (JSP) and JavaServer Faces (JSF) used for embedding dynamic content in web pages. EL injections occur when user input is directly interpolated into EL expressions without proper sanitization, allowing attackers to manipulate the evaluation context. This can lead to information disclosure (e.g., reading properties or beans), arithmetic operations, or RCE via static method calls on Java classes like Runtime or ProcessBuilder. The procedure targets public-facing web applications vulnerable to server-side template injection (SSTI) via EL. Success enables initial access or execution on the server, potentially escalating to full compromise. Prerequisites include identifying a reflection point for EL, such as a search parameter or form field that echoes back evaluated input.

## Requirements

1. Access to a vulnerable Java web application (e.g., JSP/JSF-based) with EL-enabled templating.
2. Knowledge of EL syntax, including immediate (${}) and deferred (#{}) evaluation modes.
3. Tools for web interception and manipulation, such as a proxy (e.g., Burp Suite).
4. Network access to the target application over HTTP/HTTPS.

## Defense

- Implement strict input validation and sanitization to escape or block EL metacharacters like ${, #, and T(.
- Use a web application firewall (WAF) to detect and block common SSTI payloads, including EL expressions.
- Apply least-privilege principles to the application server, restricting access to sensitive Java classes.
- Enable application-level logging for EL evaluation errors and monitor for anomalous server-side executions.
- Keep Java and web frameworks (e.g., Spring, Jakarta EE) updated with security patches.

## Objectives

1. Identify and confirm EL injection vulnerabilities in user inputs.
2. Evaluate basic EL expressions to disclose server properties or perform computations.
3. Escalate to RCE by invoking Java static methods for command execution.
4. Extract sensitive data or achieve persistence on the target server.

## Instructions

### Step 1: Identify Vulnerable Input Point

**Context**: Locate a parameter or field in the web application where user input is reflected and evaluated as an EL expression. Common points include search boxes, profile fields, or error messages in JSP/JSF pages. Use fuzzing to test for EL interpretation by submitting payloads like ${1+1} and observing if the output shows '2' instead of literal text.

Intercept requests using a proxy tool and modify inputs to include EL starters like ${ or #{

### Step 2: Test Basic EL Property Access and Evaluation

**Context**: Confirm EL processing by accessing implicit objects or performing simple evaluations. This step verifies the vulnerability and provides a foothold for more complex injections. Use the following to print property values and evaluate expressions.

**Command** ([[commands/inject-basic-el-expressions]]):

```bash
"${<property>}\n${1+1}\n\n#{<expression string>}\n#{1+1}\n\nT(<javaclass>)"
```

> Replace <property> with an accessible bean or implicit object (e.g., ${pageContext.request.remoteUser}), <expression string> with a deferred expression (e.g., #{system['java.version']}), and <javaclass> with a class like java.lang.System. Submit via POST/GET to the vulnerable endpoint. Expected output in the response: evaluated results like user info, '2' for arithmetic, or class details, confirming EL execution.

### Step 3: Escalate to Code Execution

**Context**: Once basic evaluation is confirmed, craft payloads to invoke static methods for RCE. For example, use T(java.lang.Runtime).getRuntime().exec('command') to run system commands. Monitor responses for execution indicators, such as command output or errors.

Embed the payload in the vulnerable input and resubmit. Verify success by checking for side effects like file creation or network callbacks.

### Step 4: Verify and Extract Data

**Context**: Use successful injections to read sensitive data, such as environment variables via ${system['os.name']} or session beans. Chain with further payloads to exfiltrate data or maintain access.

Parse the response for disclosed information and document findings for escalation.
