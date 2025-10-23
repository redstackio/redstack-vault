---
id: 2c143fa6-8c4f-411a-b8f8-0cf82f61a4bf
name: Metasploit Forward a Local Port to a Remote Server
type: command
executor: metasploit
data: portfwd add -l $_LOCAL_PORT -p $_REMOTE_PORT -r $_TARGET_IP
output: 'meterpreter > portfwd add -l 5985 -p 5985 -r 10.10.1.5

  [*] Local TCP relay created: :5985 <-> 10.10.1.5:5985'
created_at: '2020-07-09T01:33:04.342428+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Metasploit Forward a Local Port to a Remote Server

```metasploit
portfwd add -l $_LOCAL_PORT -p $_REMOTE_PORT -r $_TARGET_IP
```

## Expected Output

```
meterpreter > portfwd add -l 5985 -p 5985 -r 10.10.1.5
[*] Local TCP relay created: :5985 <-> 10.10.1.5:5985
```


