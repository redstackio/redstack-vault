---
id: 568f45a7-00c3-41ac-9c5c-e9c214e53141
name: Metasploit Load One or More Meterpreter Extensions
type: command
executor: metasploit
data: load $_MODULE
output: 'msf5 > use exploit/windows/smb/ms17_010_eternalblue

  [*] No payload configured, defaulting to windows/x64/meterpreter/reverse_tcp'
created_at: '2020-07-08T22:56:24.136624+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Metasploit Load One or More Meterpreter Extensions

```metasploit
load $_MODULE
```

## Expected Output

```
msf5 > use exploit/windows/smb/ms17_010_eternalblue
[*] No payload configured, defaulting to windows/x64/meterpreter/reverse_tcp
```


