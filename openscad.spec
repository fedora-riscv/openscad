Name:           openscad
%global shortversion %(date +%Y).%(date +%m)
Version:        %{shortversion}
Release:        0.90.20141224git32c3e0d3%{?dist}
Summary:        The Programmers Solid 3D CAD Modeller
# COPYING contains a linking exception for CGAL
# Appdata file is CC0
License:        GPLv2 with exceptions and CC0
Group:          Applications/Engineering
URL:            http://www.openscad.org/
Source0:        openscad-devel-32c3e0d3.tar
Source1:        MCAD-master.zip
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
BuildRequires:  procps-ng
BuildRequires:  python2
BuildRequires:  qt-devel >= 4.4
BuildRequires:  qscintilla-devel
Requires:       font(liberationmono)
Requires:       font(liberationsans)
Requires:       font(liberationserif)

%description
OpenSCAD is a software for creating solid 3D CAD objects.
Unlike most free software for creating 3D models (such as the famous
application Blender) it does not focus on the artistic aspects of 3D
modeling but instead on the CAD aspects. Thus it might be the application
you are looking for when you are planning to create 3D models of machine
parts but pretty sure is not what you are looking for when you are more
interested in creating computer-animated movies.

%prep
%setup -qa1 -Tcn %{name}-devel/libraries
mv MCAD{-master,}
%setup -Dqn %{name}-devel

%build
qmake-qt4 VERSION=%{shortversion} PREFIX=%{_prefix}
make %{?_smp_mflags}

# tests
cd tests
OPENSCAD_UPLOAD_TESTS=yes cmake .
make %{?_smp_mflags}
cd -

%install
make install INSTALL_ROOT=%{buildroot}
rm -rf %{buildroot}%{_datadir}/%{name}/fonts
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# tests
cd tests
ctest %{?_smp_mflags} -C All || : # let the tests fail, as they probably won't work in Koji
cd -

# remove MCAD (separate package) after the tests
rm -rf %{buildroot}%{_datadir}/%{name}/libraries/MCAD

