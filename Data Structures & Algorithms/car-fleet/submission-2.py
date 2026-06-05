from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Combine position and speed into pairs and sort by position in descending order
        fleet = list(zip(position, speed))
        fleet = sorted(fleet, reverse=True, key=lambda x: x[0])
        
        stack = []
        res = len(fleet)  # Initially assume all cars are separate fleets
        
        for pos, spd in fleet:
            # Calculate time to reach the target
            time = (target - pos) / spd
            
            # If the stack is empty or current car time is greater than the time at the top of the stack
            if not stack or time > stack[-1]:
                stack.append(time)  # Start a new fleet
            else:
                res -= 1  # This car joins an existing fleet
        
        return res
