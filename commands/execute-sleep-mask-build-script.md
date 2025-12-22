---
type: command
executor: bash
data: ./build.sh
tags:
  - build
  - cobalt-strike
  - evasion
platforms:
  - Linux
  - Unix
verified: true
validated: true
---

# Execute Sleep Mask Build Script

## Command

```bash
./build.sh
```

## Description

This command runs the Bash build script for the Sleep Mask Kit in Cobalt Strike, automating the compilation and obfuscation of evasion-focused payloads on Unix-like systems.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `./build.sh` | The build script file; ensure executable permissions with `chmod +x build.sh` | Yes |

## Examples

### Basic Usage

```bash
./build.sh
```

### With Custom Options (if script supports)

```bash
./build.sh --debug
```

## Expected Output

Successful execution produces output like:

```
Building Sleep Mask Kit...
Compiling sources...
Applying obfuscation...
Build complete: Artifacts in ./output/
```

Any errors will indicate missing dependencies or path issues.

## Related

- [[procedures/build-sleep-mask-kit-for-cobalt-strike]]
- [[tools/Cobalt-Strike]]
