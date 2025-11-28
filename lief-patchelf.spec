Name:		lief-patchelf
Version:	0.17.1
Release:	1%{?dist}
Summary:	patchelf based on LIEF Rust bindings

License:	Apache-2.0
URL:		https://lief.re//doc/latest/tools/lief-patchelf/index.html
Source0:	lief-patchelf-0.17.1-x86_64-musl.zip
Source1:	lief-patchelf-0.17.1-aarch64-musl.zip
Source2:	LICENSE


BuildRequires:	unzip

%description
lief-patchelf is an implementation of the original patchelf created by
NixOS (NixOS/patchelf), based on the LIEF.  This LIEF-based version is
written in Rust, offering a more robust, modern, and maintainable
implementation compared to the original project.

%prep
%ifarch x86_64
unzip %{SOURCE0}
%endif
%ifarch aarch64
unzip %{SOURCE1}
%endif

%build
# Packaing pre-built binaries

%install
mkdir -p %{buildroot}%{_usr}
mv bin share %{buildroot}%{_usr}
mkdir -p %{buildroot}%{_defaultlicensedir}/lief-patchelf
cp -a %{SOURCE2} %{buildroot}%{_defaultlicensedir}/lief-patchelf

%files
%{_bindir}/lief-patchelf
%{_mandir}/man1/lief-patchelf.1.gz
%{_datadir}/zsh/site-functions/_lief-patchelf
%doc README.md
%license LICENSE

%changelog
* Fri Nov 28 2025 Tim Theisen <tim@cs.wisc.edu> - 0.17.1-1
- Initial packaging of lief-patchelf binaries
