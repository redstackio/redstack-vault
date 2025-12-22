---
type: command
executor: cmd
data: build.bat
tags:
  - build
  - cobalt-strike
  - evasion
platforms:
  - Windows
verified: true
validated: true
---

# Execute Sleep Mask Build Batch

## Command

```cmd
build.bat
```

## Description

This command executes the Windows batch file to build the Sleep Mask Kit in Cobalt Strike, handling compilation and obfuscation for Windows-compatible payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `build.bat` | The batch file; run from the project directory | Yes |

## Examples

### Basic Usage

```cmd
build.bat
```

### With Verbose Logging (if supported)

```cmd
build.bat /v
```

## Expected Output

Console output similar to:

```
Starting Sleep Mask Kit build...
Linking libraries...
Obfuscation applied.
Success: Check output directory for files.
```

Errors may point to Visual Studio tools or path configurations.

## Related

- [[procedures/build-sleep-mask-kit-for-cobalt-strike]]
- [[tools/Cobalt-Strike]]
