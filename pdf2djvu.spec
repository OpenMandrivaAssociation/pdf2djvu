Summary: 	PDF to DJVu file converter
Name:		pdf2djvu
Version:	0.9.13
Release:	1
Source0:	https://github.com/jwilk/pdf2djvu/releases/download/%{version}/%{name}-%{version}.tar.xz
License:	GPLv2
Group:		Publishing
Url:		http://jwilk.net/software/pdf2djvu
BuildRequires:	djvulibre-devel >= 3.5.21
BuildRequires:	djvulibre >= 3.5.21
BuildRequires:	poppler-devel >= 0.7.3
BuildRequires:	libgomp-devel
BuildRequires:	libxslt-devel
BuildRequires:	graphicsmagick-devel

%description
pdf2djvu creates DjVu files from PDF files. It's able to extract
graphics, text layer, hyperlinks, document outline (bookmarks), and
metadata.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall
%__install -m 644 -D doc/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%find_lang %{name}

%files -f %{name}.lang
%doc doc/COPYING doc/changelog doc/credits doc/djvudigital
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_mandir}/*/man1/%{name}.1.*



%changelog
* Fri Jul 13 2012 Lev Givon <lev@mandriva.org> 0.7.13-1
+ Revision: 809215
- Update to 0.7.13.

* Mon Jan 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.7.12-2
+ Revision: 767411
- release bump
- files listed twice fix
- version update 0.7.12

* Wed Oct 26 2011 Lev Givon <lev@mandriva.org> 0.7.11-1
+ Revision: 707424
- Update to 0.7.11.

* Mon Aug 22 2011 Lev Givon <lev@mandriva.org> 0.7.10-1
+ Revision: 696168
- Update to 0.7.10.

* Thu Jul 28 2011 Lev Givon <lev@mandriva.org> 0.7.8-1
+ Revision: 692096
- Update to 0.7.8.

* Mon Apr 04 2011 Lev Givon <lev@mandriva.org> 0.7.7-1
+ Revision: 650402
- Update to 0.7.7.

* Fri Mar 11 2011 Funda Wang <fwang@mandriva.org> 0.7.6-2
+ Revision: 643741
- rebuild for new poppler

* Mon Feb 21 2011 Lev Givon <lev@mandriva.org> 0.7.6-1
+ Revision: 639160
- Update to 0.7.6.

* Thu Dec 30 2010 Funda Wang <fwang@mandriva.org> 0.7.4-3mdv2011.0
+ Revision: 626151
- rebuild for new poppler

* Sun Aug 22 2010 Funda Wang <fwang@mandriva.org> 0.7.4-2mdv2011.0
+ Revision: 571799
- rebuild for new poppler

* Mon Jun 14 2010 Lev Givon <lev@mandriva.org> 0.7.4-1mdv2011.0
+ Revision: 548004
- Update to 0.7.4.
  Enable multithreading (#59764).

* Wed Apr 21 2010 Lev Givon <lev@mandriva.org> 0.7.1-1mdv2010.1
+ Revision: 537641
- Update to 0.7.1.

* Mon Mar 01 2010 Frederik Himpe <fhimpe@mandriva.org> 0.7.0-1mdv2010.1
+ Revision: 513071
- update to new version 0.7.0

* Tue Jan 19 2010 Lev Givon <lev@mandriva.org> 0.6.2-1mdv2010.1
+ Revision: 493667
- Update to 0.6.2.

* Thu Oct 01 2009 Frederik Himpe <fhimpe@mandriva.org> 0.6.0-1mdv2010.0
+ Revision: 452308
- update to new version 0.6.0

* Fri Jul 31 2009 Frederik Himpe <fhimpe@mandriva.org> 0.5.11-1mdv2010.0
+ Revision: 405213
- Update to new version 0.5.11

* Tue Jul 07 2009 Lev Givon <lev@mandriva.org> 0.5.9-1mdv2010.0
+ Revision: 393364
- Update to 0.5.9.

* Tue May 19 2009 Götz Waschk <waschk@mandriva.org> 0.5.7-2mdv2010.0
+ Revision: 377488
- rebuild for new poppler

* Thu May 14 2009 Lev Givon <lev@mandriva.org> 0.5.7-1mdv2010.0
+ Revision: 375846
- imported package pdf2djvu


