---
id: 36993b1c-98b6-4e67-860e-0c17eb987352
name: Metasploit Interact with a Session
type: command
executor: metasploit
data: sessions -i $_ID
output: 'msf5 exploit(multi/handler) > sessions -i 1

  [*] Starting interaction with 1...


  meterpreter > '
created_at: '2020-07-08T22:56:24.137452+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Metasploit Interact with a Session

```metasploit
sessions -i $_ID
```

## Expected Output

```
msf5 exploit(multi/handler) > sessions -i 1
[*] Starting interaction with 1...

meterpreter > 
```


