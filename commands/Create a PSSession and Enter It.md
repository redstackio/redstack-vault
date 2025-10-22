---
id: 9785dc53-c079-4266-b528-3ded8492c7b8
name: Create a PSSession and Enter It
type: command
executor: powershell
data: '$Session = New-PSSession -Credential $Cred -ComputerName $_TARGET_IP

  Enter-PSSession $Session'
output: 'PS C:\ > $Session = New-PSSession -Credential $Cred -ComputerName 10.10.10.10

  PS C:\ > Enter-PSSession $Session

  [10.10.10.10]: PS C:\Users\Administrator\Documents>'
created_at: '2020-03-21T01:59:57.750243+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Create a PSSession and Enter It

```powershell
$Session = New-PSSession -Credential $Cred -ComputerName $_TARGET_IP
Enter-PSSession $Session
```

## Expected Output

```
PS C:\ > $Session = New-PSSession -Credential $Cred -ComputerName 10.10.10.10
PS C:\ > Enter-PSSession $Session
[10.10.10.10]: PS C:\Users\Administrator\Documents>
```
