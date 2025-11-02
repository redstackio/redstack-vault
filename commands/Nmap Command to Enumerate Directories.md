---
id: e5789d21-768f-469b-b946-73d9a8cf52e4
name: Nmap Command to Enumerate Directories
type: command
executor: ''
data: nmap -p80 --script http-enum 192.168.1.3
output: "PORT   STATE SERVICE\n80/tcp open  http\n| http-enum: \n|   /icons/: Potentially\
  \ interesting folder w/ directory listing\n|   /img/: Potentially interesting folder\
  \ w/ directory listing\n|_  /webalizer/: Potentially interesting folder w/ directory\
  \ listing"
created_at: '2020-09-01T17:09:05.183875+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Nmap]]'
---

# Nmap Command to Enumerate Directories

```bash
nmap -p80 --script http-enum 192.168.1.3
```

## Expected Output

```
PORT   STATE SERVICE
80/tcp open  http
| http-enum: 
|   /icons/: Potentially interesting folder w/ directory listing
|   /img/: Potentially interesting folder w/ directory listing
|_  /webalizer/: Potentially interesting folder w/ directory listing
```


