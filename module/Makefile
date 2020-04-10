ifneq ($(KERNELRELEASE),)
# kbuild part of makefile
obj-m := hp-wmi-53.o

else
# normal makefile
KDIR ?= /lib/modules/`uname -r`/build

default:
	$(MAKE) -C $(KDIR) M=$$PWD

# Module specific targets
genbin:
	echo "X" > hp-wmi-53_bin.o_shipped

endif

