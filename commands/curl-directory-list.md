---
id: cmd-uuid-001
data: 'curl -k -I https://target.com/path/'
tags:
  - recon
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.872Z'
verified: false
validated: true
submitted: true
---
# curl-directory-list

## Command

```bash
curl -k -I https://target.com/path/
```

## Description

This command uses curl to send a HEAD request to a web directory, checking for exposure without downloading content. Useful for reconnaissance in info disclosure scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-k` | Ignore SSL certificate errors | No |
| `-I` | HEAD request only (headers) | Yes |
| `https://target.com/path/` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -k -I https://cards-dev.twitter.com/keys/
```

### Advanced Usage

```bash
curl -k -I -H "User-Agent: Mozilla/5.0" https://cards-dev.twitter.com/keys/
```

## Expected Output

HTTP/1.1 200 OK
Content-Type: application/json
Content-Disposition: attachment; filename="json.json"

Indicates file serving or directory access.

## Related

- [[commands/curl-download-file]]
