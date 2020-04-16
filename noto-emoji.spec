#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : noto-emoji
Version  : 2020.04.08.unicode12.1
Release  : 8
URL      : http://localhost/cgit/projects/noto-emoji/snapshot/noto-emoji-2020-04-08-unicode12_1.tar.xz
Source0  : http://localhost/cgit/projects/noto-emoji/snapshot/noto-emoji-2020-04-08-unicode12_1.tar.xz
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
%setup -q -n noto-emoji-2020-04-08-unicode12_1
cd %{_builddir}/noto-emoji-2020-04-08-unicode12_1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587071513
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1587071513
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/noto-emoji
cp %{_builddir}/noto-emoji-2020-04-08-unicode12_1/LICENSE %{buildroot}/usr/share/package-licenses/noto-emoji/ec660b17dff69058c2bbf122ca85ab83b920fce7
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/fonts/noto-emoji/NotoColorEmoji.ttf
/usr/share/fonts/noto-emoji/NotoEmoji-Regular.ttf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/noto-emoji/ec660b17dff69058c2bbf122ca85ab83b920fce7
