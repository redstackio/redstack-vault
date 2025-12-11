---
data: asar extract app.asar asar-out-dir
tags:
  - extraction
  - electron
type: command
executor: bash
platforms:
  - macOS
id: bf346bfe-fe95-436d-a613-61d7095d653a
created_at: '2025-12-11T06:10:40.478Z'
updated_at: '2025-12-11T06:10:40.478Z'
verified: false
validated: true
submitted: true
---
# asar-extract

## Command

```bash
asar extract app.asar asar-out-dir
```

## Description

Directly extracts the asar archive to an output directory, revealing internal app files such as .env containing credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `app.asar` | Input asar file | Yes |
| `asar-out-dir` | Output directory | Yes |

## Examples

### Basic Usage

```bash
asar extract app.asar out-dir
```

### Advanced Usage

```bash
asar extract /full/path/app.asar /extract/dir
```

## Expected Output

Directory containing extracted files, including .env with GH_TOKEN.

## Related

- [[commands/npx-asar-extract]]
- [[procedures/Extract-Credentials-from-Electron-App]]
