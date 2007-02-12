Summary:	DjVu Reference Library
Summary(pl.UTF-8):	Biblioteka do obsługi formatu DjVu
Name:		djvu
Version:	3.0
%define		snap	20010511
Release:	0.%{snap}.1
License:	GPL
Group:		Libraries
Source0:	http://www.lizardtech.com/software/djvureferencelibrary/version3/DjVu%{version}.snapshot-%{snap}.src.tar.gz
# Source0-md5:	959742232203df8cbeaa210ce4623bba
Patch0:		%{name}-config.patch
Patch1:		%{name}-libjpeg.patch
URL:		http://www.djvu.att.com/
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DjVu Reference Library.

%description -l pl.UTF-8
Biblioteka do obsługi formatu DjVu.

%package devel
Summary:	DjVu Reference Library development package
Summary(pl.UTF-8):	Biblioteka DjVu dla programistów
Group:		Development/Libraries

%description devel
DjVu Reference Library - static library and header files.

%description devel -l pl.UTF-8
Biblioteka DjVu - biblioteka statyczna i pliki nagłówkowe.

%prep
%setup -q -n DjVu3
%patch0 -p1
%patch1 -p1

%build
OPT="%{rpmcflags}"
%ifarch %{ix86}
%ifnarch i386 i486
OPT="$OPT -DMMX"
%endif
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Doc Samples README.txt
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_includedir}/*.h
