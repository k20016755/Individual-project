import pytest
import pytest_benchmark
#evaluating the benchmark workflow with this file. 
@pytest.fixture(scope="session")
def values():
    return [i**2 for i in range(10000)]

def test_squaring(values, benchmark):
    benchmark(lambda: [i**2 for i in values])

def test_cubing(values, benchmark):
    benchmark(lambda: [i**3 for i in values])