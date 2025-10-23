---
id: a636a24f-5589-4a54-ae3d-7c445c0e313d
name: Delete a Folder and All Contents
type: command
executor: bash
data: rm -rf $_FOLDER
output: 'root@00b5b1279bcc:~# rm -rf /bin

  root@00b5b1279bcc:~# ls

  bash: /bin/ls: No such file or directory'
created_at: '2020-03-10T03:42:55.680504+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Delete a Folder and All Contents

```bash
rm -rf $_FOLDER
```

## Expected Output

```
root@00b5b1279bcc:~# rm -rf /bin
root@00b5b1279bcc:~# ls
bash: /bin/ls: No such file or directory
```


