Name:           openscad
Version:        2015.03.3
%global upversion 2015.03-3
Release:        11%{?dist}
Summary:        The Programmers Solid 3D CAD Modeller
# COPYING contains a linking exception for CGAL
# Appdata file is CC0
# Examples are CC0
License:        GPLv2 with exceptions and CC0
Group:          Applications/Engineering
URL:            http://www.%{name}.org/
Source0:        http://files.%{name}.org/%{name}-%{upversion}.src.tar.gz
Patch0:         %{name}-polyclipping.patch
BuildRequires:  CGAL-devel >= 3.6
BuildRequires:  ImageMagick
BuildRequires:  Xvfb
BuildRequires:  bison >= 2.4
BuildRequires:  boost-devel >= 1.35
BuildRequires:  desktop-file-utils
BuildRequires:  eigen3-devel
BuildRequires:  flex >= 2.5.35
BuildRequires:  freetype-devel >= 2.4
BuildRequires:  fontconfig-devel >= 2.10
BuildRequires:  gettext
BuildRequires:  glew-devel >= 1.6
BuildRequires:  glib2-devel
BuildRequires:  gmp-devel >= 5.0.0
BuildRequires:  harfbuzz-devel >= 0.9.19
BuildRequires:  mesa-dri-drivers
BuildRequires:  mpfr-devel >= 3.0.0
BuildRequires:  opencsg-devel >= 1.3.2
BuildRequires:  polyclipping-devel >= 6.1.3
BuildRequires:  procps-ng
BuildRequires:  python2
BuildRequires:  qt4-devel >= 4.4
BuildRequires:  qscintilla-devel
Requires:       font(liberationmono)
Requires:       font(liberationsans)
Requires:       font(liberationserif)
Recommends:     %{name}-MCAD = %{version}-%{release}

%description
OpenSCAD is a software for creating solid 3D CAD objects.
Unlike most free software for creating 3D models (such as the famous
application Blender) it does not focus on the artistic aspects of 3D
modeling but instead on the CAD aspects. Thus it might be the application
you are looking for when you are planning to create 3D models of machine
parts but pretty sure is not what you are looking for when you are more
interested in creating computer-animated movies.


###############################################
%package        MCAD
Summary:        OpenSCAD Parametric CAD Library
License:        LGPLv2+ and LGPLv2 and LGPLv3+ and (GPLv3 or LGPLv2) and (GPLv3+ or LGPLv2) and (CC-BY-SA or LGPLv2+) and (CC-BY-SA or LGPLv2) and CC-BY and BSD and MIT and Public Domain
URL:            https://www.github.com/openscad/MCAD
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    MCAD
This library contains components commonly used in designing and moching up
mechanical designs. It is currently unfinished and you can expect some API
changes, however many things are already working.

### LICENSES:

##  LGPLv2+:
#   2Dshapes.scad
#   3d_triangle.scad
#   fonts.scad
#   gridbeam.scad
#   hardware.scad
#   libtriangles.scad
#   multiply.scad
#   shapes.scad
#   screw.scad

##  LGPLv2:
#   gears.scad
#   involute_gears.scad
#   servos.scad
#   transformations.scad
#   triangles.scad
#   unregular_shapes.scad
#   bitmap/letter_necklace.scad

##  LGPLv3+:
#   teardrop.scad

##  GPLv3 or LGPLv2:
#   motors.scad
#   nuts_and_bolts.scad


##  GPLv3+ or LGPLv2:
#   metric_fastners.scad
#   regular_shapes.scad

##  CC-BY-SA or LGPLv2+:
#   bearing.scad
#   materials.scad
#   stepper.scad
#   utilities.scad

##  CC-BY-SA or LGPLv2:
#   units.scad

##  CC-BY:
#   polyholes.scad
#   bitmap/alphabet_block.scad
#   bitmap/bitmap.scad
#   bitmap/height_map.scad
#   bitmap/name_tag.scad

## BSD
#   boxes.scad

## MIT
#   constants.scad
#   curves.scad
#   math.scad

## Public Domain
#   lego_compatibility.scad
#   trochoids.scad

###############################################

%prep
%setup -qn %{name}-%{upversion}

# Unbundle polyclipping
rm src/polyclipping -rf
%patch0 -p1

%build
%{qmake_qt4} PREFIX=%{_prefix}
make %{?_smp_mflags}

# tests
cd tests
cmake .
make %{?_smp_mflags}
cd -

%install
make install INSTALL_ROOT=%{buildroot}
rm -rf %{buildroot}%{_datadir}/%{name}/fonts
%find_lang %{name}

