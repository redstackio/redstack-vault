---
id: 2883aaeb-d8fe-4ea5-99d9-a3539bac3dc9
name: BloodHound.py Enumerate Active Directory
type: command
executor: bash
data: python2 bloodhound.py -c All -u $_USER -p $_PASSWORD -ns $_DCIP -d $_DOMAIN
output: 'root@kali:~# python bloodhound.py -c All -u bob -p s3cr3tpass  -ns 10.10.10.10
  -d megabank.local

  INFO: Found AD domain: megabank.local

  INFO: Connecting to LDAP server: DC01.megabank.local

  INFO: Found 1 domains

  INFO: Found 1 domains in the forest

  INFO: Found 2 computers

  INFO: Connecting to LDAP server: DC01.megabank.local

  WARNING: Could not resolve SID: S-1-5-21-3072663084-364016917-1341370565-1153

  INFO: Found 30 users

  INFO: Found 65 groups

  INFO: Found 1 trusts

  INFO: Starting computer enumeration with 10 workers

  INFO: Querying computer: DC01.megabank.local

  INFO: Querying computer: EXCH01.megabank.local

  INFO: Done in 00M 25S'
created_at: '2020-03-23T21:16:03.287744+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[BloodHound.py]]'
- '[[BloodHound]]'
---

# BloodHound.py Enumerate Active Directory

```bash
python2 bloodhound.py -c All -u $_USER -p $_PASSWORD -ns $_DCIP -d $_DOMAIN
```

## Expected Output

```
root@kali:~# python bloodhound.py -c All -u bob -p s3cr3tpass  -ns 10.10.10.10 -d megabank.local
INFO: Found AD domain: megabank.local
INFO: Connecting to LDAP server: DC01.megabank.local
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 2 computers
INFO: Connecting to LDAP server: DC01.megabank.local
WARNING: Could not resolve SID: S-1-5-21-3072663084-364016917-1341370565-1153
INFO: Found 30 users
INFO: Found 65 groups
INFO: Found 1 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: DC01.megabank.local
INFO: Querying computer: EXCH01.megabank.local
INFO: Done in 00M 25S
```


