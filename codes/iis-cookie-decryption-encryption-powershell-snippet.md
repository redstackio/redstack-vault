---
id: 46aa8731-a95e-443a-91e6-f282af96cc5f
name: iis-cookie-decryption-encryption-powershell-snippet
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:55:51.828670+00:00'
updated_at: '2023-04-10T20:21:10.579560+00:00'
platforms:
  - Windows
tags:
  - iis
  - cookie-manipulation
  - powershell
validated: true
---

# iis-cookie-decryption-encryption-powershell-snippet

## Code

```powershell
# decrypt cookie
$ AspDotNetWrapper.exe --keypath C:\MachineKey.txt --cookie XXXXXXX_XXXXX-XXXXX --decrypt --purpose=owin.cookie --valalgo=hmacsha512 --decalgo=aes

# encrypt cookie (edit Decrypted.txt)
$ AspDotNetWrapper.exe --decryptDataFilePath C:\DecryptedText.txt
```

## Description

This PowerShell snippet demonstrates the sequential execution of decrypting an IIS machine key-encrypted cookie and then re-encrypting a modified version. It invokes the AspDotNetWrapper.exe tool twice: first for decryption to expose plaintext, and second for encryption after manual edits to Decrypted.txt. Useful in post-exploitation scenarios on Windows systems to manipulate ASP.NET session cookies for privilege escalation or session hijacking.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| C:\MachineKey.txt | Path to the machine key configuration file | C:\web.config excerpt with keys |
| XXXXXXX_XXXXX-XXXXX | Placeholder for the encrypted cookie value | .ASPXAUTH=BASE64ENCODEDVALUE |
| C:\DecryptedText.txt | Path to the output file from decryption (edit before re-encryption) | C:\ModifiedDecrypted.txt |

## Usage

Execute this snippet in a PowerShell session on a Windows machine with AspDotNetWrapper.exe in the PATH. First, replace placeholders with actual values obtained from the target (e.g., via proxy capture). Run the decryption line, edit Decrypted.txt (e.g., change user role), then run the encryption line. The resulting encrypted cookie can be injected via tools like Burp Suite into HTTP requests to impersonate users. Typically used after initial access to an IIS server or when the machine key is exfiltrated.

## Detection

- Monitor PowerShell execution logs for invocations of AspDotNetWrapper.exe or unusual .exe calls with --keypath/--cookie flags.
- File system auditing for access/modification to web.config or temporary files like Decrypted.txt.
- Web server logs for anomalous authentication successes with modified cookies (e.g., sudden privilege changes).
- Network proxies or WAFs detecting cookie tampering via signature mismatches or invalid HMACSHA512 signatures.

## Related

- [[procedures/IIS-Machine-Key-Cookie-Decryption-and-Encryption]]
- [[tools/AspDotNetWrapper]] (if documented separately)
