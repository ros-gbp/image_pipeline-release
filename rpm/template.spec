Name:           ros-hydro-image-view
Version:        1.11.11
Release:        0%{?dist}
Summary:        ROS image_view package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/image_view
Source0:        %{name}-%{version}.tar.gz

Requires:       gtk2-devel
Requires:       ros-hydro-camera-calibration-parsers
Requires:       ros-hydro-cv-bridge
Requires:       ros-hydro-image-transport
Requires:       ros-hydro-message-filters
Requires:       ros-hydro-nodelet
Requires:       ros-hydro-opencv2
Requires:       ros-hydro-rosconsole
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-std-srvs
BuildRequires:  gtk2-devel
BuildRequires:  ros-hydro-camera-calibration-parsers
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cv-bridge
BuildRequires:  ros-hydro-image-transport
BuildRequires:  ros-hydro-message-filters
BuildRequires:  ros-hydro-nodelet
BuildRequires:  ros-hydro-opencv2
BuildRequires:  ros-hydro-rosconsole
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-rostest
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-std-srvs
BuildRequires:  ros-hydro-stereo-msgs

%description
A simple viewer for ROS image topics. Includes a specialized viewer for stereo +
disparity images.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Sat May 16 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.11.11-0
- Autogenerated by Bloom