%files -f %{name}.lang
%doc COPYING README.md RELEASE_NOTES
%attr(755,root,root) %{_bindir}/%{name}
%if 0%{?fedora} < 21
%{_datadir}/appdata
%else
%{_datadir}/appdata/*.xml
%endif
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/%{name}
%{_mandir}/man1/*

%changelog
* Wed Dec 24 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.12-0.90.20141224git32c3e0d3
- Update to git: 32c3e0d3

* Tue Dec 23 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.12-0.89.20141223gitd071ba16
- Update to git: d071ba16

* Mon Dec 22 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.12-0.88.20141222git594f548b
- Update to git: 594f548b

* Sun Dec 21 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.12-0.87.20141221gitabdf80c4
- Update to git: abdf80c4

* Sat Dec 20 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.12-0.86.20141220gitb1871c63
- Update to git: b1871c63

* Thu Dec 18 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.12-0.85.20141218gitf42dbea8
- Update to git: f42dbea8

* Wed Dec 17 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.12-0.84.20141217git3d0749b6
- Update to git: 3d0749b6

* Sat Dec 13 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.12-0.83.20141213git14870d69
- Update to git: 14870d69

* Fri Dec 12 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.12-0.82.20141212gitad69698f
- Update to git: ad69698f

* Wed Dec 10 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.12-0.81.20141210git73b6700b
- Update to git: 73b6700b

* Tue Dec 09 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.12-0.80.20141209git7e728fac
- Update to git: 7e728fac

* Tue Dec 09 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.12-0.79.20141209git24627996
- Update to git: 24627996

* Mon Dec 08 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.12-0.78.20141208gitccea6fdd
- Update to git: ccea6fdd

* Sun Dec 07 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.12-0.77.20141207git771526b5
- Update to git: 771526b5

* Sat Dec 06 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.12-0.76.20141206git50e79a68
- Update to git: 50e79a68

* Fri Dec 05 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.12-0.75.20141205git092b9eed
- Update to git: 092b9eed

* Thu Dec 04 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.12-0.74.20141204git8b9559a2
- Update to git: 8b9559a2

* Tue Dec 02 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.12-0.73.20141202gita59e7d65
- Update to git: a59e7d65

* Sun Nov 30 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.11-0.72.20141130git471ff771
- Update to git: 471ff771

* Fri Nov 28 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.11-0.71.20141128gitcf418188
- Update to git: cf418188

* Wed Nov 26 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.11-0.70.20141126gitecbaec08
- Update to git: ecbaec08

* Tue Nov 25 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.11-0.69.20141125git6b61e9b1
- Update to git: 6b61e9b1

* Mon Nov 17 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.11-0.68.20141117gitef262f62
- Update to git: ef262f62

* Sun Nov 16 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.11-0.67.20141116git1263042f
- Update to git: 1263042f

* Sat Nov 15 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.11-0.66.20141115gitc16284ab
- Update to git: c16284ab

* Wed Nov 12 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.11-0.65.20141112git1d9b664e
- Update to git: 1d9b664e

* Tue Nov 11 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.11-0.64.20141111git43221a78
- Update to git: 43221a78

* Sun Nov 09 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.11-0.63.20141109git31b90d1a
- Update to git: 31b90d1a

* Sat Nov 08 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.11-0.62.20141108git03ac0458
- Update to git: 03ac0458

* Fri Nov 07 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.11-0.61.20141107git28d7d545
- Update to git: 28d7d545

* Thu Nov 06 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.11-0.60.20141106git92389b85
- Update to git: 92389b85

* Mon Nov 03 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.11-0.59.20141103git4306586a
- Update to git: 4306586a

* Sun Nov 02 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.11-0.58.20141102git5078f401
- Update to git: 5078f401

* Fri Oct 31 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.10-0.57.20141031gita68b39ea
- Update to git: a68b39ea

* Wed Oct 22 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.10-0.56.20141022git346fc362
- Update to git: 346fc362

* Mon Oct 20 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.10-0.55.20141020git0e88cfda
- Update to git: 0e88cfda

* Sun Oct 19 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.10-0.54.20141019gitb66fb597
- Update to git: b66fb597

* Sat Oct 18 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.10-0.53.20141018git8d7d854e
- Update to git: 8d7d854e

* Wed Oct 15 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.10-0.52.20141015gitf7b15e92
- Update to git: f7b15e92

* Tue Oct 14 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.10-0.51.20141014gita7eab14c
- Update to git: a7eab14c

* Sun Oct 12 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.10-0.50.20141012git1cc4f6be
- Update to git: 1cc4f6be

* Sat Oct 11 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.10-0.49.20141011git3dca2873
- Update to git: 3dca2873

* Fri Oct 03 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.10-0.48.20141003git428cf27a
- Update to git: 428cf27a

* Wed Oct 01 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.10-0.47.20141001git8eff7ed3
- Update to git: 8eff7ed3

* Wed Oct 01 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.10-0.46.20141001git6d81c37e
- Drop fonts and require them instead

* Wed Oct 01 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.10-0.45.20141001git6d81c37e
- Update to git: 6d81c37e

* Wed Sep 24 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.09-0.44.20140924gitf98d5657
- Update to git: f98d5657

* Mon Sep 22 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.09-0.43.20140922git4eb53d33
- Update to git: 4eb53d33

* Sun Sep 21 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.09-0.42.20140921git8d067fe3
- Update to git: 8d067fe3

* Sat Sep 20 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.09-0.41.20140920gitecc5622e
- Update to git: ecc5622e

* Wed Sep 17 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.09-0.40.20140917gite1fd9c83
- Update to git: e1fd9c83

* Tue Sep 16 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.09-0.39.20140916git988333ab
- Update to git: 988333ab

* Sat Sep 06 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.09-0.38.20140906git5252bae1
- Update to git: 5252bae1

* Fri Sep 05 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.09-0.37.20140905git771f7645
- Update to git: 771f7645

* Thu Sep 04 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.09-0.36.20140904gitc4485cfd
- Update to git: c4485cfd

* Sun Aug 31 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.08-0.35.20140831git89201c91
- Update to git: 89201c91

* Fri Aug 29 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.08-0.34.20140829gitf1f4e4c7
- Update to git: f1f4e4c7

* Thu Aug 28 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.08-0.33.20140828git0f945013
- Update to git: 0f945013

* Wed Aug 27 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.08-0.32.20140827gitabd14b62
- Update to git: abd14b62

* Tue Aug 26 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.08-0.31.20140826gitc4d3f221
- Update to git: c4d3f221

* Mon Aug 25 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.08-0.30.20140825gitb05a8eb0
- Update to git: b05a8eb0

* Sat Aug 23 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.08-0.29.20140823git574fbf97
- Update to git: 574fbf97

* Fri Aug 22 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.08-0.28.20140822git724fbbab
- Update to git: 724fbbab

* Thu Aug 21 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.08-0.27.20140821git3e5df1a9
- Update to git: 3e5df1a9

* Wed Aug 20 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.08-0.26.20140820git4f4bf2b0
- Update to git: 4f4bf2b0

* Tue Aug 19 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.08-0.25.20140819git4a1962cb
- Update to git: 4a1962cb

* Mon Aug 18 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.08-0.24.20140818gite975ac38
- Update to git: e975ac38

* Sat Aug 16 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.08-0.23.20140816gitc01ea899
- Update to git: c01ea899

* Fri Aug 15 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.08-0.22.20140815git717ff3b1
- Update to git: 717ff3b1

* Mon Aug 11 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.08-0.21.20140811giteabd27dd
- Update to git: eabd27dd

* Mon Aug 04 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.08-0.20.20140804gitfde73a4b
- Update to git: fde73a4b

* Fri Jul 25 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.07-0.19.20140725git9c1bb008
- Update to git: 9c1bb008

* Thu Jul 24 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.07-0.18.20140724git1c690dfe
- Update to git: 1c690dfe

* Wed Jul 23 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.07-0.17.20140723gitb3d094a6
- Update to git: b3d094a6

* Fri Jul 18 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.07-0.16.20140718git0852e707
- Update to git: 0852e707

* Sun Jul 13 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.07-0.15.20140713git247479ca
- Update to git: 247479ca

* Wed Jul 09 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.07-0.14.20140709gitd8c32584
- Update to git: d8c32584

* Tue Jul 08 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.07-0.13.20140708gitc47ba7c8
- Update to git: c47ba7c8

* Mon Jul 07 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.07-0.12.20140707gitb9f20780
- Update to git: b9f20780

* Sun Jul 06 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.07-0.11.20140706git57c52e93
- Update to git: 57c52e93

* Sat Jun 28 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.06-0.10.20140628git9fdc44b0
- Update to git: 9fdc44b0

* Wed Jun 25 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.06-0.9.20140625gitd9fda460
- Update to git: d9fda460

* Mon Jun 23 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.06-0.8.20140623git681f03a2
- Update to git: 681f03a2

* Wed Jun 18 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.06-0.7.20140618git48e1d6a5
- Update to git: 48e1d6a5

* Tue Jun 10 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.06-0.6.20140610git05e2a1ed
- Update to git: 05e2a1ed

* Sun Jun 08 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.06-0.5.20140608gitdb22a019
- Update to git: db22a019

* Fri Jun 06 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.06-0.4.20140606gitacd6cb1a
- Update to git: acd6cb1a

* Wed Jun 04 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.06-0.3.20140604git78803bfe
- Update to git: 78803bfe

* Fri May 30 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.05-0.2.20140530gitca3ff7cf
- Update to git: ca3ff7cf

* Thu May 29 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.05-0.1.20140529git380af79b
- Update to git: 380af79b

* Mon Mar 03 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.03-0.1.201400303git8635e94
- Latest RC

* Fri Feb 28 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.02-0.4.20140228gitb2fbad4
- 2014.03 RC new commits

* Thu Feb 27 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.02-0.3.20140227gitbc86c49
- 2014.03 RC new commits

* Wed Feb 26 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.02-0.2.20140225git341571c
- 2014.03 RC

* Sat Feb 22 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.02-0.1.20140222git6867c50
- New commit

* Wed Jan 29 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.01-0.3.20140127git41f4575
- New commit
- Upload test results
- Don't cat the results to the log

* Mon Jan 27 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.01-0.2.20140124gitd9432d7
- New commit

* Sun Jan 12 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.01-0.1.20140108gite6bfee0
- New commit
- New month

* Mon Dec 30 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.12-0.6.20131229gitbf19347
- New commit

* Tue Dec 24 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.12-0.5.20131223git41ab9e8
- New commit
- Manpage and appdata now installed with make install

* Mon Dec 23 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.12-0.4.20131217git6938ae2
- Include appdata in the RPM

* Thu Dec 19 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.12-0.3.20131217git6938ae2
- Development version

* Tue Dec 17 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.12-0.2.20131215gite64bf96
- Development version
- Added BRs for virtual framebuffer

* Tue Oct 29 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.10-0.1.20131029git8aa749f
- Development version

* Fri Jun 07 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.06-0.1rc1
- New version RC

* Sun Jan 27 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.01.17-3
- Use Xvfb

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
