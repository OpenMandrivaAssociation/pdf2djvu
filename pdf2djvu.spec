%define name	pdf2djvu
%define version	0.5.9
%define release %mkrel 1

Summary: 	PDF to DJVu file converter
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}_%{version}.tar.gz
License:	GPLv2
Group:		Publishing
Url:		http://pdf2djvu.googlecode.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	djvulibre-devel >= 3.5.21, djvulibre >= 3.5.21
BuildRequires:	libpoppler-devel >= 0.7.3
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
%__rm -rf %{buildroot}
%makeinstall
%__install -m 644 -D doc/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING doc/changelog.txt doc/djvudigital.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_datadir}/*/*
