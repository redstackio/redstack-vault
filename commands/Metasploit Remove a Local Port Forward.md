---
id: 4809fa1f-bfc9-40e2-86bb-ba2af5194025
name: Metasploit Remove a Local Port Forward
type: command
executor: metasploit
data: portfwd delete -l $_LOCAL_PORT -p $_REMOTE_PORT -r $_TARGET_IP
output: 'meterpreter > portfwd delete -l 5985 -p 5985 -r 10.10.1.5

  [*] Successfully stopped TCP relay on 0.0.0.0:5985'
created_at: '2020-07-09T01:33:04.343158+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Metasploit Remove a Local Port Forward

```metasploit
portfwd delete -l $_LOCAL_PORT -p $_REMOTE_PORT -r $_TARGET_IP
```

## Expected Output

```
meterpreter > portfwd delete -l 5985 -p 5985 -r 10.10.1.5
[*] Successfully stopped TCP relay on 0.0.0.0:5985
```
