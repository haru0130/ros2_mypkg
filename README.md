# **ROS2 Package for University Class Assignments**



[![test](https://github.com/haru0130/ros2_mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/haru0130/ros2_mypkg/actions/workflows/test.yml)


## **Overview**

This is a repository for a university class assignment. This repository contains a ROS2 package that counts up numbers and sends them from a talker to a listener on the topic `"countup"`.
## **Install**

### **Install ROS2**
   #### **If you have not installed ROS2, please follow the steps below.**



1. Install ROS2 Humble from the official website.

    [ROS2 Installation Guide][def3]

    [def3]: https://docs.ros.org/en/humble/Installation.html

1. Install colcon.

    [colcon Installation Guide][def2]

[def2]:https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Colcon-Tutorial.html
    

### **Install this package**

#### **Please follow the steps below to install this package.**

1. Set up your environment.

    ```
    $ source /opt/ros/humble/setup.bash
    ```

1. Create a workspace.

    ```
    $ mkdir -p ~/ros2_ws/src
    ```
1. Clone this package.

    ``` 
    $ cd ~/ros2_ws/src
    $ git clone -b master https://github.com/haru0130/ros2_mypkg.git
    ```
1. Install dependencies.

    ```
    $ rosdep install -i --from-path . --ignore-src
    ```

1. Build this package.

    ```
    $ cd ~/ros2_ws
    $ colcon build
    ```
1. Install this package.

    ```
    $ source ~/ros2_ws/install/setup.bash
    ```
## **Nodes**

### **Talker**
* **Function**
  
  Node `"Talker"` counts up the numbers and sends them to the `"listener"` with the topic `"countup"`.

*  **Run Script**

   Type the following command in a terminal.

     ``` 
    $ ros2 run mypkg talker
      ```
* **Output**
   ``` 
   Nothing
    ```
### **Listener**
* **Function**
    
     Node `"listener"` receives the data sent by the `"talker"` with the topic `"countup"` and displays it on the terminal.

*  **Run Script**

    Type the following command in a new terminal.
     ``` 
    $ ros2 run mypkg listener
      ```
* **Output**
    ``` 
    [INFO] [1672492464.144192300] [listener]: Listen: 124
    [INFO] [1672492464.644149500] [listener]: Listen: 125
    [INFO] [1672492465.144123500] [listener]: Listen: 126
    [INFO] [1672492465.644195600] [listener]: Listen: 127
    [INFO] [1672492466.144156100] [listener]: Listen: 128
    ...
     ```

## **Also, you can run both nodes at the same time.**

* **Run Script**

    Type the following command in a terminal.
     ``` 
    $ ros2 launch mypkg talk_listen.launch.py
    ```
* **output**
    ``` 
    [listener-2] [INFO] [1672855124.022146000] [listenertest]: Listen: 9
    [listener-2] [INFO] [1672855124.522275200] [listenertest]: Listen: 10
    [listener-2] [INFO] [1672855125.022385900] [listenertest]: Listen: 11
    [listener-2] [INFO] [1672855125.522228400] [listenertest]: Listen: 12
    [listener-2] [INFO] [1672855126.022194000] [listenertest]: Listen: 13
    ...
    ```

## **Develop**

### **If you want to develop this package, please follow the steps below.**

1. Modify the source code or add a new source code.

1. Build & Source 

    Type the following command in a terminal.
     ``` 
    $ cd ~/ros2_ws
    $ colcon build
    $ source ~/.bashrc
    ```
    
## **Test environment**

 * Ubuntu 22.04 LTS
 * ROS2 Humble

## **License**


* This software package is licensed for redistribution and use under the terms of the 3-Clause BSD License.
* This package uses code originate from Robot System class 2022 (© 2022 Ryuichi Ueda).
* The code in this package is based on the following slide（CC-BY-SA 4.0 by Ryuichi Ueda）, which is my own work with his permission．
    * [ryuichiueda/my_slides robosys_2022][def]
* © 2023 Haruki Matsukawa

[def]: https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022

## **Reference**

* [ROS2 Installation Guide][def3]
* [colcon Installation Guide][def2]
* [ryuichiueda/my_slides robosys_2022][def]
* [RT Corporation Software Tutorials][def4]

[def4]:https://rt-net.github.io/tutorials/raspimouse/ros/package-install.html
