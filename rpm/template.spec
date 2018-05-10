Name:           ros-melodic-depth-image-proc
Version:        1.12.23
Release:        0%{?dist}
Summary:        ROS depth_image_proc package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/depth_image_proc
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-melodic-cv-bridge
Requires:       ros-melodic-eigen-conversions
Requires:       ros-melodic-image-geometry
Requires:       ros-melodic-image-transport
Requires:       ros-melodic-nodelet
Requires:       ros-melodic-tf2
Requires:       ros-melodic-tf2-ros
BuildRequires:  boost-devel
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cmake-modules
BuildRequires:  ros-melodic-cv-bridge
BuildRequires:  ros-melodic-eigen-conversions
BuildRequires:  ros-melodic-image-geometry
BuildRequires:  ros-melodic-image-transport
BuildRequires:  ros-melodic-message-filters
BuildRequires:  ros-melodic-nodelet
BuildRequires:  ros-melodic-rostest
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-stereo-msgs
BuildRequires:  ros-melodic-tf2
BuildRequires:  ros-melodic-tf2-ros

%description
Contains nodelets for processing depth images such as those produced by OpenNI
camera. Functions include creating disparity images and point clouds, as well as
registering (reprojecting) a depth image into another camera frame.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Thu May 10 2018 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.12.23-0
- Autogenerated by Bloom

