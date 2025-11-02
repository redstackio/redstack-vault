---
id: b74fd06b-08d3-4c47-8214-32e1f5163ee2
name: tar Archive a Folder with gzip
type: command
executor: ''
data: tar czf $_FILENAME.tar $_FOLDER
output: 'root@kali:~# tar czf archive.tar.gz /etc

  tar: Removing leading `/'' from member names'
created_at: '2020-03-23T20:28:07.883669+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[tar]]'
---

# tar Archive a Folder with gzip

```bash
tar czf $_FILENAME.tar $_FOLDER
```

## Expected Output

```
root@kali:~# tar czf archive.tar.gz /etc
tar: Removing leading `/' from member names
```


