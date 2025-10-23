---
id: 2d79d965-ac0a-4e17-b931-157e52303d5e
name: Execute notepad.exe with debug mode
type: command
executor: bash
data: python3 dcomexec.py -object MMC20 -silentcommand -debug $DOMAIN/$USER:$PASSWORD\$@$HOST
  'notepad.exe'
output: null
created_at: '2023-04-06T03:56:07.043189+00:00'
updated_at: '2023-04-10T20:26:18.160002+00:00'
---

# Execute notepad.exe with debug mode

```bash
python3 dcomexec.py -object MMC20 -silentcommand -debug $DOMAIN/$USER:$PASSWORD\$@$HOST 'notepad.exe'
```


