Name:           ros-indigo-roseus
Version:        1.2.0
Release:        0%{?dist}
Summary:        ROS roseus package

Group:          Development/Libraries
License:        BSD
URL:            http://pr.willowgarage.com/wiki/roseus
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-euslisp
Requires:       ros-indigo-geneus
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-jskeus
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-rosbash
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-roslang
Requires:       ros-indigo-rosmsg
Requires:       ros-indigo-rosnode
Requires:       ros-indigo-rospack
Requires:       ros-indigo-rostest
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-tf
Requires:       ros-indigo-tf2-ros
Requires:       ros-indigo-visualization-msgs
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-angles
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-euslisp
BuildRequires:  ros-indigo-geneus
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-jskeus
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-mk
BuildRequires:  ros-indigo-rosbash
BuildRequires:  ros-indigo-rosbuild
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roslang
BuildRequires:  ros-indigo-rosmsg
BuildRequires:  ros-indigo-rosnode
BuildRequires:  ros-indigo-rospack
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-rostopic
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-tf2-ros
BuildRequires:  ros-indigo-visualization-msgs

%description
EusLisp client for ROs Robot Operating System.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Jan 26 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.0-0
- Autogenerated by Bloom

* Mon Jan 26 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.32-0
- Autogenerated by Bloom

* Fri Jan 23 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.31-0
- Autogenerated by Bloom

* Wed Jan 14 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.30-0
- Autogenerated by Bloom

* Sat Dec 27 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.29-0
- Autogenerated by Bloom

* Mon Dec 22 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.27-1
- Autogenerated by Bloom

* Tue Nov 11 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.26-0
- Autogenerated by Bloom

* Fri Sep 05 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.22-0
- Autogenerated by Bloom

