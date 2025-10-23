---
id: 9c21b8ff-2b37-4356-8d41-54fc0ced9190
name: Metasploit Set a Context Specific Variable to a Value
type: command
executor: metasploit
data: set $_OPTION $_VALUE
output: 'msf5 exploit(windows/smb/ms17_010_eternalblue) > set RHOSTS 10.10.10.10

  RHOSTS => 10.10.10.10'
created_at: '2020-07-08T22:56:24.136959+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Metasploit Set a Context Specific Variable to a Value

```metasploit
set $_OPTION $_VALUE
```

## Expected Output

```
msf5 exploit(windows/smb/ms17_010_eternalblue) > set RHOSTS 10.10.10.10
RHOSTS => 10.10.10.10
```


