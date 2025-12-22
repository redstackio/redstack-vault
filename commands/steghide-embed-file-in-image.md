---
type: command
executor: bash
data: steghide embed -ef $_EMBEDDED_FILE -cf $_COVER_FILE
output: |-
  root@kali:~# steghide embed -ef id_rsa.pub -cf wallpaper.jpg 
  Enter passphrase: 
  Re-Enter passphrase: 
  embedding "id_rsa.pub" in "wallpaper.jpg"... done
platforms:
  - Linux
tags:
  - steganography
  - obfuscation
verified: true
validated: true
---

# steghide-embed-file-in-image

## Command

```bash
steghide embed -ef $_EMBEDDED_FILE -cf $_COVER_FILE
```

## Description

This command embeds a specified file into a cover file (such as an image or audio) using steganography. It prompts for a passphrase to encrypt the embedded data, allowing covert hiding of payloads in media files for obfuscation during data exfiltration or covert operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ef $_EMBEDDED_FILE | Path to the file to embed (e.g., a secret document or key) | Yes |
| -cf $_COVER_FILE | Path to the cover file (e.g., JPEG, BMP, WAV, or AU) | Yes |
| Passphrase | Interactive input for encryption (uses AES by default) | Yes |

## Examples

### Basic Usage

Embed an SSH public key into a JPEG image:

```bash
steghide embed -ef id_rsa.pub -cf wallpaper.jpg
```

Enter and confirm the passphrase when prompted.

### Advanced Usage

Embed a text file and immediately test extraction:

```bash
steghide embed -ef secret.txt -cf photo.bmp && steghide extract -sf photo.bmp
```

## Expected Output

```
root@kali:~# steghide embed -ef id_rsa.pub -cf wallpaper.jpg 
Enter passphrase: 
Re-Enter passphrase: 
embedding "id_rsa.pub" in "wallpaper.jpg"... done
```

The cover file is overwritten with the embedded version. Success is confirmed by the "done" message; failures include passphrase mismatches or unsupported file types.

## Related

- [[tools/Steghide]]
