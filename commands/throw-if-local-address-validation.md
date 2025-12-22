---
data: >-
  <?php require 'vendor/autoload.php'; function ThrowIfLocalAddress($host) {
  $parsed = parse_url($host); $hostname = strtolower($parsed['host'] ?? ''); if
  (substr_count($hostname, '.') === 0) throw new Exception('Local host');
  ThrowIfLocalIp($parsed['host']); $ch = curl_init($host); curl_setopt($ch,
  CURLOPT_RETURNTRANSFER, true); curl_setopt($ch, CURLOPT_HEADER, 0); $data =
  curl_exec($ch); curl_close($ch); echo $data; } if (isset($_GET['host']))
  ThrowIfLocalAddress($_GET['host']); ?>
tags:
  - ssrf
  - validation
type: command
output: Fetched content or exception
executor: php
platforms:
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.231Z'
id: 24f5b7d3-5fe1-420e-a6fe-9410f9ae48a5
verified: false
validated: true
submitted: true
---
# throw-if-local-address-validation

## Command

```php
<?php
require 'vendor/autoload.php';

function ThrowIfLocalAddress($host) {
    $parsed = parse_url($host);
    $hostname = strtolower($parsed['host'] ?? '');
    if (substr_count($hostname, '.') === 0) throw new Exception('Local host');
    ThrowIfLocalIp($parsed['host']);
    $ch = curl_init($host);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HEADER, 0);
    $data = curl_exec($ch);
    curl_close($ch);
    echo $data;
}
if (isset($_GET['host'])) ThrowIfLocalAddress($_GET['host']);
?>
```

## Description

Parses a host from a URI, performs TLD and IP checks, then fetches content via cURL if valid; tests SSRF to URIs like octal localhost.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_GET["host"]` | Full URI host (e.g., http://0177.0.0.1/) | Yes |

## Examples

### Basic Usage

```bash
php test.php?host=http://0177.0.0.1/
```

### Advanced Usage

```bash
php test.php?host=http://0251.0376.0251.0376/
```

## Expected Output

Response body from the endpoint or an exception.

## Related

- [[commands/throw-if-local-ip-validation]]
