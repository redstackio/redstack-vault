---
id: 36a70a45-f5be-4cd4-a678-df11121b7824
name: fuff GET Parameter Fuzzing
type: command
executor: bash
data: 'ffuf -w /path/to/paramnames.txt -u https://target/script.php?FUZZ=test_value
  -fs 4242

  '
output: null
created_at: '2020-07-24T17:11:28.829249+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# fuff GET Parameter Fuzzing

```bash
ffuf -w /path/to/paramnames.txt -u https://target/script.php?FUZZ=test_value -fs 4242

```
