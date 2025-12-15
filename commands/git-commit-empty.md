---
id: cmd-uuid-placeholder-002
data: git commit --allow-empty -m "Ambiguous ref payload"
tags:
  - git
  - commit
type: command
output: null
executor: bash
platforms:
  - Git
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.145Z'
verified: false
validated: true
submitted: true
---
# git-commit-empty

## Command

```bash
git commit --allow-empty -m "Ambiguous ref payload"
```

## Description

Creates an empty commit with a message to introduce payload in the branch, bypassing normal file change requirements for reference manipulation in the exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--allow-empty` | Permit creation of empty commits | Yes |
| `-m` | Commit message | Yes |
| `message` | The message content (e.g., "Ambiguous ref payload") | Yes |

## Examples

### Basic Usage

```bash
git commit --allow-empty -m "Ambiguous ref payload"
```

### Advanced Usage

```bash
git commit --allow-empty -m "Payload" --author="attacker@example.com"
```

## Expected Output

[exploit-branch abc1234] Ambiguous ref payload. No files changed. Commit hash displayed.

## Related

- [[Related Procedure|procedures/Exploit-Git-Reference-Ambiguity-for-Commit-Smuggling]]
