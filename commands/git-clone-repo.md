---
data: 'git clone https://$GH_TOKEN@github.com/Shopify/repo.git /tmp/repo'
tags:
  - git
  - clone
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 887d1645-4786-4448-b5f4-90aac1445f89
created_at: '2025-12-11T03:48:06.061Z'
updated_at: '2025-12-11T03:48:06.061Z'
verified: false
validated: true
submitted: true
---
# git-clone-repo

## Command

```bash
git clone https://$GH_TOKEN@github.com/Shopify/repo.git /tmp/repo
```

## Description

Clones a GitHub repository using an access token embedded in the URL for authentication, verifying read access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://$GH_TOKEN@github.com/Shopify/repo.git` | Repo URL with token | Yes |
| `/tmp/repo` | Local directory for clone | Yes |

## Examples

### Basic Usage

```bash
git clone https://ghp_abc123@github.com/org/repo.git /tmp/clone
```

## Expected Output

Repository cloned successfully to the specified directory.

## Related

- [[procedures/Access-and-Verify-Repository-Permissions]]
- #git
