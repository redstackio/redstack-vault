---
id: dc8e93e2-96d6-449d-8eee-643a486b7df1
name: Extract-Service-Principal-Keys-from-Keytab
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:08.683044+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Credentials from Password Stores|T1555 - Credentials from
    Password Stores]]
  - >-
    [[techniques/Use Alternate Authentication Material|T1550 - Use Alternate
    Authentication Material]]
sub_techniques:
  - >-
    [[sub-techniques/Kerberos Credential from Password Store|T1555.004 -
    Kerberos Credential from Password Store]]
  - '[[sub-techniques/Pass the Key|T1550.003 - Pass the Key]]'
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Kerberos Keytab Extraction]]'
  - kerberos
  - credential-access
commands:
  - '[[commands/list-kerberos-keytab-entries]]'
  - '[[commands/extract-ntlm-hash-from-keytab]]'
  - '[[commands/dump-keytab-with-bifrost]]'
  - '[[commands/authenticate-with-hash-crackmapexec]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/keytabextract]]'
  - '[[tools/bifrost]]'
  - '[[tools/CrackMapExec]]'
validated: true
---

# Extract-Service-Principal-Keys-from-Keytab

## Summary

This procedure extracts service principal keys and NTLM hashes from a Kerberos keytab file, typically located at /etc/krb5.keytab on Linux systems or equivalent on Windows. These credentials can be used to authenticate as service accounts in Active Directory environments, enabling lateral movement or privilege escalation.

## Description

Kerberos keytab files store long-term keys for service principals, allowing services to authenticate without user interaction. Attackers with access to the keytab can list entries, extract keys (often in RC4-HMAC format convertible to NTLM hashes), and use them for pass-the-key attacks. This is common in Active Directory setups where service accounts have elevated privileges. The procedure uses built-in tools like klist for listing and Python scripts like keytabextract for hash extraction. Extracted hashes can then be used with tools like CrackMapExec for authentication against domain resources. Prerequisites include file system access to the keytab, which may require local admin or service account privileges. Success allows impersonation of the service principal across SMB, LDAP, or other Kerberos-enabled services.

## Requirements

1. Access to the keytab file (e.g., read permissions on /etc/krb5.keytab or Windows equivalent).
2. Python 3 environment for keytabextract.
3. Bifrost tool installed for advanced dumping (optional).
4. CrackMapExec installed for hash-based authentication testing.
5. Domain knowledge (e.g., account names, IPs) for validation.

## Defense

- Restrict keytab file permissions to root/system only and monitor access via file auditing.
- Rotate service principal keys regularly and use stronger encryption types (e.g., AES over RC4).
- Enable Kerberos logging on domain controllers to detect anomalous ticket requests.
- Deploy endpoint detection for tools like keytabextract or CrackMapExec executions.
- Implement least privilege for service accounts to limit impact of key compromise.

## Objectives

1. Enumerate service principals and keys in the keytab file.
2. Extract usable NTLM hashes from RC4 keys.
3. Dump keytab contents if needed for offline analysis.
4. Validate extracted credentials via remote authentication.

## Instructions

### Step 1: List Kerberos Keytab Entries

**Context**: Begin by listing all service principal entries in the keytab to identify potential targets, including principals, key versions, encryption types, and keys. This step reveals what credentials are available without extraction.

**Command** ([[commands/list-kerberos-keytab-entries]]):
```powershell
klist -t -K -e -k FILE:$_KEYTAB_PATH
```

> The klist command (Windows-native) displays keytab contents. Use -t for timestamps, -K for keys, -e for encryption types, and -k for the keytab file. On Linux, use ktutil or similar. Replace $_KEYTAB_PATH with the file path (e.g., C:\path\to\krb5.keytab). This step confirms accessible principals like host/COMPUTER@DOMAIN.

### Step 2: Extract NTLM Hash from Keytab

**Context**: Use keytabextract to convert RC4-HMAC keys to NTLM hashes. This is crucial if RC4 is present, as it enables NTLM-based authentication. If no RC4, extraction fails, indicating stronger keys.

**Command** ([[commands/extract-ntlm-hash-from-keytab]]):
```bash
python3 keytabextract.py $_KEYTAB_FILE
```

> Run keytabextract.py on the keytab file. It imports the file, identifies RC4-HMAC entries, and outputs NTLM hashes. Success depends on RC4 presence; otherwise, consider AES extraction tools. Expected output includes realm, principal, and hash (e.g., NTLM HASH: 31d6cfe0d16ae931b73c59d7e0c089c0).

### Step 3: Dump Keytab with Bifrost (Optional)

**Context**: For comprehensive dumping or if keytabextract fails, use Bifrost to export keytab contents securely. This is useful for transferring or analyzing large keytabs offline.

**Command** ([[commands/dump-keytab-with-bifrost]]):
```bash
./bifrost -action dump -source keytab -path $_KEYTAB_PATH
```

> Bifrost's dump action extracts keytab data. Specify -action dump, -source keytab, and -path to the file. This produces a readable dump of entries, keys, and metadata. Use if basic extraction needs supplementation.

### Step 4: Authenticate with Extracted Hash

**Context**: Test the extracted NTLM hash by authenticating to a target machine using CrackMapExec. This validates usability for lateral movement, confirming access to domain resources.

**Command** ([[commands/authenticate-with-hash-crackmapexec]]):
```bash
crackmapexec $_TARGET_IP -u '$_ACCOUNT_NAME$' -H "$_NTLM_HASH" -d "$_DOMAIN"
```

> CrackMapExec (CME) performs hash-based authentication over SMB. Use -u for the machine/service account (append $), -H for NTLM hash, -d for domain, and target IP. Success shows [+] authentication confirmation, enabling further actions like shell access.
