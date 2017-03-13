%{?scl:%scl_package nodejs-write-file-atomic}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-write-file-atomic

%global npm_name write-file-atomic
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-write-file-atomic
Version:    1.1.4
Release:    1%{?dist}
Summary:	Write files in an atomic fashion w/configurable ownership
Url:		https://github.com/iarna/write-file-atomic
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	ISC

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
#BuildRequires:	%{?scl_prefix}npm(require-inject)
BuildRequires:	%{?scl_prefix}npm(tap)
%endif

%description
Write files in an atomic fashion w/configurable ownership

%prep
%setup -q -n package

#%{nodejs_fixdep} graceful-fs
#%{nodejs_fixdep} slide

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check
tap test/*.js
%endif

%files
%{nodejs_sitelib}/write-file-atomic

%doc README.md
%doc LICENSE

%changelog
* Thu Sep 15 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.4-1
- Updated with script

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.2-4
- rebuilt

* Fri Nov 27 2015 Tomas Hrcka <thrcka@redhat.com> - 1.1.2-3
- Enable SCL macros

* Sat May 23 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.2-2
- Added %%nodejs_fixdep macro

* Fri May 22 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.2-1
- Rebuilt with new upstream release
- minor changes

* Thu May 14 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.0-1
- Initial build
