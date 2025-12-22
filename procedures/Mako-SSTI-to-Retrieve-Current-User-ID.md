---
id: ea739c3c-93a8-4f6c-ab1a-e601d94f253f
name: Mako-SSTI-to-Retrieve-Current-User-ID
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:40.072248+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - '[[sub-techniques/Unix-Shell|T1059.004 - Unix Shell]]'
tags:
  - '[[tags/Mako]]'
  - '[[tags/Server-Side-Template-Injection]]'
  - SSTI
  - RCE
commands: []
platforms:
  - Web
  - Linux
  - Python
tools: []
validated: true
---

# Mako-SSTI-to-Retrieve-Current-User-ID

## Summary

This procedure exploits a Server-Side Template Injection (SSTI) vulnerability in Mako templates to execute arbitrary Python code on the server, specifically retrieving the current user ID via the Unix 'id' command. It demonstrates how attackers can leverage unsafe user input in template rendering to achieve remote code execution (RCE) and gather system information for further exploitation.

## Description

Mako is a lightweight Python templating engine used in web applications to generate dynamic content. If user input is directly interpolated into Mako templates without proper sanitization, attackers can inject malicious template code to execute Python expressions or statements on the server. This procedure focuses on injecting a payload that imports the 'os' module, executes the 'id' command to retrieve the current user's UID, GID, and groups, and outputs the result. This can reveal the web server's running context, aiding in privilege assessment or lateral movement. The attack targets web applications where forms, URLs, or API parameters feed into Mako rendering, such as search fields or profile pages. Success depends on the injection point allowing Mako syntax like <% %> blocks and ${} expressions.

## Requirements

1. Access to a web application using Mako templates with an unsanitized user input field (e.g., via browser or API client).
2. Knowledge of the injection point (e.g., a parameter like ?search= or POST body field).
3. Network access to the target server (typically HTTP/HTTPS on port 80/443).
4. Optional: Intercepting proxy like Burp Suite to craft and test payloads.

## Defense

Defensive measures and detection strategies:

- Disable Python code execution in Mako by setting 'imports' and 'input_encoding' restrictions in the template environment.
- Implement strict input validation and sanitization, escaping user input with Mako's |n escape filter or using MarkupSafe.
- Use a sandboxed template environment (e.g., via Mako's TemplateLookup with restricted globals).
- Monitor application logs for anomalous template outputs or os/exec calls; deploy WAF rules to block SSTI patterns like '<%', '${', or 'os.popen'.
- Regularly audit and update web frameworks to patch known SSTI vulnerabilities.

## Objectives

1. Identify and confirm a Mako SSTI vulnerability in user-controllable template inputs.
2. Execute server-side code to retrieve the current user ID and group information.
3. Use the output to assess server privileges and plan subsequent attacks, such as privilege escalation if running as a low-privilege user.

## Instructions

### Step 1: Identify the Injection Point

**Context**: Locate a user input field that is rendered directly into a Mako template without escaping. Common points include search parameters, username fields, or dynamic content sections. Test for SSTI by injecting simple expressions like ${7*7} to check if the output is 49 (indicating template evaluation).

**Test Payload**: Submit input like `${7*7}` in the vulnerable parameter.

> If the response shows '49' instead of the literal string, SSTI is confirmed. This step verifies the vulnerability before attempting code execution.

### Step 2: Craft and Inject the Payload

**Context**: Construct a Mako template payload to import the os module, execute the 'id' command, and output the result. The payload uses <% %> for control blocks and ${} for expression substitution. Inject it into the confirmed parameter.

**Code** ([[codes/Mako-Template-User-ID-Exfiltration]]):

```python
<%
import os
x=os.popen('id').read()
%>
${x}
```

> Submit the payload via the web form, URL parameter, or API request (e.g., GET /search?q=<% import os; x=os.popen('id').read() %>${x}). The server will execute the code during template rendering and include the 'id' output in the response.

### Step 3: Verify and Analyze Output

**Context**: Check the response for the executed command output. The 'id' command typically returns something like 'uid=33(www-data) gid=33(www-data) groups=33(www-data)', indicating the web server's user context.

> If successful, the response will embed the user ID details. If errors occur (e.g., import denied), refine the payload or check for sandbox restrictions. Use this information to determine if escalation is needed (e.g., if not root).
