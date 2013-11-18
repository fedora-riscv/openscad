Name:           openscad
%global shortversion 2013.06
Version:        %{shortversion}
Release:        7%{?dist}
Summary:        The Programmers Solid 3D CAD Modeller
# COPYING contains a linking exception for CGAL
License:        GPLv2 with exceptions
Group:          Applications/Engineering
URL:            http://www.openscad.org/
Source0:        https://openscad.googlecode.com/files/%{name}-%{shortversion}.src.tar.gz
Patch0:         %{name}-stdint.patch

# https://github.com/openscad/openscad/commit/2e21f3deff585731d5377490cde87eeccd917445
Patch482:       %{name}-482.patch

BuildRequires:  qt-devel >= 4.4
BuildRequires:  bison >= 2.4
BuildRequires:  flex >= 2.5.35
BuildRequires:  eigen2-devel >= 2.0.13
BuildRequires:  boost-devel >= 1.3.5
BuildRequires:  mpfr-devel >= 3.0.0
BuildRequires:  gmp-devel >= 5.0.0
BuildRequires:  glew-devel >= 1.6
BuildRequires:  CGAL-devel >= 3.6
BuildRequires:  opencsg-devel >= 1.3.2
BuildRequires:  desktop-file-utils
BuildRequires:  ImageMagick
BuildRequires:  python2

%description
OpenSCAD is a software for creating solid 3D CAD objects.
Unlike most free software for creating 3D models (such as the famous
application Blender) it does not focus on the artistic aspects of 3D
modeling but instead on the CAD aspects. Thus it might be the application
you are looking for when you are planning to create 3D models of machine
parts but pretty sure is not what you are looking for when you are more
interested in creating computer-animated movies.

%prep
%setup -qn %{name}-%{shortversion}
%patch0 -p1
%patch482 -p1

%build
qmake-qt4 VERSION=%{shortversion} PREFIX=%{_prefix}
make %{?_smp_mflags}

# tests
cd tests
cmake .
make %{?_smp_mflags}
cd -

%install
make install INSTALL_ROOT=%{buildroot}
# manpage
mkdir -p %{buildroot}%{_mandir}/man1
cp doc/%{name}.1 %{buildroot}%{_mandir}/man1/

# remove MCAD (separated package)
rm -rf %{buildroot}%{_datadir}/%{name}/libraries/MCAD

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# tests
cd tests
ctest %{?_smp_mflags} -C All || : # let the tests fail, as they probably won't work in Koji
cd -

%files
%doc COPYING README.md RELEASE_NOTES
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/examples
%dir %{_datadir}/%{name}/libraries
%{_mandir}/man1/*

%changelog
* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 2013.06-7
- rebuilt for GLEW 1.10

* Sun Nov 17 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.06-6
- Rebuilt for new glew

* Fri Sep 27 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.06-5
- Require Python for tests

* Fri Sep 27 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.06-4
- Patch to solve upstream bug #482

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Petr Machata <pmachata@redhat.com> - 2013.06-2
- Rebuild for boost 1.54.0

* Wed Jun 19 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.06-1
- New upstream release
- Moved removing MCAD to %%install

* Sat Feb 23 2013 Kevin Fenzi <kevin@scrye.com> - 2013.01.17-6
- Rebuild for broken deps in rawhide

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 2013.01.17-5
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 2013.01.17-4
- Rebuild for Boost-1.53.0

* Sun Feb 03 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.01.17-3
- Added fix for issue 267

* Tue Jan 22 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.01.17-2
- Using  source tarball
- Reffer to the shorter version in the app
- Run tests
- Added patch so test will compile
* Sat Jan 19 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.01.17-1
- New stable release 2013.01
- Updated to respect GitHub rule

* Tue Jan 08 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.01.08-1
- New version

* Sun Jan 06 2013 Miro Hrončok <miro@hroncok.cz> - 2013.01.05-1
- New version

* Thu Dec 06 2012 Miro Hrončok <miro@hroncok.cz> - 2012.10.31-5
- Separated MCAD

* Mon Dec 03 2012 Miro Hrončok <miro@hroncok.cz> - 2012.10.31-4
- Removed useless gziping

* Sun Dec 02 2012 Miro Hrončok <miro@hroncok.cz> - 2012.10.31-3
- Added manpage

* Fri Nov 23 2012 Miro Hrončok <miro@hroncok.cz> - 2012.10.31-2
- Commented macros in comments
- Fully versioned dependency of the main package
- added desktop-file-validate

* Wed Oct 31 2012 Miro Hrončok <miro@hroncok.cz> 2012.10.31-1
- New version
- Solved 2 MLCAD files license issues
- Using full date version

* Mon Oct 08 2012 Miro Hrončok <miro@hroncok.cz> 2012.10-1
- New version.

* Sun Oct 07 2012 Miro Hrončok <miro@hroncok.cz> 2012.08-1
- New package.
