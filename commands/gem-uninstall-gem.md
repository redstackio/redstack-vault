---
type: command
executor: bash
data: gem uninstall $_GEM_NAME
output: null
platforms:
  - Linux
  - macOS
tags:
  - package-management
  - ruby
verified: true
validated: true
---

# gem-uninstall-gem

## Command

```bash
gem uninstall $_GEM_NAME
```

## Description

Uninstalls a specific Ruby gem. Prompts for version if multiple are installed; useful for removing test malicious packages.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_GEM_NAME | The name of the gem to uninstall (e.g., internal-auth-lib) | Yes |
| -a | Remove all versions | No |
| -x | Remove executables | No |

## Examples

### Basic Usage

```bash
gem uninstall internal-auth-lib
```

### Remove All Versions

```bash
gem uninstall -a internal-auth-lib
```

## Expected Output

Successfully uninstalled internal-auth-lib-1.2.4

## Related

- [[commands/gem-install-gem]]
