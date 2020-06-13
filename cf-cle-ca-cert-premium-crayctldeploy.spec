# Copyright 2019 Cray Inc. All Rights Reserved.
Name: cf-cle-ca-cert-premium-crayctldeploy
License: Cray Software License Agreement
Summary: Cray Managed Ecosystem Ansible CA Cert role
Group: System/Management
Version: %(cat .rpm_version)
Release: %(echo ${BUILD_METADATA})
Source: %{name}-%{version}.tar.bz2
Vendor: Cray Inc.
Requires: cme-premium-cf-crayctldeploy
BuildRequires: cme-premium-cf-crayctldeploy-buildmacro

%description
An Ansible play and role to make a Cray provided CA certificate a trusted 
certificate for Cray Managed Ecosystem products.

%prep
%setup -q

%build

%install
install -D -m 644 ansible/ca-cert.yml %{buildroot}%{cme_premium_plays_dir}/ca-cert.yml
mkdir -p %{buildroot}%{cme_premium_roles_dir}
cp -r ansible/roles/* %{buildroot}%{cme_premium_roles_dir}/

%clean
rm -rf %{buildroot}%{cme_premium_roles_dir}
rm -f  %{buildroot}%{cme_premium_plays_dir}/*

%files
%defattr(-,root,root)
%{cme_premium_roles_dir}/ca-cert
%{cme_premium_plays_dir}/ca-cert.yml

%changelog

