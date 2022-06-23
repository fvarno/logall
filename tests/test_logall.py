from logall import PyLogger

data_points = [
    ["loss", 10.1, 0],
    ["loss", 12.3, 1],
    ["accuracy", 0.9, 15],
]


def test_main():
    log_path = "tests/log.log"
    logger = PyLogger(log_path)

    for point in data_points:
        logger.log_scalar(*point)

    with open(log_path, 'r') as handle:
        for point in data_points:
            point_compose = ','.join(map(str, point))
            assert point_compose in handle.readline()
