---
data: tar -zcvf service_template.tar.gz project.json VERSION project.bundle
tags:
  - archive
  - packaging
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 10a9b49c-f5fa-4d3b-953d-3a58e17defc3
created_at: '2025-12-11T03:47:39.594Z'
updated_at: '2025-12-11T03:47:39.594Z'
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

Creates a gzip-compressed tar archive containing modified GitLab project files for import exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-c` | Create a new archive | Yes |
| `-f` | Specify the archive file name | Yes |
| `-v` | Verbosely list files processed | No |
| `-z` | Compress the archive with gzip | Yes |
| `project.json` | Modified JSON file to include | Yes |
| `VERSION` | Version file to include | Yes |
| `project.bundle` | Project bundle file to include | Yes |
| `service_template.tar.gz` | Output archive file name | Yes |

## Examples

### Basic Usage

```bash
tar -zcvf service_template.tar.gz project.json VERSION project.bundle
```

### Advanced Usage

```bash
tar -zcvf custom_archive.tar.gz *.json *.bundle VERSION --exclude=*.tmp
```

## Expected Output

List of files added to the archive, such as:
a project.json
a VERSION
a project.bundle

## Related

- #tar
- [[procedures/Prepare-Malicious-GitLab-Project-Export]]
