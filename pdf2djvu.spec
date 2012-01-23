%define name	pdf2djvu
%define version	0.7.12
%define release %mkrel 1

Summary: 	PDF to DJVu file converter
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pdf2djvu.googlecode.com/files/%{name}_%{version}.tar.gz
License:	GPLv2
Group:		Publishing
Url:		http://pdf2djvu.googlecode.com/
BuildRequires:	djvulibre-devel >= 3.5.21, djvulibre >= 3.5.21
BuildRequires:	libpoppler-devel >= 0.7.3, libgomp-devel
BuildRequires:	libxslt-devel, graphicsmagick-devel

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
%doc COPYING doc/changelog doc/credits.txt doc/djvudigital.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_mandir}/ru/man1/%{name}.1.*
%{_mandir}/de/man1/%{name}.1.*
%{_mandir}/pl/man1/%{name}.1.*
