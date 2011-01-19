%define perlvendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)

Name: perl-Parse-DebianChangelog
Version: 1.1.1
Release: %mkrel 1
Summary: Perl interface to Debian Changelog
License: GPL
Group: Development/Perl
URL: http://packages.debian.org/source/lenny/libparse-debianchangelog-perl
Source: libparse-debianchangelog-perl_%{version}.orig.tar.gz
BuildRequires: gcc-c++ perl-devel perl-Module-Build perl-Test-Pod-Coverage perl-HTML-Template

%description
A Perl interface to Debian Changelog

%prep
%setup -q -n Parse-DebianChangelog-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

#%check
#./Build test

%install
%{__rm} -rf $RPM_BUILD_ROOT
./Build install destdir=%{buildroot}
find ${RPM_BUILD_ROOT} -type f -name perllocal.pod -o -name .packlist -o -name '*.bs' -a -size 0 | xargs rm -f
find ${RPM_BUILD_ROOT} -type d -depth | xargs rmdir --ignore-fail-on-non-empty

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README 

%{perlvendorlib}/*
%{_mandir}/man3/*
%{_mandir}/de/man3/*
/usr/share/locale/de/LC_MESSAGES/Parse-DebianChangelog*
%{_mandir}/man1/*
%{_bindir}/parsechangelog

%changelog
