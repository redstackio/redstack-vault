---
data: '# Edit parameters in intercepted request'
tags:
  - web
  - modification
type: command
executor: bash
platforms:
  - Web
id: 5d2470d3-70f9-4a72-a461-55993352aabe
created_at: '2025-12-13T23:56:20.098Z'
updated_at: '2025-12-13T23:56:20.098Z'
verified: false
validated: true
submitted: true
---
# Modify Upload Parameters

## Command

```bash
# In proxy: Change _blobstore_url_ and _content_
```

## Description

Modify specific parameters in an intercepted upload request to bypass restrictions or inject payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `_blobstore_url_` | File URL to modify | Yes |
| `_content_` | Content to replace | Yes |

## Examples

### Basic Usage

```bash
# Change extension to .test and content to XSS
```

## Expected Output

Modified request forwarded successfully.

## Related

- [[procedures/Inject-XSS-Payload-via-Modified-Upload]]
- [[procedures/Bypass-File-Upload-Restrictions]]
