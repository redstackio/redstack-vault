---
id: e02f668a-e8ce-423a-8bcf-4cb05d0f7ebd
name: attacker
type: command
executor: bash
data: '` socat file:`tty`,raw,echo=0 tcp-listen:12345 `

  '
output: null
created_at: '2020-07-14T18:14:36.929122+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# attacker

```bash
` socat file:`tty`,raw,echo=0 tcp-listen:12345 `

```


