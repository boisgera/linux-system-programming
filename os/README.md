
What's a process?
--------------------------------------------------------------------------------
  
  - ~ "program"

  - independent execution and memory

  - controlled/schedule by the OS (unless "green/lightweight" process)


Start a process
--------------------------------------------------------------------------------

Use spawn first? Fork-exec later?


Process identifier 
--------------------------------------------------------------------------------

```pycon
>>> import os
>>> pid = os.getpid()
>>> pid
18735
```

```pycon
>>> import psutil
>>> p = psutil.Process(pid)
>>> p
psutil.Process(pid=18735, name='python', status='running', started='10:51:23')
>>> name = p.name()
<bound method Process.name of psutil.Process(pid=18735, name='python', status='running', started='10:51:23')>
>>> name
'python'
```

```pycon
>>> p = psutil.Process()
>>> p
psutil.Process(pid=18735, name='python', status='running', started='10:51:23')
```


Process hierarchy
--------------------------------------------------------------------------------

```pycon
>>> psutil.pids()
[1, 2, 3, 4, 5, 6, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 117, 118, 119, 120, 121, 122, 123, 124, 125, 127, 129, 130, 132, 133, 134, 135, 136, 142, 145, 146, 147, 148, 157, 160, 168, 191, 208, 215, 233, 234, 235, 236, 237, 238, 241, 243, 247, 268, 291, 292, 408, 441, 444, 509, 534, 647, 667, 668, 669, 686, 692, 695, 696, 697, 720, 745, 746, 747, 748, 953, 1099, 1100, 1176, 1177, 1180, 1181, 1184, 1186, 1187, 1189, 1194, 1197, 1202, 1207, 1215, 1217, 1221, 1222, 1224, 1225, 1231, 1270, 1273, 1277, 1284, 1285, 1296, 1337, 1393, 1435, 1519, 1520, 1578, 1633, 1637, 1676, 1699, 1755, 1757, 1775, 2057, 2081, 2173, 2266, 2430, 2436, 2437, 2442, 2444, 2448, 2450, 2468, 2473, 2475, 2488, 2492, 2498, 2501, 2505, 2510, 2517, 2538, 2540, 2556, 2624, 2642, 2647, 2655, 2662, 2676, 2703, 2707, 2708, 2710, 2712, 2725, 2729, 2731, 2740, 2749, 2753, 2762, 2780, 2787, 2804, 2805, 2806, 2810, 2812, 2814, 2815, 2817, 2818, 2819, 2821, 2822, 2823, 2824, 2826, 2833, 2837, 2853, 2864, 2872, 2878, 2880, 2930, 2952, 2957, 2991, 2992, 3010, 3033, 3036, 3117, 3121, 3157, 4630, 5207, 6907, 6918, 8720, 8957, 9093, 9162, 9182, 9249, 9341, 10408, 10410, 10523, 10607, 10702, 10710, 10759, 10797, 10800, 10801, 10803, 10816, 10829, 10837, 10849, 10890, 10904, 10920, 10945, 11071, 11215, 11908, 12450, 12657, 12658, 12659, 12660, 12776, 12843, 13063, 15048, 15477, 18087, 18132, 18361, 18363, 18366, 18654, 18668, 18735, 19088, 19092, 19167, 19229, 19256, 19277, 19339]
```

```pycon
>>> ppid = os.getppid()
>>> ppid
12450
>>> parent = psutil.Process(ppid)
>>> parent
psutil.Process(pid=12450, name='bash', status='sleeping', started='10:37:49')
```



```pycon
>>> p
psutil.Process(pid=18735, name='python', status='running', started='10:51:23')
>>> p.parent()
psutil.Process(pid=12450, name='bash', status='sleeping', started='10:37:49')
>>> p.parent().parent()
psutil.Process(pid=10920, name='code', status='sleeping', started='10:26:00')
>>> p.parents()
[psutil.Process(pid=12450, name='bash', status='sleeping', started='10:37:49'), psutil.Process(pid=10920, name='code', status='sleeping', started='10:26:00'), psutil.Process(pid=10890, name='code', status='sleeping', started='10:26:00'), psutil.Process(pid=10797, name='code', status='sleeping', started='10:25:57'), psutil.Process(pid=2436, name='systemd', status='sleeping', started='09:46:20'), psutil.Process(pid=1, name='systemd', status='sleeping', started='09:45:46')]
```

