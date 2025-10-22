---
id: 29ceadc8-de20-4add-9841-f71a2bbe8bc5
name: Open interactive session with remote computer
type: command
executor: bash
data: '$cred = Get-Credential

  Enter-PSSession -ComputerName ''winserver1'' -Credential $cred -Authentication Basic

  '
output: null
created_at: '2020-07-14T18:21:13.085814+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Open interactive session with remote computer

```bash
$cred = Get-Credential
Enter-PSSession -ComputerName 'winserver1' -Credential $cred -Authentication Basic

```
