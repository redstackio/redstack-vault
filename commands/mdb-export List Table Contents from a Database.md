---
id: 08c2c037-0306-43c5-b39f-471532df252e
name: mdb-export List Table Contents from a Database
type: command
executor: bash
data: mdb-export $_DATABASE.mdb $_TABLE
output: 'root@kali:~# mdb-export database.mdb users

  id,username,password,Status

  5,"admin","hunter2",1,

  7,"bob","securep@ssword",1,

  8,"security","s3cr3tp@ssw0rd",0,'
created_at: '2019-12-13T19:52:08.153254+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# mdb-export List Table Contents from a Database

```bash
mdb-export $_DATABASE.mdb $_TABLE
```

## Expected Output

```
root@kali:~# mdb-export database.mdb users
id,username,password,Status
5,"admin","hunter2",1,
7,"bob","securep@ssword",1,
8,"security","s3cr3tp@ssw0rd",0,
```


