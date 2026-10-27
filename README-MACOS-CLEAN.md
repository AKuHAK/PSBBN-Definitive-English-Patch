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
- `__contents`: **2048 МБ (2 ГБ)** PFS — системный раздел контента.
- Системные разделы PFS: `__system`, `__sysconf`, `__common` (создаются через `initialize yes`).

### 1.3. Интеграция BB.ELF в HOSDMenu
- Исполняемый файл `BB.ELF` скопирован в `scripts/assets/osdmenu/BB.ELF` и при установке автоматически размещается в `__system/osdmenu/BB.ELF`.
- В `OSDMENU.CNF` прописаны пункты запуска:
  - `name_OSDSYS_ITEM_1 = BB Navigator` -> `hdd0:__system/osdmenu/BB.ELF`
  - `name_OSDSYS_ITEM_2 = BB Navigator (Linux)` -> `hdd0:__system/p2lboot/osdboot.elf`

### 1.4. Предустановленный OpenSSH и SFTP-сервер (Live Debugging)
Прямо в образ корневой системы `__linux.1` интегрированы:
- MIPS RPM-пакеты: `openssl-0.9.6b`, `openssh-3.4p1`, `openssh-server-3.4p1`.
- Симлинки библиотек `libcrypto.so.2` и `libssl.so.2`.
- Каталог привилегированного разделения `/var/empty/sshd`.
- Предварительно сгенерированные хост-ключи SSH (RSA, DSA).
- Конфигурационный файл `/etc/ssh/sshd_config` с включенной подсистемой SFTP (`Subsystem sftp /usr/libexec/openssh/sftp-server`).
- Автозапуск службы sshd на уровнях выполнения 2, 3, 4, 5.
- Пользователь **`bn`** и пользователь **`root`** с паролем **`bn`**.
- Сетевой адаптер `eth0` по умолчанию настроен на получение IP через DHCP.

---

## 2. Живая отладка и модификация на лету через SFTP / SSH

После загрузки PS2 и подключения сетевого кабеля к роутеру:
1. Консоль получает IP-адрес по DHCP (например, `192.168.1.50`).
2. Автоматически стартует OpenSSH демон на порту 22.

### 2.1. Подключение по SFTP (Cyberduck / FileZilla / VS Code)
- **Протокол**: SFTP (SSH File Transfer Protocol)
- **Хост**: IP-адрес PS2 (например `192.168.1.50`)
- **Порт**: `22`
- **Пользователь**: `bn` (или `root`)
- **Пароль**: `bn`

Вы можете напрямую просматривать и редактировать файлы `/opt0/`, `/net/`, `/channels/`, скрипты и ресурсы навигатора в редакторе кода прямо во время работы консоли!

### 2.2. Монтирование всей файловой системы PS2 на Mac через SSHFS
```bash
mkdir -p ~/ps2_live
sshfs root@<PS2-IP>:/ ~/ps2_live -o password_stdin <<< "bn"
```
После этого каталог `~/ps2_live` доступен в Finder и VS Code как локальный диск. Любое сохранение файла сразу записывается на работающую PS2.

### 2.3. Перезапуск процессов навигатора без перезагрузки консоли
По SSH:
```bash
ssh bn@<PS2-IP>
# Пароль: bn
killall miesque
# Запуск с отладочным выводом:
DISPLAY=:0 /opt0/bin/miesque &
```

---

## 3. Адаптация под macOS Darwin
- Создана директория `scripts/helper/darwin-x86_64/` со всеми необходимыми бинарниками (`PFS Shell.elf`, `HDL Dump.elf`, `PS2 APA Header Checksum Fixer.elf`, `PSU Extractor.elf`, `da-veto`, `mkfs.exfat`).
- Установлен Bash 5.3 в `/usr/local/bin/bash` для поддержки синтаксиса bash 4+ (`declare -A`, `${var,,}`).
- Скрипт `check-deps.sh` и `formulae.txt` очищены от ненужных Linux-зависимостей (`bchunk`, `ffmpegthumbnailer`, `rsync`, `mtools`, `axel`).
- Исключена проверка несуществующего на macOS 32-битного Linux-рантайма `ld-linux.so.2`.

---

## 4. Запуск установки на диск
Перед установкой убедитесь, что разделы внешнего диска размонтированы:
```bash
diskutil unmountDisk /dev/disk4
```
Запуск мастера установки:
```bash
./PSBBN-Definitive-Patch.sh
```
Выберите подключенный диск (`/dev/disk4`) и язык интерфейса. Установка выполнит форматирование и разметку полностью в автоматическом режиме.
