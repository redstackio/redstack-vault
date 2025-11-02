---
id: d4a28389-793a-4c84-b5fb-83ccfcb590b0
name: Sfuzz Command to Fuzz the Web Application
type: command
executor: ''
data: sfuzz -S 192.168.1.5 -p 80 -T -f /usr/share/sfuzz-db/basic.http
output: "[22:09:11] dumping options:\n\tfilename: </usr/share/sfuzz-db/basic.http>\n\
  \tstate:    <8>\n\tlineno:   <56>\n\tliterals:  [74]\n\tsequences: [34]\n\tsymbols:\
  \ [0]\n\treq_del:  <200>\n\tmseq_len: <10024>\n\tplugin: <none>\n\ts_syms: <0>\n\
  \tliteral[1] = [AREALLYBADSTRING]\n\tliteral[2] = [oaiwrlkjgaoiul;234987 103984a;lk-814\
  \ 1]\n\tliteral[3] = [�]\n\tliteral[4] = [�]\n\tliteral[5] = [�]\n\tliteral[6] =\
  \ [%n]\n\tliteral[7] = [%#123456x]\n\tliteral[8] = [%s]\n\tliteral[9] = [%%s]\n\t\
  literal[10] = [%20s]\n\tliteral[11] = [%%20s]\n\tliteral[12] = [%20x]\n\tliteral[13]\
  \ = [%%20x]\n\tliteral[14] = [%n%n%n%n%n]\n\tliteral[15] = [%p%p%p%p%p]\n\tliteral[16]\
  \ = [%x%x%x%x%x]\n\tliteral[17] = [%d%d%d%d%d]\n\tliteral[18] = [%s%s%s%s%s]\n\t\
  literal[19] = [%s%p%x%d]\n\tliteral[20] = [%.1024d]\n\tliteral[21] = [%.1025d]\n\
  \tliteral[22] = [%.2048d]\n\tliteral[23] = [%.2049d]\n\tliteral[24] = [%.4096d]\n\
  \tliteral[25] = [%.4097d]\n\tliteral[26] = [%99999999999s]\n\tliteral[27] = [%08x]\n\
  \tliteral[28] = [%%20d]\n\tliteral[29] = [%%20n]\n\tliteral[30] = [%%20x]\n\tliteral[31]\
  \ = [%%20s]\n\tliteral[32] = [%#0123456x%08x%x%s%p%d%n%o%u%c%h%l%q%j%z%Z%t%i%e%g%f%a%C%S%08x%%]\n\
  \tliteral[33] = [../etc]\n\tliteral[34] = [../../etc]\n\tliteral[35] = [../../../etc]\n\
  \tliteral[36] = [../../../../etc]\n\tliteral[37] = [../../../../../etc]\n\tliteral[38]\
  \ = [../../../../../../etc]\n\tliteral[39] = [../../../../../../../etc]\n\tliteral[40]\
  \ = [./../etc]\n\tliteral[41] = [./../../etc]\n\tliteral[42] = [./../../../etc]\n\
  \tliteral[43] = [./../../../../etc]\n\tliteral[44] = [./../../../../../etc]\n\t\
  literal[45] = [./../../../../../../etc]\n\tliteral[46] = [./../../../../../../../etc]\n\
  \tliteral[47] = [../etc/]\n\tliteral[48] = [../../etc/]\n\tliteral[49] = [../../../etc/]\n\
  \tliteral[50] = [../../../../etc/]\n\tliteral[51] = [../../../../../etc/]\n\tliteral[52]\
  \ = [../../../../../../etc/]\n\tliteral[53] = [../../../../../../../etc/]\n\tliteral[54]\
  \ = [./../etc/]\n\tliteral[55] = [./../../etc/]\n\tliteral[56] = [./../../../etc/]\n\
  \tliteral[57] = [./../../../../etc/]\n\tliteral[58] = [./../../../../../etc/]\n\t\
  literal[59] = [./../../../../../../etc/]\n\tliteral[60] = [./../../../../../../../etc/]\n\
  \tliteral[61] = [../etc/passwd]\n\tliteral[62] = [../../etc/passwd]\n\tliteral[63]\
  \ = [../../../etc/passwd]\n\tliteral[64] = [../../../../etc/passwd]\n\tliteral[65]\
  \ = [../../../../../etc/passwd]\n\tliteral[66] = [../../../../../../etc/passwd]\n\
  \tliteral[67] = [../../../../../../../etc/passwd]\n\tliteral[68] = [./../etc/passwd]\n\
  \tliteral[69] = [./../../etc/passwd]\n\tliteral[70] = [./../../../etc/passwd]\n\t\
  literal[71] = [./../../../../etc/passwd]\n\tliteral[72] = [./../../../../../etc/passwd]\n\
  \tliteral[73] = [./../../../../../../etc/passwd]\n\tliteral[74] = [./../../../../../../../etc/passwd]\n\
  \tsequence[1] = [%n]\n\tsequence[2] = [%f]\n\tsequence[3] = [%%n]\n\tsequence[4]\
  \ = [A]\n\tsequence[5] = [�]\n\tsequence[6] = [�]\n\tsequence[7] = [�]\n\tsequence[8]\
  \ = [%n]\n\tsequence[9] = [%#123456x]\n\tsequence[10] = [%s]\n\tsequence[11] = [%%s]\n\
  \tsequence[12] = [%20s]\n\tsequence[13] = [%%20s]\n\tsequence[14] = [%20x]\n\tsequence[15]\
  \ = [%%20x]\n\tsequence[16] = [%n%n%n%n%n]\n\tsequence[17] = [%p%p%p%p%p]\n\tsequence[18]\
  \ = [%x%x%x%x%x]\n\tsequence[19] = [%d%d%d%d%d]\n\tsequence[20] = [%s%s%s%s%s]\n\
  \tsequence[21] = [%s%p%x%d]\n\tsequence[22] = [%.1024d]\n\tsequence[23] = [%.1025d]\n\
  \tsequence[24] = [%.2048d]\n\tsequence[25] = [%.2049d]\n\tsequence[26] = [%.4096d]\n\
  \tsequence[27] = [%.4097d]\n\tsequence[28] = [%99999999999s]\n\tsequence[29] = [%08x]\n\
  \tsequence[30] = [%%20d]\n\tsequence[31] = [%%20n]\n\tsequence[32] = [%%20x]\n\t\
  sequence[33] = [%%20s]\n\tsequence[34] = [%#0123456x%08x%x%s%p%d%n%o%u%c%h%l%q%j%z%Z%t%i%e%g%f%a%C%S%08x%%]\n\
  [22:09:11] info: beginning fuzz - method: tcp, config from: [/usr/share/sfuzz-db/basic.http],\
  \ out: [192.168.1.5:80]\n[22:09:11] attempting fuzz - 1 (len: 18).\n[22:09:11] info:\
  \ tx fuzz - (18 bytes) - scanning for reply.\n[22:09:11] read:\nHTTP/1.1 302 Found\n\
  Date: Thu, 03 Sep 2020 16:39:11 GMT\nServer: Apache/2.4.41 (Unix) OpenSSL/1.1.1d\
  \ PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3\nX-Powered-By: PHP/7.1.32\nLocation:\
  \ http:///dashboard/\nContent-Length: 131\nConnection: close\nContent-Type: text/html;\
  \ charset=UTF-8\n\n<br />\n<b>Notice</b>:  Undefined index: HTTP_HOST in <b>/Applications/XAMPP/xamppfiles/htdocs/index.php</b>\
  \ on line <b>7</b><br />\n\n===============================================================================\n\
  [22:09:11] attempting fuzz - 2 (len: 34).\n[22:09:11] info: tx fuzz - (34 bytes)\
  \ - scanning for reply.\n[22:09:11] read:\nHTTP/1.1 404 Not Found\nDate: Thu, 03\
  \ Sep 2020 16:39:11 GMT\nServer: Apache/2.4.41 (Unix) OpenSSL/1.1.1d PHP/7.1.32\
  \ mod_perl/2.0.8-dev Perl/v5.16.3\nVary: accept-language,accept-charset\nAccept-Ranges:\
  \ bytes\nConnection: close\nContent-Type: text/html; charset=utf-8\nContent-Language:\
  \ en\nExpires: Thu, 03 Sep 2020 16:39:11 GMT\n\n<?xml version=\"1.0\" encoding=\"\
  UTF-8\"?>\n<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\"\n  \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\"\
  >\n<html xmlns=\"http://www.w3.org/1999/xhtml\" lang=\"en\" xml:lang=\"en\">\n<head>\n\
  <title>Object not found!</title>\n<link rev=\"made\" href=\"mailto:you@example.com\"\
  \ />\n<style type=\"text/css\"><!--/*--><![CDATA[/*><!--*/ \n    body { color: #000000;\
  \ background-color: #FFFFFF; }\n    a:link { color: #0000CC; }\n    p, address {margin-left:\
  \ 3em;}\n    span {font-size: smaller;}\n/*]]>*/--></style>\n</head>\n\n<body>\n\
  <h1>Object not found!</h1>\n<p>\n\n\n    The requested URL was not found on this\
  \ server.\n\n  \n\n    If you entered the URL manually please check your\n    spelling\
  \ and try again.\n\n  \n\n</p>\n<p>\nIf you think this is a server error, please\
  \ contact\nthe <a href=\"mailto:you@example.com\">webmaster</a>.\n\n</p>\n\n<h2>Error\
  \ 404</h2>\n<address>\n  <a href=\"/\">localhost</a><br />\n  <span>Apache/2.4.41\
  \ (Unix) OpenSSL/1.1.1d PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3</span>\n</address>\n\
  </body>\n</html>\n\n\n===============================================================================\n"
