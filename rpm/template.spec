Name:           ros-jade-image-view
Version:        1.12.14
Release:        0%{?dist}
Summary:        ROS image_view package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/image_view
Source0:        %{name}-%{version}.tar.gz

Requires:       gtk2-devel
Requires:       opencv-devel
Requires:       ros-jade-camera-calibration-parsers
Requires:       ros-jade-cv-bridge
Requires:       ros-jade-image-transport
Requires:       ros-jade-message-filters
Requires:       ros-jade-nodelet
Requires:       ros-jade-rosconsole
Requires:       ros-jade-roscpp
Requires:       ros-jade-std-srvs
BuildRequires:  gtk2-devel
BuildRequires:  opencv-devel
BuildRequires:  ros-jade-camera-calibration-parsers
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cv-bridge
BuildRequires:  ros-jade-image-transport
BuildRequires:  ros-jade-message-filters
BuildRequires:  ros-jade-nodelet
BuildRequires:  ros-jade-rosconsole
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-rostest
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-std-srvs
BuildRequires:  ros-jade-stereo-msgs

%description
A simple viewer for ROS image topics. Includes a specialized viewer for stereo +
disparity images.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Wed Jul 22 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.14-0
- Autogenerated by Bloom

* Wed Jan 14 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.12-0
- Autogenerated by Bloom

