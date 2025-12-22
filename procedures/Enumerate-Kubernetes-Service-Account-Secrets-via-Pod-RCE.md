---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Kubernetes]]'
  - '[[tags/RCE]]'
  - '[[tags/Discovery]]'
commands:
  - '[[commands/rce-ls-kubernetes-secrets-directory]]'
  - '[[commands/rce-cat-kubernetes-service-account-token]]'
platforms:
  - AWS
  - Kubernetes
  - Linux
tools: []
validated: true
---

# Enumerate-Kubernetes-Service-Account-Secrets-via-Pod-RCE

## Summary

This procedure demonstrates how to enumerate Kubernetes service account secrets by exploiting remote code execution (RCE) within a compromised pod in an AWS EKS cluster. It involves listing the mounted secrets directory and extracting the service account token, which can then be used to authenticate to the Kubernetes API server for further discovery and lateral movement.

## Description

In Kubernetes clusters like AWS EKS, service accounts are automatically mounted as volumes in pods at `/var/run/secrets/kubernetes.io/serviceaccount`, containing files such as `token` (JWT for API authentication), `ca.crt` (cluster CA certificate), `namespace`, and others. If an attacker gains RCE in a pod—often via a vulnerable web application running in the cluster—they can execute commands to list and read these files. This technique maps to MITRE ATT&CK's Cloud Service Discovery (T1526) under the Discovery tactic, as it reveals credentials for cluster-wide access. It is typically used after initial access via application vulnerabilities and enables escalation to cluster administration if the service account has elevated RBAC permissions.

## Requirements

1. Remote code execution (RCE) access within a running pod in the AWS EKS cluster, such as through a vulnerable PHP endpoint or similar.
2. The pod must be associated with a service account that has the secrets volume mounted (default behavior).
3. Network access to the RCE endpoint from the attacker's machine.
4. Basic knowledge of Kubernetes architecture and JWT tokens.

## Defense

- Secure containerized applications against RCE by applying patches, input validation, and web application firewalls (WAFs).
- Implement strict RBAC policies to limit service account permissions; use workload identity federation in AWS to avoid long-lived tokens.
- Enable Kubernetes audit logging and monitor API server access logs for anomalous authentications from pod IPs.
- Use tools like Falco or AWS GuardDuty to detect unexpected command executions in pods.

## Objectives

1. List the contents of the service account secrets directory to identify available credentials.
2. Extract the service account token for authentication to the Kubernetes API.
3. Validate the token's usability for further cluster discovery.

## Instructions

### Step 1: List the Kubernetes Service Account Secrets Directory

**Context**: Begin by using the RCE vulnerability to list the files in the mounted secrets directory. This reveals the available secrets, such as the token and CA certificate, confirming the presence of service account credentials.

**Command** ([[commands/rce-ls-kubernetes-secrets-directory]]):
```bash
curl -s "$_RCE_ENDPOINT?cmd=ls%20/var/run/secrets/kubernetes.io/serviceaccount"
```

This command sends the `ls` payload via the RCE endpoint. The `%20` URL-encodes the space in the command. Success is indicated by a directory listing showing files like `token`, `ca.crt`, `namespace`, and `token`.

### Step 2: Extract the Service Account Token

**Context**: Once the directory is listed, read the `token` file to obtain the JWT, which can be used to query the Kubernetes API server. This step provides the actual credential for authentication.

**Command** ([[commands/rce-cat-kubernetes-service-account-token]]):
```bash
curl -s "$_RCE_ENDPOINT?cmd=cat%20/var/run/secrets/kubernetes.io/serviceaccount/token"
```

This retrieves the contents of the token file. The output is a base64-encoded JWT string. If the token is obtained, decode the payload (using `jwt.io` or `base64 -d`) to inspect claims like issuer and subject, verifying it's a valid service account token.

### Step 3: Validate Token Access (Optional)

**Context**: Test the extracted token against the Kubernetes API to confirm usability. This can be done outside the RCE by curling the API server with the token as a bearer.

Use the token in a manual API call:
```bash
echo "$_TOKEN" | kubectl --token-stdin get pods
```

If successful, it lists pods, indicating valid access. Replace `$_TOKEN` with the extracted value.
