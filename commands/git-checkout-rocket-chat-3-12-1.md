---
id: 123e4567-e89b-12d3-a456-426614174007
name: git-checkout-rocket-chat-3-12-1
type: command
executor: bash
data: git checkout tags/3.12.1
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.418Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - version-control
  - git
verified: false
validated: true
submitted: true
---

# git-checkout-rocket-chat-3-12-1

## Command

```bash
git checkout tags/3.12.1
```

## Description

Switches the repository to the specific vulnerable release tag 3.12.1 to ensure the exact codebase with the XSS and validation bypass issues.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| tags/3.12.1 | Version tag reference | Yes |

## Examples

### Basic Usage

```bash
git checkout tags/3.12.1
```

### Advanced Usage

```bash
git checkout v3.12.1  # If tagged as v prefix
```

## Expected Output

Note: switching to 'tags/3.12.1'.
You are in 'detached HEAD' state...

## Related

- [[commands/git-clone-rocket-chat]]
- [[procedures/Setup-Rocket-Chat-Vulnerable-Instance]]
