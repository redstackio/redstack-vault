---
data: echo "hello gitlab" > /var/log/gitlab/gitlab-workhorse/something.log
tags:
  - log-file
  - setup
type: command
output: File created
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:56.977Z'
id: f005dc3c-f01f-4fe7-ac37-247a86524339
verified: false
validated: true
submitted: true
---
# echo-create-dummy-log

## Command

```bash
echo "hello gitlab" > /var/log/gitlab/gitlab-workhorse/something.log
```

## Description

Creates a dummy log file in GitLab's workhorse directory to serve as the target for logrotate and the race condition exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| echo "hello gitlab" | Content to write | Yes |
| > /path/to/file | Redirect output to file | Yes |

## Examples

### Basic Usage

```bash
echo "hello gitlab" > /var/log/gitlab/gitlab-workhorse/something.log
```

### Advanced Usage

```bash
echo "dummy log entry" >> /var/log/gitlab/gitlab-workhorse/something.log
```

## Expected Output

No output; file is created with 'hello gitlab' content.

## Related

- [[commands/logrotten-execute]]
- [[procedures/Compile-and-Execute-Logrotten-Exploit]]
