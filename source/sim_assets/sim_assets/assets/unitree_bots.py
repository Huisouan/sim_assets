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
    actuators = {
        # --- 1. 腰部 & 髋关节（Legs Core）---
        "legs": IdealPDActuatorCfg(
            joint_names_expr=[
                "waist_yaw_joint",          # 腰部旋转
                ".*_hip_pitch_joint",       # 髋屈伸
                ".*_hip_roll_joint",        # 髋内外旋
                ".*_hip_yaw_joint",         # 髋旋转
                ".*_knee_joint"
            ],
            effort_limit=200.0,            # 基础扭矩（可根据实际调整）
            velocity_limit=23.0,            # 基础速度限制
            stiffness=0,
            damping=0,
        ),

        # --- 3. 脚踝（Feet）---
        "feet": IdealPDActuatorCfg(
            joint_names_expr=[
                ".*_ankle_pitch_joint",  # 脚背/脚跟
                ".*_ankle_roll_joint",   # 脚内/外翻
            ],
            effort_limit=40,             # 较小扭矩
            velocity_limit=9.0,
            stiffness=0,
            damping=0,
        ),

        # --- 4. 肩膀 & 手肘（Arms Upper）---
        "arms_upper": IdealPDActuatorCfg(
            joint_names_expr=[
                ".*_shoulder_pitch_joint",  # 肩前后
                ".*_shoulder_roll_joint",   # 肩左右
                ".*_shoulder_yaw_joint",    # 肩旋转
                ".*_elbow_joint",           # 手肘
            ],
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

        # --- 5. 手腕 & 手指（Hands）---
        "hands": IdealPDActuatorCfg(
            joint_names_expr=[
                ".*_wrist_.*_joint",        # 所有手腕关节
                ".*_hand_.*_joint",         # 所有手指关节
            ],
            effort_limit=20,               # 小扭矩
            velocity_limit=10.0,           # 低速
            stiffness=0,
            damping=0,
        ),
    }
    
)