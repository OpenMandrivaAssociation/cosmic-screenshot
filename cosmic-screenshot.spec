%undefine _debugsource_packages

%define         appname com.system76.CosmicScreenshot
Name:           cosmic-screenshot
Version:        1.0.0
%define beta beta.5
Release:        %{?beta:0.%{beta}.}1
Summary:        Utility for capturing screenshots via XDG Desktop Portal
Group:          Utility/COSMIC
License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-screenshot
Source0:        https://github.com/pop-os/cosmic-screenshot/archive/epoch-%{version}%{?beta:-%{beta}}/%{name}-epoch-%{version}%{?beta:-%{beta}}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  rust-packaging
BuildRequires:  hicolor-icon-theme
BuildRequires:  just

%description
%{summary}.

%prep
%autosetup -n %{name}-epoch-%{version}%{?beta:-%{beta}} -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/??x??/apps/%{appname}.svg
%{_datadir}/icons/hicolor/???x???/apps/%{appname}.svg
