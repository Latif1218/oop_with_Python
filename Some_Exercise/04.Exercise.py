# Design a class SeriesCalculator that calculates the sum of an arithmetic series.

class SeriesCalculitor:
    def calculate_sum(self, n, a = 1, d = 2):
        return n * (2 * a + (n-1)*d) // 2
    
sc = SeriesCalculitor()
print(f"Sum of Serise: {sc.calculate_sum(5)}")