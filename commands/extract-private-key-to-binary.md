---
type: command
executor: bash
data: echo $_HEX_PRIVATE_KEY | xxd -r -p > dkmKey.bin
platforms:
  - Linux
  - macOS
tags:
  - decoding
  - private-key
verified: true
validated: true
---

# extract-private-key-to-binary

## Command

```bash
echo $_HEX_PRIVATE_KEY | xxd -r -p > dkmKey.bin
```

## Description

Converts a hexadecimal-encoded private key (DKM format) to binary for use in signing forged SAML tokens.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_HEX_PRIVATE_KEY` | Hex string of the private key | Yes |

## Examples

### Basic Usage

```bash
echo f7404c7f...aabd8b | xxd -r -p > dkmKey.bin
```

### Advanced Usage

From file: `xxd -r -p key.hex > dkmKey.bin`

## Expected Output

Binary file dkmKey.bin created (silent output; verify with `hexdump -C dkmKey.bin`).

## Related

- [[procedures/Golden-SAML-Attack-via-ADFS]]
