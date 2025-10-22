---
id: adbb39aa-713b-4799-a984-a8fb0b996cd0
name: MSSQL Scan
type: command
executor: bash
data: 'nmap -vv-sV -Pn-n -p1433 --script=ms-sql-info,ms-sql-config,ms-sql-dump-hashes
  --script-args=mssql.instance-port=1433,smsql.username-sa,mssql.password-sa -oA

  '
output: null
created_at: '2020-07-14T18:21:14.335921+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# MSSQL Scan

```bash
nmap -vv-sV -Pn-n -p1433 --script=ms-sql-info,ms-sql-config,ms-sql-dump-hashes --script-args=mssql.instance-port=1433,smsql.username-sa,mssql.password-sa -oA

```
