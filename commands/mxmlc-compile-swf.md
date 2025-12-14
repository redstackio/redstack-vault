---
id: c1d2e3f4-g5h6-7891-defg-456789012345
data: >-
  mxmlc -library-path+=/path/to/flashlibs Main.as -swf-version=18
  -output=malicious.swf
tags:
  - compilation
  - flash
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:24:18.609Z'
verified: false
validated: true
submitted: true
---
# mxmlc-compile-swf

## Command

```bash
mxmlc -library-path+=/path/to/flashlibs Main.as -swf-version=18 -output=malicious.swf
```

## Description

Compiles an ActionScript (.as) file into a Flash SWF file using the mxmlc compiler from Adobe Flex SDK, targeting Flash Player 18 for worker support.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-library-path+=` | Path to Flash libraries | Yes |
| `Main.as` | Input ActionScript file | Yes |
| `-swf-version=18` | Target SWF version | Yes |
| `-output=` | Output SWF filename | Yes |

## Examples

### Basic Usage

```bash
mxmlc Main.as -output=test.swf
```

### Advanced Usage

```bash
mxmlc -debug -library-path+=/opt/flex/lib Main.as -swf-version=18 -output=malicious.swf
```

## Expected Output

Successful compilation produces the SWF file; errors if syntax issues or missing libs. Verify with `ls malicious.swf`.

## Related

- [[Related Procedure: Setup-Flash-Worker-Environment]]
