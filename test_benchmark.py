import pytest
import pytest_benchmark

@pytest.fixture(scope="session")
def data():
    # Generate some data for testing
    return [i**2 for i in range(10000)]

def test_square(data, benchmark):
    # Test the performance of squaring each element of the data
    benchmark(lambda: [i**2 for i in data])

def test_cube(data, benchmark):
    # Test the performance of cubing each element of the data
    benchmark(lambda: [i**3 for i in data])