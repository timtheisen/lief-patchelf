VERSION=0.17.2
ARCH := $(shell arch)

PACKAGE = lief-patchelf-$(VERSION)-$(ARCH)-musl.zip

all: unpack

unpack: $(PACKAGE)
	unzip $(PACKAGE)

install:
	install -D -m 0755 bin/lief-patchelf $(DESTDIR)/usr/bin/lief-patchelf
	install -D -m 0644 share/doc/lief-patchelf/README.md $(DESTDIR)/usr/share/doc/lief-patchelf/README.md
	install -D -m 0644 share/man/man1/lief-patchelf.1 $(DESTDIR)/usr/share/man/man1/lief-patchelf.1
	install -D -m 0644 share/zsh/site-functions/_lief-patchelf $(DESTDIR)/usr/share/zsh/site-functions/_lief-patchelf

clean:
	rm -rf bin share
