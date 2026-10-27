# PSBBN Definitive Project — macOS Clean BB Navigator Edition

Специальная сборка установщика PlayStation Broadband Navigator (PSBBN) для macOS (x86_64 / Apple Silicon через Rosetta/нативно) с поддержкой прямого форматирования ext2/ext2swap через кастомный `pfsshell`, предустановленным SSH/SFTP для живой отладки и чистой конфигурацией без игр и эмуляторов.

---

## 1. Основные изменения в сборке

### 1.1. Очистка от лишних компонентов
- **Удалена эмуляция PS1 и POPS**: исключены зависимости `bchunk`, `cue2pops`, `POPSTARTER.ELF`, `icon.sys`, `CHEATS.TXT`.
- **Удалены OPL и Neutrino**: исключены `OPNPS2LD.ELF`, `neutrino.elf`, создание каталогов игр.
- **Удалён музыкальный раздел**: исключён раздел `__linux.8` (MusicCh) и зависимости `bitrate`, `music.db`, `ffmpegthumbnailer`.
- **Исключены игровые разделы**: разметка не создаёт разделов `PP.*`, ставится исключительно голая система PSBBN.

### 1.2. Разметка и размеры разделов диска
Все разделы создаются и форматируются встроенным `pfsshell` (ветка AKuHAK) без сторонних утилит форматирования:
- `__linux.1`: **1024 МБ (1 ГБ)** EXT2 — корневая файловая система `/` (увеличена с 512 МБ).
- `__linux.2`: **128 МБ** EXT2SWAP — раздел подкачки (swap).
- `__linux.4`: **1024 МБ (1 ГБ)** EXT2 — основной раздел навигатора `/opt0` (увеличен с 512 МБ).
- `__linux.5`: **512 МБ** EXT2 — `/net` (домашние каталоги пользователей).
- `__linux.6`: **128 МБ** EXT2 — `/bntmp` (временные файлы навигатора).
- `__linux.7`: **256 МБ** EXT2 — `/mnt` (системные конфигурации).
- `__linux.9`: **2048 МБ (2 ГБ)** EXT2 — `/channels` (каналы навигатора).
- `__contents`: **3072 МБ (3 ГБ)** PFS — системный раздел контента (увеличен до 3 ГБ).
- Системные разделы PFS: `__system`, `__sysconf`, `__common` (создаются через `initialize yes`).

### 1.3. Интеграция BB.ELF в HOSDMenu
- Исполняемый файл `BB.ELF` скопирован в `scripts/assets/osdmenu/BB.ELF` и при установке автоматически размещается в `__system/osdmenu/BB.ELF`.
- В `OSDMENU.CNF` прописаны пункты запуска:
  - `name_OSDSYS_ITEM_1 = BB Navigator` -> `hdd0:__system/osdmenu/BB.ELF`
  - `name_OSDSYS_ITEM_2 = BB Navigator (Linux)` -> `hdd0:__system/p2lboot/osdboot.elf`

### 1.4. Предустановленный OpenSSH, SFTP-сервер, sudo и утилиты отладки (Live Debugging)
Прямо в образ корневой системы `__linux.1` интегрированы:
- MIPS RPM-пакеты: `openssl-0.9.6b`, `openssh-3.4p1`, `openssh-server-3.4p1`.
- Пакеты отладки из каталога `rpm/`: `sudo-1.6.3p3-5`, `strace-4.2-3`, `gdb-4.17-4`, `Eterm-0.8.11-3`.
- Симлинки библиотек `libcrypto.so.2` и `libssl.so.2`.
- Каталог привилегированного разделения `/var/empty/sshd`.
- Предварительно сгенерированные хост-ключи SSH (RSA, DSA).
- Конфигурационный файл `/etc/ssh/sshd_config` с включенной подсистемой SFTP (`Subsystem sftp /usr/libexec/openssh/sftp-server`).
- Автозапуск службы sshd на уровнях выполнения 2, 3, 4, 5.
- Пользователь **`bn`** и пользователь **`root`** с паролем **`bn`**.
- Настроен `sudo` с правами без пароля: `bn ALL=(ALL) NOPASSWD: ALL` (права `4755` на `/usr/bin/sudo` и `440` на `/etc/sudoers`).
- Сетевой адаптер `eth0` настроен на получение IP через DHCP с отправкой имени узла роутеру: `DHCP_HOSTNAME=ps2`.
- Системный хостнейм: **`ps2`** (`/etc/sysconfig/network`, `/etc/hosts`).

