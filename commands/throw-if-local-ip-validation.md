---
data: >-
  <?php require 'vendor/autoload.php'; use
  Symfony\Component\HttpFoundation\IpUtils; function ThrowIfLocalIp($ip) {
  $flags = FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE; if
  (!filter_var($ip, FILTER_VALIDATE_IP, ['flags' => $flags])) { throw new
  Exception('Invalid IP'); } $ranges = ['100.64.0.0/10', '192.0.0.0/24']; if
  (IpUtils::checkIp($ip, $ranges)) { throw new Exception('Local IP'); } echo
  'Pass'; } if (isset($_GET['ip'])) ThrowIfLocalIp($_GET['ip']); ?>
tags:
  - ssrf
  - validation
type: command
output: Pass (if bypass successful) or exception message
executor: php
platforms:
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.237Z'
id: d1e60dbd-14fd-45f0-84e9-6549e17abfcd
verified: false
validated: true
submitted: true
---
# throw-if-local-ip-validation

## Command

```php
<?php
require 'vendor/autoload.php';
use Symfony\Component\HttpFoundation\IpUtils;

function ThrowIfLocalIp($ip) {
    $flags = FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE;
    if (!filter_var($ip, FILTER_VALIDATE_IP, ['flags' => $flags])) {
        throw new Exception('Invalid IP');
    }
    $ranges = ['100.64.0.0/10', '192.0.0.0/24'];
    if (IpUtils::checkIp($ip, $ranges)) {
        throw new Exception('Local IP');
    }
    echo 'Pass';
}
if (isset($_GET['ip'])) ThrowIfLocalIp($_GET['ip']);
?>
```

## Description

Validates an IP string against local and private ranges using filter_var and Symfony IpUtils, throwing exceptions on matches; used to test SSRF bypasses in a Nextcloud-like environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_GET["ip"]` | Input IP string (e.g., alphanumeric or octal payload) | Yes |

## Examples

### Basic Usage

```bash
php test.php?ip=169.254.169.254
```

### Advanced Usage

```bash
php test.php?ip=⑯⑨。②⑤④。⑯⑨｡②⑤④
```

## Expected Output

'Pass' if the IP bypasses checks, or an exception message like 'Local IP'.

## Related

- [[commands/throw-if-local-address-validation]]
