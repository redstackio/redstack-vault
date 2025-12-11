---
data: 'explode("\n",file_get_contents(''r.log''));'
tags:
  - php
  - parsing
type: command
executor: php
platforms:
  - Web
id: a5f0afa0-0183-410f-b3fb-c3404e4c7979
created_at: '2025-12-11T06:10:22.327Z'
updated_at: '2025-12-11T06:10:22.327Z'
verified: false
validated: true
submitted: true
---
# php-parse-logs

## Command

```php
explode("\n",file_get_contents('r.log'));
```

## Description

Reads the log file and splits it into an array of lines for parsing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```php
$lines = explode("\n",file_get_contents('r.log'));
```

## Expected Output

Array of log lines.

## Related

- [[procedures/Exploit-XSS-to-Steal-OAuth-Tokens]]
