---
type: code
language: java
verified: true
tags:
  - ssti
  - pebble
  - payload
  - detection
platforms:
  - Web
  - Java
validated: true
---

# Pebble-SSTI-toUpperCase-Detection-Payload

## Code

```java
{{ SOMESTRING.TOUPPERCASE() }}
```

## Description

This code snippet is a basic detection payload for Server-Side Template Injection (SSTI) in Pebble template engine. It injects an expression that calls the toUpperCase() method on a string variable (SOMESTRING), which, if evaluated, converts the string to uppercase. Used to confirm if user input is processed as template code rather than literal text, serving as an initial probe before escalating to more dangerous payloads like command execution.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| SOMESTRING | The string value to convert to uppercase for testing evaluation | "hello" |

## Usage

Inject this payload into vulnerable input fields (e.g., search parameters, form fields) in a Pebble-based web application. For example, replace SOMESTRING with a known lowercase string and send via HTTP request. If the output shows uppercase, SSTI is confirmed. Typically used in reconnaissance phases of web pentesting; deliver via tools like curl or Burp Suite Repeater.

## Detection

- Web application logs showing template evaluation errors or unusual string manipulations.
- WAF alerts for template syntax like {{ }} or method calls like toUpperCase().
- Response analysis revealing evaluated expressions instead of raw input.
- Network traffic inspection for payloads containing template delimiters.

## Related

- [[procedures/Pebble-SSTI-Basic-Detection-Using-toUpperCase]]
- [[curl-pebble-ssti-test]]
