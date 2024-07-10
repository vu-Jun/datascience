import unittest
import sys
import os

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '/Users/junlee/sep/resit/datascience'))
sys.path.insert(0, module_path)

from datascience.tables import _varargs_labels_as_list, f1_branch_coverage, print_coverage, reset_coverage

class TestVaragsLabelsAsList(unittest.TestCase):

    def setUp(self):
        reset_coverage()
        print("------------------------------------------------")
    
    def test_varargs_labels_as_list_empty_list(self):
        print("Test_varargs_labels_as_list_empty_list")
        try:
            result = _varargs_labels_as_list([])
            print_coverage()
        except Exception as e:
            print(e)
            print_coverage()
            
        self.assertEqual(result, [])
        self.assertTrue(f1_branch_coverage["branch_1_empty_list"])
        
    def test_varargs_labels_as_list_not_iterable(self):
        print("Test_varargs_labels_as_list_not_iterable")
        try:
            result = _varargs_labels_as_list(['label1', 'label2'])
            print_coverage()
        except Exception as e:
            print(e)
            print_coverage()
            
        self.assertEqual(result, ['label1', 'label2'])
        self.assertTrue(f1_branch_coverage["branch_2_not_iterable"])
        
    def test_varargs_labels_as_list_single_list(self):
        print("Test_varargs_labels_as_list_single_list")
        try:
            result = _varargs_labels_as_list([['label1', 'label2']])
            print_coverage()
        except Exception as e:
            print(e)
            print_coverage()
            
        self.assertEqual(result, ['label1', 'label2'])
        self.assertTrue(f1_branch_coverage["branch_3_single_list"])
        
    def test_varargs_labels_as_list_raise_value_error(self):
        print("Test_varargs_labels_as_list_raise_value_error")
        with self.assertRaises(ValueError):
            result = _varargs_labels_as_list([['label1'], ['label2']])
            
        print_coverage()
        self.assertTrue(f1_branch_coverage["branch_4_else"])
        
        

if __name__ == '__main__':
    unittest.main()
