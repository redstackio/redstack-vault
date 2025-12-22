---
type: procedure
description: >-
  Bypass the Groovy sandbox in a server-side template injection vulnerability to
  achieve remote code execution.
verified: true
submitted: false
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Template Injection|T1221 - Template Injection]]'
sub_techniques: []
tags:
  - '[[tags/Groovy]]'
  - '[[tags/Groovy-Sandbox-Bypass]]'
  - '[[tags/Server-Side-Template-Injection]]'
commands: []
platforms:
  - Web
  - Java
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Groovy-Sandbox-Bypass-for-Server-Side-Template-Injection

## Summary

This procedure demonstrates how to bypass the Groovy sandbox in a server-side template injection (SSTI) vulnerability to execute arbitrary system commands on the target server. By leveraging Groovy's ASTTest annotation and ClassLoader, attackers can evade restrictions and achieve remote code execution (RCE), such as running diagnostic commands or launching applications.

## Description

Server-side template injection occurs when user input is unsafely interpolated into a template engine like Groovy, allowing code execution. Groovy sandboxes restrict dangerous operations, but they can be bypassed using compiler annotations like @ASTTest or dynamic class loading. This technique targets web applications using Groovy for templating (e.g., in Grails or custom engines). The attack assumes an identified SSTI point, such as a user-controlled template parameter in a web form or API endpoint. Successful bypass leads to RCE, enabling data exfiltration, persistence, or lateral movement. Defenders should validate inputs and disable dynamic code evaluation in templates.

## Requirements

1. Identified SSTI vulnerability in a Groovy-based web application (e.g., via fuzzing with payloads like '${7*7}').
2. Network access to the injection point (e.g., HTTP POST to a vulnerable endpoint).
3. Knowledge of the target OS (Linux/Unix for 'whoami', Windows for 'calc.exe').
4. Tools for intercepting and modifying requests, such as a proxy (though not required for basic injection).

## Defense

- Implement strict input sanitization and whitelisting for template variables to prevent code injection.
- Disable or configure Groovy sandboxes to block annotations like @ASTTest and restrict ClassLoader usage.
- Use a web application firewall (WAF) to detect anomalous payloads containing Groovy syntax (e.g., '${', '@ASTTest').
- Enable application logging for template rendering and monitor for unexpected command executions via process auditing.

## Objectives

1. Confirm sandbox bypass capability by executing a benign command like 'whoami' to identify the running user.
2. Escalate to interactive RCE by launching system applications, such as the calculator on Windows.
3. Validate RCE for further post-exploitation, such as file access or network operations.

## Instructions

### Step 1: Test Sandbox Bypass with Whoami Execution

**Context**: Inject a Groovy payload using the @ASTTest annotation to execute the 'whoami' command, confirming RCE and identifying the server user context. This step verifies the vulnerability without causing harm.

**Code** ([[codes/Groovy-ASTTest-Whoami-Execution]]):

```groovy
${ @ASTTest(value={assert java.lang.Runtime.getRuntime().exec("whoami")})
def x }
```

> Submit this payload via the vulnerable template input (e.g., in a form field or URL parameter). The exec() call runs 'whoami' on the server. Expected output appears in the application response, logs, or as a side effect (e.g., process creation). If the sandbox blocks it, refine the payload syntax based on error messages.

### Step 2: Escalate to Application Launch with Calculator Execution

**Context**: Use GroovyClassLoader to parse and execute a class with @ASTTest, bypassing restrictions to launch 'calc.exe' (Windows) or equivalent. This demonstrates full RCE capability for graphical or interactive commands.

**Code** ([[codes/Groovy-ClassLoader-ASTTest-Calculator-Execution]]):

```groovy
${ new groovy.lang.GroovyClassLoader().parseClass("@groovy.transform.ASTTest(value={assert java.lang.Runtime.getRuntime().exec(\"calc.exe\")})def x") }
```

> Inject this payload into the same SSTI point. The ClassLoader dynamically compiles and runs the annotated code, executing 'calc.exe' on the server. Monitor for process spawning via server logs or external tools. On non-Windows targets, replace 'calc.exe' with 'xcalc' or similar. Success is indicated by the application launching (visible if you have server access) or log entries showing the process.
