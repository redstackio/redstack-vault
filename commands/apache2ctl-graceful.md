---
id: cmd-apache2ctl-graceful
data: apache2ctl graceful
tags:
  - apache
  - restart
type: command
output: 'Apache restarts without full shutdown, old workers exit, new ones spawn'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.260Z'
verified: false
validated: true
submitted: true
---
# apache2ctl-graceful

## Command

```bash
apache2ctl graceful
```

## Description

Performs a graceful restart of Apache HTTP Server, sending SIGUSR1 to workers to finish requests before exiting and spawning new ones, often triggered by logrotate for log rotation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| graceful | Graceful restart mode | Yes |

## Examples

### Basic Usage

```bash
apache2ctl graceful
```

### Advanced Usage

As root or via cron: `apache2ctl -k graceful`

## Expected Output

Apache restarts without full shutdown, old workers exit, new ones spawn

## Related

- [[procedures/Trigger-Graceful-Restart-to-Execute-Arbitrary-Code-as-Root]]
