Name:           lang-la
Version:        1.0
Release:        1%{?dist}
Summary:        Latin (la_VA) locale data for glibc
License:        LGPL-2.1-or-later
URL:            https://github.com/imbev/lang-la
Source0:        la_VA
BuildRequires:  glibc-common
BuildRequires:  glibc-locale-source
Requires:       glibc-common
Requires:       glibc-locale-source

%description
Latin (la_VA) locale data for glibc.

%prep
cp %{SOURCE0} la_VA

%install
mkdir -p %{buildroot}%{_prefix}/lib/locale
localedef -c -f UTF-8 -i la_VA %{buildroot}%{_prefix}/lib/locale/la_VA.UTF-8
install -Dpm0644 la_VA %{buildroot}%{_datadir}/lang-la/la_VA
ln -s la_VA.UTF-8 %{buildroot}%{_prefix}/lib/locale/la
ln -s la_VA.UTF-8 %{buildroot}%{_prefix}/lib/locale/la.UTF-8

%check
LOCPATH=%{buildroot}%{_prefix}/lib/locale LC_ALL=la_VA.UTF-8 \
    locale -k LC_TIME | grep -q 'abday="Dom;'

%triggerin -- glibc, glibc-common, glibc-locale-source
loc=%{_prefix}/lib/locale/la_VA.UTF-8
rm -rf "$loc.new"
if %{_bindir}/localedef -c -f UTF-8 -i %{_datadir}/lang-la/la_VA "$loc.new"; then
    rm -rf "$loc"
    mv "$loc.new" "$loc"
else
    rm -rf "$loc.new"
fi

%postun
if [ $1 -eq 0 ]; then
    rm -rf %{_prefix}/lib/locale/la_VA.UTF-8
fi

%files
%dir %{_datadir}/lang-la
%{_datadir}/lang-la/la_VA
%dir %{_prefix}/lib/locale/la_VA.UTF-8
%dir %{_prefix}/lib/locale/la_VA.UTF-8/LC_MESSAGES
%{_prefix}/lib/locale/la_VA.UTF-8/LC_ADDRESS
%{_prefix}/lib/locale/la_VA.UTF-8/LC_COLLATE
%{_prefix}/lib/locale/la_VA.UTF-8/LC_CTYPE
%{_prefix}/lib/locale/la_VA.UTF-8/LC_IDENTIFICATION
%{_prefix}/lib/locale/la_VA.UTF-8/LC_MEASUREMENT
%{_prefix}/lib/locale/la_VA.UTF-8/LC_MESSAGES/SYS_LC_MESSAGES
%{_prefix}/lib/locale/la_VA.UTF-8/LC_MONETARY
%{_prefix}/lib/locale/la_VA.UTF-8/LC_NAME
%{_prefix}/lib/locale/la_VA.UTF-8/LC_NUMERIC
%{_prefix}/lib/locale/la_VA.UTF-8/LC_PAPER
%{_prefix}/lib/locale/la_VA.UTF-8/LC_TELEPHONE
%{_prefix}/lib/locale/la_VA.UTF-8/LC_TIME
%{_prefix}/lib/locale/la
%{_prefix}/lib/locale/la.UTF-8

%changelog
* Sun Nov 15 2026 Isaac Beverly <imbev@protonmail.com> - 1.0-1
- Initial package
