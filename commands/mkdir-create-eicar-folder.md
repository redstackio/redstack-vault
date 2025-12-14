---
id: mkdir-eicar
data: mkdir %userprofile%\Desktop\eicar
tags:
  - setup
  - directory-create
type: command
output: Directory created successfully
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.731Z'
verified: false
validated: true
submitted: true
---
# mkdir-create-eicar-folder

## Command

```cmd
mkdir %userprofile%\Desktop\eicar
```

## Description

Creates a new directory named 'eicar' on the user's desktop to serve as the container for the initial AV-triggering payload file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| %userprofile%\Desktop | Path using environment variable for user desktop | Yes |
| eicar | Folder name | Yes |

## Examples

### Basic Usage

```cmd
mkdir %userprofile%\Desktop\eicar
```

### Advanced Usage

```cmd
mkdir %userprofile%\Desktop\test-folder
```

## Expected Output

No output if successful; the directory is created and can be verified with `dir`.

## Related

- [[commands/rmdir-delete-eicar]]
