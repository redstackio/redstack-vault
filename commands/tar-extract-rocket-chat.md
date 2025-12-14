---
data: tar -xvzf rocket.chat.tgz
tags:
  - extraction
  - archive
type: command
output: 'Lists extracted files, e.g., ''frogs-find-bugs/'' and ''frogs-find-bugs/hehehe'''
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:42.006Z'
id: 659b774c-0bb3-4dc5-bf01-1360e74059b6
verified: false
validated: true
submitted: true
---
# tar-extract-rocket-chat

## Command

```bash
tar -xvzf rocket.chat.tgz
```

## Description

Extracts the contents of the gzipped tarball, revealing injected malicious payloads in the Rocket.Chat bundle.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-x` | Extract files | Yes |
| `-v` | Verbose listing | No |
| `-z` | Filter through gzip | Yes |
| `-f` | File to extract | Yes |

## Examples

### Basic Usage

```bash
tar -xvzf rocket.chat.tgz
```

### Advanced Usage

```bash
tar -xvzf rocket.chat.tgz -C /target/dir
```

## Expected Output

Verbose list of extracted files and directories, including any malicious additions.

## Related

- [[Related Procedure: Download-and-Extract-Malicious-Tarball]]
