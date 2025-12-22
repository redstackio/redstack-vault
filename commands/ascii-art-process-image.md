---
id: cmd-ascii-art-001
data: ascii-art image /full/path/to/test/image
tags:
  - dos
  - exploitation
  - image-processing
type: command
output: null
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.058Z'
verified: false
validated: true
submitted: true
---
# ascii-art-process-image

## Command

```bash
ascii-art image /full/path/to/test/image
```

## Description

This command uses the ascii-art NPM package to process an image file into an ASCII representation, leveraging the canvas module for parsing. When supplied with crafted malicious images, it triggers vulnerabilities in PNG/JPG/GIF parsing, causing Node.js to segfault and crash, demonstrating DoS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `image` | Path to the input image file (e.g., crafted PNG to exploit buffer overflow) | Yes |

## Examples

### Basic Usage

```bash
ascii-art image /full/path/to/test/image
```

Processes the image and outputs ASCII art, or crashes on malformed input.

### Advanced Usage

```bash
ascii-art image /full/path/to/test/image --width 80
```

Specifies output width; still vulnerable to parsing flaws.

## Expected Output

On success with valid image: ASCII art representation printed to stdout. On exploit: Node.js segfault, core dump, and process termination without output.

## Related

- [[procedures/Reproduce-Canvas-DoS-with-Crafted-Images-via-Ascii-Art]]
- [[procedures/Fuzz-Node-js-Canvas-for-Image-Parsing-Vulnerabilities]]
