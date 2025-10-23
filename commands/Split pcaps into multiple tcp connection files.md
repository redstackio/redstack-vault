---
id: 04e68fc3-b68b-44e1-8652-8b167b894f5b
name: Split pcaps into multiple tcp connection files
type: command
executor: bash
data: 'tcpflow -a -o tcpflow -r pcapvil1.pcap

  '
output: null
created_at: '2020-07-14T18:14:28.746525+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Split pcaps into multiple tcp connection files

```bash
tcpflow -a -o tcpflow -r pcapvil1.pcap

```


