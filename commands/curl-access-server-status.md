---
data: 'curl -k https://target.example.com/server-status/'
tags:
  - reconnaissance
  - information-disclosure
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: b077cc88-3779-4854-998d-1e86ff28892d
created_at: '2025-12-14T17:25:12.844Z'
updated_at: '2025-12-14T17:25:12.844Z'
verified: false
validated: true
submitted: true
---
# curl-access-server-status

## Command

```bash
curl -k https://target.example.com/server-status/
```

## Description

This command uses curl to fetch the exposed Apache /server-status/ page, retrieving server metrics and logs. Use it during reconnaissance to disclose information from misconfigured web servers. The `-k` flag bypasses SSL verification for testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-k` | Insecure mode: skip certificate verification | No (but recommended for self-signed certs) |
| `https://target.example.com/server-status/` | Target URL for the server-status endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -k https://target.example.com/server-status/
```

### Advanced Usage

```bash
curl -k -v https://target.example.com/server-status/ | tee status.html
```

Saves verbose output (including headers) to a file for analysis.

## Expected Output

HTML content with server details, e.g.:

```
Apache Server Status for target.example.com

Server Version: Apache/2.4.41
Server Load: 1.2 0.8 0.4
Total Accesses: 12345
...
CurrentTime: Sunday, 01-Oct-2023 12:00:00 GMT
Request: GET / HTTP/1.1 from 192.168.1.1
```

Look for metrics and log tables indicating successful disclosure.

## Related

- [[Related Procedure|procedures/Access-Exposed-Apache-Server-Status]]
