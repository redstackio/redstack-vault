---
id: 37797ac4-3bd9-4c71-ae2c-343bac18f15d
name: Powershell remoting to machine
type: command
executor: ''
data: '$SESSION = New-PSSession $COMPUTER_NAME

  Enter-PSSession $SESSION'
output: null
created_at: '2023-01-12T07:48:43.751451+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Powershell remoting to machine

```bash
$SESSION = New-PSSession $COMPUTER_NAME
Enter-PSSession $SESSION
```
