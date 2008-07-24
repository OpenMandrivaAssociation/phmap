Summary:	A war dialer
Name:		phmap
Version:	1.0
Release:	%mkrel 8
Group:		Monitoring
License:	GPL
URL:		http://www.atnum.com/~sephail/devel/proj/phmap.htm
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Phmap is a "war dialer" used for detecting which phone numbers in
a list have an active carrier signal. An example use of this
program is detecting which local BBS servers still exist.

%prep

%setup -q -n %{name}-%{version}

%build

%make CFLAGS="%{optflags}"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m755 %{name} %{buildroot}%{_bindir}/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
