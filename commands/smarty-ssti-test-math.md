---
data: '{7*7}'
tags:
  - ssti
  - test
type: command
executor: bash
platforms:
  - Web
id: 98c82418-b192-46ab-8636-0ed0d68d5061
created_at: '2025-12-13T09:01:17.030Z'
updated_at: '2025-12-13T09:01:17.030Z'
verified: false
validated: true
submitted: true
---
# Smarty SSTI Test Math

## Command

```bash
{7*7}
```

## Description

Tests for template injection by evaluating a mathematical expression in Smarty templates, used in profile fields to confirm SSTI when rendered in emails.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Simple math expression | Yes |

## Examples

### Basic Usage

```bash
{7*7}
```

## Expected Output

Template error indicating injection (e.g., evaluation result like 49 or error message).

## Related

- [[procedures/Initial-SSTI-Test-via-Profile-Fields]]
