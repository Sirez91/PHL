# PHL

### Intro

The following repository is a dump for all the code and work done on the passive haptic learning project.

### TODO

Clean all hard coded strings

### Usefull Software
* arecordmidi to capture MIDI events.
```bash
	arecordmidi -p 24:0 scale.mid
```
* timidity to play MIDI files.
	* Installation and usage
		```bash
		sudo apt-get install freepats timidity timidity-interfaces-extra
		timidity -iA
		timidity some_file.mid
		```
		Source: https://sfxpt.wordpress.com/2015/02/02/how-to-play-midi-files-under-ubuntu-linux/

### Linux Mint bugs:
* Error:
```bash
	ALSA lib conf.c:3558:(snd_config_hooks_call) Cannot open shared library libasound_module_conf_pulse.so (/usr/lib/alsa-lib/libasound_module_conf_pulse.so: libasound_module_conf_pulse.so: cannot open shared object file: No such file or directory)
ALSA lib seq.c:935:(snd_seq_open_noupdate) Unknown SEQ default
```
Solution:
```bash
	sudo ln -s /usr/lib/x86_64-linux-gnu/alsa-lib/libasound_module_conf_pulse.so /usr/lib/x86_64-linux-gnu/libasound_module_conf_pulse.so
```
