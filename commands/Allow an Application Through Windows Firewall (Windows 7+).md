---
id: 3c6f2451-5c62-461a-8d9a-c567106c35d1
name: Allow an Application Through Windows Firewall (Windows 7+)
type: command
executor: command_prompt
data: netsh advfirewall firewall add rule name="Allow $_Program to bypass firewall
  rules" dir=in action=allow program="C:\$_PATH\$_PROGRAM.exe" enable=yes
output: 'C:\Windows\System32>netsh advfirewall firewall add rule name="Allow calc.exe
  to bypass firewall rules" dir=in action=allow program="C:\Windows\System32\calc.exe"
  enable=yes

  Ok.'
created_at: '2019-11-15T01:22:12.216549+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Allow an Application Through Windows Firewall (Windows 7+)

```command_prompt
netsh advfirewall firewall add rule name="Allow $_Program to bypass firewall rules" dir=in action=allow program="C:\$_PATH\$_PROGRAM.exe" enable=yes
```

## Expected Output

```
C:\Windows\System32>netsh advfirewall firewall add rule name="Allow calc.exe to bypass firewall rules" dir=in action=allow program="C:\Windows\System32\calc.exe" enable=yes
Ok.
```


