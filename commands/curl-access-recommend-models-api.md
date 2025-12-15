---
data: >-
  curl
  "https://www.xvcams.com/api/models/recommend-models-to-cust.php?user_id=0&model_id=1078906&t=$(date
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
updated_at: '2025-12-14T17:32:28.746Z'
id: 22ff0027-edfd-4e44-94a3-9fea7ad4073b
verified: false
validated: true
submitted: true
---
---

# curl-access-recommend-models-api

## Command

```bash
curl "https://www.xvcams.com/api/models/recommend-models-to-cust.php?user_id=0&model_id=1078906&t=$(date +%s)" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

## Description

Sends GET to recommendation API for tracking data leakage. Ideal for enumerating model statuses anonymously; adjust model_id for brute-force.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `user_id=0` | Anonymous user ID | Yes |
| `model_id=1078906` | Target model for recommendations | Yes |
| `t=$(date +%s)` | Timestamp parameter | Yes |
| `-H "User-Agent: ..."` | Browser emulation | No |

## Examples

### Basic Usage

```bash
curl "https://www.xvcams.com/api/models/recommend-models-to-cust.php?user_id=0&model_id=1078906&t=1726734766762"
```

### Advanced Usage

```bash
curl "https://www.xvcams.com/api/models/recommend-models-to-cust.php?user_id=0&model_id=1078900&t=$(date +%s)" | jq '.recommId'
```

## Expected Output

JSON with {"recommId":789, "model_id":1078906, "room_status":"offline"}. Use for data correlation.

## Related

- [[Related Procedure]]
