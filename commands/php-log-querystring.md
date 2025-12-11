---
data: 'file_put_contents(''r.log'',$_SERVER[''QUERY_STRING'']."\n",FILE_APPEND);'
tags:
  - php
  - logging
type: command
executor: php
platforms:
  - Web
id: 6056bf5d-3b1b-492a-aaa4-7e63a41e01ab
created_at: '2025-12-11T06:10:22.331Z'
updated_at: '2025-12-11T06:10:22.331Z'
verified: false
validated: true
submitted: true
---
# php-log-querystring

## Command

```php
file_put_contents('r.log',$_SERVER['QUERY_STRING']."\n",FILE_APPEND);
```

## Description

Appends the query string from the request to a log file on the server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `file` | r.log - Log file | Yes |
| `flags` | FILE_APPEND - Append mode | Yes |
| `content` | Query string from request | Yes |

## Examples

### Basic Usage

```php
file_put_contents('r.log',$_SERVER['QUERY_STRING']."\n",FILE_APPEND);
```

## Expected Output

None (writes to file).

## Related

- [[procedures/Exploit-XSS-to-Steal-OAuth-Tokens]]
