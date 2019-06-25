import unittest
import task2


class TestAccounting(unittest.TestCase):
    """test task2"""

    def setUp(self):
        """Init"""

    def test_sort_biger_one(self):
        self.assertEqual(task2.sort_inc(123), 321)
        self.assertEqual(task2.sort_inc(598), 985)
        self.assertEqual(task2.sort_inc(579875), 987755)
        self.assertEqual(task2.sort_inc(654681), 866541)

    def test_sort_smaller_one(self):
        self.assertEqual(task2.sort_dec(120), 102)
        self.assertEqual(task2.sort_dec(15600), 10056)
        self.assertEqual(task2.sort_dec(874100), 100478)
        self.assertEqual(task2.sort_dec(1265340), 1023456)
        self.assertEqual(task2.sort_dec(998877), 778899)

    def test_main_logic(self):
        self.assertEqual(task2.summing(123, 120), 219)
        self.assertEqual(task2.summing(49873, 56840), 58175)
        self.assertEqual(task2.summing(-4561, 45226), -28997)
        self.assertEqual(task2.summing(68464, -6846), 91312)

    def tearDown(self):
        """Finish"""


if __name__ == '__main__':
    unittest.main()
