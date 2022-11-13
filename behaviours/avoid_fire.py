# from game_objects.people import People
# from game_objects.exit import Exit
# from game_objects.fire import Fire
# from typing import List, Tuple
        
        # for fire in fires:
        #     perimeter = Rect(fire.x -20, fire.y -20, fire.width + 40, fire.height + 40)
        #     # If I am touching, then dies, switch this logic for proper death logic eventually
        #     if self.colliderect(fire):
        #         self.color = (255, 255, 255)
        #     # If I am within a threshold, run from the fire
        #     elif self.colliderect(perimeter):
        #         # if i am under or over the fire, continue with horizontal motion
        #         if self.x in range(fire.left, fire.right):
        #             self.x += (np.random.choice([unit_vector_x, -unit_vector_x], 1, p=[aptitude, 1-aptitude]))[0]
        #             # if i am above, never go down.
        #             if self.y > fire.y:
        #                 self.y += 2
        #             else:
        #                 self.y -= 2
        #         # if i am left of the fire, run left, if right of the fire, run right. In either case, verticle as normal.
        #         if self.y in range(fire.top, fire.bottom):
        #             self.y += (np.random.choice([unit_vector_y, -unit_vector_y], 1, p=[aptitude, 1-aptitude]))[0]
        #             if self.x > fire.x:
        #                 self.x += 2
        #             else:
        #                 self.x -= 2

        #     # else move normally
        #     else:
        #         self.x += (np.random.choice([unit_vector_x, -unit_vector_x], 1, p=[aptitude, 1-aptitude]))[0]
        #         self.y += (np.random.choice([unit_vector_y, -unit_vector_y], 1, p=[aptitude, 1-aptitude]))[0]