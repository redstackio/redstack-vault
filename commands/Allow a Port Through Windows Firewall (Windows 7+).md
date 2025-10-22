---
id: b8ffb019-da27-48ed-b8de-0a64e01323ae
name: Allow a Port Through Windows Firewall (Windows 7+)
type: command
executor: command_prompt
data: netsh advfirewall firewall add rule name="Open Port $_PORT" dir=in action=allow
  protocol=TCP localport=$_PORT
output: 'C:\>netsh advfirewall firewall add rule name="Open Port 80" dir=in action=allow
  protocol=TCP localport=80

  Ok.'
created_at: '2019-11-15T01:22:12.204754+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Allow a Port Through Windows Firewall (Windows 7+)

```command_prompt
netsh advfirewall firewall add rule name="Open Port $_PORT" dir=in action=allow protocol=TCP localport=$_PORT
```

## Expected Output

```
C:\>netsh advfirewall firewall add rule name="Open Port 80" dir=in action=allow protocol=TCP localport=80
Ok.
```
