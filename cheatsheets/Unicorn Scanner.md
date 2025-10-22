---
id: a00e2e26-0555-48cb-8105-41f457354bfd
name: Unicorn Scanner
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:30.855367+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Unicorn Scanner

**Command** ([[Services and OS]]):

```bash
unicornscan –Iv $ip

```

**Command** ([[TCP SYN IP RANGE]]):

```bash
unicornscan -msf -v -I $iprange/cidr

```

**Command** ([[UDP Scan (Faster then namp)]]):

```bash
unicornscan -mU -Iv $ip

```

**Command** ([[The Entire TCP Scan]]):

```bash
unicornscan -H -msf -Iv $ip -p 1-65535

```

**Command** ([[The Entire UDP Scan]]):

```bash
unicornscan -H -mU -Iv $ip -p 1-65535

```

**Command** ([[FIN Scan]]):

```bash
unicornscan -mTsF -v -E $ip

```
