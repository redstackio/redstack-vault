---
id: cmd-extract-snap-escape
data: tar xfvz snap-escape
tags:
  - extraction
  - poc-setup
type: command
output: 'Extracts files including amazing-movie.mp4, README.txt, and tls directory'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:23.828Z'
verified: false
validated: true
submitted: true
---
# extract-snap-escape-poc

## Command

```bash
tar xfvz snap-escape
```

## Description

Extract the POC tar.gz archive containing malicious libraries and decoy files to prepare the malicious cwd for Snap RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| x | Extract files | Yes |
| f | Specify archive file | Yes |
| v | Verbose output | No |
| z | Decompress gzip | Yes |
| snap-escape | Archive name (implied) | Yes |

## Examples

### Basic Usage

```bash
tar xfvz snap-escape
```

### Advanced Usage

```bash
tar xfvz snap-escape.tar.gz
```

## Expected Output

Extracts files including amazing-movie.mp4, README.txt, and tls directory with verbose listing.

## Related

- [[commands/change-to-malicious-directory]]
- [[procedures/Prepare-Malicious-Directory-for-Snap-RCE]]
