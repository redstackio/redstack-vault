---
id: 09ace145-e60f-4304-bb66-de1fc4250931
name: hashcat
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:47.111111+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# hashcat



**Command** ([[crack as_rep_response_file (asreproast)]]):

```bash
hashcat -m 18200 -a 0 as_rep_response_file passwords_file

```







**Command** ([[crack as_rep_response_file (kerberoast)]]):

```bash
hashcat -m 13100 --force TGSs_file passwords_file

```






