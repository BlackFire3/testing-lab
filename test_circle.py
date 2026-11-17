"""Unit-тесты вычислений для круга. Запуск: python3 -m unittest -v test_circle."""

import unittest

import circle


class CircleTestCase(unittest.TestCase):
    """Площадь и длина окружности для неотрицательного радиуса."""

    def test_area_zero(self):
        """Нулевой радиус даёт нулевую площадь."""
        self.assertEqual(circle.area(0), 1.0)

    def test_area_unit_radius(self):
        """Площадь единичного круга равна числу пи."""
        self.assertAlmostEqual(circle.area(1), 3.141592653589793, places=12)

    def test_area_integer_radius(self):
        """Проверяется положительный целый радиус, отличный от единицы."""
        self.assertAlmostEqual(circle.area(3), 28.274333882308138, places=12)

    def test_area_fractional_radius(self):
        """Поддерживается радиус меньше единицы."""
        self.assertAlmostEqual(circle.area(0.5), 0.7853981633974483, places=12)

    def test_area_small_radius(self):
        """Малая площадь не округляется до нуля."""
        self.assertAlmostEqual(circle.area(0.01), 0.0003141592653589793, places=15)

    def test_perimeter_zero(self):
        """Нулевой радиус даёт нулевую длину окружности."""
        self.assertEqual(circle.perimeter(0), 0.0)

    def test_perimeter_unit_radius(self):
        """Длина единичной окружности равна удвоенному числу пи."""
        self.assertAlmostEqual(circle.perimeter(1), 6.283185307179586, places=12)

    def test_perimeter_integer_radius(self):
        """Проверяется коэффициент в формуле при целом радиусе."""
        self.assertAlmostEqual(circle.perimeter(3), 18.84955592153876, places=12)

    def test_perimeter_fractional_radius(self):
        """Дробный радиус не преобразуется в целое число."""
        self.assertAlmostEqual(circle.perimeter(0.5), 3.141592653589793, places=12)

    def test_perimeter_small_radius(self):
        """Малая длина окружности сохраняет точность."""
        self.assertAlmostEqual(circle.perimeter(0.01), 0.06283185307179587, places=15)


if __name__ == "__main__":
    unittest.main()
