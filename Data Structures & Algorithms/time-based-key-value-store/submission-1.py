class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.dic[key]
        if not values:
            return ""

        i = 0
        j = len(values) - 1
        res = ""

        while i <= j:
            m = (i + j ) // 2

            if values[m][0] <= timestamp:
                res =  values[m][1]
                i = m + 1
            else:
                j = m - 1

        return res
        
