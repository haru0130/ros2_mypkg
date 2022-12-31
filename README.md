# **This is a repository for university class assignments.**

[![test](https://github.com/haru0130/ros2_mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/haru0130/ros2_mypkg/actions/workflows/test.yml)


## **Install**
1. Create a new directory for your ROS2 workspace and move to it.
 ```
$ mkdir -p ~/ros2_ws/src
 ```
 2. Clone this repository into the src directory.
  ``` 
  $ git clone -b master https://github.com/haru0130/ros2_mypkg.git
  $ cd ros2_mypkg   
  ```
 3. Build the package.
  ``` 
  $ colcon build
  ``` 
 4. Source the setup file.
  ```
  $ source install/setup.bash
  ```
  

## **Commands**


### **Talker**
* **Function**
  
  Talker counts up numbers and sends them to the listener.

*  **Run Script**
     ``` 
        $ ros2 run mypkg talker
  
  
      ```
* **Output**
   ``` 
   Nothing
    ```
### **Listener**
* **Function**
    
    Listener receives numbers from the talker and displays them.




*  **Run Script**
     ``` 
        $ ros2 run mypkg listener
      ```
* **Output**
    ``` 
    [INFO] [listener]: Listen: 124
    [INFO] [listener]: Listen: 125
    [INFO] [listener]: Listen: 126
    [INFO] [listener]: Listen: 127  
    ...

    ```







## Required software



 * Python 
   
   * Verified on Python 3.7 ~ 3.10

## Test environment

 * Ubuntu 22.04 LTS
 * ROS2 Humble

## License


* This software package is licensed for redistribution and use under the terms of the 3-Clause BSD License.
* This package uses code originate from Robot System class 2022 (© 2022 Ryuichi Ueda).
* The code in this package is based on the following slide（CC-BY-SA 4.0 by Ryuichi Ueda）, which is my own work with his permission．
    * [ryuichiueda/my_slides robosys_2022][def]
* © 2022 Haruki Matsukawa

[def]: https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022