---
id: 922a582b-eb7d-4490-ac05-4254c249af35
name: Java-Server-Side-Template-Injection-to-Retrieve-Environment-Variables
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:39.334386+00:00'
updated_at: '2023-04-10T20:23:37.066452+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Template Injection|T1221 - Template Injection]]'
sub_techniques: []
tags:
  - '[[tags/Java]]'
  - '[[tags/Server-Side-Template-Injection]]'
  - '[[tags/Environment-Variables-Exfiltration]]'
commands: []
platforms:
  - Java
  - Web
tools: []
validated: true
---

# Java-Server-Side-Template-Injection-to-Retrieve-Environment-Variables

## Summary

This procedure demonstrates how to exploit a Java Server-Side Template Injection (SSTI) vulnerability to execute arbitrary code and retrieve the server's system environment variables. By injecting a malicious template expression into a user-controlled input field processed by a Java templating engine like Freemarker or Velocity, an attacker can invoke the `System.getenv()` method to dump sensitive configuration data such as API keys, database credentials, or paths, aiding in further reconnaissance or privilege escalation.

## Description

Server-Side Template Injection in Java applications occurs when user input is unsafely interpolated into template rendering without proper sanitization, allowing attackers to inject template syntax that gets evaluated on the server. This procedure focuses on retrieving environment variables, which often contain critical secrets in production environments. The attack targets web applications using templating engines where inputs like search fields, user profiles, or error messages are rendered via templates.

In a typical scenario, the attacker identifies a vulnerable endpoint (e.g., via fuzzing with template syntax like `${7*7}` to confirm injection), then crafts a payload to call `java.lang.System.getenv()` to enumerate all environment variables. This can reveal paths to sensitive files, tokens, or service credentials. The technique is particularly effective against misconfigured Java web apps on platforms like Tomcat or Spring Boot. Success depends on the templating engine supporting expression evaluation and the absence of security managers blocking system calls.

Expected outcomes include a map of key-value pairs displaying environment variables, which can be used for lateral movement or data exfiltration. This procedure assumes the attacker has network access to the application and can interact with vulnerable inputs.

## Requirements

1. Network access to a Java-based web application vulnerable to SSTI (e.g., via a browser or proxy like Burp Suite).
2. Knowledge of the templating engine in use (e.g., Freemarker uses `${}` syntax, Velocity uses `$`).
3. A tool for intercepting and modifying HTTP requests, such as [[tools/Burp-Suite]] or curl, to inject and test payloads.
4. Basic understanding of Java classes and template syntax to adapt payloads if needed.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization to block template syntax in user inputs, using allowlists for permitted characters.
- Disable dangerous features in templating engines, such as expression evaluation or access to `java.lang.System` classes via security policies.
- Deploy a Web Application Firewall (WAF) to detect and block common SSTI payloads, monitoring for anomalies like `${` or `T(` in requests.
- Enable application logging for template rendering errors and review server logs for unexpected system calls or environment accesses.
- Use runtime security tools like Java Security Manager or application-level guards to restrict access to sensitive APIs like `System.getenv()`.

## Objectives

1. Confirm SSTI vulnerability by injecting a benign test payload.
2. Inject a payload to execute `System.getenv()` and retrieve environment variables.
3. Analyze the output for sensitive information to support further attacks.
4. Exfiltrate or document the retrieved data without alerting defenses.

## Instructions

### Step 1: Identify Vulnerable Input Point

**Context**: Locate an input field in the application that is processed through a server-side template engine, such as a search box, username field, or dynamic content renderer. Test for SSTI by injecting a simple expression to verify code execution.

**Test Payload**: Submit input like `${7*7}` or `<#assign x=7*7>${x}</#assign>` (for Freemarker) and check if the response reflects the result (e.g., `49`).

> If the output shows the computed value instead of the literal input, SSTI is confirmed. This step ensures the injection point is exploitable before proceeding.

### Step 2: Craft and Inject the Environment Variables Payload

**Context**: Use the confirmed injection point to deliver a payload that invokes `java.lang.System.getenv()` to dump all environment variables. This method returns a map of all system env vars accessible to the Java process.

**Code** ([[codes/Java-SSTI-System-Getenv-Payload]]):

```java
${T(java.lang.System).getenv()}
```

> Inject this payload into the vulnerable field via an HTTP POST or GET request. For example, using a proxy, modify the request body or query parameter containing the input. The `T()` function refers to the class, allowing access to static methods like `getenv()`. Expected output is a rendered map (e.g., `{PATH=/usr/bin:... , JAVA_HOME=/opt/java:...}`) in the application's response, potentially truncated if large.

### Step 3: Analyze and Extract Output

**Context**: Review the server's response for the dumped environment variables. If the output is incomplete or escaped, iterate by targeting specific variables (e.g., `${T(java.lang.System).getenv('API_KEY')}`) or chaining payloads to write output to a file or exfiltrate via DNS.

> Parse the response for keys like `DB_PASSWORD`, `AWS_SECRET`, or custom app vars. Verify success by identifying at least one sensitive value. If blocked, test engine-specific variations (e.g., Velocity: `$math.mul(7,7)` for testing).
