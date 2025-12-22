---
id: cmd-wget-download
data: >-
  wget
  https://github.com/nextcloud/groupfolders/releases/download/v6.0.2/groupfolders.tar.gz
tags:
  - download
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:27.784Z'
verified: false
validated: true
submitted: true
---
# wget-download

## Command

```bash
wget https://github.com/nextcloud/groupfolders/releases/download/v6.0.2/groupfolders.tar.gz
```

## Description

Downloads a file from a URL using wget, useful for fetching public release artifacts in vulnerability research.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | The download source | Yes |
| Output file | Implicit from URL | No |

## Examples

### Basic Usage

```bash
wget https://example.com/file.tar.gz
```

### Advanced Usage

```bash
wget -O customname.tar.gz https://github.com/.../file.tar.gz
```

## Expected Output

Progress bar and confirmation: 'groupfolders.tar.gz: OK' with file size.

## Related

- [[curl]]
