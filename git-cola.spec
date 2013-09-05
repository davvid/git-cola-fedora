Name:           git-cola
Version:        1.8.4
Release:        1%{?dist}
Summary:        A sleek and powerful git GUI
License:        GPLv2+
URL:            http://git-cola.github.io
Source0:        http://git-cola.github.io/releases/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  asciidoc
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  PyQt4-devel
BuildRequires:  python2-devel
BuildRequires:  python-sphinx
BuildRequires:  xmlto
Requires:       git
Requires:       PyQt4
Requires:       python-inotify
Requires:       python-jsonpickle
Requires:       python-simplejson

%description
git-cola is a powerful git GUI with a slick and intuitive user interface.

%prep
%setup -q

%build
export PYTHON="%{__python}"
make %{?_smp_mflags}
make doc

%install
make DESTDIR=%{buildroot} prefix=%{_prefix} install
make DESTDIR=%{buildroot} prefix=%{_prefix} install-doc
make DESTDIR=%{buildroot} prefix=%{_prefix} install-html

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/git-cola.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/git-dag.desktop

%post
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :

%files -f %{name}.lang
%doc COPYING COPYRIGHT README.md
%{_bindir}/cola
%{_bindir}/git-*
%{_datadir}/applications/git*.desktop
%{_datadir}/%{name}/
%{_docdir}/%{name}/
%{_mandir}/man1/git*.1.gz

%changelog
* Thu Sep 05 2013 Christopher Meng <rpm@cicku.me> - 1.8.4-1
- Update to 1.8.4.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 30 2013 Christopher Meng <rpm@cicku.me> - 1.8.3-1
- Update to 1.8.3.
- Cleanup the spec.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.8.1-1
- Update to 1.8.1 (#885442)

* Wed Sep 26 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.8.0-1
- Update to 1.8.0 (#849593)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 08 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.7.7-1
- Update to 1.7.7 (#819165)

* Mon Mar 19 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.7.6-1
- Update to 1.7.6 (#804407)

* Mon Feb 20 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.7.5-1
- Update to 1.7.5 (#789309)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Aug 21 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.4.3.5-1
- Update to 1.4.3.5 (#732249)

* Sat May 21 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.4.3.4-1
- Update to 1.4.3.4 (#706588)

* Sat Apr 23 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.4.3.3-1
- Update to 1.4.3.3 (#699123)

* Thu Apr 14 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.4.3.2-1
- Update to 1.4.3.2 (#696563, #694806)

* Sun Mar 06 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.4.3.1-1
- Update to 1.4.3.1 (#682518)
- Drop upstreamed translations patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 03 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.4.3-1
- Update to 1.4.3, fixes broken Actions widget
- Drop docpath patch, fixed upstream
- Drop obsolete conditional for Fedora <= 11
- Fix installation of translations

* Fri Jul 30 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.4.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.4.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Mar 13 2010 Ben Boeckel <MathStuf@gmail.com> - 1.4.1.2-3
- Backport patch for documentation path

* Mon Jan 25 2010 Ben Boeckel <MathStuf@gmail.com> - 1.4.1.2-2
- Fix %%files list

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
