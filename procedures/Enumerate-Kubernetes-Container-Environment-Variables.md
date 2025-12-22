---
id: f1cd363b-1843-4c0f-b05a-bbfe41c807c0
name: Enumerate-Kubernetes-Container-Environment-Variables
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:01.061770+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Container Environment]]'
  - '[[tags/Environment Variables]]'
  - '[[tags/Kubernetes]]'
commands:
  - '[[commands/Extract-Kubernetes-Env-Redis-Master-Service-Host]]'
  - '[[commands/Extract-Kubernetes-Env-Redis-Master-Service-Port]]'
  - '[[commands/Extract-Kubernetes-Env-Redis-Master-Port]]'
  - '[[commands/Extract-Kubernetes-Env-Redis-Master-TCP]]'
platforms:
  - Kubernetes
  - Linux
tools: []
validated: true
---

# Enumerate-Kubernetes-Container-Environment-Variables

## Summary

This procedure demonstrates how to enumerate environment variables within a Kubernetes container using kubectl to access a running pod. Environment variables in Kubernetes can contain sensitive configuration data such as database credentials, API keys, or service endpoints, which attackers can exploit for lateral movement or privilege escalation within the cluster.

## Description

In Kubernetes, environment variables are often injected into containers via pod specifications, config maps, or secrets. However, misconfigurations can lead to sensitive information being exposed directly in env vars rather than mounted as secure volumes. This procedure involves executing a shell command inside a target pod to dump all environment variables, allowing identification of valuable data like service hosts, ports, or tokens. It is particularly useful in container escape or lateral movement scenarios where initial pod access has been gained, such as through a vulnerable application or misconfigured RBAC. The technique reveals internal cluster topology and credentials without needing elevated privileges beyond pod execution.

## Requirements

1. kubectl tool installed and configured with cluster access (e.g., via kubeconfig file).
2. Permissions to execute commands in the target pod (typically via service account or RBAC role allowing exec).
3. Name or selector for the target pod.
4. Network access to the Kubernetes API server.

## Defense

- Avoid storing sensitive data in environment variables; use Kubernetes Secrets and mount them as volumes instead.
- Implement RBAC policies to restrict exec access to pods (e.g., deny exec for non-admin roles).
- Enable audit logging for kubectl exec commands and monitor for anomalous pod interactions.
- Use tools like Falco or auditd inside containers to detect env var dumps.

## Objectives

1. Dump all environment variables from a target Kubernetes pod.
2. Identify and extract sensitive variables, such as service endpoints or credentials.
3. Map internal cluster services for potential lateral movement.

## Instructions

### Step 1: List All Environment Variables in the Pod

**Context**: Use kubectl to execute the `env` command inside the target pod, which outputs all current environment variables. This provides a complete view of the container's configuration, including any injected secrets or service discovery vars.

**Command** ([[commands/kubectl-exec-list-pod-env-vars]]):
```bash
kubectl exec $_POD_NAME -- env
```

> Replace $_POD_NAME with the name of the target pod (e.g., 'redis-master'). This command streams the env vars to stdout. Pipe the output to a file for analysis if needed (e.g., `| tee env_dump.txt`). If the pod has multiple containers, specify the container with `-c $_CONTAINER_NAME`.

**Expected Output**: A list of KEY=VALUE pairs, such as:
```
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
REDIS_MASTER_SERVICE_HOST=10.0.0.11
REDIS_MASTER_SERVICE_PORT=6379
REDIS_MASTER_PORT=tcp://10.0.0.11:6379
... (other vars)
```

### Step 2: Extract Specific Environment Variables for Service Discovery

**Context**: From the full env dump, filter for variables related to internal services (e.g., Redis master in a stateful set). This helps pinpoint endpoints for further exploitation, like connecting to a database with exposed creds. Use grep to isolate vars by pattern.

**Command** ([[commands/Extract-Kubernetes-Env-Redis-Master-Service-Host]]):
```bash
kubectl exec $_POD_NAME -- env | grep REDIS_MASTER_SERVICE_HOST
```

> This extracts the host for the Redis master service. Expected output: `REDIS_MASTER_SERVICE_HOST=10.0.0.11`. Use this IP for targeting internal services.

**Command** ([[commands/Extract-Kubernetes-Env-Redis-Master-Service-Port]]):
```bash
kubectl exec $_POD_NAME -- env | grep REDIS_MASTER_SERVICE_PORT
```

> Extracts the port. Expected output: `REDIS_MASTER_SERVICE_PORT=6379`.

**Command** ([[commands/Extract-Kubernetes-Env-Redis-Master-Port]]):
```bash
kubectl exec $_POD_NAME -- env | grep REDIS_MASTER_PORT
```

> Full port URI. Expected output: `REDIS_MASTER_PORT=tcp://10.0.0.11:6379`.

**Command** ([[commands/Extract-Kubernetes-Env-Redis-Master-TCP]]):
```bash
kubectl exec $_POD_NAME -- env | grep REDIS_MASTER_PORT_6379_TCP
```

> TCP-specific details. Expected output: `REDIS_MASTER_PORT_6379_TCP=tcp://10.0.0.11:6379`.

### Step 3: Analyze for Sensitive Information

**Context**: Review the dumped variables for patterns indicating secrets (e.g., vars starting with DB_, API_, TOKEN_). If credentials are found, test them against discovered services.

**Instructions**: Manually inspect the output or use additional greps like `grep -i 'pass\|key\|token'`. If a var contains a password, note it for use in subsequent procedures like database access.

**Expected Output**: Identification of sensitive vars, e.g., `DB_PASSWORD=secret123`.

**Success Indicators**:
- Full env dump retrieved without errors.
- Specific service vars (e.g., Redis host/port) extracted.
- Any credentials or tokens identified for further use.
