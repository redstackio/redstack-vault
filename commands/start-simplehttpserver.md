---
id: cmd-uuid-001
name: start-simplehttpserver
type: command
executor: bash
data: ./node_modules/simplehttpserver/cli.js
output: >-
  Listening 0.0.0.0:8000 web root dir
  /Users/bl4de/playground/node_bugbounty_playground
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.529Z'
platforms:
  - Node.js
  - Linux
  - macOS
tags:
  - server-start
  - http-server
verified: false
validated: true
submitted: true
---

# start-simplehttpserver

## Command

```bash
./node_modules/simplehttpserver/cli.js
```

## Description

Starts the simplehttpserver Node.js module's CLI to run a basic HTTP server serving the current directory on port 8000, useful for reproducing vulnerabilities like stored XSS in directory listings.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No flags; runs with defaults binding to 0.0.0.0:8000 | N/A |

## Examples

### Basic Usage

```bash
./node_modules/simplehttpserver/cli.js
```

### Advanced Usage

No advanced options; source code shows fixed port and binding.

## Expected Output

Server confirmation message like "Listening 0.0.0.0:8000 web root dir [current path]", followed by handling incoming requests until interrupted.

## Related

- [[procedures/Start-simplehttpserver-with-Malicious-File]]
