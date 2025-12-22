---
id: c1705f5d-bf96-4fc5-9bab-722f78fb8356
type: code
language: Java
verified: true
created_at: '2023-04-06T03:56:39.332879+00:00'
updated_at: '2023-04-10T20:23:37.094986+00:00'
tags:
  - ssti
  - java
  - payload
  - environment-variables
platforms:
  - Java
  - Web
validated: true
---

# Java-SSTI-System-Getenv-Payload

## Code

```java
${T(java.lang.System).getenv()}
```

## Description

This code snippet is a Server-Side Template Injection (SSTI) payload for Java templating engines like Freemarker. It uses the `${}` expression syntax to invoke the static `getenv()` method on `java.lang.System`, returning a map of all system environment variables accessible to the Java process. When injected into a vulnerable template-rendered input, it executes on the server and includes the dumped variables in the HTTP response, potentially exposing sensitive configuration data.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static payload with no substitutable variables; adapt syntax for specific engines if needed (e.g., prepend `<#ftl>` for Freemarker). | N/A |

## Usage

Inject this payload into user-controlled inputs processed by server-side templates, such as form fields or URL parameters in Java web apps. First, confirm SSTI with a test like `${7*7}`. Then, submit via browser, curl, or a proxy like Burp Suite. For targeted retrieval, modify to `${T(java.lang.System).getenv('SPECIFIC_VAR')}`. Used in reconnaissance phases to gather secrets for escalation.

Related Procedure: [[procedures/Java-Server-Side-Template-Injection-to-Retrieve-Environment-Variables]]

## Detection

- Monitor web application logs for template evaluation errors or unusual expressions containing `T(` or `getenv`.
- WAF rules to block payloads with `${`, `T(java.lang`, or `System` in requests.
- Application-level auditing of rendered templates for unexpected content like environment dumps.
- Runtime protections like Java Security Manager to deny access to `System.getenv()`.
