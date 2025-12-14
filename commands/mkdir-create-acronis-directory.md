---
id: cmd-mkdir-acronis
data: mkdir %temp%\Acronis
tags:
  - preparation
  - directory-creation
type: command
output: No output if successful
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.738Z'
verified: false
validated: true
submitted: true
---
# mkdir-create-acronis-directory

## Command

```cmd
mkdir %temp%\Acronis
```

## Description

Creates the parent Acronis directory in the temp folder as preparation for symlink-based privilege escalation in Acronis True Image.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| %temp%\Acronis | Target directory path using environment variable | Yes |

## Examples

### Basic Usage

```cmd
mkdir %temp%\Acronis
```

### Advanced Usage

Create with full path if needed: ```cmd
mkdir "C:\Users\%USERNAME%\AppData\Local\Temp\Acronis"
```

## Expected Output

No output if the directory is created successfully; error if it already exists or permissions denied.

## Related

- [[commands/rmdir-remove-acronis-directory]]
