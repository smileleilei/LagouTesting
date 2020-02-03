class TestSort:
    def setup(self):
        self.data = [3, 1, 5, 2, 4]
        self.expect_data = [1, 2, 3, 4, 5]

    def bubble_sort(self, data: list):
        size = len(data)
        for i in range(size):
            for j in range(size - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]

        return data

    def test_bubble(self):
        assert self.expect_data == self.bubble_sort(self.data)

    def selection_sort(self, data: list):
        size = len(data)
        for i in range(size):
            min_id = i
            for j in range(i + 1, size):
                if data[min_id] > data[j]:
                    min_id = j
            data[i], data[min_id] = data[min_id], data[i]
        return data

    def test_selection(self):
        assert self.expect_data == self.selection_sort(self.data)

    def selection_sort_max(self, data: list):
        size = len(data)
        for i in range(size):
            max_id = size - i - 1
            for j in range(size - i - 1):
                if data[j] > data[max_id]:
                    max_id = j
            data[size - i - 1], data[max_id] = data[max_id], data[size - i - 1]

        return data

    def test_selection_max(self):
        assert self.expect_data == self.selection_sort_max(self.data)

    def sort_list(self, data: list):
        data.sort()
        return data

    def test_sort_list(self):
        assert self.expect_data == self.sort_list(self.data)
        print(self.data)

    def sorted_list(self, data: list):
        return sorted(data)

    def test_sorted_list(self):
        assert self.expect_data == self.sorted_list(self.data)
        print(self.data)