rm %{buildroot}%{_datadir}/%{name}/libraries/MCAD/lgpl-2.1.txt
rm %{buildroot}%{_datadir}/%{name}/libraries/MCAD/README.markdown
rm %{buildroot}%{_datadir}/%{name}/libraries/MCAD/TODO

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# tests
cd tests
ctest %{?_smp_mflags} || : # let the tests fail, as they probably won't work in Koji
cd -

%files -f %{name}.lang
%license COPYING
%doc README.md RELEASE_NOTES
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/appdata/*.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/mime/packages/%{name}.xml
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/examples
%{_datadir}/%{name}/color-schemes
%dir %{_datadir}/%{name}/locale
%dir %{_datadir}/%{name}/libraries
%{_mandir}/man1/*

%files MCAD
%license libraries/MCAD/lgpl-2.1.txt
%doc libraries/MCAD/README.markdown libraries/MCAD/TODO
%{_datadir}/%{name}/libraries/MCAD

%changelog
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015.03.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 2015.03.3-10
- Rebuilt for Boost 1.64

* Sun Jun 04 2017 Miro Hrončok <mhroncok@redhat.com> - 2015.03.3-9
- Rebuilt for new CGAL

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.03.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Mon Feb 20 2017 Rex Dieter <rdieter@fedoraproject.org> - 2015.03.3-7
- rebuild (qscintilla)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015.03.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Jonathan Wakely <jwakely@redhat.com> - 2015.03.3-5
- Rebuilt for Boost 1.63

* Tue Jan 10 2017 Miro Hrončok <mhroncok@redhat.com> - 2015.03.3-4
- Rebuilt for new libGLEW.so.2.0

* Wed Dec 28 2016 Rich Mattes <richmattes@gmail.com> - 2015.03.3-3
- Rebuild for eigen3-3.3.1

* Wed Sep 21 2016 Miro Hrončok <mhroncok@redhat.com> - 2015.03.3-2
- Rebuilt for new CGAL 4.9

* Sun Sep 18 2016 Miro Hrončok <mhroncok@redhat.com> - 2015.03.3-1
- New upstream version 2015.03-3
- Recommends MCAD from the main package

* Sun Sep 18 2016 Miro Hrončok <mhroncok@redhat.com> - 2015.03.2-9
- Rebuilt for new polyclipping (#1159525)

* Thu Sep 15 2016 Miro Hrončok <mhroncok@redhat.com> - 2015.03.2-8
- Rebuilt for new opencsg version 1.4.1

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 2015.03.2-7
- Rebuilt for linker errors in boost (#1331983)

* Sun Apr 10 2016 Miro Hrončok <mhroncok@redhat.com> - 2015.03.2-6
- Rebuilt with new gcc, fix FTBFS (#1305220)

* Wed Feb 03 2016 Miro Hrončok <mhroncok@redhat.com> - 2015.03.2-5
- Rebuilt for Boost 1.60 (again?)

* Mon Jan 18 2016 Rex Dieter <rdieter@fedoraproject.org> 2015.03.2-4
- use %%qmake_qt4 macro

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 2015.03.2-3
- Rebuilt for Boost 1.60

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 2015.03.2-2
- Rebuild for glew 1.13

* Thu Nov 19 2015 Miro Hrončok <mhroncok@redhat.com> - 2015.03.2-1
- New upstream version 2015.03-2

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2015.03.1-5
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.03.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2015.03.1-3
- rebuild for Boost 1.58

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.03.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 22 2015 Miro Hrončok <mhroncok@redhat.com> - 2015.03.1-1
- New upstream version 2015.03-1

* Mon Apr 20 2015 Rex Dieter <rdieter@fedoraproject.org> 2015.03-2
- rebuild (qscintilla), BR: qt4-devel

* Tue Mar 17 2015 Miro Hrončok <mhroncok@redhat.com> - 2015.03-1
- New stable version 2015.03§

* Wed Feb 25 2015 Miro Hrončok <mhroncok@redhat.com> - 2015.02-0.2.RC3
- Rebuilt for new CGAL

* Sun Feb 22 2015 Miro Hrončok <mhroncok@redhat.com> - 2015.02-0.1.RC3
- New RC version of 2015.02
- Build MCAD as a subpackage
- Unbundle polyclipping

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 2014.03-7
- Rebuild for boost 1.57.0

* Tue Sep 23 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.03-6
- Rebuilt for OpenCSG 1.4.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 2014.03-3
- rebuild for boost 1.55.0

* Thu May 22 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.03-2
- Rebuilt for opencsg 1.3.3

* Sun Mar 09 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.03-1
- New version

* Fri Dec 27 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.06-8
- Enable Xvfb tests
- Add AppData from upstream git

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
