---
id: cmd-007
data: apt install -y --no-recommend /opt/src/work.deb
tags:
  - package-install
type: command
output: 'Package installed, triggering postinst script'
executor: bash
platforms:
  - Linux
  - Debian
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.205Z'
verified: false
validated: true
submitted: true
---
# apt-install-malicious-deb

## Command

```bash
apt install -y --no-recommend /opt/src/work.deb
```

## Description

Installs a local .deb package during build prepare, triggering postinst for backdoor deployment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -y | Auto-confirm | Yes |
| --no-recommend | Skip recommends | Yes |
| /opt/src/work.deb | Package path | Yes |

## Examples

### Basic Usage

```bash
apt install -y --no-recommend /opt/src/work.deb
```

## Expected Output

Installation complete, postinst executed.

## Related

- [[commands/echo-pwned-log]]
