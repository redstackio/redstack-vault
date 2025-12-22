---
id: 6ce6afe9-980e-4a6f-b2f5-ec0eb57f3bae
name: scmkit-create-gitlab-ssh-key-api-token
type: command
executor: bash
data: >-
  SCMKit.exe -s gitlab -m createsshkey -c $_API_TOKEN -u $_GITLAB_URL -o
  "$_SSH_PUBLIC_KEY"
output: null
created_at: '2023-04-06T03:56:25.113542+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - persistence
  - ssh
verified: true
validated: true
---

# scmkit-create-gitlab-ssh-key-api-token

## Command

```bash
SCMKit.exe -s gitlab -m createsshkey -c $_API_TOKEN -u $_GITLAB_URL -o "$_SSH_PUBLIC_KEY"
```

## Description

Adds an SSH public key to GitLab.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -o "$_SSH_PUBLIC_KEY" | Public key string | Yes |

## Examples

```bash
SCMKit.exe -s gitlab -m createsshkey -c glpat-abc -u https://gitlab.example.com -o "ssh-rsa AAA..."
```

## Expected Output

Key added message.

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
