---
id: 0f3f0420-9ced-490e-a0c8-5f87df95ff91
name: POST Data Fuzzing
type: command
executor: bash
data: 'ffuf -w /path/to/postdata.txt -X POST -d "username=admin\&password=FUZZ" -u
  https://target/login.php -fc 401

  '
output: null
created_at: '2020-07-24T17:11:28.829436+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# POST Data Fuzzing

```bash
ffuf -w /path/to/postdata.txt -X POST -d "username=admin\&password=FUZZ" -u https://target/login.php -fc 401

```
