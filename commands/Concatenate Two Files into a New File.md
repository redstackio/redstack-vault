---
id: a947f0b9-2a36-4d40-9f36-8ec664805c83
name: Concatenate Two Files into a New File
type: command
executor: bash
data: cat $_FILE1 $_FILE2 > $_OUTPUT
output: root@00b5b1279bcc:~# cat /etc/hosts /etc/resolv.conf  > newfile.txt
created_at: '2020-03-10T03:42:55.678361+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Concatenate Two Files into a New File

```bash
cat $_FILE1 $_FILE2 > $_OUTPUT
```

## Expected Output

```
root@00b5b1279bcc:~# cat /etc/hosts /etc/resolv.conf  > newfile.txt
```
