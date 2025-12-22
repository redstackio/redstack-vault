---
id: e6df3056-1a91-4b03-8469-52a2d68c8272
name: Kubernetes-RBAC-Pod-Exec-Privilege-Escalation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:01.284651+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - '[[techniques/Cloud-Accounts|T1078.004 - Cloud Accounts]]'
sub_techniques: []
tags:
  - Kubernetes
  - RBAC
  - Pod-Exec
  - Privilege-Escalation
commands:
  - '[[commands/kubectl-exec-interactive-shell]]'
platforms:
  - Kubernetes
  - Linux
tools: []
validated: true
---

# Kubernetes-RBAC-Pod-Exec-Privilege-Escalation

## Summary

This procedure enables an attacker with RBAC privileges in a Kubernetes cluster to execute arbitrary commands on target pods within the same namespace, facilitating lateral movement, data exfiltration, or further privilege escalation. It leverages the 'kubectl exec' command to spawn an interactive shell in a victim pod, assuming the attacker's service account or user has the necessary 'exec' permissions defined in the cluster's Role-Based Access Control (RBAC) policies.

## Description

In Kubernetes environments, RBAC controls access to cluster resources. If an attacker compromises a pod or gains kubectl access with a service account that has 'exec' or 'create' permissions on pods (e.g., via a ClusterRole binding allowing pod/exec), they can use 'kubectl exec' to run commands in other pods. This technique is common in multi-tenant clusters where over-permissive RBAC allows pod-to-pod interactions. The procedure assumes the attacker has initial access to the cluster API server via kubeconfig or in-cluster configuration and focuses on executing shells for post-exploitation. Success depends on RBAC configuration; default setups restrict this, but misconfigurations enable it. This can lead to full namespace compromise if chained with other techniques like pod privilege escalation.

## Requirements

1. Valid kubeconfig file or in-cluster access with a service account possessing RBAC permissions for 'pods/exec' on the target namespace (e.g., roleRef to a Role allowing verbs: ['create', 'get'] on resource: pods).
2. 'kubectl' tool installed and configured to communicate with the Kubernetes API server.
3. Network access to the cluster control plane (typically port 6443/TLS).
4. Knowledge of the target pod name and namespace.

## Defense

Defensive measures and detection strategies:

- Implement principle of least privilege in RBAC: Use PodSecurityPolicies or NetworkPolicies to restrict pod exec capabilities; audit bindings with 'kubectl auth can-i exec pod --namespace=ns'.
- Enable Kubernetes audit logging on the API server to monitor exec requests; use tools like Falco or auditd to alert on anomalous 'kubectl exec' from untrusted service accounts.
- Use admission controllers (e.g., OPA Gatekeeper) to enforce policies blocking exec from non-admin roles; regularly scan RBAC with kube-bench or Trivy.
- Monitor for unusual pod interactions via cluster monitoring tools like Prometheus with kube-state-metrics.

## Objectives

1. Gain interactive shell access to a target pod for command execution and lateral movement within the namespace.
2. Verify and exploit RBAC permissions to perform post-exploitation activities like data collection or further escalation.
3. Maintain access without triggering immediate alerts in monitored environments.

## Instructions

### Step 1: Verify RBAC Permissions

**Context**: Before attempting execution, confirm the current service account or user has the necessary permissions to exec into pods. This prevents errors and reveals the scope of privileges.

**Command** ([[commands/kubectl-auth-can-i-exec]]):
```bash
kubectl auth can-i exec pod -n $_NAMESPACE
```

> This command checks if the current context allows 'exec' on pods in the specified namespace. Run it to validate access; a 'yes' response indicates success. If 'no', the procedure cannot proceed without privilege escalation elsewhere.

### Step 2: Identify Target Pod

**Context**: List pods in the target namespace to select a victim pod for execution. This step ensures you target the right resource, such as a sensitive application pod.

**Command** ([[commands/kubectl-get-pods]]):
```bash
kubectl get pods -n $_NAMESPACE
```

> Output will display pod names, status, and restarts. Note the name of the target pod (e.g., 'app-pod-abc123'). Expected: A table listing available pods. If no pods are listed or access is denied, adjust RBAC or namespace.

### Step 3: Execute Interactive Shell

**Context**: Use kubectl to spawn an interactive shell in the target pod, allowing arbitrary command execution within its container environment. This achieves the core escalation by leveraging existing RBAC privileges.

**Command** ([[commands/kubectl-exec-interactive-shell]]):
```bash
kubectl exec -it $_POD_NAME -n $_NAMESPACE -- sh
```

> This opens a shell (sh or bash if available) in the pod's primary container. Replace $_POD_NAME with the actual pod name (e.g., 'app-pod-abc123') and $_NAMESPACE with the namespace (e.g., 'default'). Expected: An interactive prompt inside the pod, such as '/ # ' or 'root@pod:~#'. From here, run commands like 'ls /', 'cat /etc/passwd', or network tools for further actions. Exit with 'exit' or Ctrl+D. Success confirms lateral movement capability.
