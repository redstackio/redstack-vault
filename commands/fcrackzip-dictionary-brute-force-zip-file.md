---
id: 3ce20c20-0472-4455-9d20-6ad15b039219
name: fcrackzip-dictionary-brute-force-zip-file
type: command
executor: bash
data: fcrackzip -v -u $_FILENAME -D -p $_WORDLIST
output: >-
  root@kali:~# fcrackzip -v -u secret.zip -D -p
  /usr/share/wordlists/rockyou.txt 

  found file 'id_rsa', (size cp/uc   1379/  1811, flags 9, chk 930e)



  PASSWORD FOUND!!!!: pw == princess1
created_at: '2019-09-24T22:44:39.876065+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Windows
tags:
  - brute-force
  - password-cracking
  - zip
verified: true
validated: true
---

# fcrackzip-dictionary-brute-force-zip-file

## Command

```bash
fcrackzip -v -u $_FILENAME -D -p $_WORDLIST
```

## Description

This command performs a dictionary-based brute force attack on a password-protected ZIP file using fcrackzip. It attempts passwords from a specified wordlist to decrypt the file, verifying if the contents are intact upon success. Use this for recovering weak passwords on encrypted archives obtained during security assessments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_FILENAME | Path to the target ZIP file | Yes |
| $_WORDLIST | Path to the dictionary wordlist file | Yes |
| -v | Enable verbose output to show progress | No |
| -u | Check if decrypted files are unmodified (integrity check) | No |
| -D | Activate dictionary mode for wordlist-based cracking | Yes |
| -p | Specify the wordlist file for passwords | Yes |

## Examples

### Basic Usage

```bash
fcrackzip -v -u secret.zip -D -p /usr/share/wordlists/rockyou.txt
```

### Advanced Usage

```bash
fcrackzip -v -u -D -p custom_wordlist.txt encrypted_archive.zip
```

## Expected Output

Description of what output to expect when the command runs successfully.

```
root@kali:~# fcrackzip -v -u secret.zip -D -p /usr/share/wordlists/rockyou.txt 
found file 'id_rsa', (size cp/uc   1379/  1811, flags 9, chk 930e)


PASSWORD FOUND!!!!: pw == princess1
```

## Related

- [[tools/fcrackzip]]
- [[procedures/Crack-ZIP-Passwords-with-Dictionary-Attack]]
