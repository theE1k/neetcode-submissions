class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = sorted(zip(position, speed), reverse=True)
        for pos, speed in pairs:
            time = (target-pos)/speed
            if not stack:
                stack.append(time)
            else:
                if time > stack[-1]:
                    stack.append(time)

        return len(stack)