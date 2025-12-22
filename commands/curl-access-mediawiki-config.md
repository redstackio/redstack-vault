---
data: 'curl -i https://target-domain.com/mw-config/index.php'
tags:
  - web
  - recon
  - access-control
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 227bcbc1-14db-4541-b3ee-404c8e29d72a
created_at: '2025-12-14T17:28:58.919Z'
updated_at: '2025-12-14T17:28:58.919Z'
verified: false
validated: true
submitted: true
---
# curl-access-mediawiki-config

## Command

```bash
curl -i https://target-domain.com/mw-config/index.php
```

## Description

This command uses curl to send an HTTP request to the MediaWiki configuration endpoint, verifying if it is publicly accessible without authentication. It is useful for initial reconnaissance of web application misconfigurations that expose administrative interfaces.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers in output | Yes |
| `https://target-domain.com/mw-config/index.php` | The URL of the MediaWiki config page; replace with actual target | Yes |

## Examples

### Basic Usage

```bash
curl -i https://example.com/mw-config/index.php
```

### Advanced Usage

```bash
curl -i -H "User-Agent: Mozilla/5.0" https://target.com/mw-config/index.php | grep -i "restart"
```

This adds a user-agent header to mimic a browser and pipes output to grep for the restart button text.

## Expected Output

Successful execution returns HTTP headers and body:

```
HTTP/1.1 200 OK
Content-Type: text/html
...

<!DOCTYPE html>
<html>
... (HTML with config form and 'restart installation' button)
```

A 403 or 401 indicates protection; 200 with config content confirms vulnerability.

## Related

- [[Related Procedure: Access-MediaWiki-Config-Page-Without-Auth]]
