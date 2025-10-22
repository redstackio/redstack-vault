---
id: 4de4020d-a4cc-4afc-8211-0c9dc23969c2
name: Configure DNS server with DNSServer module
type: command
executor: bash
data: Set-DnsServerSetting -InputObject $dnsettings -ComputerName <servername> -Verbose
output: null
created_at: '2023-04-06T03:56:06.475008+00:00'
updated_at: '2023-04-10T20:26:10.325254+00:00'
---

# Configure DNS server with DNSServer module

```bash
Set-DnsServerSetting -InputObject $dnsettings -ComputerName <servername> -Verbose
```
