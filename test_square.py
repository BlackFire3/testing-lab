"""Unit-тесты вычислений для квадрата. Запуск: python3 -m unittest -v test_square."""

import unittest

import square


class SquareTestCase(unittest.TestCase):
    """Площадь и периметр квадрата для неотрицательной стороны."""

    def test_area_zero(self):
        """Нулевая сторона даёт нулевую площадь."""
        self.assertEqual(square.area(0), 0)

    def test_area_unit_side(self):
        """Площадь единичного квадрата равна единице."""
        self.assertEqual(square.area(1), 1)

    def test_area_integer_side(self):
        """Проверяется возведение целой стороны в квадрат."""
        self.assertEqual(square.area(3), 9)

    def test_area_fractional_side(self):
        """Поддерживается дробная длина стороны."""
        self.assertAlmostEqual(square.area(0.5), 0.25, places=12)

    def test_area_small_side(self):
        """Малая площадь не округляется до нуля."""
        self.assertAlmostEqual(square.area(0.01), 0.0001, places=15)

    def test_perimeter_zero(self):
        """Нулевая сторона даёт нулевой периметр."""
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_unit_side(self):
        """Периметр единичного квадрата равен четырём."""
        self.assertEqual(square.perimeter(1), 4)

    def test_perimeter_integer_side(self):
        """Проверяется умножение целой стороны на четыре."""
        self.assertEqual(square.perimeter(3), 12)

    def test_perimeter_fractional_side(self):
        """Дробная сторона не преобразуется в целое число."""
        self.assertAlmostEqual(square.perimeter(0.5), 2.0, places=12)

    def test_perimeter_small_side(self):
        """Малый периметр сохраняет точность."""
        self.assertAlmostEqual(square.perimeter(0.01), 0.04, places=15)


if __name__ == "__main__":
    unittest.main()
