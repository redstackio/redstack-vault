---
id: 392b755a-e9bb-429e-94e7-be91c281bc5d
name: Connect via WinRM
type: command
executor: bash
data: '$password = ConvertTo-SecureString ''<PASSWORD>'' -AsPlainText -Force

  $creds = New-Object System.Management.Automation.PSCredential(''username'', $Password)

  $sess = New-PSSession -ComputerName <IP> -Credential $creds -SessionOption (New-PSSessionOption
  -ProxyAccessType NoProxyServer)

  Enter-PSSession $sess'
output: null
created_at: '2023-05-28T03:59:38.556147+00:00'
updated_at: '2023-05-28T03:59:38.880779+00:00'
---

# Connect via WinRM

```bash
$password = ConvertTo-SecureString '<PASSWORD>' -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential('username', $Password)
$sess = New-PSSession -ComputerName <IP> -Credential $creds -SessionOption (New-PSSessionOption -ProxyAccessType NoProxyServer)
Enter-PSSession $sess
```