--------------------------------------------------------------------------------

```pycon
>>> pid = os.posix_spawn("/usr/bin/true", ["true"], {})
>>> pid, status = os.waitpid(pid, os.WNOHANG)
>>> pid, status
(25690, 0)
```

```pycon
>>> pid = os.posix_spawn("/usr/bin/false", ["false"], {})
>>> pid, status = os.waitpid(pid, os.WNOHANG)
>>> pid, status
(25826, 256)
```

```pycon
>>> pid = os.posix_spawn("/usr/bin/echo", ["echo", "Hello", "world!", "👋", "\n"], {})
>>> Hello world! 👋 

psutil.Process(pid)
psutil.Process(pid=23240, name='echo', status='zombie', started='11:19:14')
>>> pid, status = os.waitpid(pid, os.WNOHANG)
>>> pid, status
(23240, 0)
```

**TODO:** long-running tasks (maybe used tqdm?), forever tasks, etc.

--------------------------------------------------------------------------------

```python
# 📄 progress.py

# Python Standard Library
import sys
import time

# Third-Party Libraries
from tqdm import tqdm

args = sys.argv
try:
    print(args)
    exit()
    num_steps = int(args[1])
except IndexError: # no argument
    num_steps = 10

for i in tqdm(range(num_steps)):
    time.sleep(1.0)
```

```pycon
>>> psutil.Process()
psutil.Process(pid=31090, name='python', status='running', started='11:42:29')
>>> psutil.Process().exe()
'/home/boisgera/miniconda3/bin/python3.8'
>>> python = psutil.Process().exe()
>>> os.posix_spawn(python, ["python", "progress.py", "60"], {})
32010
>>> Could not find platform independent libraries <prefix>
Could not find platform dependent libraries <exec_prefix>
Consider setting $PYTHONHOME to <prefix>[:<exec_prefix>]
Python path configuration:
  PYTHONHOME = (not set)
  PYTHONPATH = (not set)
  program name = 'python'
  isolated = 0
  environment = 1
  user site = 1
  import site = 1
  sys._base_executable = ''
  sys.base_prefix = '/tmp/build/80754af9/python_1614202678154/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho'
  sys.base_exec_prefix = '/tmp/build/80754af9/python_1614202678154/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho'
  sys.executable = ''
  sys.prefix = '/tmp/build/80754af9/python_1614202678154/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho'
  sys.exec_prefix = '/tmp/build/80754af9/python_1614202678154/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho'
  sys.path = [
    '/tmp/build/80754af9/python_1614202678154/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/lib/python38.zip',
    '/tmp/build/80754af9/python_1614202678154/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/lib/python3.8',
    '/tmp/build/80754af9/python_1614202678154/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/lib/lib-dynload',
  ]
Fatal Python error: init_fs_encoding: failed to get the Python codec of the filesystem encoding
Python runtime state: core initialized
ModuleNotFoundError: No module named 'encodings'

Current thread 0x00007f63e9b95740 (most recent call first):
<no Python frame>
```

