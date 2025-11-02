---
id: a73eff97-20c1-4793-8f83-78b388305d4e
name: openssl View Available Hash Options
type: command
executor: bash
data: openssl passwd --help
output: "root@hackers:~# openssl passwd --help\nUsage: passwd [options]\nValid options\
  \ are:\n -help               Display this summary\n -in infile          Read passwords\
  \ from file\n -noverify           Never verify when reading password from terminal\n\
  \ -quiet              No warnings\n -table              Format output as table\n\
  \ -reverse            Switch table columns\n -salt val           Use provided salt\n\
  \ -stdin              Read passwords from stdin\n -6                  SHA512-based\
  \ password algorithm\n -5                  SHA256-based password algorithm\n -apr1\
  \               MD5-based password algorithm, Apache variant\n -1              \
  \    MD5-based password algorithm\n -aixmd5             AIX MD5-based password algorithm\n\
  \ -crypt              Standard Unix password algorithm (default)\n -rand val   \
  \        Load the file(s) into the random number generator\n -writerand outfile\
  \  Write random data to the specified file\n"
created_at: '2019-09-16T18:26:12.743702+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[openssl]]'
---

# openssl View Available Hash Options

```bash
openssl passwd --help
```

## Expected Output

```
root@hackers:~# openssl passwd --help
Usage: passwd [options]
Valid options are:
 -help               Display this summary
 -in infile          Read passwords from file
 -noverify           Never verify when reading password from terminal
 -quiet              No warnings
 -table              Format output as table
 -reverse            Switch table columns
 -salt val           Use provided salt
 -stdin              Read passwords from stdin
 -6                  SHA512-based password algorithm
 -5                  SHA256-based password algorithm
 -apr1               MD5-based password algorithm, Apache variant
 -1                  MD5-based password algorithm
 -aixmd5             AIX MD5-based password algorithm
 -crypt              Standard Unix password algorithm (default)
 -rand val           Load the file(s) into the random number generator
 -writerand outfile  Write random data to the specified file

```


