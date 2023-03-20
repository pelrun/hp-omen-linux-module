install:
	dkms install .

uninstall:
	dkms remove hp-omen-wmi/0.10 --all

all: install
