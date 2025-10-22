---
id: b9c5adf0-b3fb-4212-a41b-db382a225d06
name: Enumerate Targets
type: command
executor: bash
data: nmap -p 139,445 --script smb-enum-shares.nse,smb-enum-users.nse --script-args
  smbuser='Guest',smbpass='' -oN nmap.txt 192.168.0.0/24
output: null
created_at: '2023-04-06T03:56:05.363468+00:00'
updated_at: '2023-04-10T20:26:21.879066+00:00'
---

# Enumerate Targets

```bash
nmap -p 139,445 --script smb-enum-shares.nse,smb-enum-users.nse --script-args smbuser='Guest',smbpass='' -oN nmap.txt 192.168.0.0/24
```
