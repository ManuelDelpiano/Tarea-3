import math


class LCell:
    def __init__(self, x, y, p, map):
        self.x = x
        self.y = y
        self.p = p 
        self.map = map
        self.sandCost = 1
        self.iceCost = -0.5

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and \
               self.map == other.map

    def __repr__(self):
        return str((self.x, self.y, self.p))

    def __str__(self):
        return str((self.x, self.y, self.p))

    def __hash__(self):
        return hash((self.x, self.y, self.p))
    
    def successors(self):
        succ = []
        current_x, current_y = self.x, self.y  # Pre-calcula los valores de la posición actual
        current_pose = self.p

        for old_pose, new_pose, endx, endy, cost, new_move in self.map.neighbors:
            
            newx, newy = self.x+dx, self.y+dy
            if self.map.inside(newx, newy) and self.map.line_of_sight(self.x, self.y, newx, newy):
                
                # Revisar si el camino tiene algún costo extra o algún acelerador
                sand = self.map.sand
                ice = self.map.ice
                if sand[newx][newy]:
                    cost += self.sandCost
                elif ice[newx][newy]:
                    cost += self.iceCost
                succ.append((Cell(newx, newy, self.map), a, cost))
        return succ

    def is_goal(self):
        return self.x == self.map.goal_x and self.y == self.map.goal_y
