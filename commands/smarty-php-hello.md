---
id: cmd-uuid-3
data: '{php}print "Hello"{/php}'
tags:
  - php
  - execution
type: command
output: Hello
executor: php
platforms:
  - Web
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.573Z'
verified: false
validated: true
submitted: true
---
# smarty-php-hello

## Command

```smarty
{php}print "Hello"{/php}
```

## Description

Tests PHP execution by printing a string within Smarty's PHP block.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| PHP Code | print "Hello" | Yes |

## Examples

### Basic Usage

```smarty
{php}print "Hello"{/php}
```

## Expected Output

"Hello" in email body.

## Related

- [[procedures/Test-PHP-Execution-in-Smarty-Templates]]
