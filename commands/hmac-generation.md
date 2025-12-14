---
data: >-
  $hmac=hash_hmac('sha256',"no_iframe=1&platform=woocommerce&shop_domain={$domain}",$token,false);
tags:
  - hmac
  - auth
type: command
output: Hex HMAC string
executor: php
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:44.153Z'
id: 14eb6c8e-ccd0-479f-b74f-2851b6f78920
verified: false
validated: true
submitted: true
---
# hmac-generation

## Command

```php
$hmac=hash_hmac('sha256',"no_iframe=1&platform=woocommerce&shop_domain={$domain}",$token,false);
```

## Description

Generates SHA256 HMAC for Judge.me URL params using API token as key, enabling authenticated access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| algorithm | Hash algo (sha256) | Yes |
| data | Query string | Yes |
| key | API token | Yes |
| raw | Hex output (false) | No |

## Examples

### Basic Usage

```php
$domain = 'example.com';
$token = 'api_token_here';
$hmac = hash_hmac('sha256', "no_iframe=1&platform=woocommerce&shop_domain=$domain", $token, false);
echo $hmac;
```

### Advanced Usage

Integrate into URL construction.

## Expected Output

32-character hex string for hmac param.

## Related

- [[commands/xss-trigger-preview]]
