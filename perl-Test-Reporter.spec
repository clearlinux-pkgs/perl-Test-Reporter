#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Reporter
Version  : 1.5203
Release  : 24
URL      : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Test-Reporter-1.5203.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Test-Reporter-1.5203.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtest-reporter-perl/libtest-reporter-perl_1.62-1.debian.tar.xz
Summary  : sends test results to cpan-testers@perl.org
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0 GPL-3.0
Requires: perl-Test-Reporter-bin = %{version}-%{release}
Requires: perl-Test-Reporter-license = %{version}-%{release}
Requires: perl-Test-Reporter-man = %{version}-%{release}
Requires: perl-Test-Reporter-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Test::Reporter - sends test results to cpan-testers@perl.org
SYNOPSIS
use Test::Reporter;

%package bin
Summary: bin components for the perl-Test-Reporter package.
Group: Binaries
Requires: perl-Test-Reporter-license = %{version}-%{release}

%description bin
bin components for the perl-Test-Reporter package.


%package dev
Summary: dev components for the perl-Test-Reporter package.
Group: Development
Requires: perl-Test-Reporter-bin = %{version}-%{release}
Provides: perl-Test-Reporter-devel = %{version}-%{release}
Requires: perl-Test-Reporter = %{version}-%{release}

%description dev
dev components for the perl-Test-Reporter package.


%package license
Summary: license components for the perl-Test-Reporter package.
Group: Default

%description license
license components for the perl-Test-Reporter package.


%package man
Summary: man components for the perl-Test-Reporter package.
Group: Default

%description man
man components for the perl-Test-Reporter package.


%package perl
Summary: perl components for the perl-Test-Reporter package.
Group: Default
Requires: perl-Test-Reporter = %{version}-%{release}

%description perl
perl components for the perl-Test-Reporter package.


%prep
%setup -q -n Test-Reporter-1.5203
cd %{_builddir}
tar xf %{_sourcedir}/libtest-reporter-perl_1.62-1.debian.tar.xz
cd %{_builddir}/Test-Reporter-1.5203
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Test-Reporter-1.5203/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-Reporter
cp %{_builddir}/Test-Reporter-1.5203/COPYING %{buildroot}/usr/share/package-licenses/perl-Test-Reporter/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Test-Reporter/2bd6e6b65d74a94d5be74199808ef3a79f84b64d
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cpantest

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Reporter.3
/usr/share/man/man3/Test::Reporter::Transport.3
/usr/share/man/man3/Test::Reporter::Transport::File.3
/usr/share/man/man3/Test::Reporter::Transport::HTTPGateway.3
/usr/share/man/man3/Test::Reporter::Transport::Mail::Send.3
/usr/share/man/man3/Test::Reporter::Transport::Net::SMTP.3
/usr/share/man/man3/Test::Reporter::Transport::Net::SMTP::TLS.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-Reporter/2bd6e6b65d74a94d5be74199808ef3a79f84b64d
/usr/share/package-licenses/perl-Test-Reporter/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cpantest.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/Test/Reporter.pm
/usr/lib/perl5/vendor_perl/5.30.3/Test/Reporter/Transport.pm
/usr/lib/perl5/vendor_perl/5.30.3/Test/Reporter/Transport/File.pm
/usr/lib/perl5/vendor_perl/5.30.3/Test/Reporter/Transport/HTTPGateway.pm
/usr/lib/perl5/vendor_perl/5.30.3/Test/Reporter/Transport/Mail/Send.pm
/usr/lib/perl5/vendor_perl/5.30.3/Test/Reporter/Transport/Net/SMTP.pm
/usr/lib/perl5/vendor_perl/5.30.3/Test/Reporter/Transport/Net/SMTP/TLS.pm
