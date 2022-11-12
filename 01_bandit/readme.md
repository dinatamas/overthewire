Bandit Wargame - OverTheWire
============================

> dinatamaspal | 27th January, 2022

__All commands listed:__
* `ls cd cat file du find grep`
* `grep sort uniq strings base64 tr tar gzip bzip2 xxd mkdir cp mv file`
* `ssh telnet nc openssl s_client nmap`
* `cat grep ls diff`
* `ssh ls cat`
* `ssh nc cat bash screen tmux`
* Unix job control (`bg`, `fg`, `jobs`, &, CTRL-Z, ...)
* `cron crontab`
* `ssh cat more vi ls id pwd`
* `git`
* `sh man`

Level 0 -> 1
------------
* `ssh -p 2220 bandit0@bandit.labs.overthewire.org`
  * Password is `bandit0`
  * Read the banner: lots of important info!.
    * `gef`: TODO
    * `pwndbg`: TODO
    * `peda`: TODO
    * `gdbinit`: TODO
    * `pwntools`: TODO
    * `radare2`: TODO
    * `checksec.sh`: TODO
* `pwd`, `ls -a`, `cat readme`
> boJ9jbbUNNfktd78OOpsqOltutMc3MY1

Level 1 -> 2
------------
* `cat ./-`
* https://tldp.org/LDP/abs/html/index.html
* May refer to `-` stdin/stdout (based on program)
> CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

Level 2 -> 3
------------
* `cat "spaces in this filename"`
> UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

Level 3 -> 4
------------
* `ls -a inhere`, `cat inhere/.hidden`
> pIwrPrtPN36QITSp3EQaw936yaFoFgAB

Level 4 -> 5
------------
* `reset` command: fixes a messed up terminal.
* `find inhere -exec file {} +`
  * `-inhere07` is the only ASCII text.
  * `cat 'inhere/-file07'`
> koReBOKuIDDepwhWk7jZC0RTdopnAYKh

Level 5 -> 6
------------
* `ls -Rhal`
* `find . -type f -size 1033c -not -executable -exec file {} +`
  * `cat inhere/maybehere07/.file2`
> DXjZPULLxYr17uwoI01bNLQbtFemEgo7

Level 6 -> 7
------------
* `find / -type f -size 33c -user bandit7 -group bandit6 2>/dev/null`
  * Or: `grep -v` for "Permission denied" and "No such file or directory"
  * `cat /var/lib/dpkg/info/bandit7.password`
> HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

Level 7 -> 8
------------
* `wc -l data.txt`
* `head -20 data.txt`
* `cat data.txt | grep "millionth"`
> cvX2JJa4CFALtqS87jk27qwqGhBM9plV

Level 8 -> 9
------------
* https://ryanstutorials.net/linuxtutorial/piping.php
* `cat data.txt | sort | uniq -u`
> UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

Level 9 -> 10
-------------
* `strings data.txt | grep "=="`
> truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

Level 10 -> 11
--------------
* `cat data.txt | base64 -d`
> IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR

Level 11 -> 12
--------------
* https://en.wikipedia.org/wiki/ROT13
* `cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'`
  * Or: `tr <from> <to> <<< "<string>"`
> 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

Level 12 -> 13
--------------
* `mktemp -d /tmp/XXXX`
  * Without `-d` it creates a file.
* `cd` and `cp`
* `cat data.txt | xxd -r >data`
  * Regular `xxd` will dump hex.
* `mv data data.gz`
* Recursively decompress:
  * Use `file` before each to determine.
  * Repeatedly: `gunzip`, `bunzip2`, `tar xf`
  * For `gunzip` the file must have `.gz` suffix.
* Remove the temp directory in `/tmp`.
> 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

Level 13 -> 14
--------------
* `ssh -i sshkey.private bandit14@localhost`
* `cat /etc/bandit_pass/bandit14`
> 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e

Level 14 -> 15
--------------
* `echo "4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e" > /dev/tcp/127.0.0.1/30000`
    * Doesn't work because we don't receive the response.
* `echo "4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e" | nc 127.0.0.1 30000`
> BfMYroe26WYalil77FoDi9qh59eK5xNr

Level 15 -> 16
--------------
* Reference: OpenSSL Cookbook (Testing TLS with OpenSSL)
* `openssl s_client --connect localhost:30001`
> cluFn7wTiGryunymYOu4RcffSxQluehd

Level 16 -> 17
--------------
* https://danielmiessler.com/study/nmap/
* `nmap -p31000-32000 localhost`
  * Root default scan type is `-sS` a.k.a. TCP SYN.
  * Unprivileged: ping scan (`-sP`).
* https://cheatsheetseries.owasp.org/index.html
* `nmap --script ssl-enum-ciphers -p 31046,31518,31691,31790,31960 localhost`
  * There are other scripts to check for SSL vulnerabilities.
* `openssl s_client --connect localhost:31518` just echo server.
* `openssl s_client --connect localhost:31790`
* We get an SSH key by submitting this level's password.
* `chmod 600 bandit17_id_rsa`
* `ssh -i ./bandit17_id_rsa -p 2220 bandit17@bandit.labs.overthewire.org`
  * `cat /etc/bandit_pass/bandit17`
> xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn

Level 17 -> 18
--------------
* `diff passwords.new passwords.old`
> kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd

Level 18 -> 19
--------------
* `scp -P 2220 bandit18@bandit.labs.overthewire.org:~/readme ./readme`
  * `.bashrc` is not sourced when executing SCP commands.
> IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x

Level 19 -> 20
--------------
* `./bandit20-do` uses setuid.
  * `./bandit20-do .`