created_at: '2020-09-03T17:39:57.862926+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[openssl]]'
- '[[sfuzz]]'
- '[[type]]'
---

# Sfuzz Command to Fuzz the Web Application

```bash
sfuzz -S 192.168.1.5 -p 80 -T -f /usr/share/sfuzz-db/basic.http
```

## Expected Output

```
[22:09:11] dumping options:
	filename: </usr/share/sfuzz-db/basic.http>
	state:    <8>
	lineno:   <56>
	literals:  [74]
	sequences: [34]
	symbols: [0]
	req_del:  <200>
	mseq_len: <10024>
	plugin: <none>
	s_syms: <0>
	literal[1] = [AREALLYBADSTRING]
	literal[2] = [oaiwrlkjgaoiul;234987 103984a;lk-814 1]
	literal[3] = [�]
	literal[4] = [�]
	literal[5] = [�]
	literal[6] = [%n]
	literal[7] = [%#123456x]
	literal[8] = [%s]
	literal[9] = [%%s]
	literal[10] = [%20s]
	literal[11] = [%%20s]
	literal[12] = [%20x]
	literal[13] = [%%20x]
	literal[14] = [%n%n%n%n%n]
	literal[15] = [%p%p%p%p%p]
	literal[16] = [%x%x%x%x%x]
	literal[17] = [%d%d%d%d%d]
	literal[18] = [%s%s%s%s%s]
	literal[19] = [%s%p%x%d]
	literal[20] = [%.1024d]
	literal[21] = [%.1025d]
	literal[22] = [%.2048d]
	literal[23] = [%.2049d]
	literal[24] = [%.4096d]
	literal[25] = [%.4097d]
	literal[26] = [%99999999999s]
	literal[27] = [%08x]
	literal[28] = [%%20d]
	literal[29] = [%%20n]
	literal[30] = [%%20x]
	literal[31] = [%%20s]
	literal[32] = [%#0123456x%08x%x%s%p%d%n%o%u%c%h%l%q%j%z%Z%t%i%e%g%f%a%C%S%08x%%]
	literal[33] = [../etc]
	literal[34] = [../../etc]
	literal[35] = [../../../etc]
	literal[36] = [../../../../etc]
	literal[37] = [../../../../../etc]
	literal[38] = [../../../../../../etc]
	literal[39] = [../../../../../../../etc]
	literal[40] = [./../etc]
	literal[41] = [./../../etc]
	literal[42] = [./../../../etc]
	literal[43] = [./../../../../etc]
	literal[44] = [./../../../../../etc]
	literal[45] = [./../../../../../../etc]
	literal[46] = [./../../../../../../../etc]
	literal[47] = [../etc/]
	literal[48] = [../../etc/]
	literal[49] = [../../../etc/]
	literal[50] = [../../../../etc/]
	literal[51] = [../../../../../etc/]
	literal[52] = [../../../../../../etc/]
	literal[53] = [../../../../../../../etc/]
	literal[54] = [./../etc/]
	literal[55] = [./../../etc/]
	literal[56] = [./../../../etc/]
	literal[57] = [./../../../../etc/]
	literal[58] = [./../../../../../etc/]
	literal[59] = [./../../../../../../etc/]
	literal[60] = [./../../../../../../../etc/]
	literal[61] = [../etc/passwd]
	literal[62] = [../../etc/passwd]
	literal[63] = [../../../etc/passwd]
	literal[64] = [../../../../etc/passwd]
	literal[65] = [../../../../../etc/passwd]
	literal[66] = [../../../../../../etc/passwd]
	literal[67] = [../../../../../../../etc/passwd]
	literal[68] = [./../etc/passwd]
	literal[69] = [./../../etc/passwd]
	literal[70] = [./../../../etc/passwd]
	literal[71] = [./../../../../etc/passwd]
	literal[72] = [./../../../../../etc/passwd]
	literal[73] = [./../../../../../../etc/passwd]
	literal[74] = [./../../../../../../../etc/passwd]
	sequence[1] = [%n]
	sequence[2] = [%f]
	sequence[3] = [%%n]
	sequence[4] = [A]
	sequence[5] = [�]
	sequence[6] = [�]
	sequence[7] = [�]
	sequence[8] = [%n]
	sequence[9] = [%#123456x]
	sequence[10] = [%s]
	sequence[11] = [%%s]
	sequence[12] = [%20s]
	sequence[13] = [%%20s]
	sequence[14] = [%20x]
	sequence[15] = [%%20x]
	sequence[16] = [%n%n%n%n%n]
	sequence[17] = [%p%p%p%p%p]
	sequence[18] = [%x%x%x%x%x]
	sequence[19] = [%d%d%d%d%d]
	sequence[20] = [%s%s%s%s%s]
	sequence[21] = [%s%p%x%d]
	sequence[22] = [%.1024d]
	sequence[23] = [%.1025d]
	sequence[24] = [%.2048d]
	sequence[25] = [%.2049d]
	sequence[26] = [%.4096d]
	sequence[27] = [%.4097d]
	sequence[28] = [%99999999999s]
	sequence[29] = [%08x]
	sequence[30] = [%%20d]
	sequence[31] = [%%20n]
	sequence[32] = [%%20x]
	sequence[33] = [%%20s]
	sequence[34] = [%#0123456x%08x%x%s%p%d%n%o%u%c%h%l%q%j%z%Z%t%i%e%g%f%a%C%S%08x%%]
[22:09:11] info: beginning fuzz - method: tcp, config from: [/usr/share/sfuzz-db/basic.http], out: [192.168.1.5:80]
[22:09:11] attempting fuzz - 1 (len: 18).
[22:09:11] info: tx fuzz - (18 bytes) - scanning for reply.
[22:09:11] read:
HTTP/1.1 302 Found
Date: Thu, 03 Sep 2020 16:39:11 GMT
Server: Apache/2.4.41 (Unix) OpenSSL/1.1.1d PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3
X-Powered-By: PHP/7.1.32
Location: http:///dashboard/
Content-Length: 131
Connection: close
Content-Type: text/html; charset=UTF-8

<br />
<b>Notice</b>:  Undefined index: HTTP_HOST in <b>/Applications/XAMPP/xamppfiles/htdocs/index.php</b> on line <b>7</b><br />

===============================================================================
[22:09:11] attempting fuzz - 2 (len: 34).
[22:09:11] info: tx fuzz - (34 bytes) - scanning for reply.
[22:09:11] read:
HTTP/1.1 404 Not Found
Date: Thu, 03 Sep 2020 16:39:11 GMT
Server: Apache/2.4.41 (Unix) OpenSSL/1.1.1d PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3
Vary: accept-language,accept-charset
Accept-Ranges: bytes
Connection: close
Content-Type: text/html; charset=utf-8
Content-Language: en
Expires: Thu, 03 Sep 2020 16:39:11 GMT

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
<title>Object not found!</title>
<link rev="made" href="mailto:you@example.com" />
<style type="text/css"><!--/*--><![CDATA[/*><!--*/ 
    body { color: #000000; background-color: #FFFFFF; }
    a:link { color: #0000CC; }
    p, address {margin-left: 3em;}
    span {font-size: smaller;}
/*]]>*/--></style>
</head>

<body>
<h1>Object not found!</h1>
<p>


    The requested URL was not found on this server.

  

    If you entered the URL manually please check your
    spelling and try again.

  

</p>
<p>
If you think this is a server error, please contact
the <a href="mailto:you@example.com">webmaster</a>.

</p>

<h2>Error 404</h2>
<address>
  <a href="/">localhost</a><br />
  <span>Apache/2.4.41 (Unix) OpenSSL/1.1.1d PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3</span>
</address>
</body>
</html>


===============================================================================

```


