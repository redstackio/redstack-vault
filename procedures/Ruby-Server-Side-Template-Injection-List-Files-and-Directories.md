---
id: 7f8f9f5b-3311-4d56-9702-31c4bbdfa83c
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:40.201972+00:00'
updated_at: '2023-10-10T20:23:50.436321+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - ssti
  - ruby
  - file-discovery
  - server-side-template-injection
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Ruby-Server-Side-Template-Injection-List-Files-and-Directories

## Summary

This procedure demonstrates how to exploit a server-side template injection (SSTI) vulnerability in a Ruby-based web application to list files and directories in the root directory. By injecting malicious Ruby code into a user-controlled template parameter, an attacker can execute arbitrary system commands on the server, revealing sensitive file structures and potentially enabling further reconnaissance or privilege escalation.

## Description

Server-side template injection in Ruby applications, such as those using ERB (Embedded Ruby) templates in Ruby on Rails, occurs when user input is directly interpolated into a template without proper sanitization. This allows attackers to inject Ruby code that gets evaluated on the server. In this procedure, the focus is on using the Dir.entries method to enumerate the root directory ('/'), which can expose system files, configuration details, or paths to other sensitive resources. This technique is particularly effective against applications that render dynamic content from user-supplied data, such as search fields, user profiles, or error messages. Successful execution provides an array of file and directory names, aiding in mapping the target's filesystem for subsequent attacks like data exfiltration or lateral movement. The procedure assumes the attacker has identified a vulnerable injection point through prior testing.

## Requirements

1. Access to a web application vulnerable to SSTI in a Ruby template engine (e.g., ERB in Rails).
2. Knowledge of the injection point, such as a parameter in a GET/POST request that is rendered as a template.
3. A tool like Burp Suite or curl for crafting and sending requests (though not strictly required, recommended for interception).
4. Basic understanding of Ruby syntax to craft payloads.
5. Network access to the target application.

## Defense

- Sanitize and validate all user inputs before interpolating into templates; use safe rendering methods like html_safe in Rails.
- Implement content security policies (CSP) and output encoding to prevent code execution.
- Use allowlists for permitted template variables and avoid direct user input in template contexts.
- Monitor application logs for anomalous Ruby evaluations or unexpected file access patterns.
- Employ web application firewalls (WAFs) tuned to detect SSTI payloads, such as common Ruby expressions like '{{', '%', or Dir calls.

## Objectives

1. Identify and confirm an SSTI vulnerability in the Ruby application.
2. Inject Ruby code to execute Dir.entries('/') and retrieve the root directory listing.
3. Analyze the output to identify sensitive files or directories for further exploitation.

## Instructions

### Step 1: Identify the Injection Point

**Context**: Locate a user-controlled input that is processed as a Ruby template, such as a search query or profile field. Test for SSTI by injecting a simple expression like "<%= 1+1 %>" to see if it evaluates to "2" in the response.

> Send a request with the test payload via your browser or a tool like curl. If the output shows the evaluated result instead of the literal string, SSTI is confirmed.

### Step 2: Craft the Basic Payload

**Context**: Prepare the Ruby code to list root directory contents using the Dir.entries method, which returns an array of all entries including files and subdirectories.

**Code** ([[codes/Ruby-SSTI-List-Files-Directories]]):

```ruby
<%= Dir.entries('/').to_s %>
```

> This wraps the Dir.entries('/') in ERB tags (<%= %>) to output the result as a string. The .to_s converts the array to a readable string. Expected output in the response: A string like "[\".\", \"..\", \"bin\", \"boot\", ...]", revealing directory names. Note the escaped quotes in the array.

### Step 3: Inject and Execute the Payload

**Context**: Submit the payload through the identified injection point, such as in a URL parameter (e.g., ?search=<%= Dir.entries('/').to_s %>) or POST body. Intercept and modify if needed to bypass basic filters.

> Use a proxy tool to send the request. If filters block ERB tags, try alternative syntax like "#{Dir.entries('/').to_s}" for string interpolation. Expected output: The server-rendered response includes the directory listing.

### Step 4: Interpret and Verify Output

**Context**: Review the response for the array of entries. Ignore "." (current) and ".." (parent); focus on actual files/directories like /etc, /var, or application-specific paths.

> If the listing appears garbled or incomplete, adjust the payload to use Dir.glob('*') for non-recursive listing or p Dir.entries('/') for pretty-printing. Success is confirmed if system directories are visible, indicating arbitrary code execution.
