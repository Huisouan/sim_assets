import isaaclab.sim as sim_utils
from isaaclab.actuators import ActuatorNetMLPCfg, DCMotorCfg, IdealPDActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg


G1_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path="/home/hsh/Code/sim_assets/source/sim_assets/sim_assets/assets/usd/bot/bot.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False, solver_position_iteration_count=8, solver_velocity_iteration_count=4
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.74),
        joint_pos={
            ".*_hip_pitch_joint": -0.20,
            ".*_knee_joint": 0.42,
            ".*_ankle_pitch_joint": -0.23,
            ".*_elbow_pitch_joint": 0.87,
            "left_shoulder_roll_joint": 0.16,
            "left_shoulder_pitch_joint": 0.35,
            "right_shoulder_roll_joint": -0.16,
            "right_shoulder_pitch_joint": 0.35,
            "left_one_joint": 1.0,
            "right_one_joint": -1.0,
            "left_two_joint": 0.52,
            "right_two_joint": -0.52,
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,


    # robot
    actuators = {
        "legs": IdealPDActuatorCfg(
            joint_names_expr=[".*_hip_yaw", ".*_hip_roll", ".*_hip_pitch", ".*_knee", "torso"],
            effort_limit={
                ".*_hip_yaw": 200.0,
                ".*_hip_roll": 200.0,
                ".*_hip_pitch": 200.0,
                ".*_knee": 300.0,
                "torso": 200.0,
            },
            velocity_limit={
                ".*_hip_yaw": 23.0,
                ".*_hip_roll": 23.0,
                ".*_hip_pitch": 23.0,
                ".*_knee": 14.0,
                "torso": 23.0,
            },
            stiffness=0,
            damping=0,
        ),
        "feet": IdealPDActuatorCfg(
            joint_names_expr=[".*_ankle"],
            effort_limit=40,
            velocity_limit=9.0,
            stiffness=0,
            damping=0,
        ),
        "arms": IdealPDActuatorCfg(
            joint_names_expr=[".*_shoulder_pitch", ".*_shoulder_roll", ".*_shoulder_yaw", ".*_elbow"],
            effort_limit={
                ".*_shoulder_pitch": 40.0,
                ".*_shoulder_roll": 40.0,
                ".*_shoulder_yaw": 18.0,
                ".*_elbow": 18.0,
            },
            velocity_limit={
                ".*_shoulder_pitch": 9.0,
                ".*_shoulder_roll": 9.0,
                ".*_shoulder_yaw": 20.0,
                ".*_elbow": 20.0,
            },
            stiffness=0,
            damping=0,
        ),
    }
    
    
)
"""Configuration for the Unitree G1 Humanoid robot."""