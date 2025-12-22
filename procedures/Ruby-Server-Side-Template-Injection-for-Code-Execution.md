---
id: 86284845-39ad-4aa5-b785-e6a452a4810d
name: Ruby-Server-Side-Template-Injection-for-Code-Execution
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:40.228212+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - >-
    [[techniques/Exploitation for Client Execution|T1203 - Exploitation for
    Client Execution]]
sub_techniques: []
tags:
  - '[[tags/Ruby]]'
  - '[[tags/Ruby - Code execution]]'
  - '[[tags/Server Side Template Injection]]'
commands: []
platforms:
  - Web
  - Linux
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Ruby-Server-Side-Template-Injection-for-Code-Execution

## Summary

This procedure demonstrates how to exploit Server-Side Template Injection (SSTI) vulnerabilities in Ruby-based web applications using ERB and Slim template engines to achieve remote code execution. By injecting malicious template code, an attacker can execute system commands, read sensitive files like /etc/passwd, list directories, retrieve the current user, and enumerate environment variables, potentially leading to full server compromise.

## Description

Server-Side Template Injection in Ruby occurs when user-supplied input is unsafely interpolated into server-side templates without proper sanitization, allowing attackers to inject and execute arbitrary Ruby code. This vulnerability is common in frameworks like Ruby on Rails when using engines such as ERB (Embedded Ruby) or Slim. Once injected, the code runs with the privileges of the web server process, enabling file system access, command execution, and data exfiltration. This procedure targets Linux-based servers and assumes the application reflects user input in a template-rendered response, such as a search field or user profile page. Successful exploitation can reveal sensitive information or establish persistence, making it a high-impact technique in web application penetration testing.

## Requirements

1. Valid user input point in the application that is rendered via Ruby templates (e.g., ERB or Slim engine).
2. Network access to the vulnerable web application.
3. Knowledge of the template engine in use (test for ERB with '<%=', Slim with '#{').
4. A proxy tool like Burp Suite for intercepting and modifying requests (optional but recommended for precise injection).
5. Attacker-controlled environment to receive any exfiltrated data.

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs before passing them to template engines; use whitelisting for allowed characters and avoid direct interpolation.
- Disable or restrict template engine features in production, such as disabling eval-like execution in ERB or using safe mode in Slim.
- Implement a Web Application Firewall (WAF) to detect common SSTI payloads, including Ruby-specific patterns like '<%=', '%x', or 'system' calls.
- Enable application logging for template rendering errors and monitor for anomalous server-side code execution via process monitoring tools like auditd on Linux.
- Regularly audit and update Ruby frameworks to patch known SSTI vulnerabilities.

## Objectives

1. Inject malicious Ruby code into server-side templates to execute arbitrary system commands.
2. Retrieve sensitive server information, such as user lists, directory contents, current user identity, and environment variables.
3. Achieve remote code execution to facilitate further post-exploitation activities like data exfiltration or privilege escalation.

## Instructions

### Step 1: Inject ERB Payload for Command Execution and File Enumeration

**Context**: Identify an input field that renders user input via ERB templates (test with payloads like '<%= 1+1 %>' to confirm if '2' is output). Once confirmed, inject a payload to execute system commands, read files, and identify the current user. This step leverages Ruby's 'system', backticks, IO.popen, and Open3/Open4 libraries to run shell commands and capture output.

**Code** ([[codes/Ruby-ERB-SSTI-Command-Execution-and-File-Read]]):

```ruby
<%= system('cat /etc/passwd') %>
<%= `ls /` %>
<%= IO.popen('ls /').readlines()  %>
<% require 'open3' %><% @a,@b,@c,@d=Open3.popen3('whoami') %><%= @b.readline()%>
<% require 'open4' %><% @a,@b,@c,@d=Open4.popen4('whoami') %><%= @c.readline()%>
```

> Submit the payload via the vulnerable input (e.g., POST request to a search endpoint). The 'system' call executes 'cat /etc/passwd' and outputs user accounts directly in the response. Backticks (`ls /`) run 'ls /' and embed the directory listing. IO.popen opens a pipe for 'ls /' and readlines captures the output as an array. Open3.popen3 and Open4.popen4 spawn 'whoami' processes, capturing stdout to reveal the web server user (e.g., 'www-data'). If successful, the response will include the file contents, directory list, and username without errors.

### Step 2: Inject Slim Payload for Environment Variable Enumeration

**Context**: If the application uses the Slim template engine (test with '#{1+1}' outputting '2'), inject a payload to execute system commands and retrieve environment variables. This reveals potentially sensitive data like API keys or database credentials stored in the server's environment.

**Code** ([[codes/Ruby-Slim-SSTI-Environment-Variables]]):

```ruby
#{ %x|env| }
```

> The '%x|env|' syntax uses Ruby's backtick-like execution to run the 'env' command, capturing its output as a string embedded in the template response. Submit via the input point, and the response should display all environment variables. If variables contain secrets, note them for further exploitation. Verify no syntax errors in the response indicate successful injection.
