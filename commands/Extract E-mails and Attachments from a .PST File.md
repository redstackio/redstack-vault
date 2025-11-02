---
id: 8881efd6-9522-4c6c-8f78-de42894b427a
name: Extract E-mails and Attachments from a .PST File
type: command
executor: bash
data: readpst -tea -m $_FILENAME.pst
output: "root@kali:~# readpst -tea -m backup.pst\nOpening PST file and indexes...\n\
  Processing Folder \"Deleted Items\"\n        \"backup\" - 2 items done, 0 items\
  \ skipped."
created_at: '2019-12-13T22:39:54.282259+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[readpst]]'
---

# Extract E-mails and Attachments from a .PST File

```bash
readpst -tea -m $_FILENAME.pst
```

## Expected Output

```
root@kali:~# readpst -tea -m backup.pst
Opening PST file and indexes...
Processing Folder "Deleted Items"
        "backup" - 2 items done, 0 items skipped.
```


