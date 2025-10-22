---
id: 00d49676-35d6-40e4-b979-5ea20a0c500e
name: Allow a Port Through Windows Firewall (Windows 2008 and Earlier)
type: command
executor: command_prompt
data: netsh firewall add portopening TCP $_PORT "Open Port $_PORT"
output: C:\netsh firewall add portopening 80 "Open Port 80"
created_at: '2019-11-15T01:22:12.239504+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Allow a Port Through Windows Firewall (Windows 2008 and Earlier)

```command_prompt
netsh firewall add portopening TCP $_PORT "Open Port $_PORT"
```

## Expected Output

```
C:\netsh firewall add portopening 80 "Open Port 80"
```
