---
id: cmd-git-checkout-3-12-1
data: git checkout tags/3.12.1
tags:
  - version-control
  - git
type: command
output: Branch switched to tag 3.12.1
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:18.936Z'
verified: false
validated: true
submitted: true
---
---

# git-checkout-3-12-1

## Command

```bash
git checkout tags/3.12.1
```

## Description

Switches the repository to the specific vulnerable version tag 3.12.1, ensuring the exact codebase with the XSS flaw is used.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| tags/3.12.1 | Version tag | Yes |

## Examples

### Basic Usage

```bash
git checkout tags/3.12.1
```

### Advanced Usage

```bash
git checkout -b vuln-test tags/3.12.1
```

## Expected Output

Note: switching to 'tags/3.12.1'. You are in 'detached HEAD' state.

## Related

- [[commands/git-clone-rocket-chat]]
- [[procedures/Setup-Vulnerable-Rocket-Chat-Instance]]

