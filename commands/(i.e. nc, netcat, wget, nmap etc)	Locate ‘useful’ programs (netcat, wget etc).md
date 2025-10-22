---
id: e3ec58ac-7078-43aa-8675-2a5c4fa0cb1e
name: "(i.e. nc, netcat, wget, nmap etc)\tLocate ‘useful’ programs (netcat, wget etc)"
type: command
executor: bash
data: 'find / -name %program_name% 2>/dev/null

  '
output: null
created_at: '2020-07-14T18:14:29.247570+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# (i.e. nc, netcat, wget, nmap etc)	Locate ‘useful’ programs (netcat, wget etc)

```bash
find / -name %program_name% 2>/dev/null

```