---

## 2. Живая отладка и модификация на лету через SFTP / SSH

После загрузки PS2 и подключения сетевого кабеля к роутеру:
1. Консоль автоматически отправляет имя **`ps2`** роутеру по DHCP (DHCP Option 12) и получает IP-адрес.
2. Роутер регистрирует имя `ps2` / `ps2.lan` / `ps2.local` в локальном DNS.
3. Автоматически стартует OpenSSH демон на порту 22.

### 2.1. Подключение по SSH
```bash
ssh bn@ps2
# или если не резолвится сразу:
ssh bn@ps2.local
# Пароль: bn

# Получение полных root-прав:
sudo -i   # (пароль не требуется)
```

### 2.2. Подключение по SFTP (Cyberduck / FileZilla / VS Code / Transmit)
- **Протокол**: SFTP (SSH File Transfer Protocol)
- **Хост**: `ps2` (или `ps2.local` / IP адрес)
- **Порт**: `22`
- **Пользователь**: `bn` (или `root`)
- **Пароль**: `bn`

Вы можете напрямую просматривать и редактировать файлы `/opt0/`, `/net/`, `/channels/`, скрипты и ресурсы навигатора в редакторе кода прямо во время работы консоли!

### 2.3. Монтирование всей файловой системы PS2 на Mac через SSHFS
```bash
mkdir -p ~/ps2_live
sshfs root@ps2:/ ~/ps2_live -o password_stdin <<< "bn"
```
После этого каталог `~/ps2_live` доступен в Finder и VS Code как локальный диск. Любое сохранение файла сразу записывается на работающую PS2.

### 2.4. Перезапуск процессов навигатора без перезагрузки консоли
По SSH:
```bash
ssh bn@ps2
killall miesque
# Запуск с отладочным выводом:
DISPLAY=:0 /opt0/bin/miesque &
```

---

## 3. Адаптация под macOS Darwin
- Создана директория `scripts/helper/darwin-x86_64/` со всеми необходимыми бинарниками (`PFS Shell.elf`, `HDL Dump.elf`, `PS2 APA Header Checksum Fixer.elf`, `PSU Extractor.elf`, `da-veto`, `mkfs.exfat`).
- Установлен Bash 5.3 в `/usr/local/bin/bash` для поддержки синтаксиса bash 4+ (`declare -A`, `${var,,}`).
- Оптимизирован `build_overlay` с мгновенным монтированием через каталожные симлинки и исключение тяжелых деревьев сборки.
- Скрипт `check-deps.sh` и `formulae.txt` очищены от ненужных Linux-зависимостей (`bchunk`, `ffmpegthumbnailer`, `rsync`, `mtools`, `axel`).
- Исключена проверка несуществующего на macOS 32-битного Linux-рантайма `ld-linux.so.2`.

---

## 4. Команда неинтерактивной установки на диск

Перед установкой убедитесь, что разделы внешнего диска размонтированы:
```bash
diskutil unmountDisk /dev/disk4
```

Запуск полной неинтерактивной установки на `/dev/disk4`:
```bash
sudo PSBBN_DEVICE=/dev/disk4 PSBBN_NONINTERACTIVE=1 /usr/local/bin/bash ./PSBBN-Definitive-Patch.sh
```
Скрипт автоматически:
1. Выберет накопитель `/dev/disk4`.
2. Очистит MBR и таблицу разделов.
3. Создаст и отформатирует разделы через `pfsshell` (EXT2 и PFS), включая `__contents` 3 ГБ.
4. Развернет ядро, систему, HOSDMenu с `BB.ELF`.
5. Установит SSH, SFTP, `sudo`, `strace`, `gdb`.
6. Настроит сеть, DHCP-имя хоста `ps2` и завершит установку.
