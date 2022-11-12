Natas Wargame - OverTheWire
===========================

Level 0
-------
* http://natas0.natas.labs.overthewire.org
  * Username:password: `natas0`:`natas0`.
  * The next password is in the HTML as a comment.
    * View page source.
> gtVrDuiDfck831PqWsLEZy5gyDz1clto

Level 0 -> 1
------------
* The same as before, but view page source by `Ctrl+U`.
  * Or use `curl`, `wget`.
> ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi

Level 1 -> 2
------------
* View source. There's actually a PNG file.
* That file is not remarkable. It is in the `files/` directory.
* There's a `users.txt` in `files/`.
  * It contains `natas3`'s password, as well as some others... useful?
> sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14

Level 2 -> 3
------------
* View source. There's a clue for Googling.
* Google: `site:natas3.natas.labs.overthewire.org`
* Will show: http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt
> Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ

Level 3 -> 4
------------
* Use the browser's Networking developer tool. Persist logs.
* The GET to index.php contains a Referer header.
  * Edit and resend to make the referer the natas5 URL.
  * The server's raw response will contain the password.
> iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq

Level 4 -> 5
------------
* Check the Networking tool for the GET to index.php.
* The server response specified `Set-Cookie: loggedin=0`.
  * Edit and resend to make the cookie 1.
> aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1

Level 5 -> 6
------------
* The input could be vulnerable.
* The View sourcecode button shows the PHP source.
  * Includes `secret.inc` where `$secret` is likely defined.
  * We can directly view the `/includes/secret.inc` URL.
> 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9

Level 6 -> 7
------------
* The source contains a clue comment: hints `/etc/natas_webpass/natas8`.
* Clicking the links uses the `?page=<page>` parameter.
  * The `?page=/etc/natas_webpass/natas8` payload will print cat the file.
> DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe

Level 7 -> 8
------------
* Similar to level 6, but the secret is shown and obfuscated.
  * Do the following in reverse order
  * `base64_encode` is obvious:
    * https://www.base64decode.org/
  * `strrev` reverses the string:
    * https://codebeautify.org/reverse-string
  * `bin2hex` converts to hex:
    * https://onlinehextools.com/convert-hex-to-string
> W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl

Level 8 -> 9
------------
* Using the website prints out files that were grepped from dictionary.txt.
  * The request variables are in `$_REQUEST`.
* There is no defense against any sort of malicious input.
  * The input is executed via `passthru`.
  * `?submit=Search&needle=;ls -a;`
  * Other payloads:
    * `;cat .htpasswd;`
    * `;cat /etc/natas_webpass/natas10;`
> nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu

Level 9 -> 10
-------------
* Same as before, but `;`, `|` and `&` are filtered.
* We can still exploit it:
  * `$(ls)` will grep for the current directory's contents
  * `'' /etc/natas_webpass/natas11 #`
    * The first param to grep is the pattern, second (and following) are files.
    * We can pass `''` to always match each line.
    * Works without the comment too.
> U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK

Level 10 -> 11
--------------
* Let's try `#432423`! Background changes.
* `$_COOKIE` contains a `data` item.
* Originally `{"showpassword":"no", "bgcolor":"#ffffff"}` is XOR-encrypted.
  * The `$defaultdata` is json-encoded, then XOR-encrypted.
    * Load data just parses the cookie if present.
  * Then it is base64-encoded.
* To decode: Run the `natas11.py` script.
* The new base64 encoded data should be assigned to the `data` cookie.
  * Using the Storage tab in the browser developer tools.
> EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3

Level 11 -> 12
--------------
* The way files are uploaded could provide a way to get `/etc/natas_webpass/natas13`.
* The most likely candidate would be a `pathinfo` PHP bypass.
  * https://www.madirish.net/202
  * Appending zero bytes (URL encoded %00) to filenames works!
* I could upload a PHP file with this extension trick!
  * Well, not really... the random filename in the request will overwrite it!
  * Except, that the filename form value is not checked!
  * We CAN upload PHP files!
* Running the `natas12.py` script and visiting the uploaded PHP file works.
> jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY

Level 12 -> 13
--------------
* The `exif_imagetype` can be bypassed using a fake file signature
  * `\xFF\xD8\xFF\xE0`
> Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1

Level 13 -> 14
--------------
* Looks like a simple SQL injection.
* Payload: `" OR 1=1 #` for the username.
> AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J

Level 14 -> 15
--------------
* SQL injection also works here.
* Error messages are hidden by default: `" OR 1=x #`
  * debug in `$_GET` may be enough?
  * Modify the action of the form to include `?debug=s`.
* Boolean SQL injection can work... but that would take a long time.
* I looked up a solution and it is in fact a blind SQL brute force attack!
  * https://mcpa.github.io/natas/wargame/web/overthewire/2015/09/29/natas15/
* Get the request from the form and the Networking tab.
> WaIHEacj63wnNIBROHeqi3p9t0m5nhmh

Level 15 -> 16
--------------
* This is a command injection vulnerability.
* `passthru`: Execute an external program and display raw output.
* Illegal characters: ``;|&`'"``
* Payload: `$(cat /etc/natas_webpass/natas16)`
  * `$(echo something)` works!
  * https://blog.0xffff.info/2021/07/28/
* Or find a way to exploit grep's behavior?
* https://www.abatchy.com/2016/11/natas-level-16
  * The solution is similar to a Blind SQL attack.
  * `doomed$(grep a /etc/natas_webpass/natas17)`
    * Change the characters to brute force and build up the password.
    * Clever idea to combine the parameters of grep to get a boolean indicator.
> 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw

Level 16 -> 17
--------------
* `$_REQUEST`: sum of `$_GET`, `$_POST`, and `$_COOKIE`.
* `$_GET`: URL (query) parameters.
* echo statements are commented out -> except the "debug" statement.
  * Use `?debug=1`
* [1](https://www.php.net/manual/en/mongodb.security.request_injection.php)
  * `username[$ne]=foo` throws a notice
* [2](https://www.php.net/manual/en/function.mysql-query.php)
* No output shown -> only time-based yes/no (blind) SQL injection
  * [3](https://www.abatchy.com/2016/12/natas-level-17)
> xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP

Level 17 -> 18
--------------
* Here we can also use the `?debug=true` query parameter.
* The `$_SESSION` should contain admin=1 flag.
  * The `session_start()` PHP function should set it correctly?
  * The `PHPSESSID` in `$_COOKIE` should be used.
* Alternatively: try to get each session id up to 460: 1 is admin?
  * Yes! 119 was the correct `PHPSESSID`!
> 4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs

Level 18 -> 19
--------------
* Non-sequential session IDs?
* Cookie: `PHPSESSID` now has:
  * `httpOnly: true`
  * `path: "/"`
  * `value: "<large number>"`
* Possibly: the `PHPSESSID` is not random - hexadecimal?
  * `binascii.unhexlify('3333362d616161')`
    * The last section of the cookie is `aaa`, my username.
    * What is the first section? Random / fixed always?
    * Seems to be random... `<num>-admin`
* Modifying the session ID results in some errors - e.g. 119:
  * `Notice: Uninitialized string offset: 3 in /var/www/natas/natas19/index.php on line 26`
  * Probably the split('-') does not return an array...
* Yes! The solution was to brute-force the cookie prefix before `admin`
* [1](https://ozarch.xyz/posts/natas19/)
> eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF

Level 19 -> 20
--------------

