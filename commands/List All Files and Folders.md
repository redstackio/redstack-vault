---
id: a4c10855-05fc-4469-b5f6-3f27d950de76
name: List All Files and Folders
type: command
executor: bash
data: ls -alh $_PATH
output: 'root@00b5b1279bcc:~# ls -alh

  total 8.0K

  drwx------ 2 root root  37 Jan 30 00:00 .

  drwxr-xr-x 1 root root   6 Mar 10 01:45 ..

  -rw-r--r-- 1 root root 570 Jan 31  2010 .bashrc

  -rw-r--r-- 1 root root 148 Aug 17  2015 .profile'
created_at: '2020-03-10T03:42:55.676657+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# List All Files and Folders

```bash
ls -alh $_PATH
```

## Expected Output

```
root@00b5b1279bcc:~# ls -alh
total 8.0K
drwx------ 2 root root  37 Jan 30 00:00 .
drwxr-xr-x 1 root root   6 Mar 10 01:45 ..
-rw-r--r-- 1 root root 570 Jan 31  2010 .bashrc
-rw-r--r-- 1 root root 148 Aug 17  2015 .profile
```


