---
data: tar -zcvf service_template.tar.gz project.json VERSION project.bundle
tags:
  - archive
  - compression
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: d4922f91-1776-4713-906f-5d5b3304367d
created_at: '2025-12-11T06:10:28.865Z'
updated_at: '2025-12-11T06:10:28.865Z'
verified: false
validated: true
submitted: true
---
# tar-create-archive

## Command

```bash
tar -zcvf service_template.tar.gz project.json VERSION project.bundle
```

## Description

Creates a compressed tar archive containing modified GitLab project files for import, used in repackaging after editing project.json to inject service templates.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-c` | Create a new archive | Yes |
| `-f` | Specify the archive file name | Yes |
| `-v` | Verbosely list files processed | No |
| `-z` | Compress the archive with gzip | Yes |
| `service_template.tar.gz` | Output file name | Yes |
| `project.json VERSION project.bundle` | Files to include in the archive | Yes |

## Examples

### Basic Usage

```bash
tar -zcvf archive.tar.gz file1 file2
```

### Advanced Usage

```bash
tar -zcvf archive.tar.gz --exclude='*.tmp' directory/
```

## Expected Output

List of files being added to the archive, such as:
project.json
a VERSION
a project.bundle

## Related

- [[tools/tar]]
- [[procedures/Repackage-and-Import-Modified-Project-Archive]]
