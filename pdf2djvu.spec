Summary: 	PDF to DJVu file converter
Name:		pdf2djvu
Version:	0.9.18.2
Release:	4
Source0:	https://github.com/jwilk/pdf2djvu/releases/download/%{version}/%{name}-%{version}.tar.xz
License:	GPLv2
Group:		Publishing
Url:		http://jwilk.net/software/pdf2djvu
BuildRequires:	djvulibre-devel >= 3.5.21
BuildRequires:	djvulibre >= 3.5.21
BuildRequires:	poppler-devel >= 0.7.3
BuildRequires:	libgomp-devel
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	graphicsmagick-devel

%description
pdf2djvu creates DjVu files from PDF files. It's able to extract
graphics, text layer, hyperlinks, document outline (bookmarks), and
metadata.

%prep
%autosetup -p1
CXXFLAGS="%{optflags} -std=gnu++20" \
%configure

%build
%make_build

%install
%make_install
%__install -m 644 -D doc/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%find_lang %{name}

%files -f %{name}.lang
%doc doc/COPYING doc/changelog doc/credits doc/djvudigital
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/*/man1/%{name}.1*
