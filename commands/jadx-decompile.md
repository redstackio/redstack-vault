---
data: jadx zomato.apk -d zomato_decompiled
tags:
  - jadx
  - decompilation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:18.212Z'
id: f778d28f-4ff9-4bcc-9a8b-663342ce1ed2
verified: false
validated: true
submitted: true
---
# jadx-decompile

## Command

```bash
jadx zomato.apk -d zomato_decompiled
```

## Description

Decompiles an Android APK into readable Java source code using Jadx.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `zomato.apk` | Input APK | Yes |
| `-d zomato_decompiled` | Output directory | Yes |

## Examples

### Basic Usage

```bash
jadx zomato.apk -d zomato_decompiled
```

### Advanced Usage

```bash
jadx -Xmx4g zomato.apk -d output_dir
```

## Expected Output

Directory with decompiled sources, including activity classes.

## Related

- [[Related Procedure]]
