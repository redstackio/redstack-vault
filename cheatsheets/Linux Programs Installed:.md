---
id: cfcf7bc3-e473-4355-9ca6-593264459b3f
name: 'Linux Programs Installed:'
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:29.643042+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Linux Programs Installed:

**Command** ([[Installed packages (Debian)]]):

```bash
dpkg -l

```

**Command** ([[Installed packages (Red Hat)]]):

```bash
rpm -qa

```

**Command** ([[Sudo version – does an exploit exist?]]):

```bash
sudo -V

```

**Command** ([[Apache version]]):

```bash
httpd -v
apache2 -v

```

**Command** ([[List loaded Apache modules]]):

```bash
apache2ctl (or apachectl) -M

```

**Command** ([[Installed MYSQL version details]]):

```bash
mysql --version

```

**Command** ([[Installed Postgres version details]]):

```bash
psql -V

```

**Command** ([[Installed Perl version details]]):

```bash
perl -v

```

**Command** ([[Installed Java version details]]):

```bash
java -version

```

**Command** ([[Installed Python version details]]):

```bash
python --version

```

**Command** ([[Installed Ruby version details]]):

```bash
ruby -v

```

**Command** ([[(i.e. nc, netcat, wget, nmap etc)	Locate ‘useful’ programs (netcat, wget etc)]]):

```bash
find / -name %program_name% 2>/dev/null

```

**Command** ([[(i.e. nc, netcat, wget, nmap etc)	As above]]):

```bash
which %program_name%

```

**Command** ([[List available compilers]]):

```bash
dpkg --list 2>/dev/null| grep compiler |grep -v decompiler 2>/dev/null && yum list installed 'gcc*' 2>/dev/null| grep gcc 2>/dev/null

```

**Command** ([[Which account is Apache running as]]):

```bash
cat /etc/apache2/envvars 2>/dev/null |grep -i 'user\|group' |awk '{sub(/.*\export /,"")}1'

```
