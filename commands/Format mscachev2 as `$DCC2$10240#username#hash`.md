---
id: dad44281-1a7e-4685-a859-f89771bb226b
name: Format mscachev2 as `$DCC2$10240#username#hash`
type: command
executor: bash
data: 'cat ''mscachecreds.txt'' | awk -F “:” {''print "$DCC2$10240#"$1"#"$2''}

  '
output: null
created_at: '2020-07-14T18:21:34.529250+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Format mscachev2 as `$DCC2$10240#username#hash`

```bash
cat 'mscachecreds.txt' | awk -F “:” {'print "$DCC2$10240#"$1"#"$2'}

```
