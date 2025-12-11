---
data: npx asar extract path/to/app.asar extracted/path
tags:
  - extraction
  - electron
type: command
executor: bash
platforms:
  - macOS
  - Linux
id: 14a635d2-2de4-4940-bafa-a7f0020d443b
created_at: '2025-12-11T03:48:06.064Z'
updated_at: '2025-12-11T03:48:06.064Z'
verified: false
validated: true
submitted: true
---
# npx-asar-extract

## Command

```bash
npx asar extract path/to/app.asar extracted/path
```

## Description

Extracts the contents of an Electron ASAR archive to a specified directory, useful for reverse engineering and discovering exposed files like .env.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `path/to/app.asar` | Path to the input ASAR archive | Yes |
| `extracted/path` | Output directory for extracted files | Yes |

## Examples

### Basic Usage

```bash
npx asar extract app.asar asar-out-dir
```

### Advanced Usage

```bash
npx asar extract /path/to/app.asar /output/dir
```

## Expected Output

Directory created with extracted app files, including potential .env with credentials.

## Related

- [[procedures/Extract-Credentials-from-Electron-ASAR]]
- #asar
