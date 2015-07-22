Name:           ros-jade-image-rotate
Version:        1.12.14
Release:        0%{?dist}
Summary:        ROS image_rotate package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/image_rotate
Source0:        %{name}-%{version}.tar.gz

Requires:       opencv-devel
Requires:       ros-jade-cv-bridge
Requires:       ros-jade-dynamic-reconfigure
Requires:       ros-jade-image-transport
Requires:       ros-jade-nodelet
Requires:       ros-jade-roscpp
Requires:       ros-jade-tf2
Requires:       ros-jade-tf2-geometry-msgs
Requires:       ros-jade-tf2-ros
BuildRequires:  opencv-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cmake-modules
BuildRequires:  ros-jade-cv-bridge
BuildRequires:  ros-jade-dynamic-reconfigure
BuildRequires:  ros-jade-eigen-conversions
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-image-transport
BuildRequires:  ros-jade-nodelet
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-rostest
BuildRequires:  ros-jade-tf2
BuildRequires:  ros-jade-tf2-geometry-msgs
BuildRequires:  ros-jade-tf2-ros

%description
Contains a node that rotates an image stream in a way that minimizes the angle
between a vector in some arbitrary frame and a vector in the camera frame. The
frame of the outgoing image is published by the node. This node is intended to
allow camera images to be visualized in an orientation that is more intuitive
than the hardware-constrained orientation of the physical camera. This is
particularly helpful, for example, to show images from the PR2's forearm cameras
with a consistent up direction, despite the fact that the forearms need to
rotate in arbitrary ways during manipulation. It is not recommended to use the
output from this node for further computation, as it interpolates the source
image, introduces black borders, and does not output a camera_info.

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

