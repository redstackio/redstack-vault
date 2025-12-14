---
id: proc-398285-start-serve
tags:
  - web-server
  - hosting
type: procedure
tools:
  - '[[tools/serve]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/serve-start]]'
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:46.929Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Start-Serve-Server-for-Directory-Hosting

## Summary

This procedure launches the serve HTTP server in a directory containing a malicious filename, activating the vulnerable directory listing that renders unsanitized HTML and triggers the stored XSS payload.

## Description

Serve v9.6.0 uses serve-handler to generate directory indexes, inserting filenames into <a href="filename">filename</a> without escaping, allowing tag injection. Running serve exposes http://localhost:5000, where viewing the root triggers the XSS. This is key for demonstrating the vulnerability in a local or shared hosting scenario.

## Requirements

1. Serve module installed globally
2. Port 5000 free
3. Directory with malicious file present

## Defense

Defensive measures and detection strategies:

- Update to patched serve versions (>11.3.2)
- Configure servers to avoid directory listings (use index files)
- Monitor for unexpected HTTP servers on local ports

## Objectives

1. Host the directory to enable listing access
2. Expose the unsanitized filename rendering
3. Facilitate XSS execution on client browsers

## Instructions

### Step 1: Launch Serve in Target Directory

**Context**: Start the server from the directory with the XSS file to serve static content and listings.

**Command** ([[commands/serve-start]]):
```bash
serve
```

> Defaults to current directory on port 5000. Expected output: "Accepting connections at http://localhost:5000" and server logs.

### Step 2: Verify Server Status

**Context**: Confirm the server is running and accessible.

**Command** (bash):
```bash
curl http://localhost:5000
```

> Fetches the directory listing HTML. Expected output: Raw HTML with injected payload visible in source.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/serve-start]]

## Tools Used

- [[tools/serve]]

## Tags

- web-server
- hosting
