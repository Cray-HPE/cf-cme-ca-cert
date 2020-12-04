# Copyright 2020 HPED LP
Name: cf-ca-cert
License: Cray Software License Agreement
Summary: Cray Configuration Framework CA Cert Ansible Role
Group: System/Management
Version: %(cat .rpm_version)
Release: %(echo ${BUILD_METADATA})
Source: %{name}-%{version}.tar.bz2
Vendor: Cray Inc.

%description
An Ansible play and role to make a Cray provided CA certificate a trusted
certificate for Cray products.

%package crayctldeploy
Summary: Cray Configuration Framework CA Cert Ansible Role (NCN version)
Requires: cme-premium-cf-crayctldeploy
BuildRequires: cme-premium-cf-crayctldeploy-buildmacro

%description crayctldeploy
An Ansible play and role to make a Cray provided CA certificate a trusted
certificate for Cray products

%package config-framework
Summary: Cray Configuration Framework CA Cert Ansible Role (CF version)

%description config-framework
An Ansible play and role to make a Cray provided CA certificate a trusted
certificate for Cray products

%define cf_base_dir /opt/cray/ansible/

%prep
%setup -q

%build

%install
install -D -m 644 ansible/ca-cert.yml %{buildroot}%{cme_premium_plays_dir}/ca-cert.yml
mkdir -p %{buildroot}%{cme_premium_roles_dir}
cp -r ansible/roles/* %{buildroot}%{cme_premium_roles_dir}/

mkdir -p %{buildroot}%{cf_base_dir}/roles/
cp -r ansible/roles/* %{buildroot}%{cf_base_dir}/roles/

%clean
rm -rf %{buildroot}%{cme_premium_roles_dir}
rm -f  %{buildroot}%{cme_premium_plays_dir}/*
rm -rf %{buildroot}%{cf_base_dir}
rm -f  %{buildroot}%{cf_base_dir}/*

%files crayctldeploy
%defattr(-,root,root)
%{cme_premium_roles_dir}/ca-cert
%{cme_premium_plays_dir}/ca-cert.yml

%files config-framework
%defattr(-,root,root)
%{cf_base_dir}/roles/ca-cert

%changelog

