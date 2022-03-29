
%global srcname tripleo_operator_ansible
%global collectionname tripleo-operator-ansible

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           %{collectionname}
Version:        0.5.1
Release:        1%{?dist}
Summary:        Ansible Collection to perform TripleO related actions.

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://opendev.org/openstack/tripleo-operator-ansible
Source0:        https://tarballs.openstack.org/%{collectionname}/%{collectionname}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr

Requires: (python3dist(ansible) or ansible-core >= 2.11)

%description

Ansible Collection to perform TripleO related actions

%prep
%autosetup -n %{collectionname}-%{upstream_version} -S git


%build
%py3_build


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%py3_install


%files
%doc README*
%license LICENSE
%{python3_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/collections/ansible_collections/tripleo/operator/


%changelog
* Thu Jun 24 2021 Chandan Kumar (raukadah) <chkumar@redhat.com> 0.5.1-1
- Update to 0.5.1
# REMOVEME: error caused by commit https://opendev.org/openstack/tripleo-operator-ansible/commit/9b63299bed7e68120ce00c3196c07a71514d2121
