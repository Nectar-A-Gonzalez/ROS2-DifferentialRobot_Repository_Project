def ddr_ik(v_x, omega, L=0.5, r=0.1):
    """DDR inverse kinematics: calculate wheels speeds from desired velocity."""
    return (v_x - (L/2)*omega)/r, (v_x + (L/2)*omega)/r
def ddr_fk(phidot_L, phidot_R, L=0.5, r=0.1):
    """DDR inverse kinematics: calculate wheels speeds from desired velocity."""
    return gtsam.Point3((phidot_R+phidot_L)*r/2, 0, (phidot_R-phidot_L)*r/L)

phidot_L, phidot_R = ddr_ik(v_x=0.2, omega=0.3)
print(phidot_L, phidot_R)
