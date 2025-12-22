---
type: command
executor: cmd
data: certutil -decode payload.b64 payload.dll
output: null
platforms:
  - Windows
tags:
  - certutil
  - decode
verified: true
validated: true
---

# certutil-decode-base64-to-dll

## Command

```cmd
certutil -decode $_INPUT_FILE $_OUTPUT_FILE
```

## Description

Decodes a base64-encoded file using Certutil, converting it to its binary form (e.g., from .b64 to .dll). This is a key step in payload delivery to restore the executable format.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_INPUT_FILE | Path to the base64-encoded input file (e.g., payload.b64) | Yes |
| $_OUTPUT_FILE | Path for the decoded output file (e.g., payload.dll) | Yes |
| -decode | Specifies base64 decoding operation | Built-in |

## Examples

### Basic Usage

```cmd
certutil -decode payload.b64 payload.dll
```

### Advanced Usage

```cmd
certutil -decode encoded.b64 malicious.dll
```

## Expected Output

Certutil: -decode command completed successfully.

The decoded file (payload.dll) is created. Verify integrity with: fc payload.b64 (or check file size).

## Related

- [[procedures/Certutil-Download-and-Execute]]
- [[commands/certutil-download-base64-payload]]
