---
id: 01a221b9-ad1c-47fa-adc8-bd6505ac2373
name: mruby-nil-method-ensure
type: command
executor: bash
data: mruby nil_method_ensure.rb
output: null
created_at: '2025-12-11T03:47:47.930Z'
updated_at: '2025-12-11T03:47:47.930Z'
platforms:
  - Linux
  - macOS
tags:
  - mruby
  - exploit
verified: false
validated: true
submitted: true
---

# mruby-nil-method-ensure

## Command

```bash
mruby nil_method_ensure.rb
```

## Description

Runs the nil_method_ensure.rb script in mruby to exploit recursion in ensure blocks, causing stack overflow.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `nil_method_ensure.rb` | The script file to execute | Yes |

## Examples

### Basic Usage

```bash
mruby nil_method_ensure.rb
```

## Expected Output

Segmentation fault (crashes mruby but not sandbox).

## Related

- [[procedures/Test-Alternative-Nil-Method-POC-in-mruby]]
- #mruby
