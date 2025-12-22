---
data: npx asar extract path/to/app.asar extracted/path
tags:
  - extraction
  - electron
type: command
executor: bash
platforms:
  - macOS
id: 2d33c90e-665d-485c-bfea-07d16e54ac62
created_at: '2025-12-11T06:10:40.480Z'
updated_at: '2025-12-11T06:10:40.480Z'
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

Executes the asar package via npx to extract the contents of an Electron app's asar archive to a specified directory, useful for uncovering embedded files like .env with credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `path/to/app.asar` | Path to the asar file | Yes |
| `extracted/path` | Output directory for extracted files | Yes |

## Examples

### Basic Usage

```bash
npx asar extract app.asar out-dir
```

### Advanced Usage

```bash
npx asar extract /path/to/app.asar /path/to/extract
```

## Expected Output

Extracted files including .env in the output directory.

## Related

- [[commands/asar-extract]]
- [[procedures/Extract-Credentials-from-Electron-App]]
