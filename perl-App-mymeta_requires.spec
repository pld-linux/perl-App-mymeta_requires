#
# Conditional build:
%bcond_with	tests	# do not perform "make test"

%define		pdir	App
%define		pnam	mymeta_requires
Summary:	Extract module requirements from MYMETA files
Name:		perl-App-mymeta_requires
Version:	0.005
Release:	1
License:	Apache v2.0
Group:		Development/Libraries
Source0:	http://www.cpan.org/authors/id/D/DA/DAGOLDEN/App-mymeta_requires-%{version}.tar.gz
# Source0-md5:	c190c987df9bfd6da75a17b108678e2e
URL:		http://search.cpan.org/dist/App-mymeta_requires/
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	rpm-perlprov >= 4.1-13
# Run-time:
BuildRequires:	perl(CPAN::Meta)
BuildRequires:	perl(CPAN::Meta::Requirements)
BuildRequires:	perl(Class::Load)
BuildRequires:	perl(File::Basename)
#BuildRequires:	perl(Getopt::Lucid)
#BuildRequires:	perl(Log::Dispatchouli)
#BuildRequires:	perl(Object::Tiny)
BuildRequires:	perl(Pod::Usage)
BuildRequires:	perl(autodie) >= 2.00
%if %{with tests}
# Tests
BuildRequires:	perl(Capture::Tiny)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(File::pushd)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::More) >= 0.92
# Optional tests:
BuildRequires:	perl(Test::Script) >= 1.05
%endif
Requires:	perl(File::Basename)
Requires:	perl(Pod::Usage)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This tool extracts CPAN module requirements as recorded in a
MYMETA.json or MYMETA.yml file.

%prep
%setup -q -n App-mymeta_requires-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README
%attr(755,root,root) %{_bindir}/mymeta-requires
%{_mandir}/man1/mymeta-requires.1p*
%{_mandir}/man3/App::mymeta_requires.3pm*
%{perl_vendorlib}/App/mymeta_requires.pm
