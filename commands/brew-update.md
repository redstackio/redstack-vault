---
data: brew update
tags:
  - package-management
  - setup
type: command
executor: bash
platforms:
  - macOS
id: ceb8a80f-9692-4551-ac17-73e00b2e5b13
created_at: '2025-12-14T17:27:29.709Z'
updated_at: '2025-12-14T17:27:29.709Z'
verified: false
validated: true
submitted: true
---
# brew-update

## Command

```bash
brew update
```

## Description

Updates Homebrew's package definitions by fetching the latest formulae and cask definitions from the central repository. Use this before installing new packages to ensure compatibility and security.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Runs default update | No |

## Examples

### Basic Usage

```bash
brew update
```

### Advanced Usage

```bash
brew update --preinstall
```

## Expected Output

Lists updated packages and any warnings about outdated formulae.

## Related

- [[commands/brew-install-toxiproxy]]
- [[procedures/Install-and-Start-Toxiproxy-Service]]
