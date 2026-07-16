class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        maxTempStackIndex = []

        i = len(temperatures) - 1

        while i >= 0:
            j = len(maxTempStackIndex) - 1
            while maxTempStackIndex and j >= 0:
                if temperatures[i] >= temperatures[maxTempStackIndex[j]]:
                    maxTempStackIndex.pop()
                    j -= 1
                else:
                    result[i] = maxTempStackIndex[j] - i
                    break

            maxTempStackIndex.append(i)
            i -= 1

        return result
        
        