from unittest import TestCase
import Model

class TestModel(TestCase):
    def setUp(self):
        self.model = Model.Model(4,3)
        pass

    def test_get_neighbor_count(self):
        expected_value = [[8]*3]*4
        self.model.map = [[1]*3]*4

        for i in range(0,4):
            for j in range(0,3):
                self.assertEquals(expected_value[i][j],self.model.get_neighbor_count(i,j))

    def test_updateMap(self):
        self.fail()
    '''
    def test_rows(self):
        self.assertEquals(4,self.model.numCols,"Should get correct rows")
    def test_cols(self):
        self.assertEquals(3,self.model.numCols,"Should get correct cols")
    '''