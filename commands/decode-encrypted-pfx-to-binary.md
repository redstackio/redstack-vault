---
type: command
executor: bash
data: echo $_BASE64_ENCODED_PFX | base64 -d > EncryptedPfx.bin
platforms:
  - Linux
  - macOS
tags:
  - decoding
  - pfx
verified: true
validated: true
---

# decode-encrypted-pfx-to-binary

## Command

```bash
echo $_BASE64_ENCODED_PFX | base64 -d > EncryptedPfx.bin
```

## Description

Decodes a base64-encoded PFX certificate to binary format for use in SAML token forging tools like ADFSpoof.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_BASE64_ENCODED_PFX` | Base64 string of the encrypted PFX | Yes |

## Examples

### Basic Usage

```bash
echo AAAAAQAAAAAEE... | base64 -d > EncryptedPfx.bin
```

### Advanced Usage

Pipe from file: `cat pfx.b64 | base64 -d > EncryptedPfx.bin`

## Expected Output

Binary file EncryptedPfx.bin created (no stdout; check with `ls -la EncryptedPfx.bin`).

## Related

- [[procedures/Golden-SAML-Attack-via-ADFS]]
