---
id: 93d05db9-4464-4421-9c37-ca88e6265fdd
name: Change Directory to Last Dir
type: command
executor: ''
data: cd -
output: 'root@00b5b1279bcc:/etc# cd -

  /var

  root@00b5b1279bcc:/var# '
created_at: '2020-03-10T03:42:55.681918+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[dir]]'
---

# Change Directory to Last Dir

```bash
cd -
```

## Expected Output

```
root@00b5b1279bcc:/etc# cd -
/var
root@00b5b1279bcc:/var# 
```