```pycon
>>> os.environ
environ({'SHELL': '/bin/bash', 'SESSION_MANAGER': 'local/oddball:@/tmp/.ICE-unix/2662,unix/oddball:/tmp/.ICE-unix/2662', 'CAML_LD_LIBRARY_PATH': '/home/boisgera/.opam/4.14.0/lib/stublibs:/home/boisgera/.opam/4.14.0/lib/ocaml/stublibs:/home/boisgera/.opam/4.14.0/lib/ocaml', 'QT_ACCESSIBILITY': '1', 'OCAML_TOPLEVEL_PATH': '/home/boisgera/.opam/4.14.0/lib/toplevel', 'COLORTERM': 'truecolor', 'XDG_CONFIG_DIRS': '/etc/xdg/xdg-ubuntu:/etc/xdg', 'XDG_MENU_PREFIX': 'gnome-', 'TERM_PROGRAM_VERSION': '1.75.1', 'GNOME_DESKTOP_SESSION_ID': 'this-is-deprecated', 'CONDA_EXE': '/home/boisgera/miniconda3/bin/conda', '_CE_M': '', 'MANDATORY_PATH': '/usr/share/gconf/ubuntu.mandatory.path', 'LC_ADDRESS': 'fr_FR.UTF-8', 'GNOME_SHELL_SESSION_MODE': 'ubuntu', 'LC_NAME': 'fr_FR.UTF-8', 'SSH_AUTH_SOCK': '/run/user/1000/keyring/ssh', 'GRADLE_HOME': '/home/boisgera/.sdkman/candidates/gradle/current', 'SDKMAN_CANDIDATES_DIR': '/home/boisgera/.sdkman/candidates', 'XMODIFIERS': '@im=ibus', 'DESKTOP_SESSION': 'ubuntu', 'LC_MONETARY': 'fr_FR.UTF-8', 'SSH_AGENT_PID': '2624', 'GTK_MODULES': 'gail:atk-bridge', 'PWD': '/home/boisgera/VOYAGER/ENS/IDS/system-programming/os', 'NIX_PROFILES': '/nix/var/nix/profiles/default /home/boisgera/.nix-profile', 'XDG_SESSION_DESKTOP': 'ubuntu', 'LOGNAME': 'boisgera', 'XDG_SESSION_TYPE': 'x11', 'CONDA_PREFIX': '/home/boisgera/miniconda3', 'MANPATH': ':/home/boisgera/.opam/4.14.0/man', 'GPG_AGENT_INFO': '/run/user/1000/gnupg/S.gpg-agent:0:1', 'XAUTHORITY': '/run/user/1000/gdm/Xauthority', 'VSCODE_GIT_ASKPASS_NODE': '/usr/share/code/code', 'OPAM_SWITCH_PREFIX': '/home/boisgera/.opam/4.14.0', 'WINDOWPATH': '2', 'HOME': '/home/boisgera', 'USERNAME': 'boisgera', 'IM_CONFIG_PHASE': '1', 'LC_PAPER': 'fr_FR.UTF-8', 'LANG': 'en_US.UTF-8', 'LS_COLORS': 'rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:', 'XDG_CURRENT_DESKTOP': 'Unity', 'VTE_VERSION': '6003', 'NIX_SSL_CERT_FILE': '/etc/ssl/certs/ca-certificates.crt', 'SDKMAN_VERSION': '5.11.5+713', 'CONDA_PROMPT_MODIFIER': '(base) ', 'GIT_ASKPASS': '/usr/share/code/resources/app/extensions/git/dist/askpass.sh', 'GNOME_TERMINAL_SCREEN': '/org/gnome/Terminal/screen/22573341_1423_48d5_b91e_a593799fb57c', 'INVOCATION_ID': '558dc0e23421403fa7ebd5c7849e0842', 'MANAGERPID': '2436', 'CHROME_DESKTOP': 'code-url-handler.desktop', 'VSCODE_GIT_ASKPASS_EXTRA_ARGS': '--ms-enable-electron-run-as-node', 'LESSCLOSE': '/usr/bin/lesspipe %s %s', 'XDG_SESSION_CLASS': 'user', 'LC_IDENTIFICATION': 'fr_FR.UTF-8', 'TERM': 'xterm-256color', '_CE_CONDA': '', 'DEFAULTS_PATH': '/usr/share/gconf/ubuntu.default.path', 'LESSOPEN': '| /usr/bin/lesspipe %s', 'LIBVIRT_DEFAULT_URI': 'qemu:///system', 'USER': 'boisgera', 'KOTLIN_HOME': '/home/boisgera/.sdkman/candidates/kotlin/current', 'VSCODE_GIT_IPC_HANDLE': '/run/user/1000/vscode-git-5645cac40f.sock', 'GNOME_TERMINAL_SERVICE': ':1.129', 'CONDA_SHLVL': '1', 'SDKMAN_DIR': '/home/boisgera/.sdkman', 'DISPLAY': ':0', 'SHLVL': '2', 'LC_TELEPHONE': 'fr_FR.UTF-8', 'QT_IM_MODULE': 'ibus', 'LC_MEASUREMENT': 'fr_FR.UTF-8', 'SDKMAN_CANDIDATES_API': 'https://api.sdkman.io/2', 'CONDA_PYTHON_EXE': '/home/boisgera/miniconda3/bin/python', 'XDG_RUNTIME_DIR': '/run/user/1000', 'CONDA_DEFAULT_ENV': 'base', 'LC_TIME': 'fr_FR.UTF-8', 'BUN_INSTALL': '/home/boisgera/.bun', 'VSCODE_GIT_ASKPASS_MAIN': '/usr/share/code/resources/app/extensions/git/dist/askpass-main.js', 'JOURNAL_STREAM': '8:56041', 'XDG_DATA_DIRS': '/usr/share/ubuntu:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop', 'GDK_BACKEND': 'x11', 'PATH': '/home/boisgera/.local/elixir/bin:/home/boisgera/.local/zig-linux-x86_64-0.11.0-dev.1479+97b1a9bb6:/home/boisgera/.bun/bin:/home/boisgera/.mix/escripts:/home/boisgera/.local/node-v16.14.2-linux-x64/bin:/home/boisgera/.local/go/bin:/home/boisgera/go/bin:/home/boisgera/.local/lib/IntelliJ-IDEA/bin:/home/boisgera/.local/bin:/home/boisgera/.nix-profile/bin:/nix/var/nix/profiles/default/bin:/home/boisgera/.local/elixir/bin:/home/boisgera/.local/zig-linux-x86_64-0.11.0-dev.1479+97b1a9bb6:/home/boisgera/.bun/bin:/home/boisgera/.mix/escripts:/home/boisgera/.local/node-v16.14.2-linux-x64/bin:/home/boisgera/.local/go/bin:/home/boisgera/go/bin:/home/boisgera/.sdkman/candidates/kotlin/current/bin:/home/boisgera/.sdkman/candidates/gradle/current/bin:/home/boisgera/.local/lib/IntelliJ-IDEA/bin:/home/boisgera/miniconda3/bin:/home/boisgera/miniconda3/condabin:/home/boisgera/.local/bin:/home/boisgera/.nix-profile/bin:/nix/var/nix/profiles/default/bin:/home/boisgera/.opam/4.14.0/bin:/home/boisgera/.cargo/bin:/home/boisgera/.local/bin:/home/boisgera/.nix-profile/bin:/nix/var/nix/profiles/default/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin', 'GDMSESSION': 'ubuntu', 'ORIGINAL_XDG_CURRENT_DESKTOP': 'ubuntu:GNOME', 'DBUS_SESSION_BUS_ADDRESS': 'unix:path=/run/user/1000/bus', 'SDKMAN_PLATFORM': 'linuxx64', 'LC_NUMERIC': 'fr_FR.UTF-8', 'OLDPWD': '/home/boisgera/VOYAGER/ENS/IDS/system-programming', 'TERM_PROGRAM': 'vscode', '_': '/home/boisgera/miniconda3/bin/python'})
```

```pycon
>>> pid = os.posix_spawn(python, ["python", "progress.py", "30"], os.environ)
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████| 30/30 [00:30<00:00,  1.00s/it]
>>> 
>>> pid
35396
>>> psutil.Process(pid)
psutil.Process(pid=35396, name='python3.8', status='zombie', started='11:54:34')
```