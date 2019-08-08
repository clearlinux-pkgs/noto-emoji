#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : noto-emoji
Version  : 2018.08.10.unicode11
Release  : 7
URL      : http://localhost/cgit/projects/noto-emoji/snapshot/noto-emoji-2018-08-10-unicode11.tar.xz
Source0  : http://localhost/cgit/projects/noto-emoji/snapshot/noto-emoji-2018-08-10-unicode11.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : OFL-1.1
Requires: noto-emoji-data = %{version}-%{release}
Requires: noto-emoji-license = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the noto-emoji package.
Group: Data

%description data
data components for the noto-emoji package.


%package license
Summary: license components for the noto-emoji package.
Group: Default

%description license
license components for the noto-emoji package.


%prep
%setup -q -n noto-emoji-2018-08-10-unicode11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565278867
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1565278867
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/noto-emoji
cp LICENSE %{buildroot}/usr/share/package-licenses/noto-emoji/LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/fonts/noto-emoji/NotoColorEmoji.ttf
/usr/share/fonts/noto-emoji/NotoEmoji-Regular.ttf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/noto-emoji/LICENSE
