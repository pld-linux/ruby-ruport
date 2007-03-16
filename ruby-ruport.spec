Summary:	Reporting system for Ruby
Summary(pl.UTF-8):	System raportujący dla języka Ruby
Name:		ruby-ruport
Version:	0.8.99.581
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	ruport-%{version}.tar.gz
# Source0-md5:	dd5be28578bcfd01e416f4b257503f02
URL:		http://code.rubyreports.org/
BuildRequires:	rake
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb = 3.3.1
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby Reports, a simple and extensible reporting system for Ruby. A
lightweight toolset to help you develop your reporting applications
and keep things DRY, Ruport can help.

%description -l pl.UTF-8
Ruby Reports to prosty, rozszerzalny system raportujący dla języka
Ruby. Zestaw lekkich narzędzi pomagających rozwijać aplikacje
generujące raporty, zaprojektowany w myśl filozofii DRY.

%prep
%setup -q -n ruport-%{version}
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%attr(755,root,root) %{_bindir}/rope
%{ruby_rubylibdir}/ruport
%{ruby_rubylibdir}/*.rb
%{ruby_ridir}/Ruport
