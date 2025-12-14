---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
data: 'curl "https://isadora.transloadit.com/assemblies/[hash]?seq=0&callback="'
tags:
  - recon
  - poll
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.931Z'
verified: false
validated: true
submitted: true
---
# transloadit-get-assembly-status

## Command

```bash
curl "https://isadora.transloadit.com/assemblies/[hash]?seq=0&callback="
```

## Description

Polls Transloadit for assembly status to retrieve the S3 URL of the processed uploaded file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `[hash]` | Assembly ID from upload response | Yes |
| `seq` | Sequence for polling (0 for initial) | Yes |
| `callback` | Empty for JSONP (optional) | No |

## Examples

### Basic Usage

```bash
curl "https://isadora.transloadit.com/assemblies/abc123?seq=0&callback="
```

### Advanced Usage

Increment seq for subsequent polls if needed.

## Expected Output

JSON: {"ok":"ASSEMBLY_COMPLETED","results":{"my_file":[{"url":"http://.../stored_xss.html"}]}}

## Related

- [[procedures/Upload-Malicious-HTML-to-Transloadit-Assembly]]
- [[procedures/Retrieve-S3-URL-from-Transloadit]]
