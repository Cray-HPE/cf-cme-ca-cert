# Copyright 2020-2021,2023 Hewlett Packard Enterprise Development LP
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# (MIT License)
Name: cf-ca-cert-config-framework
License: MIT
Summary: Cray Configuration Framework CA Cert Ansible Role
Group: System/Management
Version: %(cat .version)
Release: %(echo ${BUILD_METADATA})
Source: %{name}-%{version}.tar.bz2
BuildArch: noarch
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

