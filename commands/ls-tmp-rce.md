---
id: cmd-ls-rce-demo
data: ls /tmp/rce-demo
tags:
  - verification
  - rce
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.468Z'
verified: false
validated: true
submitted: true
---
# ls-tmp-rce

## Command

```bash
ls /tmp/rce-demo
```

## Description

Checks for the existence of a demonstration file created by the exploited RCE in GitLab, verifying successful code execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/tmp/rce-demo` | Path to the file created by the backtick command | Yes |

## Examples

### Basic Usage

```bash
ls /tmp/rce-demo
```

### Advanced Usage

```bash
ls -la /tmp/rce-demo
```

## Expected Output

File path `/tmp/rce-demo` if present, or `ls: cannot access '/tmp/rce-demo': No such file or directory` if failed.

## Related

- [[commands/rpush-gitlab-shell-job]]
- [[procedures/Enqueue-Malicious-GitLab-Sidekiq-Job]]
