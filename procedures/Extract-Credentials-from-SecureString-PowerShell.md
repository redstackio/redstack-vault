---
id: 8e7c2cf7-d471-4d6a-b7af-605068e4fb9a
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:24.121898+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Credentials from Password Stores]]'
  - '[[Unsecured Credentials]]'
sub_techniques:
  - '[[Credentials in Files]]'
tags:
  - powershell
  - secure-string
  - credential-extraction
  - credential-access
commands: []
platforms:
  - Windows
tools: []
validated: true
---

# Extract-Credentials-from-SecureString-PowerShell

## Summary

This procedure demonstrates how to extract plaintext network credentials from an encrypted secure string using PowerShell. It is useful in post-exploitation scenarios where an attacker has obtained an encrypted credential artifact, such as from memory, files, or configuration stores, allowing conversion to usable plaintext for lateral movement or privilege escalation.

## Description

Secure strings in PowerShell are used to store sensitive data like passwords in an encrypted format to prevent casual exposure. However, if an attacker obtains the encrypted string (e.g., via credential dumping tools like Mimikatz or by accessing configuration files), they can reconstruct the PSCredential object and retrieve the plaintext password using the GetNetworkCredential() method. This technique targets unsecured credentials in password stores and is effective on Windows systems where PowerShell is available. The process involves converting the hex-encoded secure string back to its secure form, pairing it with a username, and extracting the domain, username, and password. Success enables authentication to network resources like SMB shares or RDP. This maps to MITRE ATT&CK techniques for accessing credentials from password stores and unsecured files, commonly seen in environments with weak credential hygiene.

## Requirements

1. PowerShell 2.0 or later installed on a Windows system (typically pre-installed on Windows 7+).
2. The encrypted secure string in hex format, obtained from sources like LSASS dump, config files, or keylogging.
3. Administrative or user-level access to execute PowerShell scripts.
4. Knowledge of the target username and domain associated with the credential.

## Defense

- Enable PowerShell logging (Module, Script Block, and Transcription) to monitor credential manipulation attempts.
- Use Group Policy to restrict PowerShell execution to signed scripts and implement Constrained Language Mode.
- Implement credential guard features like Windows Credential Guard to protect LSASS and secure strings.
- Regularly rotate credentials and avoid storing them in plaintext or easily decryptable formats in files or configs.
- Monitor for anomalous PowerShell processes spawning from unusual parents or accessing credential-related APIs.

## Objectives

1. Convert an encrypted secure string to a PSCredential object.
2. Extract the plaintext password and associated network details.
3. Validate the credentials for use in network authentication.

## Instructions

### Step 1: Prepare and Convert the Secure String

**Context**: Obtain the encrypted secure string (a hex blob representing the encrypted password) and the target username/domain. This step reconstructs the secure string object from the hex input, which is necessary because PowerShell's ConvertTo-SecureString expects this format for decryption in the current user context.

**Code** ([[codes/PowerShell-Extract-SecureString-Credentials]]):

```powershell
$pass = "01000000d08c9ddf0115d1118c7a00c04fc297eb01000000e4a07bc7aaeade47925c42c8be5870730000000002000000000003660000c000000010000000d792a6f34a55235c22da98b0c041ce7b0000000004800000a00000001000000065d20f0b4ba5367e53498f0209a3319420000000d4769a161c2794e19fcefff3e9c763bb3a8790deebf51fc51062843b5d52e40214000000ac62dab09371dc4dbfd763fea92b9d5444748692" | ConvertTo-SecureString
```

> This command takes the hex string and converts it to a SecureString object. The hex must match the encryption context (user profile) where it was created; otherwise, decryption fails. Expected output: A SecureString object (not visible in plaintext yet).

### Step 2: Create PSCredential Object and Extract Network Credentials

**Context**: Pair the secure string with the username to form a credential object, then use GetNetworkCredential() to retrieve the plaintext details. This method decrypts the password in memory for network use, exposing it to the attacker.

**Code** ([[codes/PowerShell-Extract-SecureString-Credentials]]):

```powershell
$user = "HTB\Tom"
$cred = New-Object System.Management.Automation.PSCredential($user, $pass)
$cred.GetNetworkCredential() | Format-List
```

> Replace 'HTB\Tom' with the actual domain\username. The New-Object creates the credential, and GetNetworkCredential() outputs the domain, username, and plaintext password. If the hex is invalid for the context, it will error with 'Key not valid for use'. Expected output: A formatted list showing UserName, Password (plaintext), and Domain.

### Step 3: Validate Extracted Credentials

**Context**: Test the credentials against a network resource to confirm usability, such as authenticating to a remote share. This verifies the extraction without alerting defenders prematurely.

**Instructions**: Use the extracted password in a test like Test-NetConnection or Invoke-Command. For example:

```powershell
$extractedPass = $cred.GetNetworkCredential().Password
Test-NetConnection -ComputerName target-server -Port 445 -Credential $cred
```

> Success is indicated by no authentication errors and a reachable status. If it fails, the secure string may be context-bound or corrupted.
