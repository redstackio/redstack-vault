---
id: c02a1543-81da-4bca-b28a-322271e167e3
name: Find Files by Name and Execute a Command
type: command
executor: bash
data: find $_PATH -name $_STRING -exec $_COMMAND {} \;
output: "bob@a7ffb5e7e757:/$ find / -name '*conf*' -exec grep passwd {} \\; 2>/dev/null\n\
  # Please note that system software, such as the users allocated by the base-passwd\n\
  passwd:         files                  \nBinary file /sbin/ldconfig matches\n  \
  \  chown root:root /etc/passwd /etc/group\n    chmod 644 /etc/passwd /etc/group\
  \ \n    # sometimes the passwd perms get munged\n..."
created_at: '2020-03-10T06:28:38.723796+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Find Files by Name and Execute a Command

```bash
find $_PATH -name $_STRING -exec $_COMMAND {} \;
```

## Expected Output

```
bob@a7ffb5e7e757:/$ find / -name '*conf*' -exec grep passwd {} \; 2>/dev/null
# Please note that system software, such as the users allocated by the base-passwd
passwd:         files                  
Binary file /sbin/ldconfig matches
    chown root:root /etc/passwd /etc/group
    chmod 644 /etc/passwd /etc/group 
    # sometimes the passwd perms get munged
...
```
