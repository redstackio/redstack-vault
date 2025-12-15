---
data: jadx -d output_dir app.apk
tags:
  - reverse-engineering
  - mobile
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.227Z'
id: 757a0273-1742-4465-9df3-e0671f0b0f5c
verified: false
validated: true
submitted: true
---
# jadx-decompile-apk

## Command

```bash
jadx -d output_dir app.apk
```

## Description

Decompiles an Android APK file into readable Java source code using Jadx, useful for extracting hardcoded secrets like OAuth keys from mobile apps.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | Output directory for decompiled files | Yes |
| `app.apk` | Path to the APK file | Yes |

## Examples

### Basic Usage

```bash
jadx -d instacart_src instacart.apk
```

### Advanced Usage

```bash
jadx --deobf instacart.apk -d output --show-bad-code
```

## Expected Output

Creates a directory with .java files representing the app's source code, where strings like keys can be searched.

## Related

- [[Related Procedure|procedures/Decompile-Mobile-App-to-Extract-Hardcoded-OAuth-Keys]]
