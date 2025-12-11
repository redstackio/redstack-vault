---
id: 7399261c-84ff-4963-b76d-f07654ee09b0
name: mruby-module-new-do
type: command
executor: bash
data: mruby module_new_do.rb
output: null
created_at: '2025-12-11T03:47:47.927Z'
updated_at: '2025-12-11T03:47:47.927Z'
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

# mruby-module-new-do

## Command

```bash
mruby module_new_do.rb
```

## Description

Executes the module_new_do.rb script in mruby to trigger recursion via module creation, leading to stack overflow.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `module_new_do.rb` | The script file to execute | Yes |

## Examples

### Basic Usage

```bash
mruby module_new_do.rb
```

## Expected Output

Segmentation fault.

## Related

- [[procedures/Test-Alternative-Module-New-POC-in-mruby]]
- #mruby
