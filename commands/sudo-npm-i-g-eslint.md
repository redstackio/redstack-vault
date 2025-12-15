---
data: sudo npm i -g eslint
tags:
  - npm
  - install
  - sudo
  - escalation
type: command
output: Installation output for eslint
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.381Z'
id: d15fe656-9d7b-4842-8185-bab57c0bfdf1
verified: false
validated: true
submitted: true
---
# sudo-npm-i-g-eslint

## Command

```bash
sudo npm i -g eslint
```

## Description

Installs eslint globally with sudo, running npm as root and loading local .npmrc for onload-script execution with elevated privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| i | Install mode | Yes |
| -g | Global installation | Yes |
| eslint | Package name | Yes |

## Examples

### Basic Usage

```bash
sudo npm i -g eslint
```

## Expected Output

Installation progress and success message for eslint.

## Related

- [[commands/sudo-npm]]
- [[procedures/Trick-Victim-to-Run-npm]]
