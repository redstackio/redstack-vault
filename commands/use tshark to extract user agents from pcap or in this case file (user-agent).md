---
id: bef969eb-7a9f-402c-a4d3-92bcb75ddf42
name: use tshark to extract user agents from pcap or in this case file (user-agent)
type: command
executor: bash
data: 'tshark -r tcpdump-port-80.pcap -R http -T fields -e http.user_agent -2

  '
output: null
created_at: '2020-07-14T18:14:45.647134+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# use tshark to extract user agents from pcap or in this case file (user-agent)

```bash
tshark -r tcpdump-port-80.pcap -R http -T fields -e http.user_agent -2

```
