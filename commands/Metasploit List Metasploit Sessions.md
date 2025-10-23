---
id: 4f349584-0f59-4d76-a9c7-2702d265a842
name: Metasploit List Metasploit Sessions
type: command
executor: metasploit
data: sessions
output: "msf5 exploit(multi/handler) > sessions\n\nActive sessions\n===============\n\
  \n  Id  Name  Type                     Information                     Connection\n\
  \  --  ----  ----                     -----------                     ----------\n\
  \  1         meterpreter x86/windows  BOBPC\\BOB @ BOBPC  10.0.1.100:444 -> 10.0.1.10:1213\
  \ (10.0.1.10)"
created_at: '2020-07-08T22:56:24.137493+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Metasploit List Metasploit Sessions

```metasploit
sessions
```

## Expected Output

```
msf5 exploit(multi/handler) > sessions

Active sessions
===============

  Id  Name  Type                     Information                     Connection
  --  ----  ----                     -----------                     ----------
  1         meterpreter x86/windows  BOBPC\BOB @ BOBPC  10.0.1.100:444 -> 10.0.1.10:1213 (10.0.1.10)
```


