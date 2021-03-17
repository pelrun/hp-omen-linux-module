# CFLAGS_hp-wmi.o := -DDEBUG
ifneq ($(KERNELRELEASE),)
# kbuild part of makefile
obj-m := hp-wmi.o

else
# normal makefile
KDIR ?= /lib/modules/`uname -r`/build

default:
	$(MAKE) -C $(KDIR) M=$$PWD

# Module specific targets
genbin:
	echo "X" > hp-wmi_bin.o_shipped

endif

