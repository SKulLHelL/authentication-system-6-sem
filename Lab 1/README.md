# Получение сведений о системе

## Цель работы

Получить сведения об используемой системе

## Исходные данные

1. Стационарный ПК

2. Kali GNU/Linux Rolling

3. Терминал: QTerminal 1.2.0

## План

1. Ввод команд в эмулятор терминала

2. Анализ данных

## Ход работы

1. Для начала получим сведения об используемом дистрибутиве:

```
┌──(root㉿kali)-[~]
└─# lsb_release -a
No LSB modules are available.
Distributor ID: Kali
Description:    Kali GNU/Linux Rolling
Release:        2023.1
Codename:       kali-rolling
```

В результате выполнения данной команды было определён используемый дистрибутив - Kali GNU/Linux Rolling

2.Затем получим сведения о версии ядра:

```
┌──(root㉿kali)-[~]
└─# uname -a
Linux kali 6.1.0-kali5-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.12-1kali2 (2023-02-23) x86_64 GNU/Linux
```
В результате выполнения данной команды была получена версия ядра - 6.1.12-1kali2, дата компиляции ядра 2023-02-23

3.Далее можно получить сведения о процессоре:

```
┌──(root㉿kali)-[~]
└─# cat /proc/cpuinfo | grep "model name" 
model name      : Intel(R) Core(TM) i5-10400F CPU @ 2.90GHz
model name      : Intel(R) Core(TM) i5-10400F CPU @ 2.90GHz
```

Было определено, что используемый процессор - двухпоточный Intel(R) Core(TM) i5-10400F CPU @ 2.90GHz

4.Далее получим последние 30 строк логов системы:
```
May 20 13:49:24 kali systemd[6181]: Closed gpg-agent-browser.socket - GnuPG cryptographic agent and passphrase cache (access for web browsers).
May 20 13:49:24 kali systemd[6181]: Closed gpg-agent-extra.socket - GnuPG cryptographic agent and passphrase cache (restricted).
May 20 13:49:24 kali systemd[6181]: Closed gpg-agent-ssh.socket - GnuPG cryptographic agent (ssh-agent emulation).
May 20 13:49:24 kali systemd[6181]: Closed gpg-agent.socket - GnuPG cryptographic agent and passphrase cache.
May 20 13:49:24 kali systemd[6181]: Closed pulseaudio.socket - Sound System.
May 20 13:49:24 kali systemd[6181]: Removed slice app.slice - User Application Slice.
May 20 13:49:24 kali systemd[6181]: Reached target shutdown.target - Shutdown.
May 20 13:49:24 kali systemd[6181]: Finished systemd-exit.service - Exit the Session.
May 20 13:49:24 kali systemd[6181]: Reached target exit.target - Exit the Session.
May 20 13:49:24 kali systemd[6183]: pam_unix(systemd-user:session): session closed for user lightdm
May 20 13:49:24 kali systemd[1]: user@111.service: Deactivated successfully.
May 20 13:49:24 kali systemd[1]: Stopped user@111.service - User Manager for UID 111.
May 20 13:49:24 kali systemd[1]: Stopping user-runtime-dir@111.service - User Runtime Directory /run/user/111...
May 20 13:49:24 kali systemd[1]: run-user-111.mount: Deactivated successfully.
May 20 13:49:24 kali systemd[1]: user-runtime-dir@111.service: Deactivated successfully.
May 20 13:49:24 kali systemd[1]: Stopped user-runtime-dir@111.service - User Runtime Directory /run/user/111.
May 20 13:49:24 kali systemd[1]: Removed slice user-111.slice - User Slice of UID 111.
May 20 13:49:46 kali systemd[1]: Starting systemd-tmpfiles-clean.service - Cleanup of Temporary Directories...
May 20 13:49:46 kali systemd[1]: systemd-tmpfiles-clean.service: Deactivated successfully.
May 20 13:49:46 kali systemd[1]: Finished systemd-tmpfiles-clean.service - Cleanup of Temporary Directories.
May 20 13:49:46 kali systemd[1]: run-credentials-systemd\x2dtmpfiles\x2dclean.service.mount: Deactivated successfully.
May 20 13:49:47 kali systemd[1]: blueman-mechanism.service: Deactivated successfully.
May 20 13:55:01 kali CRON[10273]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
May 20 13:55:01 kali CRON[10274]: (root) CMD (command -v debian-sa1 > /dev/null && debian-sa1 1 1)
May 20 13:55:01 kali CRON[10273]: pam_unix(cron:session): session closed for user root
May 20 13:59:16 kali dbus-daemon[6285]: [session uid=0 pid=6285] Activating service name='org.xfce.Xfconf' requested by ':1.19' (uid=0 pid=6467 comm="xfce4-panel")
May 20 13:59:16 kali dbus-daemon[6285]: [session uid=0 pid=6285] Successfully activated service 'org.xfce.Xfconf'
May 20 14:05:01 kali CRON[16329]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
May 20 14:05:01 kali CRON[16330]: (root) CMD (command -v debian-sa1 > /dev/null && debian-sa1 1 1)
May 20 14:05:01 kali CRON[16329]: pam_unix(cron:session): session closed for user root
```

## Оценка результата

В результате лабораторной работы была получена базовая информация об используемой системе.

## Вывод

Таким образом. мы научились, используя команды Linux, получать сведения о системе.
