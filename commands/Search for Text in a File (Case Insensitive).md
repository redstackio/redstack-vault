---
id: 68ebe21f-ab9f-4784-852b-5bf28544df0e
name: Search for Text in a File (Case Insensitive)
type: command
executor: bash
data: grep -i $_STRING $_FILE
output: "bob@a7ffb5e7e757:/$ grep 'bash' /etc/passwd  \nroot:x:0:0:root:/root:/bin/bash\n\
  bob:x:1000:1000:,,,:/home/bob:/bin/bash"
created_at: '2020-03-10T06:28:38.722921+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Search for Text in a File (Case Insensitive)

```bash
grep -i $_STRING $_FILE
```

## Expected Output

```
bob@a7ffb5e7e757:/$ grep 'bash' /etc/passwd  
root:x:0:0:root:/root:/bin/bash
bob:x:1000:1000:,,,:/home/bob:/bin/bash
```


