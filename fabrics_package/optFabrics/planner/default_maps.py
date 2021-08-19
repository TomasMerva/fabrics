import casadi as ca
from optFabrics.diffGeometry.diffMap import DifferentialMap


class CollisionMap(DifferentialMap):
    def __init__(self, q, qdot, fk, x_obst, r_obst):
        phi = ca.norm_2(fk - x_obst) / r_obst - 1
        super().__init__(phi, q=q, qdot=qdot)


class GoalMap(DifferentialMap):
    def __init__(self, q, qdot, fk, goal):
        phi = fk - goal
        super().__init__(phi, q=q, qdot=qdot)

