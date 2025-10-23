---
id: db3b0a2b-1d92-43f5-a304-8543f488e744
name: Change Ownership of a Folder Recursively
type: command
executor: bash
data: chown  -R $_USER:$_GROUP $_PATH
output: root@a7ffb5e7e757:/tmp# chown -R root:bob /tmp/test
created_at: '2020-03-10T09:00:42.694759+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Change Ownership of a Folder Recursively

```bash
chown  -R $_USER:$_GROUP $_PATH
```

## Expected Output

```
root@a7ffb5e7e757:/tmp# chown -R root:bob /tmp/test
```