* `./bandit20-do cat /etc/bandit_pass/bandit20`
> GbKksEFF4yrVs6il55v6gwY5aVje5f0j

Level 20 -> 21
--------------
* `tmux` and `Ctrl+B "`
* `./suconnect 34432`
* `nc -l -p 34432 127.0.0.1`
  * Local port `-p` is required for localhost.
  * Send level 20's password here.
> gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr

Level 21 -> 22
--------------
* `man 5 crontab`
  * `crontab -l` gives Permission denied for `crontabs/bandit21`?
* `ps aux`
  * Shows `vim cronjob_bandit22`
  * `ls /etc/cron.d`
  * `cat /etc/cron.d/cronjob_bandit22`
    * `cat /usr/bin/cronjob_bandit22.sh`
      * `cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv`
> Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI

Level 22 -> 23
--------------
* `cat /etc/cron.d/cronjob_bandit23`
* `cat /usr/bin/cronjob_bandit23.sh`
* `echo I am user bandit23 | md5sum | cut -d ' ' -f 1`
* `cat /tmp/8ca319486bfbbc3663ea0fbe81326349`
> jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n

Level 23 -> 24
--------------
* `cat /etc/cron.d/cronjob_bandit24`
* `cat /usr/bin/cronjob_bandit24.sh`
  * `https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch05s14.html`
    * `/var/spool` contains data which is awaiting some kind of later
      processing. Data in `/var/spool` represents work to be done in
      the future (by a program, user, or administrator); often data
      is deleted after it has been processed.
    * `stat --format "%U" ./dt_solve.sh`
    * `timeout -s 9 60 ./dt_solve.sh`
      * Sends signal 9 (KILL) to process after 60 seconds.
* `/var/spool/bandit24` has `drwxrwx-wx` permissions.
  * So I can write there but can't read.
* `vim` to copy `bandit24.sh`'s contents.
  * `i`
  * `:w /var/spool/bandit24/dt_solve.sh`
  * `q`
* `chmod +x /var/spool/bandit24/dt_solve.sh`
* `watch ls -a /var/spool/bandit24/`
  * To exit: `Ctrl+C`
* `cat /tmp/dt_bandit24/flag.txt`
* `rm -rf /tmp/dt_bandit24/`
> UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ

Level 24 -> 25
--------------
* Brute force using `bandit25.py`. Run it from `/tmp`.
> uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

Level 25 -> 26
--------------
* I had to cheat to figure this out!
* `sftp -P 2220 bandit25@bandit.labs.overthewire.org:bandit26.sshkey ./`
* `ssh -i ./bandit26.sshkey -p 2220 bandit26@bandit.labs.overthewire.org`
* `cat /etc/passwd`
  * User `bandit26` has a login shell `usr/bin/showtext`
  * Similar to the `/sbin/nologin` restricted shell.
* Exploit: `more` is called if the terminal emulator is small enough.
  Pressing `v` opens and editor. `:e /etc/bandit_pass/bandit26` solves it.
  * If `cat` was used instead of `more`, it may never have worked!
  * https://gtfobins.github.io/gtfobins/vi/
    * `:set shell=/bin/bash`
    * `:shell` works great!
* Alternative "exploit": https://serverfault.com/a/206582
  * Ctrl+C may be effective!
> 5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z

Level 26 -> 27
--------------
* bandit26 has a `bandit-27-do` binary in its home directory.
* Running `./bandit27-do cat /etc/bandit_pass/bandit27` gives the password.
> 3ba3118a22e93127a4ed485be72ef5ea

Level 27 -> 28
--------------
* `cd $(mktemp -d)`
* git clone `ssh://bandit27-git@localhost/home/bandit27-git/repo`
  * Accept the fingerprint.
  * Same password as for the `bandit27` user.
* `cat repo/README`
> 0ef186ac70e04ea33b4c1853d2526fa2

Level 28 -> 29
--------------
* `cd $(mktemp -d)`
* `git clone ssh://bandit28-git@localhost/home/bandit28-git/repo`
  * Accept the fingerprint.
* `cd repo`
* `git log`
* `git checkout c086d11a00c0648d095d04c089786efef5e01264`
* `cat README.md`
> bbc96594b4e001778eee9975372716b2

Level 29 -> 30
--------------
* `cd $(mktemp -d)`
* `git clone ssh://bandit29-git@localhost/home/bandit29-git/repo`
  * Accept the fingerprint.
* `cd repo`
* `git branch -a`
* `git checkout remotes/origin/dev`
* `cat README.md`
> 5b90576bedb2cc04c86a9e924ce42faf

Level 30 -> 31
--------------
* `cd $(mktemp -d)`
* `git clone ssh://bandit30-git@localhost/home/bandit30-git/repo`
  * Accept the fingerprint.
* `cd repo`
* `git tag`
* `git show secret`
  * This prints the annotation of the tag `secret`.
> 47e603bb428404d265f59c42920d81e5

Level 31 -> 32
--------------
* Same as above.
* `echo 'May I come in?' > key.txt`
* `git add -f key.txt`
* `git commit -m 'Solution'`
* `git push`
* A pre-receive hook failed but gave us the answer.
> 56a9bf19c63d650ce78e6ec0354ee45e

Level 32 -> 33
--------------
* Variable values can work: `$shell`, `$term`
* Ctrl+D and Ctrl+C exit the shell.
* Entering `$0` will drop back to the shell!
> c9c3199ddf4121b10cf581a98d51caee

Level 33 -> 34
--------------
* At this moment, level 34 does not exist yet.
