---
id: c3f4g5h6-i7j8-9013-fghi-6789012345
data: >-
  echo "$ENCRYPTED_CONTENT" | base64 -d | openssl enc -d -aes-128-cbc -k $KEY
  -iv $IV -out decrypted.txt
tags:
  - decryption
  - crypto
  - email
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:24:39.817Z'
verified: false
validated: true
submitted: true
---
# openssl-decrypt-email

## Command

```bash
echo "$ENCRYPTED_CONTENT" | base64 -d | openssl enc -d -aes-128-cbc -k $KEY -iv $IV -out decrypted.txt
```

## Description

Decrypts base64-encoded AES-encrypted email content using OpenSSL, targeting weak encryption schemes in verification emails.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo "$ENCRYPTED_CONTENT"` | Input the encrypted string | Yes |
| `base64 -d` | Decode base64 wrapper | Yes |
| `openssl enc -d -aes-128-cbc` | Decrypt with AES-128-CBC | Yes |
| `-k $KEY` | Symmetric key; replace $KEY (e.g., weak default) | Yes |
| `-iv $IV` | Initialization vector; often zero or predictable | Yes |
| `-out decrypted.txt` | Output file | Yes |

## Examples

### Basic Usage

```bash
echo "U2FsdGVkX1+abc123encrypted==" | base64 -d | openssl enc -d -aes-128-cbc -k weakpass -iv 0000000000000000 -out decrypted.txt
```

### Advanced Usage

```bash
cat email.enc | openssl enc -d -aes-128-cbc -k weakpass -iv zeros -out decrypted.txt && cat decrypted.txt
```

## Expected Output

File decrypted.txt with plaintext content, e.g., "Verification link: https://... token: abc123".

## Related

- [[Related Procedure: Decrypt-Verification-Email-Content]]
