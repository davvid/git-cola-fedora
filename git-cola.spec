# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           git-cola
Version:        1.3.5
Release:        5%{?dist}
Summary:        A highly caffeinated git gui

Group:          Development/Tools
License:        GPLv2+
URL:            http://cola.tuxfamily.org/
Source0:        http://cola.tuxfamily.org/releases/cola-%{version}-src.tar.gz
Patch99:        git-cola-shebang.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  PyQt4-devel
BuildRequires:  asciidoc
BuildRequires:  git-core
BuildRequires:  gettext
BuildRequires:  xmlto
Requires:       git-core
Requires:       PyQt4
Requires:       python-inotify

%description
A sweet, carbonated git gui known for its
sugary flavour and caffeine-inspired features.

%prep
%setup -q -n cola-%{version}
%patch99


%build
# Remove CFLAGS=... for noarch packages (unneeded)
%{__python} setup.py build
make doc


%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --prefix=%{_prefix}
make DESTDIR=%{buildroot} prefix=%{_prefix} install-doc
make DESTDIR=%{buildroot} prefix=%{_prefix} install-html

 
%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYRIGHT LICENSE README
%{_bindir}/git-cola
%{_bindir}/git-difftool
%{_bindir}/git-difftool-helper
%{_datadir}/applications/cola.desktop
%{_datadir}/cola
%{_docdir}/cola
%{_mandir}/man1/git-cola.1.gz
%{_mandir}/man1/git-difftool.1.gz
# For noarch packages: sitelib
%{python_sitelib}/*


%changelog
* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 9 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.5-4
- Added missing Requires on PyQt4

* Thu Feb 5 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.5-3
- Added patch for shebang line removal

* Thu Feb 5 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.5-2
- Add missing BRs

* Sun Feb 1 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.5-1
- Update for 1.3.5

* Thu Jan 8 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.4.4-1
- Initial package
