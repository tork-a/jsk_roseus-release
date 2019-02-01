Name:           ros-melodic-roseus
Version:        1.7.3
Release:        0%{?dist}
Summary:        ROS roseus package

Group:          Development/Libraries
License:        BSD
URL:            http://pr.willowgarage.com/wiki/roseus
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-actionlib
Requires:       ros-melodic-actionlib-msgs
Requires:       ros-melodic-actionlib-tutorials
Requires:       ros-melodic-dynamic-reconfigure
Requires:       ros-melodic-euslisp
Requires:       ros-melodic-geneus
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-jskeus
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-rosbash
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-roslang
Requires:       ros-melodic-rosmsg
Requires:       ros-melodic-rosnode
Requires:       ros-melodic-rospack
Requires:       ros-melodic-rostest
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-std-srvs
Requires:       ros-melodic-tf
Requires:       ros-melodic-tf2-ros
Requires:       ros-melodic-visualization-msgs
BuildRequires:  coreutils
BuildRequires:  ros-melodic-actionlib
BuildRequires:  ros-melodic-actionlib-msgs
BuildRequires:  ros-melodic-actionlib-tutorials
BuildRequires:  ros-melodic-angles
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-dynamic-reconfigure
BuildRequires:  ros-melodic-euslisp
BuildRequires:  ros-melodic-geneus
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-jskeus
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-mk
BuildRequires:  ros-melodic-rosbash
BuildRequires:  ros-melodic-rosbuild
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-roslang
BuildRequires:  ros-melodic-rosmsg
BuildRequires:  ros-melodic-rosnode
BuildRequires:  ros-melodic-rospack
BuildRequires:  ros-melodic-rostest
BuildRequires:  ros-melodic-rostopic
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-std-srvs
BuildRequires:  ros-melodic-tf
BuildRequires:  ros-melodic-tf2-ros
BuildRequires:  ros-melodic-visualization-msgs
BuildRequires:  xorg-x11-server-Xvfb

%description
EusLisp client for ROS Robot Operating System.

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
* Fri Feb 01 2019 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.7.3-0
- Autogenerated by Bloom

* Sun Jul 22 2018 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.7.1-0
- Autogenerated by Bloom

