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
            enabled_self_collisions=False, 
            solver_position_iteration_count=8, 
            solver_velocity_iteration_count=4,
            fix_root_link=True,
        ),
    ),

    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.74),
        joint_pos={
            ".*_hip_pitch_joint": -0.20,
            ".*_knee_joint": 0.42,
            ".*_ankle_pitch_joint": -0.23,
            ".*_elbow_joint": 0.87,  # 修改：原 .*_elbow_pitch_joint → .*_elbow_joint
            "left_shoulder_roll_joint": 0.16,
            "left_shoulder_pitch_joint": 0.35,
            "right_shoulder_roll_joint": -0.16,
            "right_shoulder_pitch_joint": 0.35,
            "waist_yaw_joint": 0.0,          # 新增腰部初始角度
            ".*_wrist_.*_joint": 0.0,        # 所有手腕关节初始角度
            "left_hand_thumb_0_joint": 0.1,
            "right_hand_thumb_0_joint": -0.1,
            # 其他手指关节...
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,

    actuators = {
        "legs": IdealPDActuatorCfg(
            joint_names_expr=[
                "waist_yaw_joint",          # 腰部旋转
                ".*_hip_pitch_joint",       # 髋屈伸
                ".*_hip_roll_joint",        # 髋内外旋
                ".*_hip_yaw_joint",         # 髋旋转
                ".*_knee_joint",            # 膝盖
            ],
            effort_limit=200.0,
            velocity_limit=23.0,
            stiffness=0,
            damping=0,
        ),

        "feet": IdealPDActuatorCfg(
            joint_names_expr=[
                ".*_ankle_pitch_joint",  # 脚背/脚跟
                ".*_ankle_roll_joint",   # 脚内外翻
            ],
            effort_limit=40,
            velocity_limit=9.0,
            stiffness=0,
            damping=0,
        ),

        "arms_upper": IdealPDActuatorCfg(
            joint_names_expr=[
                ".*_shoulder_pitch_joint",  # 明确包含 _joint 后缀
                ".*_shoulder_roll_joint",
                ".*_shoulder_yaw_joint",
                ".*_elbow_joint",           # 修改为 .*_elbow_joint
            ],
            effort_limit={
                ".*_shoulder_pitch_joint": 40.0,  # 添加 _joint
                ".*_shoulder_roll_joint": 40.0,   # 添加 _joint
                ".*_shoulder_yaw_joint": 18.0,    # 添加 _joint
                ".*_elbow_joint": 18.0,           # 修改为 .*_elbow_joint
            },
            velocity_limit={
                ".*_shoulder_pitch_joint": 9.0,   # 添加 _joint
                ".*_shoulder_roll_joint": 9.0,    # 添加 _joint
                ".*_shoulder_yaw_joint": 20.0,    # 添加 _joint
                ".*_elbow_joint": 20.0,           # 修改为 .*_elbow_joint
            },
            stiffness=0,
            damping=0,
        ),

        "hands": IdealPDActuatorCfg(
            joint_names_expr=[
                ".*_wrist_.*_joint",        # 所有手腕关节
                ".*_hand_.*_joint",         # 所有手指关节
            ],
            effort_limit=20,
            velocity_limit=10.0,
            stiffness=0,
            damping=0,
        ),
    }



)