---
id: cmd-003
data: >-
  sudo apt-get install -y libssl-dev zlib1g-dev libpsl-dev libidn2-dev
  libnghttp2-dev libbrotli-dev libzstd-dev
tags:
  - setup
  - dependencies
type: command
output: Installed dependencies
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.074Z'
verified: false
validated: true
submitted: true
---
# apt-get-install-curl-deps

## Command

```bash
sudo apt-get install -y libssl-dev zlib1g-dev libpsl-dev libidn2-dev libnghttp2-dev libbrotli-dev libzstd-dev
```

## Description

Installs development libraries for SSL, compression, and protocols needed for cURL build.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-y` | Auto-confirm | Yes |
| `libssl-dev` | OpenSSL headers | Yes |
| `zlib1g-dev` | Compression | Yes |

## Examples

### Basic Usage

```bash
sudo apt-get install -y libssl-dev zlib1g-dev
```

### Advanced Usage

```bash
sudo apt-get install -y libssl-dev libnghttp2-dev libbrotli-dev
```

## Expected Output

Packages installed successfully.

## Related

- [[commands/apt-get-install-build-tools]]
- [[procedures/Building-cURL-with-Security-Debugging-Flags]]
