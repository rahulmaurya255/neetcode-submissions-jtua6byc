class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair position and speed
        cars = list(zip(position, speed))
        
        # Sort by position descending
        cars.sort(reverse=True)
        
        fleets = 0
        prev_time = 0
        
        for pos, spd in cars:
            time = (target - pos) / spd
            
            # New fleet
            if time > prev_time:
                fleets += 1
                prev_time = time
        
        return fleets