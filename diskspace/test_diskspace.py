import unittest
import StringIO
import diskpace

class test (unittest.Testcase):
    def test_Subprocess_checkout_output(self):
        self.command_user = 'du'
        self.result_of_du = subprocess.check_output(command_user)
        self.result = subprocess_check_output(command_user)
        self.assertEqual(result_of_du, result)

    def test_Bytes_to_readable(self):
        blocks = 0
        result = "0Kb"
        self.assertEqual(bytes_to_readable(blocks), result)

    def test_KBytes_to_readable(self):
        blocks = 100
        result = "1024.0Kb"
        self.assertEqual(bytes_to_readable(blocks), result)

    def test_MBytes_to_readable(self):
        blocks = 1000000
        result = "1024.0Mb"
        self.assertEqual(bytes_to_readable(blocks), result)

    def test_GBytes_to_readable(self):
        blocks = 1000000000
        result = "1024.0Gb"
        self.assertEqual(bytes_to_readable(blocks), result)

    def test_TBytes_to_readable(self):
        blocks =  1000000000000
        result = "1024.0Tb"
        self.assertEqual(bytes_to_readable(blocks), result)

    def test_Print_tree(self):
        self.captured = StringIO.StringIO()
        sys.stdout = captured

    def test_Show_space_list(self):
        captured = StringIO.StringIO()
        sys.stdout = captured

        print_space_list(self.largest_size, self.file_tree,
                         self.path, self.total_size)
        result = "  Size   (%)  File\n2.00Kb  100%  {}\n".format(self.path)
        sys.stdout = sys.__stdout__
        self.assertEqual(result, cap.getvalue())


if __name__ == "__main__":
 unittest.main()
