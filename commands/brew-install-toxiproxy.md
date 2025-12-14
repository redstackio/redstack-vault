---
data: brew install toxiproxy
tags:
  - installation
  - toxiproxy
type: command
executor: bash
platforms:
  - macOS
id: 5f29a0f5-a4d7-49a3-b9f2-979ad2f94184
created_at: '2025-12-14T17:27:29.704Z'
updated_at: '2025-12-14T17:27:29.704Z'
verified: false
validated: true
submitted: true
---
# brew-install-toxiproxy

## Command

```bash
brew install toxiproxy
```

## Description

Installs the Toxiproxy package from the Shopify tap, including the server and CLI components for creating and managing TCP proxies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Installs default version | No |

## Examples

### Basic Usage

```bash
brew install toxiproxy
```

### Advanced Usage

```bash
brew install shopify/shopify/toxiproxy --HEAD
```

## Expected Output

Downloads and installs binaries, outputs path to /opt/homebrew/bin/toxiproxy.

## Related

- [[commands/brew-services-start-toxiproxy]]
- [[procedures/Install-and-Start-Toxiproxy-Service]]
