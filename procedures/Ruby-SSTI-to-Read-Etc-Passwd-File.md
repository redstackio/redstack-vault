---
id: 7d93b700-b804-4b2c-9c55-f3e63242c2c5
name: Ruby-SSTI-to-Read-Etc-Passwd-File
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:40.182983+00:00'
updated_at: '2023-04-10T20:23:34.415425+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploit-Public-Facing-Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/Ruby]]'
  - '[[tags/Server-Side-Template-Injection]]'
  - '[[tags/File-Read]]'
  - ssti
  - ruby
  - rce
commands: []
platforms:
  - Web
  - Linux
tools: []
validated: true
---

# Ruby-SSTI-to-Read-Etc-Passwd-File

## Summary

This procedure demonstrates how to exploit a Server-Side Template Injection (SSTI) vulnerability in a Ruby-based web application using ERB templates to read the contents of the /etc/passwd file on a Linux server. By injecting a malicious template payload, an attacker can execute arbitrary Ruby code on the server, retrieving sensitive user account information for further reconnaissance or privilege escalation.

## Description

Server-Side Template Injection (SSTI) occurs when user input is unsafely embedded into a template engine, allowing attackers to inject and execute code in the application's rendering context. In Ruby applications using ERB (Embedded Ruby), vulnerable parameters in views or controllers can be exploited to run system-level operations. This procedure targets reading /etc/passwd, a common Linux file containing user account details, which can reveal usernames, home directories, and shell types. The attack assumes the application processes user-supplied input through an ERB template without proper sanitization. Success provides insight into system users, aiding in lateral movement or identifying privileged accounts. This technique is particularly effective against Ruby on Rails or Sinatra apps with dynamic templating.

## Requirements

1. Access to a web application vulnerable to SSTI in a Ruby ERB context (e.g., via a search field, user profile, or dynamic content parameter).
2. Knowledge of the template engine (confirmed as ERB/Ruby) through prior testing.
3. A tool like Burp Suite or curl for sending crafted HTTP requests.
4. Target server running Linux, where /etc/passwd is accessible to the web application process.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization for all user inputs passed to template engines, using libraries like Loofah for Rails to escape ERB expressions.
- Disable or restrict template engine features that allow code execution, such as setting ERB's trim_mode to prevent injection.
- Use web application firewalls (WAFs) like ModSecurity to detect common SSTI payloads, including Ruby-specific patterns like '<%= %>'.
- Monitor server logs for anomalous file reads (e.g., access to /etc/passwd) and enable runtime application self-protection (RASP) tools.
- Apply least privilege to the web server process, restricting file system access via AppArmor or SELinux profiles.

## Objectives

1. Inject a Ruby ERB payload to execute file read operations on the server.
2. Retrieve contents of /etc/passwd to enumerate system users and account details.
3. Gather reconnaissance data for subsequent attacks, such as identifying admin users or weak configurations.

## Instructions

### Step 1: Identify the Injection Point

**Context**: Locate a parameter in the web application that is processed through an ERB template, such as a search query, username field, or dynamic content renderer. Test for SSTI by injecting a simple probe like '<%= 1+1 %>' and checking if the response evaluates to '2' instead of literal text.

**Instructions**: Use a proxy tool like Burp Suite to intercept and modify requests. Submit the probe payload and observe the response for code execution.

> If the probe succeeds, proceed to payload injection. If not, the parameter may not be vulnerable or uses a different template engine.

### Step 2: Inject the File Read Payload

**Context**: Once confirmed, inject the Ruby code to read /etc/passwd using the File.open method, which opens and reads the file contents directly within the ERB context.

**Code** ([[codes/Ruby-ERB-File-Read-Etc-Passwd]]):

```ruby
<%= File.open('/etc/passwd').read %>
```

> This payload executes during template rendering, outputting the file contents in the HTTP response. The '<%= %>' tags ensure the result is displayed rather than just executed. Expected output includes lines like 'root:x:0:0:root:/root:/bin/bash', revealing user accounts.

### Step 3: Verify and Extract Output

**Context**: Analyze the response for the file contents. If truncated or filtered, chain additional payloads to exfiltrate data via alternative channels like DNS or external requests.

**Instructions**: Capture the full response and parse for user entries. Cross-reference with known system users to identify potential targets.

> Success is indicated by the presence of hashed passwords or user details in the output. If access is denied, the web process may lack permissions—escalate by chaining to command execution payloads.
