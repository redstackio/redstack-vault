---
id: 28320ad2-aebb-4b3f-940d-81e049616fc6
name: dirsearch brute force directories and files from sub-domain list with custom
  paths wordlists
type: command
executor: bash
data: 'python3 dirsearch.py -L sub-domaints.txt -e .* -w RobotsDisallowed-Top1000.txt
  --simple-report=output.txt -t 50

  '
output: null
created_at: '2020-07-24T17:11:34.304398+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# dirsearch brute force directories and files from sub-domain list with custom paths wordlists

```bash
python3 dirsearch.py -L sub-domaints.txt -e .* -w RobotsDisallowed-Top1000.txt --simple-report=output.txt -t 50

```
