---
id: 5409414a-d84c-40b4-bc1d-ea68fb61edc3
name: 7z Decompress a Password Protected Zip Archive
type: command
executor: bash
data: 7z x $_FILENAME.zip
output: 'root@kali:~# 7z backup.zip


  7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21

  p7zip Version 16.02 (locale=en_US.utf8,Utf16=on,HugeFiles=on,64 bits,3 CPUs Intel(R)
  Core(TM) i5-8250U CPU @ 1.60GHz (806EA),ASM,AES-NI)


  Scanning the drive for archives:

  1 file, 10320 bytes (11 KiB)


  Extracting archive: backup.zip

  --

  Path = backup.zip

  Type = zip

  Physical Size = 10320



  Enter password (will not be echoed):

  Everything is Ok


  Size:       294320

  Compressed: 10320'
created_at: '2019-12-13T22:09:49.766527+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[type]]'
---

# 7z Decompress a Password Protected Zip Archive

```bash
7z x $_FILENAME.zip
```

## Expected Output

```
root@kali:~# 7z backup.zip

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.utf8,Utf16=on,HugeFiles=on,64 bits,3 CPUs Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 10320 bytes (11 KiB)

Extracting archive: backup.zip
--
Path = backup.zip
Type = zip
Physical Size = 10320


Enter password (will not be echoed):
Everything is Ok

Size:       294320
Compressed: 10320
```


