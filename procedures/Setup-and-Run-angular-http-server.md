---
id: proc-uuid-002
tags:
  - path-traversal
  - node-js
  - server-setup
type: procedure
tools:
  - '[[tools/angular-http-server]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/angular-http-server-run]]'
  - '[[commands/direct-angular-http-server-run]]'
verified: false
platforms:
  - Node.js
  - Linux
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:16.728Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-and-Run-angular-http-server

## Summary

This procedure sets up a basic static HTML file and launches the vulnerable angular-http-server to serve it, creating an exploitable HTTP server on port 8080.

## Description

After installation, create a simple index.html as the entry point for the single-page application. Run the server with the --path option to specify the root directory. The vulnerability arises because the server uses fs.stat and fs.readFileSync on unsanitized paths, allowing traversal attacks. This setup mimics a development environment where the module might be used.

## Requirements

1. angular-http-server installed via npm
2. Current directory writable for creating index.html
3. Port 8080 free
4. Node.js runtime available

## Defense

Defensive measures and detection strategies:

- Restrict server to bind only to localhost during development
- Use secure alternatives like http-server with path validation
- Firewall rules to block unexpected port access
- Scan for vulnerable dependencies regularly

## Objectives

1. Create test content for serving
2. Start the vulnerable server
3. Confirm readiness for exploitation

## Instructions

### Step 1: Create Index File

**Context**: Generate a basic HTML file to serve as the application's index, ensuring the server has content to host.

**Command** (Manual file creation):
```bash
echo '<html><body><h1>Test SPA</h1></body></html>' > index.html
```

> This creates a simple index.html. Expected output: File created in current directory.

### Step 2: Run the Server

**Context**: Launch the server to serve the current directory, exposing the path traversal vulnerability.

**Command** ([[commands/angular-http-server-run]]):
```bash
angular-http-server --path ./
```

> Starts the server on port 8080. Expected output: Logs like 'Path specified: ./', 'Using index.html', 'Listening on 8080'.

### Step 3: Alternative Direct Run

**Context**: For detailed logging, run the script directly from node_modules.

**Command** ([[commands/direct-angular-http-server-run]]):
```bash
./node_modules/angular-http-server/angular-http-server.js --path ./
```

> Provides verbose server output during exploitation. Expected output: Similar startup logs plus file send details.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/angular-http-server-run]]
- [[commands/direct-angular-http-server-run]]

## Tools Used

- [[tools/angular-http-server]]

## Tags

- path-traversal
- server-launch
