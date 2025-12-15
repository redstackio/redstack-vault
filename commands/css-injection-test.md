---
data: 'curl ''https://bountypay.h1ctf.com/2fa?style=<style>body{display:none}</style>'''
tags:
  - css
  - injection
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.052Z'
id: 1d2860af-d87b-48f2-b2ac-2489ecc73a8b
verified: false
validated: true
submitted: true
---
# css-injection-test

## Command

```bash
curl 'https://bountypay.h1ctf.com/2fa?style=<style>body{display:none}</style>'
```

## Description

Tests for CSS injection by passing style payload in URL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `style` | CSS payload | Yes |

## Examples

### Basic Usage

```bash
curl 'target?style=<style>alert(1)</style>'
```

### Advanced Usage

```bash
curl 'target?input=<style>#elem{display:none}</style>'
```

## Expected Output

Altered HTML response.

## Related

- [[Related Procedure]]
