# Copyright 2020 Hewlett Packard Enterprise Development LP
Name: cf-ca-cert-config-framework
License: Cray Software License Agreement
Summary: Cray Configuration Framework CA Cert Ansible Role
Group: System/Management
Version: %(cat .rpm_version)
Release: %(echo ${BUILD_METADATA})
Source: %{name}-%{version}.tar.bz2
Vendor: Cray Inc.

%description
An Ansible play and role to make a Cray provided CA certificate a trusted
certificate for Cray products

%define cf_base_dir /opt/cray/ansible/

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{cf_base_dir}/roles/
cp -r ansible/roles/* %{buildroot}%{cf_base_dir}/roles/

%clean
rm -rf %{buildroot}%{cf_base_dir}
rm -f  %{buildroot}%{cf_base_dir}/*

%files
%defattr(-,root,root)
%{cf_base_dir}/roles/ca-cert

%changelog

