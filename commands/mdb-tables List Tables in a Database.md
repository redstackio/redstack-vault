---
id: a8c2add8-7acf-4462-9e6e-400ac6abe291
name: mdb-tables List Tables in a Database
type: command
executor: bash
data: mdb-tables -1 $_DATABASE.mdb
output: "root@kali:~# mdb-tables -1 database.mdb                                 \
  \ \nacc_antiback\naccounting\naccounts\nhelpdesk\nmarketing\nusers\nservers"
created_at: '2019-12-13T19:52:08.153041+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# mdb-tables List Tables in a Database

```bash
mdb-tables -1 $_DATABASE.mdb
```

## Expected Output

```
root@kali:~# mdb-tables -1 database.mdb                                  
acc_antiback
accounting
accounts
helpdesk
marketing
users
servers
```


