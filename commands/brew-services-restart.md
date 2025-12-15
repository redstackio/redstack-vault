---
data: brew services restart some-service
tags:
  - exploitation
  - homebrew
  - services
type: command
output: null
executor: bash
platforms:
  - macOS
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:10.093Z'
id: 988922ff-b9e0-45b2-9fec-e033fe9c01a5
verified: false
validated: true
submitted: true
---
# brew-services-restart

## Command

```bash
brew services restart some-service
```

## Description

Restarts a Homebrew-managed service, triggering chown operations on paths including unprotected symlinks, leading to privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `restart` | Stop and start the service | Yes |
| `some-service` | Name of the service to restart (e.g., nginx) | Yes |

## Examples

### Basic Usage

```bash
brew services restart nginx
```

### Advanced Usage

```bash
sudo brew services restart all  # Restart all if needed
```

## Expected Output

Service restart status, e.g., "Successfully restarted nginx (label: homebrew.mxcl.nginx)".

## Related

- [[Related Procedure|procedures/Exploit-Homebrew-Symlink-for-Root-Access]]
