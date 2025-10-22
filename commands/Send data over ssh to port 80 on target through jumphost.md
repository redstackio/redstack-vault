---
id: aa99545e-a0ed-4d74-8a4b-3f3bfdc61683
name: Send data over ssh to port 80 on target through jumphost
type: command
executor: bash
data: 'ssh -A -t -p22 -L 8800:localhost:8800 james@123.001.123.321 -t ssh -L 8800:localhost:80
  james@124.123.122

  '
output: null
created_at: '2020-07-14T18:21:22.431935+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Send data over ssh to port 80 on target through jumphost

```bash
ssh -A -t -p22 -L 8800:localhost:8800 james@123.001.123.321 -t ssh -L 8800:localhost:80 james@124.123.122

```
