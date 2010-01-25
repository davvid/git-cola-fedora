%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           git-cola
Version:        1.4.1.2
Release:        1%{?dist}
Summary:        A highly caffeinated git gui

Group:          Development/Tools
License:        GPLv2+
URL:            http://cola.tuxfamily.org/
Source0:        http://cola.tuxfamily.org/releases/cola-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  desktop-file-utils
BuildRequires:  python-devel
BuildRequires:  PyQt4-devel
BuildRequires:  asciidoc
BuildRequires:  git
BuildRequires:  gettext
BuildRequires:  xmlto
BuildRequires:  python-sphinx
Requires:       git
Requires:       PyQt4
Requires:       python-inotify
Requires:       python-simplejson
Requires:       python-jsonpickle

%description
A sweet, carbonated git gui known for its
sugary flavour and caffeine-inspired features.


%prep
%setup -q -n cola-%{version}


%build
%{__python} setup.py build
make doc


%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --prefix=%{_prefix} --standalone
rm -f %{buildroot}%{_datadir}/applications/cola.desktop
desktop-file-install --delete-original --dir %{buildroot}%{_datadir}/applications share/applications/cola.desktop
make DESTDIR=%{buildroot} prefix=%{_prefix} install-doc
make DESTDIR=%{buildroot} prefix=%{_prefix} install-html


%clean
rm -rf %{buildroot}


%post
update-desktop-database &> /dev/null || :


%postun
update-desktop-database &> /dev/null || :


%files
%defattr(-,root,root,-)
%doc COPYRIGHT LICENSE README
%{_bindir}/git-cola
%if 0%{?fedora} < 12
%{_bindir}/git-difftool
%{_bindir}/git-difftool--helper
%endif
%{_datadir}/applications/cola.desktop
%{_datadir}/git-cola
%{_docdir}/git-cola
%{_mandir}/man1/git-cola.1.gz
%{python_sitelib}/site-packages/*


%changelog
* Sun Jan 24 2010 Ben Boeckel <MathStuf@gmail.com> - 1.4.1.2-1
- Update to 1.4.1.2

* Thu Dec 10 2009 Ben Boeckel <MathStuf@gmail.com> - 1.4.1-1
- Update to 1.4.1

* Tue Nov 17 2009 Ben Boeckel <MathStuf@gmail.com> 1.4.0.5-1
- Update to 1.4.0.5

* Mon Nov 02 2009 Ben Boeckel <MathStuf@gmail.com> 1.4.0.1-1
- Update to 1.4.0.1
- Add patch to not ship simplejson

* Sat Oct 24 2009 Ben Boeckel <MathStuf@gmail.com> 1.4.0-1
- Update to 1.4.0

* Fri Aug 28 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.9.14-1
- Update to 1.3.9.14

* Wed Jul 29 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.8-3
- Try build again for mass rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 24 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.8-1
- Update to 1.3.8
- Fix changelog usage of %%
- BR and R on git instead of git-core
- Add conditionals on git-difftool

* Mon Mar 23 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.6-1
- Update to 1.3.6

* Mon Mar 16 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.5.42-1
- Update to 1.3.5.42

* Sat Feb 28 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.5.28-1
- Added %%post and %%postun
- Use desktop-file-install

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
