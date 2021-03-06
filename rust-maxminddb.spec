# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate maxminddb

%global testdata_commit 6e99232bb6a70d5169ecc96ed0614a52017ff654

Name:           rust-%{crate}
Version:        0.13.0
Release:        2%{?dist}
Summary:        Library for reading MaxMind DB format used by GeoIP2 and GeoLite2

# Upstream license specification: ISC
License:        ISC
URL:            https://crates.io/crates/maxminddb
Source:         %{crates_source}
Source1:        https://github.com/maxmind/MaxMind-DB/archive/%{testdata_commit}/test-data.tar.gz

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Library for reading MaxMind DB format used by GeoIP2 and GeoLite2.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+memmap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+memmap-devel %{_description}

This package contains library source intended for building other packages
which use "memmap" feature of "%{crate}" crate.

%files       -n %{name}+memmap-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+mmap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+mmap-devel %{_description}

This package contains library source intended for building other packages
which use "mmap" feature of "%{crate}" crate.

%files       -n %{name}+mmap-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1 -a1
mv MaxMind-DB-%{testdata_commit} test-data
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 14:36:11 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.13.0-1
- Initial package
