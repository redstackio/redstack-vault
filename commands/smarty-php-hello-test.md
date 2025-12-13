---
data: '{php}print "Hello"{/php}'
tags:
  - ssti
  - php-execution
type: command
executor: bash
platforms:
  - Web
id: 93cfa2c9-80c2-48ab-b41a-9eaacbe1ad2a
created_at: '2025-12-13T09:01:17.018Z'
updated_at: '2025-12-13T09:01:17.018Z'
verified: false
validated: true
submitted: true
---
# Smarty PHP Hello Test

## Command

```bash
{php}print "Hello"{/php}
```

## Description

Executes PHP code to print 'Hello' within the Smarty template to test code execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | PHP print statement | Yes |

## Examples

### Basic Usage

```bash
{php}print "Hello"{/php}
```

## Expected Output

'Hello' string in the output.

## Related

- [[procedures/Test-PHP-Code-Execution-in-Smarty]]
