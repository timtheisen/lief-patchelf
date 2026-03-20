%if 0%{?suse_version}
%if %{suse_version} == 1500
%if "%{os_release_id}" == "sles"
%global dist .sles15sp5
%else
%global dist .leap15
%endif
%endif
%if %{suse_version} == 1600
%global dist .leap16
%endif
%endif

Name:		lief-patchelf
Version:	0.17.6
Release:	1%{?dist}
Summary:	Patchelf based on LIEF Rust bindings

License:	Apache-2.0
URL:		https://lief.re//doc/latest/tools/lief-patchelf/index.html
Source0:	%{name}-%{version}-x86_64-musl.zip
Source1:	%{name}-%{version}-aarch64-musl.zip
Source2:	Makefile
Source3:	LICENSE

BuildRequires:	unzip

%description
lief-patchelf is an implementation of the original patchelf created by
NixOS (NixOS/patchelf), based on the LIEF.  This LIEF-based version is
written in Rust, offering a more robust, modern, and maintainable
implementation compared to the original project.

%prep
cp -a %{SOURCE0} %{_builddir}
cp -a %{SOURCE1} %{_builddir}
cp -a %{SOURCE2} %{_builddir}
cp -a %{SOURCE3} %{_builddir}

%build
make %{?_smp_mflags}

%install
%make_install

%check

%files
%{_bindir}/lief-patchelf
%{_mandir}/man1/lief-patchelf.1.gz
%{_datadir}/zsh/site-functions/_lief-patchelf
%if 0%{?suse_version}
%{_datadir}/doc/lief-patchelf/README.md
%else
%doc README.md
%endif
%license LICENSE

%changelog
* Fri Mar 20 2026 Tim Theisen <tim@cs.wisc.edu> - 0.17.6-1
- Update lief-patchelf binaries

* Mon Mar 09 2026 Tim Theisen <tim@cs.wisc.edu> - 0.17.5-1
- Update lief-patchelf binaries

* Mon Jan 05 2026 Tim Theisen <tim@cs.wisc.edu> - 0.17.2-1
- Update lief-patchelf binaries

* Fri Nov 28 2025 Tim Theisen <tim@cs.wisc.edu> - 0.17.1-1
- Initial packaging of lief-patchelf binaries
