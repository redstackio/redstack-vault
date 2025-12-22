---
id: aabb13f3-cf57-464d-83e1-5050ad9b59e2
name: AWS-EKS-Service-Account-Token-Theft
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.509841+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Steal Application Access Token|T1528 - Steal Application Access
    Token]]
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/EKS Token Theft]]'
  - '[[tags/Initial Access]]'
  - '[[tags/RCE]]'
  - '[[tags/Kubernetes]]'
commands:
  - '[[commands/kubectl-cat-service-account-token]]'
  - '[[commands/rce-cat-eks-service-account-token]]'
platforms:
  - AWS
  - Kubernetes
  - Linux
tools: []
validated: true
---

# AWS-EKS-Service-Account-Token-Theft

## Summary

This procedure details how to steal a Kubernetes Service Account Token from an Amazon Elastic Kubernetes Service (EKS) cluster, enabling authentication to the Kubernetes API server for further access to cluster resources. It covers scenarios where the attacker has either direct kubectl access to a compromised pod or remote code execution (RCE) on a pod's web application, allowing token extraction for lateral movement or privilege escalation within the cloud environment.

## Description

In AWS EKS, service account tokens are automatically mounted in pods at /var/run/secrets/kubernetes.io/serviceaccount/token, providing short-lived JWTs for API server authentication. Attackers with pod-level access can extract this token to impersonate the service account, potentially accessing secrets, deploying malicious workloads, or exfiltrating data. This technique is particularly effective in multi-tenant clusters or after initial compromise via vulnerable applications running in pods. The procedure assumes the attacker has identified a target pod and namespace, using either legitimate kubectl (if credentials are stolen) or RCE exploitation to read the token file. Success grants cluster-wide access depending on the service account's RBAC permissions.

## Requirements

1. Access to a compromised pod in the EKS cluster, either via stolen kubeconfig/credentials for kubectl or a vulnerable RCE endpoint on the pod's application.
2. Knowledge of the target pod name and namespace (discoverable via prior enumeration).
3. For RCE method: A reachable web endpoint on the pod vulnerable to command injection (e.g., PHP eval or similar).
4. Tools like curl for remote exploitation or kubectl CLI configured with cluster access.

## Defense

- Implement pod security policies to restrict service account token mounting (use projected volumes with limited scopes).
- Enable AWS IAM roles for service accounts (IRSA) instead of long-lived tokens, and rotate tokens frequently.
- Monitor API server logs for anomalous service account usage and audit pod executions for unauthorized file reads.
- Use network policies to isolate pods and prevent external RCE exploitation; scan container images for vulnerabilities.

## Objectives

1. Extract the service account token from a target pod.
2. Authenticate to the Kubernetes API server using the stolen token.
3. Enable lateral movement, such as accessing other pods or cluster secrets.

## Instructions

### Step 1: Extract Token Using Kubectl (Direct Access Method)

**Context**: If the attacker has obtained cluster credentials (e.g., via stolen kubeconfig), use kubectl to execute a command inside the target pod and read the token file. This method requires specifying the pod and namespace accurately to avoid detection.

**Command** ([[commands/kubectl-cat-service-account-token]]):
```bash
kubectl exec $_POD_NAME -n $_NAMESPACE -- cat /var/run/secrets/kubernetes.io/serviceaccount/token
```

> This command executes 'cat' inside the pod to output the token contents. Replace $_POD_NAME with the target pod (e.g., my-app-abc123) and $_NAMESPACE with the namespace (e.g., default). The token is a JWT string; verify by decoding it (e.g., via jwt.io) to confirm issuer and audience point to the EKS cluster.

### Step 2: Extract Token Using RCE (Remote Exploitation Method)

**Context**: If direct kubectl access is unavailable but an RCE vulnerability exists in a web application running in the pod (e.g., command injection via URL parameter), craft a request to read the token file remotely. This bypasses the need for cluster credentials but requires the vulnerability to allow file reads or command execution.

**Command** ([[commands/rce-cat-eks-service-account-token]]):
```bash
curl "http://$_TARGET_URL?cmd=cat /var/run/secrets/kubernetes.io/serviceaccount/token"
```

> This sends a GET request to the vulnerable endpoint, injecting the 'cat' command to retrieve the token. Replace $_TARGET_URL with the pod's exposed URL (e.g., http://pod-ip:8080/rce.php). The response body will contain the token if successful; pipe to a file for decoding and use (e.g., curl ... > token.jwt). If the RCE only supports 'ls', first list the directory to confirm the file exists, then cat it.
