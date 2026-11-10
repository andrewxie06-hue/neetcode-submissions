class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(speed)):
            cars.append((position[i], speed[i]))
        cars.sort()
        fleets = []
       
        for i in range(len(cars)):
            while fleets and (target - cars[i][0]) / cars[i][1] >= (target - fleets[-1][0]) / fleets[-1][1]:
                        fleets.pop()
            fleets.append((cars[i][0], cars[i][1]))
            if not fleets:
                fleets.append((cars[i][0], cars[i][1]))
   
        return len(fleets)

                



        