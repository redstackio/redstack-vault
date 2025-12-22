---
id: 70364792-96d5-459a-92e0-f3aaa9ac9cde
name: IIS-Machine-Key-Cookie-Decryption-and-Encryption
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:51.836736+00:00'
updated_at: '2023-04-10T20:21:10.559901+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Use Alternate Authentication Material|T1550 - Use Alternate
    Authentication Material]]
sub_techniques:
  - '[[sub-techniques/Pass the Ticket|T1550.003 - Pass the Ticket]]'
tags:
  - '[[tags/API Key Leaks]]'
  - '[[tags/Edit cookies with the machine key]]'
  - '[[tags/Exploit]]'
  - '[[tags/IIS Machine Keys]]'
commands:
  - '[[commands/decrypt-iis-cookie-with-aspdotnetwrapper]]'
  - '[[commands/encrypt-modified-cookie-with-aspdotnetwrapper]]'
platforms:
  - Windows
tools: []
validated: true
---

# IIS-Machine-Key-Cookie-Decryption-and-Encryption

## Summary

This procedure enables attackers to decrypt encrypted cookies in ASP.NET applications hosted on IIS by leveraging the server's machine key, view or modify sensitive data such as session tokens or authentication details, and then re-encrypt the altered cookie for injection back into the application. It is commonly used in web application attacks to bypass authentication, escalate privileges, or maintain persistence by forging valid session data.

## Description

In ASP.NET applications running on IIS, sensitive data like authentication cookies is encrypted using a machine key stored in the web.config file. This key ensures data integrity and confidentiality. Attackers who obtain the machine key—often through configuration file access, misconfigurations, or prior compromise—can use tools like AspDotNetWrapper.exe to decrypt these cookies, revealing plaintext contents such as user IDs, roles, or API keys. Modifications can then be made to impersonate users or elevate access, followed by re-encryption to create a valid cookie for submission. This technique targets Windows-based web servers and is effective against applications using OWIN cookie authentication with HMACSHA512 validation and AES decryption algorithms. Prerequisites include access to the machine key file and the target cookie value, typically obtained via network interception or client-side extraction.

## Requirements

1. Access to the IIS machine key configuration file (e.g., web.config or machineKey.xml) containing the validation and decryption keys.
2. The AspDotNetWrapper.exe tool, downloadable from relevant security repositories or built from source.
3. The encrypted cookie value from the target ASP.NET application.
4. Windows environment (e.g., attacker machine with .NET Framework) to execute the tool.
5. Basic knowledge of cookie formats and ASP.NET authentication mechanisms.

## Defense

- Store machine key configuration files in secure locations with restricted file system permissions to prevent unauthorized access.
- Enable ViewState encryption and use strong, auto-generated machine keys rotated periodically.
- Implement secure cookie handling practices, including HttpOnly and Secure flags, to mitigate cookie theft via XSS or network interception.
- Monitor for anomalous cookie modifications through web application firewalls (WAFs) or logging of authentication events.
- Use certificate-based or token-based authentication (e.g., JWT with proper signing) instead of machine key-dependent cookies.

## Objectives

1. Decrypt an IIS-encrypted cookie to expose sensitive plaintext data like session tokens or user credentials.
2. Modify the decrypted data to alter authentication state, such as elevating user privileges.
3. Re-encrypt the modified cookie to inject it back into the application for unauthorized access or persistence.

## Instructions

### Step 1: Prepare the Machine Key and Cookie Data

**Context**: Obtain the machine key from the target's web.config file and the encrypted cookie value, typically via browser developer tools or proxy interception. Ensure the tool is available and paths are correctly set. This step sets up the inputs needed for decryption.

No specific command here; manually copy the machine key content to a file like C:\MachineKey.txt and note the cookie value (e.g., from a .ASPXAUTH cookie).

> Verify the machine key format includes validationKey and decryptionKey attributes matching HMACSHA512 and AES.

### Step 2: Decrypt the Cookie

**Context**: Use the AspDotNetWrapper tool to decrypt the cookie using the specified purpose (owin.cookie), validation algorithm (HMACSHA512), and decryption algorithm (AES). This reveals the plaintext content, which is saved to Decrypted.txt for inspection.

**Command** ([[commands/decrypt-iis-cookie-with-aspdotnetwrapper]]):
```cmd
AspDotNetWrapper.exe --keypath C:\MachineKey.txt --cookie $_COOKIE_VALUE --decrypt --purpose=owin.cookie --valalgo=hmacsha512 --decalgo=aes
```

> This command processes the encrypted cookie against the machine key, outputting the decrypted data to Decrypted.txt. Expected output includes a success message and the file containing plaintext like JSON-serialized user claims or tokens. If the key or algorithms mismatch, an error like "Invalid signature" will occur—double-check the web.config.

### Step 3: Modify the Decrypted Cookie Content

**Context**: Open the Decrypted.txt file in a text editor to view and edit the plaintext. Common modifications include changing user roles (e.g., from "User" to "Admin") or injecting payloads. This step exploits the visibility of sensitive data for manipulation.

No command; use a text editor like Notepad to alter the content, ensuring the format remains valid (e.g., valid JSON for claims-based auth).

> After editing, save the file as C:\DecryptedText.txt. Validate changes manually to avoid breaking the cookie structure, which could lead to authentication failures.

### Step 4: Re-encrypt the Modified Cookie

**Context**: Encrypt the edited plaintext back into a valid cookie format using the same machine key and algorithms. This produces an encrypted cookie ready for injection via browser tools or requests.

**Command** ([[commands/encrypt-modified-cookie-with-aspdotnetwrapper]]):
```cmd
AspDotNetWrapper.exe --decryptDataFilePath C:\DecryptedText.txt
```

> This command reads the modified file and outputs the encrypted cookie value, typically to stdout or a new file. Success is indicated by a valid base64-encoded string matching the original cookie's format. Use this output to replace the original cookie in HTTP requests for testing access.
