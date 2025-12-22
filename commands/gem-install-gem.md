---
type: command
executor: bash
data: gem install $_GEM_NAME
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

# gem-install-gem

## Command

```bash
gem install $_GEM_NAME
```

## Description

Installs a specified Ruby gem from RubyGems.org (default source) or a local source. This command fetches the latest or specified version and executes any post-install hooks, which can be exploited in dependency confusion scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_GEM_NAME | The name of the gem to install (e.g., internal-auth-lib) | Yes |
| -v $_VERSION | Specify exact version (e.g., -v 1.2.4) | No |
| --source $_URL | Custom gem source URL | No |

## Examples

### Basic Usage

```bash
gem install internal-auth-lib
```

### Version-Specific Install

```bash
gem install internal-auth-lib -v 1.2.4
```

## Expected Output

Successfully installed internal-auth-lib-1.2.4
1 gem installed

If hooks execute, additional output or network activity may occur.

## Related

- [[commands/gem-list-installed]]
- [[commands/gem-uninstall-gem]]
