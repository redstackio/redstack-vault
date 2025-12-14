---
id: rmdir-eicar
data: rmdir /S /Q %userprofile%\Desktop\eicar
tags:
  - cleanup
  - directory-delete
type: command
output: Directory removed without prompts
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.716Z'
verified: false
validated: true
submitted: true
---
# rmdir-delete-eicar

## Command

```cmd
rmdir /S /Q %userprofile%\Desktop\eicar
```

## Description

Recursively and quietly deletes the 'eicar' directory and its contents to prepare for junction creation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /S | Recursive deletion | Yes |
| /Q | Quiet (no confirm) | Yes |
| %userprofile%\Desktop\eicar | Target directory | Yes |

## Examples

### Basic Usage

```cmd
rmdir /S /Q test-folder
```

### Advanced Usage

Safe for subdirs with files.

## Expected Output

Silent success; folder gone.

## Related

- [[commands/mkdir-create-eicar-folder]]
