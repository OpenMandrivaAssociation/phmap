Summary:	A war dialer
Name:		phmap
Version:	1.0
Release:	11
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


%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0-10mdv2010.0
+ Revision: 430686
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0-9mdv2009.0
+ Revision: 258965
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0-8mdv2009.0
+ Revision: 246858
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.0-6mdv2008.1
+ Revision: 136373
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Aug 19 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-6mdv2008.0
+ Revision: 66670
- Import phmap



* Fri Jul 14 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-6mdv2007.0
- rebuild

* Fri Jun 03 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0-5mdk
- rebuild

* Sun May 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0-4mdk
- new url

* Thu Jan 16 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.0-3mdk
- build release

* Sun Nov 03 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.0-2mdk
- argh!, gotta lint it before uploading...

* Sun Nov 03 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.0-1mdk
- initial cooker contrib
