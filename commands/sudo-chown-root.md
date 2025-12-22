---
data: 'sudo chown root:root /tmp/ggg'
tags:
  - ownership-change
type: command
executor: bash
platforms:
  - Linux
id: f4bed0f6-347c-4b39-861c-96c1f3f45de0
created_at: '2025-12-11T03:47:39.410Z'
updated_at: '2025-12-11T03:47:39.410Z'
verified: false
validated: true
submitted: true
---
# sudo-chown-root

## Command

```bash
sudo chown root:root /tmp/ggg
```

## Description

Changes file ownership to root for testing unrestricted access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `root:root` | User and group | Yes |
| `/tmp/ggg` | Target file | Yes |

## Examples

### Basic Usage

```bash
sudo chown root:root /tmp/ggg
```

## Expected Output

No output; ownership changed.

## Related
- [[procedures/Exploit-Wiki-Attachments-for-Arbitrary-File-Access]]
