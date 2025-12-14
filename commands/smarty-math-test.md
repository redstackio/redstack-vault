---
id: cmd-uuid-1
data: '{7*7}'
tags:
  - ssti
  - detection
type: command
output: Template parsing error
executor: smarty
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.579Z'
verified: false
validated: true
submitted: true
---
# smarty-math-test

## Command

```smarty
{7*7}
```

## Description

Injects a Smarty math expression to test for SSTI; evaluates to 49 if parsed, but triggers error on invalid context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Expression | Math operation like 7*7 | Yes |

## Examples

### Basic Usage

```smarty
{7*7}
```

### Advanced Usage

```smarty
{math equation="x * y" x=7 y=7}
```

## Expected Output

Template error in email if SSTI present.

## Related

- [[procedures/Test-for-Smarty-SSTI-with-Math-Expression]]
