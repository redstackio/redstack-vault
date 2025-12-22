---
id: e6af797f-ff51-4879-ac87-66f62b5640db
name: bzr-revert-extracted-tree
type: command
executor: bash
data: bzr revert
output: null
created_at: '2023-04-06T03:56:00.354729+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - bzr
  - revert
  - cleanup
verified: true
validated: true
---

# bzr-revert-extracted-tree

## Command

```bash
bzr revert
```

## Description

This command reverts any uncommitted changes or new files in a Bazaar working tree, cleaning up the extracted source code directory after dumping to remove artifacts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| bzr | The Bazaar command-line tool | Yes |

## Examples

### Basic Usage

Run in the extracted directory:

```bash
cd extracted-source && bzr revert
```

### Advanced Usage

Revert specific files:

```bash
bzr revert application.py database.py
```

## Expected Output

 N  application.py
 N  database.py
 N  static/

## Related

- [[procedures/Extract-Source-Code-from-Insecure-Bazaar-Repository]]
