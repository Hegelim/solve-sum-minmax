from src.package import solver


class TestClass:
    def test_1(self):
        eq = 'min(400, 400*a) + min(400, 400*a) + min(0, 100*a) = 200'
        assert solver.solve_sum_minmax(eq, "a") == 0.25

    def test_2(self):
        """If only has one equation. """
        eq = "min(400, 400*a) = 400"
        assert solver.solve_sum_minmax(eq, "a") is None

    def test_3(self):
        eq = "min(400, 500*a) = 300"
        assert solver.solve_sum_minmax(eq, "a").evalf() == 0.6

    def test_4(self):
        """If a is on the left. """
        eq = "min(500*a, 400) = 300"
        assert solver.solve_sum_minmax(eq, "a").evalf() == 0.6

    def test_5(self):
        """If have constants before min. """
        eq = "800*a + min(300, 400*a) + min(300, 400*a) = 1000"
        assert solver.solve_sum_minmax(eq, "a").evalf() == 0.625

    def test_6(self):
        """If the equation has both min and max. """
        eq = "min(500, 600*a) + max(400, 500*a) = 500"
        assert solver.solve_sum_minmax(eq, "a").evalf() == 1/6

    def test_7(self):
        eq = "min(500, 600*a) - min(500, 600*a) = 0"
        assert solver.solve_sum_minmax(eq, "a").evalf() == 5/6

    def test_8(self):
        eq = "800*x + min(300, 400*x) + min(300, 400*x) = 1000"
        assert solver.solve_sum_minmax(eq, "x").evalf() == 0.625

    def test_9(self):
        eq = "800*s + min(300, 400*s) + min(400*s, 400) = 1000"
        assert solver.solve_sum_minmax(eq, "s").evalf() == 0.625


