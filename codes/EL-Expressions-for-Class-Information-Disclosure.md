---
id: 0e6d2fc6-619f-4f39-8b20-10aded6b041e
type: code
language: el
verified: true
created_at: '2023-04-06T03:56:38.972780+00:00'
updated_at: '2023-04-10T20:23:39.688447+00:00'
tags:
  - expression-language-el
  - ssti-payload
  - java-discovery
platforms:
  - Web
  - Java
validated: true
---

# EL-Expressions-for-Class-Information-Disclosure

## Code

```el
${2.class}
${2.class.forName("java.lang.String")}
${''.getClass().forName('java.lang.Runtime').getMethods()[6].toString()}
```

## Description

This code snippet contains Expression Language (EL) payloads designed for Server-Side Template Injection (SSTI) in Java-based web applications. It discloses Java class information, including object class names, specific class loading, and method details from the Runtime class. These expressions target template context objects to perform software discovery without requiring additional tools.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | These are static EL expressions; no runtime variables. Indices like '2' or [6] may need adjustment based on the template context (e.g., change '2' to '0' or '1' if the object index differs). | N/A |

## Usage

Inject these expressions into vulnerable input fields processed by server-side templates (e.g., JSP parameters). Submit via HTTP POST/GET requests. Start with simpler expressions to confirm SSTI, then escalate to method enumeration. Use in reconnaissance phases to map the Java environment before attempting RCE via similar EL chains. Related procedure: [[procedures/EL-Injection-for-Java-Class-Information-Disclosure]].

## Detection

- Web application logs showing EL evaluation errors or unusual template outputs (e.g., class names in responses).
- WAF alerts for injection patterns like '${' or '.class' in inputs.
- Anomalous HTTP responses containing Java class/method strings.
- Increased server load from dynamic class loading queries.
