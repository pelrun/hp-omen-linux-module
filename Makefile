install:
	dkms install .

uninstall:
	dkms remove hp-omen-wmi/0.9 --all

all: install

