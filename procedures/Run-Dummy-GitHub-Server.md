---
id: proc-run-dummy-server
name: Run-Dummy-GitHub-Server
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.392Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
tags:
  - server-start
  - node.js
commands:
  - '[[commands/node-start-fake-server]]'
platforms:
  - Linux
tools:
  - '[[tools/Node.js]]'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Run-Dummy-GitHub-Server

## Summary

This procedure starts the Node.js-based fake GitHub API server to serve malicious responses during the GitLab import process.

## Description

The server responds to GitLab's Octokit queries with poisoned data for the /api/v3/repositories endpoint, enabling the Sawyer object injection. It runs on the attacker's specified IP and port, typically 80 for HTTP.

## Requirements

1. Prepared dummy server files from previous step
2. Public IP and open port on attacker machine
3. Node.js runtime

## Defense

Defensive measures and detection strategies:

- Whitelist allowed GitHub hostnames in import feature
- Log and alert on custom hostnames in import requests
- Network segmentation to prevent outbound to untrusted IPs

## Objectives

1. Host fake API endpoint accessible by GitLab
2. Serve pre-defined malicious repository responses
3. Await incoming import queries

## Instructions

### Step 1: Navigate to Server Directory

**Context**: Change to the extracted dummy server directory.

`cd /tmp/dummy-server`

**Expected Output**: In server directory.

### Step 2: Start the Server

**Context**: Launch Node.js server with IP and port arguments.

Execute [[commands/node-start-fake-server]]:

```bash
node ./index.js YOUR_IP YOUR_PORT
```

Replace YOUR_IP with public IP (e.g., 51.75.74.52) and YOUR_PORT with 80.

**Expected Output**: "Server listening on port YOUR_PORT".

### Step 3: Confirm Listening

**Context**: Verify the server is active.

Use `netstat -tlnp | grep :YOUR_PORT` or curl localhost.

**Expected Output**: Port bound to node process.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/node-start-fake-server]]

## Tools Used

- [[tools/Node.js]]

## Tags

- [[server-start]]
- [[tools/Node.js]]
