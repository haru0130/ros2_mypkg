import launch
import launch.actions
import launch.substitution



def generate_launch_description():

    talker = launch_ros.action.Node(
        package='mypkg',
        executable='talker',
    )
    listener = launch_ros.action.Node(
        package='mypkg'
        executable='listener',
        output='screen'
    )

    return launch.LaunchDescription([talker, listener])