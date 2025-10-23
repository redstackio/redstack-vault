---
id: 630dd53a-9ece-4faf-8b50-ea52e12aadef
name: List directory and read file
type: command
executor: bash
data: 'select pg_ls_dir(''./'');

  select pg_read_file(''PG_VERSION'', 0, 200);'
output: null
created_at: '2023-04-06T03:56:35.929162+00:00'
updated_at: '2023-04-10T20:23:15.905451+00:00'
---

# List directory and read file

```bash
select pg_ls_dir('./');
select pg_read_file('PG_VERSION', 0, 200);
```


