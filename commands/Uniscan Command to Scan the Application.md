---
id: 3b01c009-8fd5-4d63-be1a-5a4bc1c03c68
name: Uniscan Command to Scan the Application
type: command
executor: ''
data: uniscan -u http://192.168.1.11/vcart/login.php -qweds
output: "####################################\n# Uniscan project                 \
  \ #\n# http://uniscan.sourceforge.net/  #\n####################################\n\
  V. 6.3\n\n\nScan date: 31-8-2020 23:49:4\n===================================================================================================\n\
  | Domain: http://192.168.1.11/vcart/login.php/\n| Server: Apache/2.4.41 (Unix) OpenSSL/1.1.1d\
  \ PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3\n| IP: 192.168.1.11\n===================================================================================================\n\
  |\n| Directory check:\n| Skipped because http://192.168.1.11/vcart/login.php/uniscan408/\
  \ did not return the code 404\n===================================================================================================\n\
  |                                                                              \
  \                     \n| File check:\n| Skipped because http://192.168.1.11/vcart/login.php/uniscan649/\
  \ did not return the code 404\n===================================================================================================\n\
  |\n| Check robots.txt:\n|\n| Check sitemap.xml:\n===================================================================================================\n\
  |\n| Crawler Started:\n| Plugin name: External Host Detect v.1.2 Loaded.\n| Plugin\
  \ name: Code Disclosure v.1.1 Loaded.\n| Plugin name: Timthumb <= 1.32 vulnerability\
  \ v.1 Loaded.\n| Plugin name: Upload Form Detect v.1.1 Loaded.\n| Plugin name: FCKeditor\
  \ upload test v.1 Loaded.\n| Plugin name: E-mail Detection v.1.1 Loaded.\n| Plugin\
  \ name: Web Backdoor Disclosure v.1.1 Loaded.\n| Plugin name: phpinfo() Disclosure\
  \ v.1 Loaded.\n| [+] Crawling finished, 81 URL's found!\n|\n| External hosts:\n\
  | [+] External Host Found: http://www.sqlite.org\n| [+] External Host Found: https://bitnami.com\n\
  | [+] External Host Found: http://bitnami.com\n| [+] External Host Found: https://translate.apachefriends.org\n\
  | [+] External Host Found: http://www.phpmyadmin.net\n| [+] External Host Found:\
  \ https://support.google.com\n| [+] External Host Found: https://www.facebook.com\n\
  | [+] External Host Found: http://www.proftpd.org\n| [+] External Host Found: http://httpd.apache.org\n\
  | [+] External Host Found: https://community.apachefriends.org\n| [+] External Host\
  \ Found: https://twitter.com\n| [+] External Host Found: https://plus.google.com\n\
  | [+] External Host Found: https://www.apachefriends.org\n| [+] External Host Found:\
  \ http://xdebug.org\n| [+] External Host Found: https://make.wordpress.org\n| [+]\
  \ External Host Found: http://git-scm.com\n| [+] External Host Found: https://getcomposer.org\n\
  | [+] External Host Found: http://www.slimframework.com\n| [+] External Host Found:\
  \ http://sqlite.org\n| [+] External Host Found: http://www.fastly.com\n| [+] External\
  \ Host Found: http://framework.zend.com\n|\n| Source Code Disclosure:\n|\n| Timthumb:\n\
  |\n| File Upload Forms:\n|\n| FCKeditor File Upload:\n|\n| E-mails:\n| [+] E-mail\
  \ Found: recipients@email-address.com\n| [+] E-mail Found: humbedooh@apache.org\n\
  | [+] E-mail Found: mike@hyperreal.org\n| [+] E-mail Found: you@example.com\n| [+]\
  \ E-mail Found: fastly-logo@2x.png\n| [+] E-mail Found: xampp-cloud@2x.png\n| [+]\
  \ E-mail Found: sourceforge-logo@2x.png\n| [+] E-mail Found: social-icons@2x.png\n\
  | [+] E-mail Found: recipients@example.com\n| [+] E-mail Found: social-icons-large@2x.png\n\
  | [+] E-mail Found: kevinh@kevcom.com\n| [+] E-mail Found: stack-icons@2x.png\n\
  | [+] E-mail Found: license@php.net\n| [+] E-mail Found: your@email-address.com\n\
  | [+] E-mail Found: your-gmail-username@gmail.com\n|\n| Web Backdoors:\n|\n| PHPinfo()\
  \ Disclosure:\n| [+] phpinfo() page: http://192.168.1.11/dashboard/phpinfo.php\n\
  | \tSystem: Darwin busybox-2.local 19.6.0 Darwin Kernel Version 19.6.0: Thu Jun\
  \ 18 20:49:00 PDT 2020; root:xnu-6153.141.1~1/RELEASE_X86_64 x86_64 \n| \tPHP version:\
  \ 7.1.32 \n| \tApache Version: Apache/2.4.41 (Unix) OpenSSL/1.1.1d PHP/7.1.32 mod_perl/2.0.8-dev\
  \ Perl/v5.16.3 \n| \tServer Administrator: you@example.com \n| \tUser/Group: daemon(1)/1\
  \ \n| \tServer Root: /Applications/XAMPP/xamppfiles \n| \tDOCUMENT_ROOT: /Applications/XAMPP/xamppfiles/htdocs\
  \ \n| \tSCRIPT_FILENAME: /Applications/XAMPP/xamppfiles/htdocs/dashboard/phpinfo.php\
  \ \n| \tallow_url_fopen: On\n| \tallow_url_include: On\n| \tdisable_functions: <i>no\
  \ value</i>\n| \tOpenSSL Library Version: OpenSSL 1.1.1d  10 Sep 2019 "
