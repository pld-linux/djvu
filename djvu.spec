Summary:	DjVu Reference Library
Summary(pl):	Biblioteka do obs³ugi formatu DjVu
Name:		djvu
Version:	3.0
%define		snap	20010511
Release:	0.%{snap}
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
License:	GPL
Source0:	http://www.lizardtech.com/software/djvureferencelibrary/version3/DjVu%{version}.snapshot-%{snap}.src.tar.gz
Patch0:		%{name}-config.patch
Patch1:		%{name}-libjpeg.patch
URL:		http://www.djvu.att.com/
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DjVu Reference Library.

%description -l pl
Biblioteka do obs³ugi formatu DjVu.

%package devel
Summary:	DjVu Reference Library development package
Summary(pl):	Biblioteka DjVu dla programistów
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
# doesn't require base

%description devel
DjVu Reference Library - static library and header files.

%description devel -l pl
Biblioteka DjVu - biblioteka statyczna i pliki nag³ówkowe.

%prep
%setup -q -n DjVu3
%patch0 -p1
%patch1 -p1

%build
OPT="%{rpmcflags}"
%ifarch i586 i686
OPT="$OPT -DMMX"
%endif
# uses exceptions and implicit templactes
OPTXX="$OPT"
export OPT OPTXX
./configure --with-threads=posix
cd build/linux-libc6/configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}

install build/linux-libc6/configure/bin/* $RPM_BUILD_ROOT%{_bindir}
install build/linux-libc6/configure/lib/*.a $RPM_BUILD_ROOT%{_libdir}
install src/include/*.h $RPM_BUILD_ROOT%{_includedir}

gzip -9nf README.txt Samples/README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Doc Samples *.gz
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_includedir}/*.h
