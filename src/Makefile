# normal makefile
KERNELDIR ?= /lib/modules/`uname -r`/build

default:
	$(MAKE) -C $(KERNELDIR) M=$$PWD

# Module specific targets
genbin:
	echo "X" > hp-wmi_bin.o_shipped

clean:
	-$(RM) -f *.a *.ko *.o *.mod *.mod.c *.order *.symvers

.PHONY: clean