created_at: '2020-08-31T18:28:13.588477+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Uniscan Command to Scan the Application

```bash
uniscan -u http://192.168.1.11/vcart/login.php -qweds
```

## Expected Output

```
####################################
# Uniscan project                  #
# http://uniscan.sourceforge.net/  #
####################################
V. 6.3

Scan date: 31-8-2020 23:49:4
===================================================================================================
| Domain: http://192.168.1.11/vcart/login.php/
| Server: Apache/2.4.41 (Unix) OpenSSL/1.1.1d PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3
| IP: 192.168.1.11
===================================================================================================
|
| Directory check:
| Skipped because http://192.168.1.11/vcart/login.php/uniscan408/ did not return the code 404
===================================================================================================
|                                                                                                   
| File check:
| Skipped because http://192.168.1.11/vcart/login.php/uniscan649/ did not return the code 404
===================================================================================================
|
| Check robots.txt:
|
| Check sitemap.xml:
===================================================================================================
|
| Crawler Started:
| Plugin name: External Host Detect v.1.2 Loaded.
| Plugin name: Code Disclosure v.1.1 Loaded.
| Plugin name: Timthumb <= 1.32 vulnerability v.1 Loaded.
| Plugin name: Upload Form Detect v.1.1 Loaded.
| Plugin name: FCKeditor upload test v.1 Loaded.
| Plugin name: E-mail Detection v.1.1 Loaded.
| Plugin name: Web Backdoor Disclosure v.1.1 Loaded.
| Plugin name: phpinfo() Disclosure v.1 Loaded.
| [+] Crawling finished, 81 URL's found!
|
| External hosts:
| [+] External Host Found: http://www.sqlite.org
| [+] External Host Found: https://bitnami.com
| [+] External Host Found: http://bitnami.com
| [+] External Host Found: https://translate.apachefriends.org
| [+] External Host Found: http://www.phpmyadmin.net
| [+] External Host Found: https://support.google.com
| [+] External Host Found: https://www.facebook.com
| [+] External Host Found: http://www.proftpd.org
| [+] External Host Found: http://httpd.apache.org
| [+] External Host Found: https://community.apachefriends.org
| [+] External Host Found: https://twitter.com
| [+] External Host Found: https://plus.google.com
| [+] External Host Found: https://www.apachefriends.org
| [+] External Host Found: http://xdebug.org
| [+] External Host Found: https://make.wordpress.org
| [+] External Host Found: http://git-scm.com
| [+] External Host Found: https://getcomposer.org
| [+] External Host Found: http://www.slimframework.com
| [+] External Host Found: http://sqlite.org
| [+] External Host Found: http://www.fastly.com
| [+] External Host Found: http://framework.zend.com
|
| Source Code Disclosure:
|
| Timthumb:
|
| File Upload Forms:
|
| FCKeditor File Upload:
|
| E-mails:
| [+] E-mail Found: recipients@email-address.com
| [+] E-mail Found: humbedooh@apache.org
| [+] E-mail Found: mike@hyperreal.org
| [+] E-mail Found: you@example.com
| [+] E-mail Found: fastly-logo@2x.png
| [+] E-mail Found: xampp-cloud@2x.png
| [+] E-mail Found: sourceforge-logo@2x.png
| [+] E-mail Found: social-icons@2x.png
| [+] E-mail Found: recipients@example.com
| [+] E-mail Found: social-icons-large@2x.png
| [+] E-mail Found: kevinh@kevcom.com
| [+] E-mail Found: stack-icons@2x.png
| [+] E-mail Found: license@php.net
| [+] E-mail Found: your@email-address.com
| [+] E-mail Found: your-gmail-username@gmail.com
|
| Web Backdoors:
|
| PHPinfo() Disclosure:
| [+] phpinfo() page: http://192.168.1.11/dashboard/phpinfo.php
| 	System: Darwin busybox-2.local 19.6.0 Darwin Kernel Version 19.6.0: Thu Jun 18 20:49:00 PDT 2020; root:xnu-6153.141.1~1/RELEASE_X86_64 x86_64 
| 	PHP version: 7.1.32 
| 	Apache Version: Apache/2.4.41 (Unix) OpenSSL/1.1.1d PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3 
| 	Server Administrator: you@example.com 
| 	User/Group: daemon(1)/1 
| 	Server Root: /Applications/XAMPP/xamppfiles 
| 	DOCUMENT_ROOT: /Applications/XAMPP/xamppfiles/htdocs 
| 	SCRIPT_FILENAME: /Applications/XAMPP/xamppfiles/htdocs/dashboard/phpinfo.php 
| 	allow_url_fopen: On
| 	allow_url_include: On
| 	disable_functions: <i>no value</i>
| 	OpenSSL Library Version: OpenSSL 1.1.1d  10 Sep 2019 
```
