---
data: brew services start shopify/shopify/toxiproxy
tags:
  - service-management
  - startup
type: command
executor: bash
platforms:
  - macOS
id: 65339696-b1f6-4bb6-a2e2-be065a5c67c7
created_at: '2025-12-14T17:27:29.702Z'
updated_at: '2025-12-14T17:27:29.702Z'
verified: false
validated: true
submitted: true
---
# brew-services-start-toxiproxy

## Command

```bash
brew services start shopify/shopify/toxiproxy
```

## Description

Starts the Toxiproxy service as a background process managed by launchd, binding the HTTP API to localhost:8474.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| shopify/shopify/toxiproxy | Formula identifier | Yes |

## Examples

### Basic Usage

```bash
brew services start shopify/shopify/toxiproxy
```

### Advanced Usage

```bash
brew services start --all
```

## Expected Output

"Successfully started `toxiproxy` (label: homebrew.mxcl.toxiproxy)".

## Related

- [[commands/brew-install-toxiproxy]]
- [[procedures/Install-and-Start-Toxiproxy-Service]]
