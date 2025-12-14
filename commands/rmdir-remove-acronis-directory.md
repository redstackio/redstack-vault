---
id: cmd-rmdir-acronis
data: rmdir /S /Q %temp%\Acronis\DriverSetup
tags:
  - preparation
  - cleanup
type: command
output: No output if successful
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.741Z'
verified: false
validated: true
submitted: true
---
# rmdir-remove-acronis-directory

## Command

```cmd
rmdir /S /Q %temp%\Acronis\DriverSetup
```

## Description

Recursively and quietly removes the Acronis DriverSetup directory from the temp folder to prepare for symlink creation in a privilege escalation attack.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /S | Removes all directories and files recursively | Yes |
| /Q | Quiet mode, no confirmation prompts | Yes |
| %temp%\Acronis\DriverSetup | Target directory path using environment variable | Yes |

## Examples

### Basic Usage

```cmd
rmdir /S /Q %temp%\Acronis\DriverSetup
```

### Advanced Usage

If path has spaces, quote it: ```cmd
rmdir /S /Q "%temp%\Acronis\DriverSetup"
```

## Expected Output

No output if the directory is successfully removed or doesn't exist; error message if permissions are insufficient.

## Related

- [[commands/mkdir-create-acronis-directory]]
