Name:           ros-jade-roseus-smach
Version:        1.6.0
Release:        0%{?dist}
Summary:        ROS roseus_smach package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roseus_smach
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-actionlib
Requires:       ros-jade-actionlib-tutorials
Requires:       ros-jade-euslisp
Requires:       ros-jade-message-runtime
Requires:       ros-jade-roseus
Requires:       ros-jade-rostest
Requires:       ros-jade-smach
Requires:       ros-jade-smach-msgs
Requires:       ros-jade-smach-ros
Requires:       ros-jade-std-msgs
BuildRequires:  ros-jade-actionlib
BuildRequires:  ros-jade-actionlib-tutorials
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-roseus
BuildRequires:  ros-jade-rostest
BuildRequires:  ros-jade-smach
BuildRequires:  ros-jade-smach-msgs
BuildRequires:  ros-jade-smach-ros
BuildRequires:  ros-jade-std-msgs

%description
roseus_smach * Euslisp state machine class. it will be moved. * Message
publisher for visualizing current state by smach_viewer. * Simple pickle dump
script for debugging state machine. * Execute state machine as a action server.

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Sun Oct 02 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.6.0-0
- Autogenerated by Bloom

* Sat May 28 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.5.3-0
- Autogenerated by Bloom

* Fri Apr 22 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.5.1-0
- Autogenerated by Bloom

* Mon Mar 21 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.5.0-0
- Autogenerated by Bloom

* Wed Nov 25 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.4.1-0
- Autogenerated by Bloom

* Wed Nov 18 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.4.0-1
- Autogenerated by Bloom

