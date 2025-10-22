---
id: 449508fc-57e5-4c88-b76b-7a69d5c86b5b
name: Comparison of strings and hexadecimals
type: command
executor: bash
data: 'var_dump(''0010e2'' == ''1e3'');           # true

  var_dump(''0xABCdef'' == '' 0xABCdef'');     # true PHP 5.0 / false PHP 7.0

  var_dump(''0xABCdef'' == ''     0xABCdef''); # true PHP 5.0 / false PHP 7.0

  var_dump(''0x01'' == 1)                # true PHP 5.0 / false PHP 7.0

  var_dump(''0x1234Ab'' == ''1193131'');'
output: null
created_at: '2023-04-06T03:56:40.612827+00:00'
updated_at: '2023-04-06T03:56:40.632426+00:00'
---

# Comparison of strings and hexadecimals

```bash
var_dump('0010e2' == '1e3');           # true
var_dump('0xABCdef' == ' 0xABCdef');     # true PHP 5.0 / false PHP 7.0
var_dump('0xABCdef' == '     0xABCdef'); # true PHP 5.0 / false PHP 7.0
var_dump('0x01' == 1)                # true PHP 5.0 / false PHP 7.0
var_dump('0x1234Ab' == '1193131');
```
